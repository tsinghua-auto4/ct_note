import re

target = input().rstrip()
ptn    = input().rstrip()

pattern = re.compile(ptn)

print(len(pattern.findall(target)))