# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS
import requests
import json

#https://store.steampowered.com/api/appdetails/?appids=730

def crawler_init():

	steam_appid = '1500'
	req = requests.get('https://store.steampowered.com/api/appdetails/?appids='+steam_appid) 
	
	if req.status_code != 200:
		print ('Falha ao baixar pagina')
		exit(1)

	parsed_json = json.loads(req.text)

	#get Characteristics
	list_data = list()
	list_data.append(parsed_json[steam_appid]['data']['type'])
	list_data.append(parsed_json[steam_appid]['data']['name'])
	list_data.append(parsed_json[steam_appid]['data']['required_age'])
	#list_data.append(parsed_json[steam_appid]['data']['controller_support'])
	list_data.append(parsed_json[steam_appid]['data']['is_free'])
	print(list_data)

	#get detailed_description
	detailed_description = parsed_json[steam_appid]['data']['detailed_description']

	#get about_the_game
	about_the_game = parsed_json[steam_appid]['data']['about_the_game']

	#get short_description
	short_description = parsed_json[steam_appid]['data']['short_description']

	#get supported_languages
	supported_languages = parsed_json[steam_appid]['data']['supported_languages']

	#get header_image
	try:
		header_image = parsed_json[steam_appid]['data']['header_image']
	except:
		print('Não possui imagem de cabeçalho!\n')

	#get website
	try:
		website = parsed_json[steam_appid]['data']['website']
	except:
		print('Não possui website!\n')

	#get requiriments
	#Windowns
	try:
		pc_requirements = parsed_json[steam_appid]['data']['pc_requirements']
	except:
		print('Não possui requirimentos para Windowns\n')

	#MAC
	try:
		mac_requiriments = parsed_json[steam_appid]['data']['mac_requirements']
	except:
		print('Não possui requirimentos para MAC\n')

	#Linux
	try:
		linux_requiriments = parsed_json[steam_appid]['data']['linux_requirements']
	except:
		print('Não possui requirimentos para Linux\n')

	#get developers
	list_developers = list()
	try:
		for developer in parsed_json[steam_appid]['data']['developers']:
			list_developers.append(developer)
	except:
		print('Não possui Desenvolvedores cadastrados\n')

	#get price_overview
	dict_price = {}
	try:
		dict_price = {'currency':parsed_json[steam_appid]['data']['price_overview']['currency'], 'initial':parsed_json[steam_appid]['data']['price_overview']['initial'], 'final':parsed_json[steam_appid]['data']['price_overview']['final'], 'final_formatted':parsed_json[steam_appid]['data']['price_overview']['final_formatted']}
	except:
		print('Preço Não Encontrado, ou jogo gŕatis')
	print(dict_price)

	# get platforms
	list_platforms = list()
	try:
		for platform in parsed_json[steam_appid]['data']['platforms'].keys():
			if(parsed_json[steam_appid]['data']['platforms'][str(platform)] == True):
				list_platforms.append(platform)
	except:
		print('Não possui plataformas cadastradas\n')


	#get metacritic
	list_metacritic = list()
	try:
		for info in parsed_json[steam_appid]['data']['metacritic'].values():
			list_metacritic.append(info)
	except:
		print('Não possui nota no metacritic\n')

	#get categories
	list_categories = list()
	for categorie in parsed_json[steam_appid]['data']['categories']:
		list_categories.append(categorie['description'])

	#get genres
	list_genres = list()
	for genre in parsed_json[steam_appid]['data']['genres']:
		list_genres.append(genre['description'])

	#get screenshots
	list_screenshots = list()
	for link in parsed_json[steam_appid]['data']['screenshots']:
		try:
			dict_links = {'path_thumbnail':str(link['path_thumbnail']), 'path_full':str(link['path_full'])}
			list_screenshots.append(dict_links)
		except:
			print('Link screenshot não encontrado\n')

	#get movies
	list_movies = list()
	for link in parsed_json[steam_appid]['data']['movies']:
		try:
			dict_links = {'name':str(link['name']), 'thumbnail':str(link['thumbnail']), '480':str(link['webm']['480']), 'max':str(link['webm']['max'])}
			list_movies.append(dict_links)
		except:
			print('Link vídeo não encontrado\n')
	
	#get recommendations
	try:
		recommendations = parsed_json[steam_appid]['data']['recommendations']['total']
	except:
		print('Jogo não possui recomendações')
	print(recommendations)

	#get release_date
	try:
		dict_date = {'coming_soon':parsed_json[steam_appid]['data']['release_date']['coming_soon'], 'date':str(parsed_json[steam_appid]['data']['release_date']['date'])}
	except:
		print('Não foi encontrada a data de lançamento')
	print(dict_date)



crawler_init()