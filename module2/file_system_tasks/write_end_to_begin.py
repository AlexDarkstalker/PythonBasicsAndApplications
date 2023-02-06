with open('dataset_24465_4.txt', 'r', encoding='utf8') as file, open('reverse_copy.txt', 'a', encoding='utf8') as wr:
    open('reverse_copy.txt', 'w').close()
    for line in reversed(list(file)):
        wr.write(line)
file.close()
wr.close()
