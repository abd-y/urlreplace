# urlreplace
Replace list of url quary parameters. This script replace only the spicified parameter with user spicified quary.
inspierd by qsreplace.
# help
```
usage: urlreplace [-h] [-u URLS] [-p PARAMETERS] [-v VALUE] [-no-url-encode]
                  [-m MATCH]

replace list of url quary parameters.

optional arguments:
  -h, --help      show this help message and exit
  -u URLS         urls file path
  -p PARAMETERS   parameter names file path
  -v VALUE        replace the query with a value
  -no-url-encode  no url encode.
  -m MATCH        the value that exists in the parameter Example: for file
                  path '/' or for url 'http' Note: value must be on all urls
                  provided
```
# Example
The following example will replace all url quaries that have redirect parameter with "https://example.com"
```
python3 urlreplace.py -u endpoints.txt -p redirect -v https://example.com -m http
```
