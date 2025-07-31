import json
import sys
from rich.tree import Tree
from rich.console import Console
from rich import box
from rich.panel import Panel

def render_json_tree(data, tree):
    if isinstance(data, dict):
        for key, value in data.items():
            branch = tree.add(f"[bold cyan]{key}[/]")
            render_json_tree(value, branch)
    elif isinstance(data, list):
        for index, item in enumerate(data):
            branch = tree.add(f"[green][{index}][/]")
            render_json_tree(item, branch)
    else:
        tree.add(f"[magenta]{repr(data)}[/]")

def main():
    if len(sys.argv) != 2:
        print("Usage: python json_rich_tree.py <path_to_json_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"[red]Error:[/] {e}")
        sys.exit(1)

    console = Console()
    root = Tree(f"[bold underline yellow]📄 {file_path}[/]", guide_style="bold bright_blue")
    render_json_tree(data, root)

    console.print(Panel.fit(root, title="JSON Tree View", box=box.DOUBLE, border_style="bright_blue"))

if __name__ == "__main__":
    main()

