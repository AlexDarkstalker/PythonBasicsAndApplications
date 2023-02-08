import sys
import re


pattern = r"z.{3}z"
for line in sys.stdin:
    line = line.strip()
    if re.search(pattern, line):
        print(line)
