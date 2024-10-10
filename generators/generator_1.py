# def file_read():
#     with open('files/test.txt', 'r') as f:
#         for line in f:
#             yield line

# print('\n')
# for ch in file_read():
#     print(ch)

with open('files/test.txt', 'r') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()

