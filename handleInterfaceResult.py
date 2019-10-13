import requests
import re
import json
#r1=requests.get("http://piaofang.maoyan.com/second-box")
#print(r1.text)

def require():
    import requests
    import json
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
    url = 'http://piaofang.maoyan.com/second-box'
    #s = json.dumps({'coin_type': 'bch', 'coin_address': '192Vrf3A9HZU3BhSYatm4eTeVAadASZpxH','actual_amount':'0.001','access_id':'C16F3EF3EB3A4391B1C1FA64CBBDD70A','tonce':y})
    r= requests.get(url, headers=headers)
    return r.text
r1=require()
result=json.loads(r1)
#print(result['data']['list'])
l=result['data']['list']
#print(len(l))
fileName = 'movie2.txt'
for i in range(0,len(l)):
    print(l[i]['movieName'])
    with open(fileName, 'a') as file_obj:
        file_obj.write(l[i]['movieName']+'\n')
