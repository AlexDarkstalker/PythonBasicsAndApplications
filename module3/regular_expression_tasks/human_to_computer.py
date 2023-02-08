import sys
import re


pattern = r"human"
for line in sys.stdin:
    line = line.strip()
    print(re.sub(pattern, "computer", line))
