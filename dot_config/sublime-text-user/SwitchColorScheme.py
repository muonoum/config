import sublime
import sublime_plugin


class SwitchColorSchemeCommand(sublime_plugin.ApplicationCommand):
  def run(self):
    settings = sublime.load_settings("Preferences.sublime-settings")

    light_scheme = settings.get("light_color_scheme", "Breakers.sublime-color-scheme")
    dark_scheme = settings.get("dark_color_scheme", "Mariana.sublime-color-scheme")
    current_scheme = settings.get("color_scheme", light_scheme)

    if current_scheme == light_scheme:
      settings.set("color_scheme", dark_scheme)
    else:
      settings.set("color_scheme", light_scheme)

    sublime.save_settings("Preferences.sublime-settings")

