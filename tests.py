from Predicting_number_sequences import is_valid_expression, depth, evaluate, random_expression, generate_rest, predict_rest
import operator

def test_1():
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 1

    print(is_valid_expression(expression, function_symbols, leaf_symbols))

    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'y'

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))


    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 2.0

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 123, 'x']

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', ['+', 0, -1], ['f', 1, 'x']]

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['+', ['f', 1, 'x'], -1]

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y', -1, 0, 1]
    expression = ['f', 0, ['f', 0, ['f', 0, ['f', 0, 'x']]]]

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = 'f'

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['f', 1, 0, -1]

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['x', 0, 1]

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))
    
    function_symbols = ['f', '+']
    leaf_symbols = ['x', 'y']
    expression = ['g', 0, 'y']

    print(is_valid_expression(
            expression, function_symbols, leaf_symbols))

def test_2():
    expression = 12
    print(depth(expression))

    expression = 'weight'
    print(depth(expression))

    expression = ['add', 12, 'x']
    print(depth(expression))

    expression = ['add', ['add', 22, 'y'], 'x']
    print(depth(expression))

def test_3():
    bindings = {}
    expression = 12
    print(evaluate(expression, bindings))

    bindings = {'x':5, 'y':10, 'time':15}
    expression = 'y'
    print(evaluate(expression, bindings))

    bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
    expression = ['add', 12, 'x']
    print(evaluate(expression, bindings))

    bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
    expression = ['add', ['add', 22, 'y'], 'x']
    print(evaluate(expression, bindings))

def test_4():
    function_symbols = ['f', 'g', 'h']
    constant_leaves =  list(range(-2, 3))
    variable_leaves = ['x', 'y', 'i']
    leaves = constant_leaves + variable_leaves
    max_depth = 4

    for _ in range(10000):
        expression = random_expression(function_symbols, leaves, max_depth)
        if not is_valid_expression(expression, function_symbols, leaves):
            print("The following expression is not valid:\n", expression)
            break
    else:
        print("OK")

def test_5():
    initial_sequence = [0, 1, 2]
    expression = 'i' 
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression,
                        length_to_generate))

    # no particular pattern, just an example expression
    initial_sequence = [-1, 1, 367]
    expression = 'i' 
    length_to_generate = 4
    print(generate_rest(initial_sequence,
                        expression,
                        length_to_generate))
    
    initial_sequence = [4, 6, 8, 10]
    expression = ['*', ['+', 'i', 2], 2]
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))
    

    initial_sequence = [4, 6, 8, 10]
    expression = ['+', 2, 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))

    initial_sequence = [0, 1]
    expression = 'x'
    length_to_generate = 6
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))

    initial_sequence = [0, 1]
    expression = ['+', 'x', 'y']
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))

    initial_sequence = [367, 367, 367]
    expression = 'y'
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))

    initial_sequence = [0, 1, 2]
    expression = -1 
    length_to_generate = 5
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))

    initial_sequence = [0, 1, 2]
    expression = 'i'
    length_to_generate = 0
    print(generate_rest(initial_sequence, 
                        expression, 
                        length_to_generate))

def test_6():
    sequence = [0, 1, 2, 3, 4, 5, 6, 7]
    the_rest = predict_rest(sequence)
    print(sequence)
    print(the_rest)

    sequence = [0, 2, 4, 6, 8, 10, 12, 14]
    print(predict_rest(sequence))

    sequence = [31, 29, 27, 25, 23, 21]
    print(predict_rest(sequence))

    sequence = [0, 1, 4, 9, 16, 25, 36, 49]
    print(predict_rest(sequence))

    sequence = [3, 2, 3, 6, 11, 18, 27, 38]
    print(predict_rest(sequence))

    sequence =  [0, 1, 1, 2, 3, 5, 8, 13]
    print(predict_rest(sequence))

    sequence = [0, -1, 1, 0, 1, -1, 2, -1]
    print(predict_rest(sequence))

    sequence = [1, 3, -5, 13, -31, 75, -181, 437]
    print(predict_rest(sequence))


def main():
    print("\nTest 1:")
    test_1()

    print("\nTest 2:")
    test_2()

    print("\nTest 3:")
    test_3()

    print("\nTest 4:")
    test_4()

    print("\nTest 5:")
    test_5()

    print("\nTest 6:")
    test_6()

main()