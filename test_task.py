import tokenize
import ast


def calc_fix_comments(filename):
    reports = 0
    with open(filename, 'rb') as f:
        tokens = tokenize.tokenize(f.readline)
        for token in tokens:
            if token.type == 60:
                if 'TODO' in token.string or 'FIXME' in token.string:
                    reports += 1
    return reports


def prepare_ast(filename):
    with open(filename) as f:
        code = f.read()
    root = ast.parse(code)
    return root


def define_parents(root):
    for node in ast.walk(root):
        for child in ast.iter_child_nodes(node):
            child.parent = node


def calc_names(node):
    var_names = Counter()
    func_names = Counter()
    define_parents(node)
    for i in ast.walk(node):
        if isinstance(i, ast.FunctionDef):
            func_names += Counter({i.name: 1})
        if isinstance(i, ast.Name):
            name = i.id
            if not isinstance(i.parent, ast.Call):
                var_names += Counter({name: 1})
            else:
                if i in i.parent.args:
                    var_names += Counter({name: 1})
                else:
                    func_names += Counter({name: 1})
    return var_names, func_names


# Task 1
print(calc_fix_comments('test.py'))

# Task 2
print(calc_names(prepare_ast('test.py'))[0])

# Task 3
print(calc_names(prepare_ast('test.py'))[1])
