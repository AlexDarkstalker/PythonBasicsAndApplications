import json


def get_inherited(cur_class, classes_inherited, inherited_set):
    for child in classes_inherited[cur_class]:
        if child in classes_inherited.keys() and child not in inherited_set:
            inherited_set.add(child)
            inherited_set.update(get_inherited(child, classes_inherited, inherited_set))
    return inherited_set


data_list = json.loads(input())
class_inheritance = {}
for elem in data_list:
    for parent in elem["parents"]:
        if parent in class_inheritance.keys():
            class_inheritance[parent].add(elem["name"])
        else:
            class_inheritance[parent] = set()
            class_inheritance[parent].add(elem["name"])
    if elem["name"] not in class_inheritance.keys():
        class_inheritance[elem["name"]] = set()
    # print(class_inheritance)
for cls in sorted(class_inheritance.keys()):
    cls_children_set = set()
    print(cls, ":", len(get_inherited(cls, class_inheritance, cls_children_set)) + 1)
