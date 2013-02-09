__author__ = 'mdzhachvadze'

file_name="../rule.txt"
file = open(file_name, 'r')
words = file.read().split()
file.close()

dict = {}
for word in words:
    if dict.has_key(word):
        dict[word] += 1
    else:
        dict[word] = 1

for key in dict.keys():
    print key,'->',dict[key]