#!/usr/bin/python

for i in range (1, 101):
	print i,("fizzbuzz" if (i % 5 == 0) else "fizz") if (i % 3 == 0) else ("buzz" if (i % 5 == 0) else "")
	

#(i%3=0?(i%5=0?"fizzbuzz":"fizz"):(i%5=0?"buzz":i))
