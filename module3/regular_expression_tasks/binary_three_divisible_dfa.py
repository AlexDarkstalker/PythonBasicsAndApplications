import sys
import re


pattern = r"\b(0|(1(01*0)*1))+$"
for line in sys.stdin:
    line = line.strip()
    if re.match(pattern, line):
        print(line)
