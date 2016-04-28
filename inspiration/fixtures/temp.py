import ast

a = []
a.append(1)
a.append(2)

print(str(a))

b = str(a)

c = ast.literal_eval(b)

print(type(c))