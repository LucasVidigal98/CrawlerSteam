# -*- coding: utf-8 -*-
#
from bs4 import BeautifulSoup as BS
import requests
import json

def crawler_review():

	req = requests.get('https://steamcommunity.com/app/730/homecontent/?userreviewscursor=AoIFP%2Bv2QIAAAAB98NPaAQ%3D%3D&userreviewsoffset=60&p=7&workshopitemspage=7&readytouseitemspage=7&mtxitemspage=7&itemspage=7&screenshotspage=7&videospage=7&artpage=7&allguidepage=7&webguidepage=7&integratedguidepage=7&discussionspage=7&numperpage=10&browsefilter=trendweek&browsefilter=trendweek&appid=730&appHubSubSection=10&appHubSubSection=10&l=brazilian&filterLanguage=default&searchText=&forceanon=1')
	soup = BS(req.text, 'html.parser')
	file = open('cOMPER.html', 'w')
	file.write(req.text)
	file.close()
	reviews = soup.find_all(class_='apphub_Card modalContentLink interactable')
	user_info = soup.find_all(class_='apphub_CardContentAuthorName offline ellipsis')
	avatars = soup.find_all(class_='appHubIconHolder offline')

	print(len(reviews))
	print(user_info)

	#Coleta informações do usuário
	steam_id = ''
	name_steam = ''

	list_names = list()
	list_steam_id = list()

	for info in user_info:
		steam_id = str(info.find_all('a'))
		name_steam = str(info.find_all('a'))
		print(steam_id[10:steam_id.rfind('"')])
		list_steam_id.append(steam_id[10:steam_id.rfind("\"")])
		print(name_steam[steam_id.rfind('"')+2:steam_id.rfind('<')])
		list_names.append(name_steam[steam_id.rfind("\"")+2:steam_id.rfind('<')])

	#Coletar o avatar do usuário
	avatar_list = list()

	for avatar in avatars:
		c_avatar = str(avatar)
		print(c_avatar[48:c_avatar.rfind('"')])
		avatar_list.append(c_avatar)

	#Coletar as horas jogadas pelo usuario que fez o comentário
	hours_list = list()

	for hour in reviews:
		c_hour = str(hour.find_all(class_='hours'))
		print(c_hour[20:c_hour.rfind('<')])
		hours_list.append(c_hour)

	#Coletar tipo da recomendação. Recomenda / Não recomenda
	recommendations_list = list()

	for recommendation in reviews:
		type_recommendation = str(recommendation.find_all(class_='title'))
		print(type_recommendation[20:type_recommendation.rfind('<')])
		recommendations_list.append(type_recommendation[20:type_recommendation.rfind('<')])

	#Coletar a data do comentário/recomendação
	date_list = list()

	for date in reviews:
		c_date = str(date.find_all(class_='date_posted'))
		print(c_date[37:c_date.rfind('<')])
		date_list.append(c_date)

	#Coletar o conteúdo do comentário/avaliação

	reviews_list = list()

	for review in reviews:
		c_review = str(review.find_all(class_='apphub_CardTextContent'))
		#Remover tabs da string
		no_tab = c_review[95:c_review.rfind('<')].split('\t')
		reviews_list.append(no_tab[12])

		print(reviews_list)

	#print(teste[3].find_all(class_='apphub_CardTextContent'))
	
	#print(bnext[0].find_all('a'))

	#t = str(teste[0])
	#print(t[88:])
	#print(teste2)

	'''
	dic = {'zoio':'angu'}
	parsed_json = json.dumps(dic)
	print(parsed_json)
	'''



crawler_review()