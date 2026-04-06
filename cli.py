import sys
import argparse
from tree_logic import parse_indented_text, format_tree

def main():
    parser = argparse.ArgumentParser(description="Convert indented text into a Unicode tree diagram.")
    parser.add_argument("-s", "--spaces", type=int, default=2, help="Number of spaces per level (default: 2)")
    args = parser.parse_args()

    # Read all lines from stdin
    input_text = sys.stdin.read()
    
    if not input_text.strip():
        return

    parsed = parse_indented_text(input_text, spaces_per_level=args.spaces)
    tree_str = format_tree(parsed)
    print(tree_str)

if __name__ == "__main__":
    main()
