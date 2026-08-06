import argparse
from pathlib import Path


def main():
    topic_name = 'String'

    parser = argparse.ArgumentParser(
        description="LeetCode script to create directories and files"
    )
    parser.add_argument(
        "-n", "--name", type=str, help="directory name"
    )
    args = parser.parse_args()

    # If a name is not provided via -n, we ask via input()
    dir_name = args.name
    if not dir_name:
        dir_name = input("Enter the directory name: ").strip().lower().replace(' ', '-')
        # replaced_name = strip_name.replace(' ', '-')
        # dir_name = replaced_name.lower()

    if not dir_name:
        print("Error, name cannot be empty")
        return

    # creating dir
    target_dir = Path(topic_name) / dir_name
    target_dir.mkdir(parents=True, exist_ok=True)

    # solution.py va notes.md creating
    solution_file = target_dir / "solution.py"
    notes_file = target_dir / "notes.md"

    if not solution_file.exists():
        solution_file.touch()
        print(f"Created: {solution_file}")

    if not notes_file.exists():
        notes_file.touch()
        print(f"Created: {notes_file}")

    print(f"Successfully created! '{target_dir.resolve()}'")


if __name__ == "__main__":
    main()