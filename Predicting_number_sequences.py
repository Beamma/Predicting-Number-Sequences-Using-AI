from random import randint, choice

def is_valid_expression(object, function_symbols, leaf_symbols):
    if isinstance(object, int) or object in leaf_symbols:
        return True
    
    if isinstance(object, list):
        if len(object) == 3:
            if object[0] in function_symbols and is_valid_expression(object[1], function_symbols, leaf_symbols) and is_valid_expression(object[2], function_symbols, leaf_symbols):
                return True

    return False

def depth(expression):
    if isinstance(expression, int) or isinstance(expression, str):
        return 0
    
    return max(depth(expression[1]), depth(expression[2])) + 1

def evaluate(expression, bindings):
    if isinstance(expression, int):
        return expression

    elif expression in list(bindings.keys()):
        return bindings[expression]

    else:
        func = bindings[expression[0]]
        return (func(evaluate(expression[1], bindings), evaluate(expression[2], bindings)))
    
def random_expression(function_symbols, leaves, max_depth):
    if max_depth == 0:
        return choice(leaves)

    if randint(0, 1) == 0:
        return choice(leaves)

    else:
        
        return choice([[choice(function_symbols), choice(leaves), choice(leaves)],
                       [choice(function_symbols), random_expression(function_symbols, leaves, max_depth-1), choice(leaves)],
                       [choice(function_symbols), choice(leaves), random_expression(function_symbols, leaves, max_depth-1)],
                       [choice(function_symbols), random_expression(function_symbols, leaves, max_depth-1), random_expression(function_symbols, leaves, max_depth-1)]])

def generate_rest(initial_sequence, expression, length):
    og_len = len(initial_sequence)
    rest = [] + initial_sequence
    for i in range(og_len, og_len + length):
        x = rest[-2]
        y = rest[-1]
        rest.append(evaluate(expression, {'x': x, 'y': y, 'i': i, '+': lambda x, y: x + y, '-': lambda x, y: x - y, '*':lambda x, y: x * y}))
    return rest[og_len:]

def predict_rest(sequence):
    while True:
        expression = random_expression(['+', '-', '*'], ['x', 'y', 'i'] + list(range(-2, 3)), 3)
        tail_sequence = generate_rest([sequence[0], sequence[1]], expression, len(sequence)-2)
        if tail_sequence == sequence[2:]:
            ans = generate_rest(sequence, expression, 5)
            return ans

