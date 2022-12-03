# List Duplicate Lines in a file
# 
print("-"*40)
print("List Duplicate Lines in a file")
print("-"*40)
print("")

from pathlib import Path

file_read = Path('arquivo.txt').read_text()
convert_list = file_read.splitlines()
result = set(convert_list)
print(*result, sep = '\n')

