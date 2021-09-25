import re


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


f = open("./usca312.txt", "r")
lines = f.read()
matches = re.findall(r"\d", lines)
numbers = list(map(int, matches))
chunks_list = list(chunks(numbers, 312))
print(chunks_list)
