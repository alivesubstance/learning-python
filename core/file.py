__author__ = 'mdzhachvadze'

f = open('test', 'w')
f.write("I am\n")
f.write("Supa star")
f.close()

f = open('test', 'r')

bytes = f.read()
print bytes

print bytes.split()

f.close()

