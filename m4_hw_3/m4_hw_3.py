import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(directory, prefix=""):
    if not directory.is_dir():
        print(Fore.RED + f"{directory} не є директорією.")
        return

    items = list(directory.iterdir())
    for index, item in enumerate(items):
        connector = "└── " if index == len(items) - 1 else "├── "

        if item.name.startswith('.'):
            continue

        if item.is_dir():
            print(Fore.BLUE + f"{prefix}{connector}📂 {item.name}")
            print_directory_structure(item, prefix + ("    " if index == len(items) - 1 else "│   "))
        else:
            print(Fore.GREEN + f"{prefix}{connector}📜 {item.name}")

def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Будь ласка, передайте шлях до директорії як аргумент.")
        return
    
    path = Path(sys.argv[1])

    if not path.exists():
        print(Fore.RED + f"Шлях {path} не існує.")
        return

    print(Fore.YELLOW + f"📦 {path.name}")
    
    print_directory_structure(path)

if __name__ == "__main__":
    main()
