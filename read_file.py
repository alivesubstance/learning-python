__author__ = 'jericho'

file = open("/proc/meminfo", "r")

for line in file.readlines():
    print line,

file.close()