import sys
import re


pattern = r"\b(\w)(\w)"
for line in sys.stdin:
    line = line.strip()
    print(re.sub(pattern, r"\2\1", line))
