from pprint import pprint
import json
import requests
from bs4 import BeautifulSoup
def Amazon_site(url):
	page=requests.get(url)
	soup=BeautifulSoup(page.text,"html.parser")
	# print(soup)
	div=soup.findAll('div',class_='_1UoZlX')
	# print(div)
	big_list=[]
	for i in div:
		# print(raiting)
		dict_1={}
		a=i.find('div',class_='_1-2Iqu row')
		mobil_name=a.find('div',class_='_3wU53n').text
		p=i.find('div',class_="_1vC4OE _2rQ-NK").text
		price=p[1:]	
		raiting=i.find('div',class_='hGSR34')
		if raiting != None:
			dict_1['rating']=raiting.get_text()
		
		var=i.find_all('li',class_='tVe95H')
		list_details=[]
		for k in var:
			list_details.append(k.get_text())
		# print(list_details)
		dict_1['name']=mobil_name
		dict_1['price']=price
		dict_1['ram']=list_details[0]
		dict_1["display"]=list_details[1]
		dict_1["camera"]=list_details[2]
		dict_1['Battery']=list_details[3]
		dict_1['Processor']=list_details[4]
		if len(list_details) == 6:
			dict_1['Brand and warranty']=list_details[5]
		# pprint(dict_1)
		big_list.append(dict_1)


	return (big_list)
# pprint(Amazon_site(link))

url_link='https://www.flipkart.com/search?q=all+4g+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6&as-pos=0&as-type=RECENT&as-searchtext=all%204g'
def all_flipkatd_detaild(link):
	page=requests.get(link)
	soup=BeautifulSoup(page.text,"html.parser")
	# print(soup)
	div=soup.find('nav',class_='_1ypTlJ')
	link=div.find_all('a')
	# print(div)
	add=1
	big_dict={}
	for j in link[:len(link)-1]:
		# a=j['href']
		link_mobil="https://www.flipkart.com"+j['href']
		all_data=Amazon_site(link_mobil)
		big_dict[add]=all_data
		file=str(add)+'.json'
		with open(file,"w+") as smal_file:
			json.dump(all_data,smal_file)
		add+=1
	with open('mobile_details.json','w+') as new_file:
		json.dump(big_dict,new_file)
	pprint(big_dict)

all_flipkatd_detaild(url_link)
