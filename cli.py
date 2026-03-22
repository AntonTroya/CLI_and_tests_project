import sys
import argparse
from file_operations import copy_file, delete_path

def main():
    parser = argparse.ArgumentParser(
        description="Simple file manager CLI utility"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Команда copy
    copy_parser = subparsers.add_parser("copy", help="Copy a file")
    copy_parser.add_argument("source", help="Source file path")
    copy_parser.add_argument("destination", help="Destination file or directory")

    # Команда delete
    delete_parser = subparsers.add_parser("delete", help="Delete a file or directory")
    delete_parser.add_argument("path", help="Path to file or directory")

    args = parser.parse_args()

    try:
        if args.command == "copy":
            copy_file(args.source, args.destination)
        elif args.command == "delete":
            delete_path(args.path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()


    

