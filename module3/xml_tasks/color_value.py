from xml.etree import ElementTree


def count_color_values(elem, level, color_values):
    color_values[elem.attrib["color"]] += level
    for child in elem:
        count_color_values(child, level + 1, color_values)
    return color_values


xml_string = input()
tree = ElementTree.ElementTree(ElementTree.fromstring(xml_string))
root = tree.getroot()
color_values = {"red": 0, "green": 0, "blue": 0}
print(*count_color_values(root, 1, color_values).values())
