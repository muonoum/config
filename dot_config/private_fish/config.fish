if status is-interactive
  set fish_greeting

  set --export EDITOR hx
  set --export ERL_AFLAGS '-kernel shell_history enabled'
  set --export GOPATH $HOME/.local/share/go
  set --export KUBECONFIG admin.kubeconfig
  set --export XDG_CONFIG_HOME $HOME/.config

  eval "$(/opt/homebrew/bin/brew shellenv)"
  eval "$(starship init fish)"

  alias gum-filter 'gum filter --prompt="# " --indicator="+" --placeholder=""'
  alias k kubecolor

  fish_add_path $(go env GOPATH)/bin
  fish_add_path $HOME/.cabal/bin
  fish_add_path $HOME/.ghcup/bin
  fish_add_path $HOME/.local/bin
  fish_add_path $HOME/.cargo/bin
end
