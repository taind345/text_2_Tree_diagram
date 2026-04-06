import sys
import argparse
from tree_logic import parse_indented_text, format_tree

def main():
    parser = argparse.ArgumentParser(description="Convert indented text into a Unicode tree diagram.")
    parser.add_argument("-s", "--spaces", type=int, default=2, help="Number of spaces per level (default: 2)")
    args = parser.parse_args()

    txt = sys.stdin.read()
    if txt.strip():
        print(format_tree(parse_indented_text(txt, args.spaces)))

if __name__ == "__main__":
    main()
