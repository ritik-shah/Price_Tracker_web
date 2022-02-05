from bs4 import BeautifulSoup
from DBConnection import Db
URL="https://www.amazon.in/dp/9354227260/ref=syn_sd_onsite_desktop_332?psc=1&pd_rd_w=VfJUX&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBUVhES01TRlVHTFMmZW5jcnlwdGVkSWQ9QTA0MTAyMzkxTjE2NURHVDBMVk1HJmVuY3J5cHRlZEFkSWQ9QTAzMDE1NzNGOVdGRjMwVlg4Q1omd2lkZ2V0TmFtZT1zZF9vbnNpdGVfZGVza3RvcCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
import requests
# headers_Get = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Accept-Encoding': 'gzip, deflate',
#         'DNT': '1',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1'
#     }
c=Db()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
}
r = requests.get(URL, headers=headers)
# print(r.text)
soup = BeautifulSoup(r.content,'html.parser')


f=soup.findAll("span",class_= "a-offscreen")


f=soup.findAll("span",class_= "a-price a-text-price a-size-medium apexPriceToPay")


price=""

# print(len(f))
for i in f:
    price=i.text

if len(f)==0:
    f=soup.findAll("span",class_="a-size-base a-color-price a-color-price")
    for i in f:
        price = i.text
if len(f)==0:
    f=soup.find("span",class_= "a-price-whole")
    price = i.text
print(price)
qry="INSERT INTO prevprice (pbid,pr_date,pr_amt,pr_time) values ('',curdate(),'"+price+"',curtime())"
res=c.insert(qry)
