from bs4 import BeautifulSoup

URL="https://www.amazon.in/dp/9354227260/ref=syn_sd_onsite_desktop_332?psc=1&pd_rd_w=VfJUX&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBUVhES01TRlVHTFMmZW5jcnlwdGVkSWQ9QTA0MTAyMzkxTjE2NURHVDBMVk1HJmVuY3J5cHRlZEFkSWQ9QTAzMDE1NzNGOVdGRjMwVlg4Q1omd2lkZ2V0TmFtZT1zZF9vbnNpdGVfZGVza3RvcCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1",
}

r=requests.get(URL,headers=headers)

soup=BeautifulSoup(r.content,'html.parser')


print(r.content)


with open("a.txt",'w') as a:
    a.write(str(r.content))
    a.close()

# f=soup.findAll("ul",class_="a-unordered-list a-nostyle a-button-list a-horizontal")
# print(len(f))
# for i in f:
#      print(i.text)