from bs4 import BeautifulSoup as bs

import requests

import csv

url = 'www.nuforc.org/webreports/ndxevent.html'
r = requests.get('http://' + str(url))
data = r.text

soup = bs (data, 'html5lib')

l = []
test = [['one', 'two'], [3,4]]

for link in soup.find_all ('a'):
	print (link.get('href'))
	
	new_url = 'www.nuforc.org/webreports/' + str (link.get('href'))
	new_r = requests.get('http://' + str (new_url))
	new_data = new_r.text
	
	new_soup = bs (new_data, 'html5lib')
	
	for item in new_soup.find_all('tr'):
		temp_list = []
		for detail in item.find_all('td'):
			temp_list.append(detail.get_text())
		l.append(temp_list)

with open ('ufo_data.csv', 'wt') as myfile:
	wr = csv.writer(myfile)
	try:
		wr.writerows(l)
	except:
		print ('err')

#for each in l:
	#print (each)	
	#print (new_soup.prettify)
	

