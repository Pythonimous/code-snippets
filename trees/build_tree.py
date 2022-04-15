def to_tree(relations):
    nodes = {}
    trees = {}
    for parent_id, node_id in relations:
        node_children = {}
        nodes[node_id] = node_children
        if not parent_id:
            trees[node_id] = node_children

    for parent_id, node_id in relations:
        if parent_id:
            nodes[parent_id][node_id] = nodes[node_id]
    return trees


if __name__ == "__main__":
    source = [
        (None, 'a'),
        (None, 'b'),
        (None, 'c'),
        ('a', 'a1'),
        ('a', 'a2'),
        ('a2', 'a21'),
        ('a2', 'a22'),
        ('b', 'b1'),
        ('b1', 'b11'),
        ('b11', 'b111'),
        ('b', 'b2'),
        ('c', 'c1'),
    ]

    expected = {
        'a': {'a1': {}, 'a2': {'a21': {}, 'a22': {}}},
        'b': {'b1': {'b11': {'b111': {}}}, 'b2': {}},
        'c': {'c1': {}},
    }
    tree = to_tree(source)
    assert to_tree(source) == expected
