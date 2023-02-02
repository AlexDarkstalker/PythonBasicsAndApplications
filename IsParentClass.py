def is_parent(param, param1, classes_inheritance):
    if not classes_inheritance.keys().__contains__(param1):
        return False
    if param == param1 or classes_inheritance[param1].__contains__(param):
        return True
    elif len(classes_inheritance[param1]) > 0:
        result = False
        for claz in classes_inheritance[param1]:
            result |= is_parent(param, claz, classes_inheritance)
        return result
    return False


num_classes = int(input())
classes_inheritance = {}
for i in range(num_classes):
    inheritance_string = input()
    if inheritance_string.__contains__(':'):
        k = inheritance_string.split(':')[0].strip()
        v = list(inheritance_string.split(':')[1].split())
    else:
        k = inheritance_string.strip()
        v = []
    classes_inheritance[k] = v
num_queries = int(input())
answers = [False] * num_queries
for i in range(num_queries):
    queru = input().split()
    answers[i] = "Yes" if is_parent(queru[0], queru[1], classes_inheritance) else "No"
print(classes_inheritance)
print(*answers, sep='\n')
