import re

def parse_indented_text(text: str, spaces_per_level: int = 2) -> list[tuple[int, str]]:
    """
    Parses multiline text and returns a list of (level, content) tuples.
    This version uses a relative indentation stack for maximum robustness.
    """
    lines = text.splitlines()
    parsed_nodes = []
    
    # Indentation stack stores the whitespace strings encountered
    indent_stack = [""]
    
    for line in lines:
        if not line.strip():
            continue
            
        match = re.match(r'^(\s*)', line)
        whitespace = match.group(1) if match else ""
        content = line.strip()
        
        # Canonicalize whitespace (tabs to spaces)
        # Using the user's spaces_per_level as the tab width
        canonical_ws = whitespace.replace('\t', ' ' * spaces_per_level)
        
        # Determine level based on the stack
        if len(canonical_ws) > len(indent_stack[-1]):
            # Increase level
            indent_stack.append(canonical_ws)
        elif len(canonical_ws) < len(indent_stack[-1]):
            # Decrease level: pop until we find a match or smaller
            while len(indent_stack) > 1 and len(canonical_ws) < len(indent_stack[-1]):
                indent_stack.pop()
            # If it's still not equal, it's a new intermediate level (rare inconsistency)
            if canonical_ws != indent_stack[-1]:
                 # Just push it as a new level above current top
                 if len(canonical_ws) > len(indent_stack[-1]):
                     indent_stack.append(canonical_ws)
                 # else: it's level 0 or same as some parent
        
        level = len(indent_stack) - 1
        parsed_nodes.append((level, content))
        
    return parsed_nodes

def format_tree(nodes: list[tuple[int, str]]) -> str:
    """
    Converts list of (level, content) into a box-drawing tree string.
    """
    if not nodes:
        return ""
        
    lines = []
    
    for i, (level, content) in enumerate(nodes):
        if level == 0:
            lines.append(content)
            continue
            
        prefix_parts = []
        for l in range(1, level):
            has_more_at_level = False
            for next_node in nodes[i+1:]:
                if next_node[0] == l:
                    has_more_at_level = True
                    break
                if next_node[0] < l:
                    break
            
            if has_more_at_level:
                prefix_parts.append("│   ")
            else:
                prefix_parts.append("    ")
        
        # Now for the current level's branch
        is_last_child = True
        for next_node in nodes[i+1:]:
            if next_node[0] == level:
                is_last_child = False
                break
            if next_node[0] < level:
                break
                
        branch = "└── " if is_last_child else "├── "
        lines.append("".join(prefix_parts) + branch + content)
        
    return "\n".join(lines)
