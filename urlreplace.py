#!/usr/bin/python3
import urllib.parse
import argparse

parser = argparse.ArgumentParser(description="replace list of url quary parameters.")
parser.add_argument("-u", dest="urls", help="urls file path")
parser.add_argument("-p", dest="parameters", help="parameter names file path")
parser.add_argument("-v", dest="value", help="replace the query with a value")
parser.add_argument("-no-url-encode", dest="urlencode", help="no url encode.", action="store_true")
parser.add_argument("-m", dest="match", help="the value that exists in the parameter Example: for file path '/' or for url 'http' Note: value must be on all urls provided")

args = parser.parse_args()

def replace():
	file = open(args.urls, 'r').read().split("\n")
	parameters = open(args.parameters, 'r').read().split('\n')

	for i in file:
		for j in parameters:
			if j in i:
				index = i.index("=" + args.match)
				if "&" in i[index:len(i)]:
					substring = i[index:len(i)]
					ind = substring.index("&")
					ind = len(substring) - ind
					if not args.urlencode:
						print(i.replace(i[index:len(i) - ind], '=' + urllib.parse.quote(args.value, safe='')))
					else:
						print(i.replace(i[index:len(i) - ind], '=' + args.value))
				else:
					if not args.urlencode:
						print(i.replace(i[index:len(i)], '=' + urllib.parse.quote(args.value, safe='')))
					else:
						print(i.replace(i[index:len(i)], '=' + args.value))
				break

try:
	replace()
except ValueError:
	print("value: '" + args.match + "' not found, value must be in all urls")

except:
	parser.print_help()
