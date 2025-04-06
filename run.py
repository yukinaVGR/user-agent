import requests as r,os
from bs4 import BeautifulSoup as par
# subscribe yt gwe banh 
loop=0
def awal ():
	vgr=[]
	os.system("clear")
	global loop 
	x=par(r.get("https://whatmyuseragent.com/browser",headers={"user-agent":"Mozilla/5.0"}).content,"html.parser")
	f=x.select("ul.list-group li.list-group-item a")
	for z in f:
		loop+=1
		href=z["href"].strip()
		type=z.text.strip()
		print(f"{loop}. {type} • {href}")
		vgr.append((type, href))
	try:
		pilih=int(input("Masukkan Type User Agent : "))
		if 1 <= pilih <= len(vgr):
			nama,href = vgr[pilih-1]
			print(f"Kamu Memilih Type {nama}")
			get_ua(href)
		else:
			print(f"Nomor Yang anda masukkan tidak valid")
	except ValueError:
		print(f"Harus angka yang dimasukkan ! ")
			
def get_ua(url):
	name=url.split("/")[3]
	x=par(r.get(f"https://whatmyuseragent.com{url}").content,"html.parser")
	y=x.select("tbody tr")
	for row in y:
		i=row.select_one("td.useragent")
		print(i.text.strip())
		with open(f"{name}.txt","w") as f:
			f.write(i.text.strip())
	print(f"Berhasil Mengambil Useragent. Useragent Disimpan Ke {name}.txt")
if __name__ == "__main__":
	awal()