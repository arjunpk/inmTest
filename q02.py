#!/usr/bin/python

def reverse(s):
    return ''.join([s[i] for i in xrange(len(s)-1, -1, -1)])

ip=raw_input("String to be reversed:")

print "Using Custom Function"
print reverse(ip)

print "Using InBuilt Function"
print ''.join(reversed(ip))
