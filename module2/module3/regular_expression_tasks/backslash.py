import sys
import re


pattern = r"\\"
for line in sys.stdin:
    line = line.strip()
    if re.search(pattern, line):
        print(line)
