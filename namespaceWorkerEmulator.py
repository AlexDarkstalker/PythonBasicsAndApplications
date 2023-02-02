def create(namespace, parent):
    key = namespace
    value = (parent, [])
    global namespaces
    namespaces[key] = value


def add(namespace, var):
    global namespaces
    if namespace in namespaces.keys():
        namespaces[namespace][1].append(var)


def get(namespace, var):
    global namespaces
    if namespace == 'global' and var not in namespaces[namespace][1]:
        return None
    elif var in namespaces[namespace][1]:
        return namespace
    return get(namespaces[namespace][0], var)


def execute_command(command, namespace, arg):
    global commands
    if command in commands.keys():
        if command == 'get':
            print(get(namespace, arg))
        else:
            commands[command](namespace, arg)


namespaces = {
    'global': ('', [])
}
commands = {
    'create': create,
    'add': add,
    'get': get
            }
num_commands = int(input())
for i in range(num_commands):
    command, namespace, arg = input().split()
    execute_command(command, namespace, arg)
