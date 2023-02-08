import re


x = "hello\nworld"
print(x)
x = r"hello\nworld"
print(x)
print(re.match)
print(re.search)
print(re.findall)
print(re.sub)

pattern = r"abc"
string_1 = "abcd"
string_2 = "babcd"
print(re.match(pattern, string_1))
print(re.match(pattern, string_2))
print(re.search(pattern, string_1))
print(re.search(pattern, string_2))

pattern_1 = r"a[abc]c"
strings = "abc, aac, acc"
print(re.findall(pattern_1, strings))
print(re.sub(pattern_1, "abc", strings))

pattern_2 = r"a[a-zA-Z]c"
strings_1 = "abc, aac, acc, anc, aMc"
print(re.findall(pattern_2, strings_1))
print(re.sub(pattern_2, "abc", strings_1))

pattern_3 = r"a[^a-zA-Z]c"
strings_2 = "abc, a.c, acc, a-c, aMc"
print(re.findall(pattern_3, strings_2))
print(re.sub(pattern_3, "abc", strings_2))
