import requests
import json
import re
output = requests.get('https://scanner.tradingview.com/india/scan')
content = output.text
parse_json = json.loads(content)
nsedata = parse_json['data']
print (nsedata)
for exact in nsedata: # function to print NSE data only
    exactdata = exact['s']
    #nselist = re.findall(',exactdata)
    #print (nselist)
    print (exactdata) # printing data with BSE and NSE both
