# Made by RomaSimp1e
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common import keys
url = 'https://www.infocar.ua/'

headers = {
	'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}


req = requests.get(url, headers=headers)
src = req.text
# print(src)

with open('infocar.html', 'w') as file:
	file.write(src)
#
# def infocar():
# 	with open('infocar.html') as file:
# 		src = file.read()
#
#
# 	soup = BeautifulSoup(src, 'lxml')
# 	print('---------------------------------------------------------------------------------------')
#
# 	print('Infocar.ua')
#
# 	print('---------------------------------------------------------------------------------------')
#
#
# 	sublinks = soup.find(class_='sublinks').find_all(['a'])
# 	for i in sublinks:
# 		i_text = i.text
# 		i_url = i.get('href')
# 		print(f"{i_text}: https:{i_url}")
#
# 	print('---------------------------------------------------------------------------------------')
#
#
# 	newcars = soup.find(class_='newcars').find_all(['a'])
# 	for j in newcars:
# 		j_text = j.text
# 		j_url = j.get('href')
# 		print(f'{j_text}: https:{j_url}')
#
# 	print('---------------------------------------------------------------------------------------')
#
# 	topcars = soup.find(class_='topmarks').find_all(['a'])
# 	for t in topcars:
# 		t_tx = t.text
# 		t_url = t.get('href')
# 		print(f'{t_tx}: https:{t_url}')
#
# 	print('---------------------------------------------------------------------------------------')
# 	videos = soup.find(id='videos').find_all(['a', 'title'])
# 	for v in videos:
# 		v_text = v.text
# 		v_url = v.get('href')
# 		print(f'{v_text}: https:{v_url}')
#
# 	print('---------------------------------------------------------------------------------------')
#
# 	socials = soup.find(id='socials').find_all('a')
# 	for c in socials:
# 		c_tx = c.text
# 		c_url = c.get('href')
# 		print(f'{c_tx}: https:{c_url}')
#
# 	print('---------------------------------------------------------------------------------------')
#
#
# print('-' * 160)
#
#
# if __name__ == '__main__':
# 	infocar()
	
	