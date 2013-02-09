__author__ = 'jericho'

s = "spam"
print s[:1] + "l" + s[2:]
print "sl" + s[2:]
print s[-4:-3] + "l" + s[-2:0]

l = list(s)
l[1]="l"
print str(l)