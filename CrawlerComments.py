# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS
import requests
import json
import urllib.parse

def crawler_review(appid):

	id_review = 0
	first = True

	for page in range(1, 5):

		req = ''

		print('Cometários coletados até o momento = ' + str(id_review))
		print('Coletando cometários Appid = '+ str(appid) + 'Página = ' + str(page))

		if first == True:
			print('Aqui')
			req = requests.get('https://steamcommunity.com/app/'+str(appid)+'/homecontent/?p='+str(page)+'&workshopitemspage='+str(page)+'&readytouseitemspage='+str(page)+'&mtxitemspage='+str(page)+'&itemspage='+str(page)+'&screenshotspage='+str(page)+'&videospage='+str(page)+'&artpage='+str(page)+'&allguidepage='+str(page)+'&webguidepage='+str(page)+'&integratedguidepage='+str(page)+'&discussionspage='+str(page)+'&numperpage=10&browsefilter=trendweek&browsefilter=trendweek&l=brazilian&appHubSubSection=10&filterLanguage=default&searchText=&forceanon=1')
			first = False
		else:
			print('Aqui2')
			req = requests.get('https://steamcommunity.com/app/'+str(appid)+'/homecontent/?userreviewscursor='+urllib.parse.quote(userreviewscursor)+'&userreviewsoffset='+userreviewsoffset+'&p='+str(page)+'&workshopitemspage='+str(page)+'&readytouseitemspage='+str(page)+'&mtxitemspage='+str(page)+'&itemspage='+str(page)+'&screenshotspage='+str(page)+'&videospage='+str(page)+'&artpage='+str(page)+'&allguidepage='+str(page)+'&webguidepage='+str(page)+'&integratedguidepage='+str(page)+'&discussionspage='+str(page)+'&numperpage=10&browsefilter=trendweek&browsefilter=trendweek&l=brazilian&appHubSubSection=10&filterLanguage=default&searchText=&forceanon=1')
		
		soup = BS(req.text, 'html.parser')
		file = open('Html/cOMPER.html', 'w')
		file.write(req.text)
		file.close()
		reviews = soup.find_all(class_='apphub_Card modalContentLink interactable')
		user_info = soup.find_all(class_='apphub_friend_block')
		avatars = soup.find_all(class_='appHubIconHolder offline')

		#Coleta informações do usuário
		list_names = list()
		list_steam_id = list()
		avatar_list = list()

		for info in user_info:
			steam_id = str(info.find_all('a'))
			name_steam = str(info.find_all('a'))
			avatar = str(info.find_all('img'))
			print(steam_id[10:steam_id.rfind('"')])
			list_steam_id.append(steam_id[10:steam_id.rfind("\"")])
			print(name_steam[steam_id.rfind('"')+2:steam_id.rfind('<')])
			list_names.append(name_steam[steam_id.rfind("\"")+2:steam_id.rfind('<')])
			print(avatar[11:avatar.rfind('"')])
			avatar_list.append(avatar[11:avatar.rfind('"')])

		#Coletar as horas jogadas pelo usuario que fez o comentário
		hours_list = list()

		for hour in reviews:
			c_hour = str(hour.find_all(class_='hours'))
			print(c_hour[20:c_hour.rfind('<')])
			hours_list.append(c_hour[20:c_hour.rfind('<')])

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
			date_list.append(c_date[37:c_date.rfind('<')])

		#Coletar o conteúdo do comentário/avaliação

		reviews_list = list()
		count = 0
		for review in reviews:
			c_review = str(review.find_all(class_='apphub_CardTextContent'))
			#Remover tabs da string
			no_tab = c_review[95:c_review.rfind('<')].split('\t')

			try:
				reviews_list.append(no_tab[12])
			except:
				reviews_list.append('')

			print(reviews_list)

		#Criar o json do comentário/recomendação

		content_reviews = dict()
		print(len(reviews))
		print(len(user_info))
		if len(reviews) == len(user_info):

			for i in range(0, len(reviews)):
				content = {'user':list_names[i], 'steam_id':list_steam_id[i], 'avatar':avatar_list[i], 'hours':hours_list[i], 'recommendation':recommendations_list[i], 'date':date_list[i], 'review':reviews_list[i]}
				print(content)
				content_reviews.update({id_review:content})
				id_review += 1

		user_cards = soup.find_all('input')
		userreviewscursor = str(user_cards[0])
		userreviewscursor = userreviewscursor[53:userreviewscursor.rfind('"')]
		print(userreviewscursor)
		userreviewsoffset = str(user_cards[1])
		userreviewsoffset = userreviewsoffset[53:userreviewsoffset.rfind('"')]
		print(userreviewsoffset)
		ok = str(input('OK: '))

	parsed_json = json.dumps(content_reviews)
	file = open("Comentarios.json", "w")
	file.write(parsed_json)
	file.close()
	print(parsed_json)



crawler_review(730)