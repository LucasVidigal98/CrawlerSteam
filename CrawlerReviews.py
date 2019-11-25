# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS
import requests
import json
import urllib.parse

def crawler_reviews(appid, name, recommendations):
	
	if int(recommendations) == 0:
		return 

	if int(recommendations) > 1000000:
		n_rec = int(int(recommendations) / 3)
	elif int(recommendations) > 500000:
		n_rec = int(int(recommendations) / 2)
	else:
		n_rec = int(recommendations)

	id_review = 0
	first = True
	trouble = False
	number_pages = int(int(n_rec/10))
	page = 1
	count_trouble = 0

	while page < number_pages:

		req = ''

		print('Cometários coletados até o momento = ' + str(id_review) + ' de ' + str(n_rec), end='\r')
		#print('Coletando cometários Jogo '+ str(name) + ' Página ' + str(page) + ' de ' + str(number_pages), end='\n')

		if trouble == False:

			if first == True:
				req = requests.get('https://steamcommunity.com/app/'+str(appid)+'/homecontent/?p='+str(page)+'&workshopitemspage='+str(page)+'&readytouseitemspage='+str(page)+'&mtxitemspage='+str(page)+'&itemspage='+str(page)+'&screenshotspage='+str(page)+'&videospage='+str(page)+'&artpage='+str(page)+'&allguidepage='+str(page)+'&webguidepage='+str(page)+'&integratedguidepage='+str(page)+'&discussionspage='+str(page)+'&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid='+str(appid)+'snr=1_5_100010_&l=brazilian&appHubSubSection=10&filterLanguage=default&searchText=forceanon=1')
				first = False

			else:
				req = requests.get('https://steamcommunity.com/app/'+str(appid)+'/homecontent/?userreviewscursor='+urllib.parse.quote(userreviewscursor)+'&userreviewsoffset='+userreviewsoffset+'&p='+str(page)+'&workshopitemspage='+str(page)+'&readytouseitemspage='+str(page)+'&mtxitemspage='+str(page)+'&itemspage='+str(page)+'&screenshotspage='+str(page)+'&videospage='+str(page)+'&artpage='+str(page)+'&allguidepage='+str(page)+'&webguidepage='+str(page)+'&integratedguidepage='+str(page)+'&discussionspage='+str(page)+'&numperpage=10browsefilter=toprated&browsefilter=toprated&appid='+str(appid)+'snr=1_5_100010_&l=brazilian&appHubSubSection=10&filterLanguage=default&searchText=forceanon=1')
		
		else:

			if count_trouble >= 5:
				break

			print('aqui2')
			print(count_trouble)
			try:
				req = requests.get('https://steamcommunity.com/app/'+str(appid)+'/homecontent/?userreviewscursor='+urllib.parse.quote(userreviewscursor)+'&userreviewsoffset='+userreviewsoffset+'&p='+str(page)+'&workshopitemspage='+str(page)+'&readytouseitemspage='+str(page)+'&mtxitemspage='+str(page)+'&itemspage='+str(page)+'&screenshotspage='+str(page)+'&videospage='+str(page)+'&artpage='+str(page)+'&allguidepage='+str(page)+'&webguidepage='+str(page)+'&integratedguidepage='+str(page)+'&discussionspage='+str(page)+'&numperpage=10browsefilter=toprated&browsefilter=toprated&appid='+str(appid)+'snr=1_5_100010_&l=brazilian&appHubSubSection=10&filterLanguage=default&searchText=forceanon=1')
				trouble = False
			except:
				try:
					req = requests.get('https://steamcommunity.com/app/'+str(appid)+'/homecontent/?p='+str(page)+'&workshopitemspage='+str(page)+'&readytouseitemspage='+str(page)+'&mtxitemspage='+str(page)+'&itemspage='+str(page)+'&screenshotspage='+str(page)+'&videospage='+str(page)+'&artpage='+str(page)+'&allguidepage='+str(page)+'&webguidepage='+str(page)+'&integratedguidepage='+str(page)+'&discussionspage='+str(page)+'&numperpage=10&browsefilter=toprated&browsefilter=toprated&appid='+str(appid)+'snr=1_5_100010_&l=brazilian&appHubSubSection=10&filterLanguage=default&searchText=forceanon=1')
					trouble = False
				except:
					pass

		soup = BS(req.text, 'html.parser')
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
			list_steam_id.append(steam_id[10:steam_id.rfind("\"")])
			list_names.append(name_steam[steam_id.rfind("\"")+2:steam_id.rfind('<')])
			avatar_list.append(avatar[11:avatar.rfind('"')])

		#Coletar as horas jogadas pelo usuario que fez o comentário
		hours_list = list()

		for hour in reviews:
			c_hour = str(hour.find_all(class_='hours'))
			hours_list.append(c_hour[20:c_hour.rfind('<')])

		#Coletar tipo da recomendação. Recomenda / Não recomenda
		recommendations_list = list()

		for recommendation in reviews:
			type_recommendation = str(recommendation.find_all(class_='title'))
			recommendations_list.append(type_recommendation[20:type_recommendation.rfind('<')])

		#Coletar a data do comentário/recomendação
		date_list = list()

		for date in reviews:
			c_date = str(date.find_all(class_='date_posted'))
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
				try:
					reviews_list.append(no_tab[10])
				except:
					reviews_list.append('')
				
		#Criar o json do comentário/recomendação

		content_reviews = dict()
		if len(reviews) == len(user_info):

			for i in range(0, len(reviews)):
				content = {'user':list_names[i], 'steam_id':list_steam_id[i], 'avatar':avatar_list[i], 'hours':hours_list[i], 'recommendation':recommendations_list[i], 'date':date_list[i], 'review':reviews_list[i]}
				content_reviews.update({id_review:content})
				id_review += 1

			parsed_json = json.dumps(content_reviews)
			file = open('Games/'+ str(name) +'/Page'+str(page)+'Reviews.json', 'w')
			file.write(parsed_json)
			file.close()

		try:
			user_cards = soup.find_all('input')
			userreviewscursor = str(user_cards[0])
			userreviewscursor = userreviewscursor[53:userreviewscursor.rfind('"')]
			userreviewsoffset = str(user_cards[1])
			userreviewsoffset = userreviewsoffset[53:userreviewsoffset.rfind('"')]
			count_trouble = 0
			'''
			file = open('Html/cOMPER.html', 'w')
			file.write(req.text)
			file.close()
			'''
			page += 1
		except:
			print('Aqui1')
			trouble = True
			count_trouble += 1
			continue