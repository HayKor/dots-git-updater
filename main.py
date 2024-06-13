import os, shutil

# Some needed vars
config_dirs = ["i3", "nvim", "picom", "polybar", "dunst", "ohmyposh", "rofi", "kitty"]
git_repo_path = r"/home/arthur/git-repos/dotfiles/config/"
config_path = r"/home/arthur/.config/"

for dir in config_dirs:
    path_to_dot = os.path.join(git_repo_path, dir)
    path_to_conf = os.path.join(config_path, dir)
    try:
        shutil.rmtree(path_to_dot)
        print(f"{path_to_dot} successfully deleted!!")
    except Exception as e:
        pass
    shutil.copytree(path_to_conf, path_to_dot)
    print(f"{path_to_conf} successfully copied to {path_to_dot}.")
