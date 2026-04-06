from tree_logic import parse_indented_text, format_tree

def test_odd_indentation():
    text = """
Root
 1 level (1 space)
   2 level (3 spaces)
"""
    # Current behavior with indent=2
    parsed = parse_indented_text(text, spaces_per_level=2)
    print("Parsed (indent=2):", parsed)
    # 1 space // 2 = 0
    # 3 spaces // 2 = 1
    # Result: Root, 1 level (0), 2 level (1)
    # Output:
    # Root
    # 1 level (1 space)
    # └── 2 level (3 spaces)
    print("Tree:\n", format_tree(parsed))

if __name__ == "__main__":
    test_odd_indentation()
