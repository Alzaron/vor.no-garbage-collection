import json
import requests
import bs4
appkey = ""
kommunenr = ""
gatenavn = ""
gatekode = ""
husnr = ""
url = "https://komteksky.norkart.no/komtek.renovasjonwebapi/api/tommekalender/?kommunenr="+kommunenr+"&gatenavn="+gatenavn+"&gatekode="+gatekode+"&husnr="+husnr+" HTTP/1.1"






headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
    'Host': "norkartrenovasjon.azurewebsites.net",
    'Sec-Ch-Ua': "Chromium",
    'Content-Type': "undefined",
    'Renovasjonappkey': appkey,
    'Kommunenr': kommunenr,
    'Accept': "*/*",
    'Origin': "https://www.vor.no",
    'Sec-Fetch-Site': "cross-site",
    'Sec-Fetch-Mode': "cors",
    'Sec-Fetch-Dest': "empty",
    'Referer': "https://www.vor.no/",
    'Accept-Encoding': "gzip, deflate",
    'Accept-Language': "en-US,en;q=0.9",
    'Connection': "close"

    }

#print("GET", url, headers)
response = requests.get(url, headers=headers)



r =response.text


print(r)
