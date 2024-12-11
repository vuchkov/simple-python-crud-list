root = {
    'value': 10,
    'nodes': [{
        'value': 20,
        'nodes': [{
            'value': 30
        },{
            'value': 20,
            'nodes': [{
                'value': 25
            }]
        }]
    }]
}

def sum_root(root):
    sum_all_value = 0
    for row in root:
        if row[0] == 'value':
            print(row[0]['value'])
            sum_all_value += int(row['value'])
        if 'nodes' in row and 'value' in row['nodes']:
            sum_all_value += sum_root(row['nodes'])
    return sum_all_value

def recursive_sum(root):
    current_sum = 0
    if not isinstance(root, str):
        for value, nodes in root.items():
            if isinstance(value, int):
                current_sum += value
            else:
                current_sum += recursive_sum(nodes)
    return current_sum

print(sum_root(root))
print(recursive_sum(root))