def count_overlap(t, s):
    count_ = 0
    start = 0
    while True:
        start = t.find(s, start) + 1
        if start > 0:
            count_ += 1
        else:
            return count_


input_str = input()
input_to_find = input()
print(count_overlap(input_str, input_to_find))
