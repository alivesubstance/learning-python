__author__ = 'jericho'

s = "12345qwerty"
for c in s:
    print ord(c),

print '\n', [ord(c) for c in s]

for tuple in list(enumerate(s)):
    print ord(s[tuple[0]]),

print '\n'

for idx in range(len(s)):
    print ord(s[idx]),

print '\n'

for tuple in list(enumerate(s)):
    for t in tuple:
        print ord(s[t]),
        break

print '\n'

i=0
while i < len(s):
    print ord(s[i]),
    i += 1

sum = 0
for c in s:
    sum += ord(c)
print "\nsum=", sum

arr = []
for c in s:
    arr.append([ord(c)])
print "\n", arr

print "map(ord, s)=", map(ord, s)
