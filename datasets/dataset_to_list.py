import re

f = open("./usca312.txt", "r")
lines = f.read()
matches = re.findall(r"\d", lines)
print(matches)
