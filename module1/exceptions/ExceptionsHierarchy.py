def get_inherited(exception, exceptions_hierarchy, inherited_set):
    inherited_set.add(exception)
    if exception in exceptions_hierarchy.keys():
        for exc in exceptions_hierarchy[exception]:
            if exc not in inherited_set:
                inherited_set.add(exc)
                inherited_set |= get_inherited(exc, exceptions_hierarchy, inherited_set)
        return inherited_set
    else:
        return inherited_set


num_exceptions = int(input())
exceptions_hierarchy = {}
for i in range(num_exceptions):
    exception_string = input()
    if exception_string.__contains__(':'):
        k = exception_string.split(':')[0].strip()
        for ex in exception_string.split(':')[1].split():
            if ex in exceptions_hierarchy.keys():
                exceptions_hierarchy[ex].append(k)
            else:
                exceptions_hierarchy[ex] = [k]
    else:
        k = exception_string.strip()
        if k not in exceptions_hierarchy.keys():
            v = []
            exceptions_hierarchy[k] = v
num_called_exceptions = int(input())
inherited_set = set()
redundant_exceptions = []
for i in range(num_called_exceptions):
    exception = input()
    if exception in inherited_set and exception not in redundant_exceptions:
        redundant_exceptions.append(exception)
    inherited_set |= get_inherited(exception, exceptions_hierarchy, inherited_set)
print(*redundant_exceptions, sep='\n')
