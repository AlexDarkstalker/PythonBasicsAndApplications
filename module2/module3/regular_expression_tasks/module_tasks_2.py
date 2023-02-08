import re


pattern_1 = r"ab*a"
pattern_2 = r"ab+a"
pattern_3 = r"ab?a"
pattern_4 = r"ab{2,4}a"
string = "aa aba abba abbba abbbba"
print(re.findall(pattern_1, string))
print(re.findall(pattern_2, string))
print(re.findall(pattern_3, string))
print(re.findall(pattern_4, string))

pattern_greed = r"a[ab]+a"
pattern_generous = r"a[ab]+?a"
string_2 = "abaaba"
print(re.findall(pattern_greed, string_2))
print(re.findall(pattern_generous, string_2))

pattern_group = r"(test|text)*"
string_3 = "texttext"
print(re.match(pattern_group, string_3))

pattern_group_2 = r"((abc)|(test|text)*)"
string_4 = "abc"
print(re.match(pattern_group_2, string_4), re.match(pattern_group_2, string_4).groups(), sep='\n')
print(re.match(pattern_group_2, string_3), re.match(pattern_group_2, string_3).groups(), sep='\n')

pattern_hello = r"Hello (abc|test)"
string_hello = "Hello abc"
match = re.match(pattern_hello, string_hello)
print(match, match.group(0), match.group(1), sep='\n')

pattern_group_3 = r"(\w+)-\1"
string_5 = "test-test"
string_6 = "text-test"
string_7 = "text-text chow-chow"
print(re.match(pattern_group_3, string_5))
print(re.match(pattern_group_3, string_6))
print(re.sub(pattern_group_3, r"\1", string_7))

pattern_group_4 = r"((\w+)-\2)"
print(re.findall(pattern_group_4, string_7))
print(re.match(pattern_group_4, string_7))
print(re.search(pattern_group_4, string_7))
print(re.sub(pattern_group_4, r"\2", string_7))

print(re.match(r"text", "TEXT", re.IGNORECASE))
print(re.match(r"(te)*xt", "TEXT", re.IGNORECASE | re.DEBUG))
print(re.match(r"(te)*?xt", "TEXT", re.IGNORECASE | re.DEBUG))

