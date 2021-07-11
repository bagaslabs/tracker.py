from urllib import request
import json
import os
import time
from time import sleep

R = '\033[31m' # merah
G = '\033[32m' # hijau
C = '\033[36m' # biru
W = '\033[0m' # putih

print(G + "IP TRACKER " + W + "🇮🇩")
print(" ")
print(G + "Version =" + C + " 1.6.0")
print(" ")
print(G +'Progam start...')
sleep(0.99)

print(G + "======================================================")






while True:
    #input Ip
    Ip = input(G + "ENTER IP : " + C)
    
    
    print(G +"LOOKING FOR IP :" + C + Ip + G + (" Loading..."))
    sleep(2)
    url = "http://ip-api.com/json/"
    r = request.urlopen(url + Ip)
    data = r.read()
    m = json.loads(data)
    
    print(G + "======================================================")
    
    print(f"""    
    status : {m['status']}
    IP : {m['query']}
    country : {m['country']}
    countryCode: {m['countryCode']}
    city : {m['city']}
    region : {m['region']}
    region name:{m['regionName']}
    timezone : {m['timezone']}
    ISP : {m['isp']}
    Organization : {m['org']}
    zip : {m['zip']}
    latitude : {m['lat']}
    longitude : {m['lon']}
    org : {m['org']}
    as : {m['as']}
    """)
    
    latitude = (f"""{m['lat']}""")
    longtitude = (f"""{m['lon']}""")
    	
    
    print("[+] MAP LOCATION :")
    link = (C + "https://www.google.com/maps/place/")
    
    link_map = print(link + latitude + "+" + longtitude )
    
    print("")
    print("")
    print("""
    
    
    
    
    
    
    """)
    
    
    
    
    
    
    
  
    
    
  
   
  
   
   
    