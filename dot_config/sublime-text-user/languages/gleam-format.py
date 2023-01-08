import os
import sublime
import sublime_plugin
import subprocess
import shutil


class GleamFormat(sublime_plugin.TextCommand):
  def run(self, edit):
    settings = sublime.load_settings("Plugins.sublime-settings")

    if not settings.get("gleam", {}).get("format_enabled", True):
      print("formatting is disabled")
      return

    command = settings.get("gleam", {}).get("format_command", None)

    if command is None or not os.access(command, os.X_OK):
      command = shutil.which("gleam")
    if command is None:
      return

    region = sublime.Region(0, self.view.size())
    content = self.view.substr(region)

    stdout, stderr = subprocess.Popen(
      [command, "format", "--stdin"],
      stdin=subprocess.PIPE,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
    ).communicate(input=bytes(content, 'UTF-8'))

    if stderr.strip():
      open_panel(self.view, stderr.strip().decode())
    else:
      self.view.replace(edit, region, stdout.decode('UTF-8'))
      self.view.window().run_command("hide_panel",
        {"panel": "output.gleam_format"})


class GleamFormatOnSave(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    scope = view.scope_name(0)
    if scope.find('source.gleam') != -1:
      view.run_command('gleam_format')


def open_panel(view, content):
    window = view.window()
    panel = window.create_output_panel("gleam_format")
    panel.set_read_only(False)
    panel.run_command('erase_view')
    panel.run_command('append', {'characters': content})
    panel.set_read_only(True)
    window.run_command("show_panel", {"panel": "output.gleam_format"})
