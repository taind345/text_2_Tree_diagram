import re

def parse_indented_text(text: str, spaces_per_level: int = 2) -> list[tuple[int, str]]:
    """Parses text and returns (level, content) tuples based on indentation."""
    nodes = []
    indent_stack = [""]
    
    for line in text.splitlines():
        if not line.strip(): continue
        
        ws = re.match(r'^(\s*)', line).group(1) or ""
        # Canonicalize whitespace (tabs to spaces)
        canonical_ws = ws.replace('\t', ' ' * spaces_per_level)
        
        if len(canonical_ws) > len(indent_stack[-1]):
            indent_stack.append(canonical_ws)
        elif len(canonical_ws) < len(indent_stack[-1]):
            while len(indent_stack) > 1 and len(canonical_ws) < len(indent_stack[-1]):
                indent_stack.pop()
        
        nodes.append((len(indent_stack) - 1, line.strip()))
    return nodes

def format_tree(nodes: list[tuple[int, str]]) -> str:
    """Converts (level, content) into a Unicode tree string."""
    if not nodes: return ""
    lines = []
    
    for i, (lvl, content) in enumerate(nodes):
        if lvl == 0:
            lines.append(content)
            continue
            
        # Build prefix for ancestors
        prefix = ""
        for parent_lvl in range(1, lvl):
            has_more = any(n[0] == parent_lvl for n in nodes[i+1:])
            # Actually, the logic needs to check if the parent level continues or not
            # Let's simplify this with a peek ahead
            continues = False
            for next_node in nodes[i+1:]:
                if next_node[0] == parent_lvl:
                    continues = True
                    break
                if next_node[0] < parent_lvl: break
            prefix += "│   " if continues else "    "
        
        # Check if current node is the last child of its parent
        is_last = True
        for next_node in nodes[i+1:]:
            if next_node[0] == lvl:
                is_last = False
                break
            if next_node[0] < lvl: break
                
        lines.append(f"{prefix}{'└── ' if is_last else '├── '}{content}")
        
    return "\n".join(lines)
