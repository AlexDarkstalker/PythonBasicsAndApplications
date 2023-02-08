import sys
import re


pattern = r"([01]+?)$"
for line in sys.stdin:
    line = line.strip()
    if re.match(pattern, line):
        if int(re.match(pattern, line).group(1), 2) % 3 == 0:
            print(line)
