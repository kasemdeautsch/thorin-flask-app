import os

# file = open("dump.txt", "r")
# content = file.read()
# print(content)
# file.close()

# with open("dump.txt", "r") as file:
#     data = file.read()
#     print(data)

# with open("dump.txt", "r") as file:
#     for line in file:
#         print(line, end="->>")

# with open("dump.txt", "r") as file:
#     print(file.read(50))

# with open("dump.txt", "r") as file:
#     print(file.readline())

with open("dump.txt", "r") as file:
    lines = file.readlines()
    # print(lines[1])
    for line in lines:
        print(line, end="")