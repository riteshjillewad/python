import ast

code = "a = 10"

tree = ast.parse(code)

print(ast.dump(tree, indent=4))