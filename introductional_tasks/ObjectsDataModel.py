count = 0
unique_objects = []
for obj in objects:
    if id(obj) not in unique_objects:
        unique_objects.append(id(obj))
print(len(unique_objects))
