# khusaro-noctalia-dots

Dotfiles for my Arch + Hyprland desktop setup themed around **Noctalia**.

## Contents
- `.config/hypr` — Hyprland config (hyprland.lua, noctalia.lua)
- `.config/noctalia` — Noctalia shell config
- `.config/nvim` — Neovim config
- `.config/kitty`, `fish`, `btop`, `cava`, `fastfetch`, `yazi`, `ranger`, `mpd`, `mpv`, `imv`
- `.config/gtk-3.0`, `gtk-4.0`, `qt5ct`, `qt6ct`, `Kvantum`, `fontconfig`, `xsettingsd`, `nwg-look`
- `.config/Code - OSS` — VSCode OSS settings
- `.local/bin` — helper scripts
- `.local/state/noctalia` — Noctalia settings/state

## Install
Clone and symlink (or use your preferred dotfiles manager):

```sh
git clone https://github.com/watersniffer/khusaro-noctalia-dots.git ~/dotfiles
# then symlink files into $HOME
```

> Note: shell rc files (`.bashrc`, `.zshrc`, `.gitconfig`, etc.) were not captured because the
> previous `~/dotfiles` directory they pointed to is missing. Re-add them as needed.
