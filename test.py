import math

tree = {
    'A': ('MAX', ['B', 'C']),
    'B': ('MIN', ['D', 'E']),
    'C': ('MIN', ['F', 'G']),
    'D': ('MAX', ['H', 'I']),
    'E': ('MAX', ['J', 'K']),
    'F': ('MAX', ['L', 'M']),
    'G': ('MAX', ['N', 'O']),
    'H': ('LEAF', 3),
    'I': ('LEAF', 12),
    'J': ('LEAF', 8),
    'K': ('LEAF', 2),
    'L': ('LEAF', 4),
    'M': ('LEAF', 6),
    'N': ('LEAF', 14),
    'O': ('LEAF', 5),
}

def run_alpha_beta(is_r2l=False):
    nodes_visited = 0
    pruned_count = 0

    def evaluate(node, alpha, beta):
        nonlocal nodes_visited, pruned_count
        nodes_visited += 1
        
        node_type, value = tree[node]
        
        if node_type == 'LEAF':
            return value
        
        children = list(reversed(value)) if is_r2l else list(value)
        
        if node_type == 'MAX':
            v = -math.inf
            for i, child in enumerate(children):
                v = max(v, evaluate(child, alpha, beta))
                alpha = max(alpha, v)
                if beta <= alpha:
                    pruned_count += (len(children) - 1 - i)
                    break
            return v
        else: # MIN
            v = math.inf
            for i, child in enumerate(children):
                v = min(v, evaluate(child, alpha, beta))
                beta = min(beta, v)
                if beta <= alpha:
                    pruned_count += (len(children) - 1 - i)
                    break
            return v

    res_val = evaluate('A', -math.inf, math.inf)
    return nodes_visited, pruned_count, res_val

l2r_nodes, l2r_pruned, l2r_val = run_alpha_beta(is_r2l=False)
r2l_nodes, r2l_pruned, r2l_val = run_alpha_beta(is_r2l=True)

print(f"L2R: Alpha-beta nodes = {l2r_nodes}, Pruned = {l2r_pruned}")
print(f"R2L: Alpha-beta nodes = {r2l_nodes}, Pruned = {r2l_pruned}")