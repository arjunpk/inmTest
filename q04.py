#!/usr/bin/python
import sys, getopt, re, json

def main(argv):
   	try:
      		opts, args = getopt.getopt(argv,"j:u:a:c:i:")
		
   	except getopt.GetoptError:
      		print 'Usage: q04.py -j <json file> -u <default user> -a <default api key> -c <default connection string> -i <default ip address>'
      		sys.exit(1)
	for opt, arg in opts:
		if opt == '-j':
			jsonFile = arg
		elif opt == '-u':
			user = arg
		elif opt == '-a':
			apiKey = arg
		elif opt == '-c':
			connString = arg
		elif opt == '-i':
			ipAdd = arg

	with open(jsonFile, 'r') as jFile:
		#print(json.dumps((eval(jFile.read()))))
		fStr = re.sub(r'[^A-Za-z0-9,:_\-\.]+', '', jFile.read())
		jData = dict(u.split(":") for u in fStr.split(","))
		
	with open(jsonFile, 'w')as jFile:
        	if not jData['user'] or jData['user']=="null":
                	jData['user'] = user
	        if not jData['api_key'] or jData['api_key']=="null":
        	        jData['api_key'] = apiKey
	        if not jData['conn_string'] or jData['conn_string']=="null":
        	        jData['conn_string'] = connString
	        if not jData['ip_address'] or jData['ip_address']=="null":
	                jData['ip_address'] = ipAdd
		
	        json.dump(jData, jFile)

if __name__ == "__main__":
   	main(sys.argv[1:])
