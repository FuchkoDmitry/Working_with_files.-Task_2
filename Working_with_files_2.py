import os
from pprint import pprint
# v1
data = {}
files_list = []
for filename in os.listdir():
    if filename.endswith('.txt'):
        files_list.append(filename)
        with open(filename, encoding='utf-8') as file:
            lines = file.read().split('\n')
            # print(lines)
            data[filename] = (len(lines), lines)
pprint(files_list)
pprint(sorted(data.values()))
pprint(len(sorted(data.values())))
print(data)

# data = {}
# lines_list = []
# for filename in os.listdir():
#     if filename.endswith('.txt'):
#         # files_list.append(filename)
#         with open(filename, encoding='utf-8') as file:
#             line = file.readline().strip()
#             lines_list.append(line)
#             # print(lines)
#             # data[filename] = (len(lines_list), lines_list)
#         print(lines_list)
#         print(data)
# print(data)
# print(os.listdir())

# if file.endswith('.txt'):
#     print('file')
print(os.getcwd())
print(os.path.join(os.getcwd()))
