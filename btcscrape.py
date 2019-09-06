f __name__ == '__main__': 
    main()
def main(): 
    '''My main btc scrape'''
   	from urllib import request 
	import json 
	from pprint import pprint
	from datetime import datetime, date, time
	import sqlite3
	import time

	while True: 
   	 url = 'https://api.coindesk.com/v1/bpi/currentprice/GBP.json'
    	 header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

   	 req = request.Request(url, headers=header)
   	 conn = sqlite3.connect(r'C:\projects\BitCoinProj\crypto')
   	 c = conn.cursor()
    
   	 with request.urlopen(req) as data: 
       	 	jdata = json.load(data)
        	pprint(jdata)
       		dt = datetime.strptime(jdata['time']['updateduk'], "%b %d, %Y at %H:%M BST")
        	rate = jdata['bpi']['GBP']['rate_float']
        	currency = jdata['bpi']['GBP']['code']
        	param = (dt, currency, rate)
        	c.execute('INSERT INTO BTC (pricedate , currency , rate)VALUES(?,?,?)', param)
        	conn.commit()
        	conn.close()
        	time.sleep(60)