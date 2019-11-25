# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup as BS
import requests
import json
import os
from CrawlerReviews import *

#https://store.steampowered.com/api/appdetails/?appids=730

def crawler_init(id_thread, max):

	try:
		os.mkdir('Games/')
	except:
		pass


	file = open('LastGame' + str(id_thread) + '.txt', 'r')
	last = file.readline()
	file.close()

	for steam_appid in range(int(last), max):
		
		req = requests.get('https://store.steampowered.com/api/appdetails/?appids='+str(str(steam_appid))+'&l=portuguese') 

		if req.status_code != 200:
			print ('Falha ao baixar pagina appid ' + str(steam_appid))
			continue

		parsed_json = json.loads(req.text)

		#Invalid appid
		#print('appid = ' + str(steam_appid) + ' ' + str(parsed_json[str(steam_appid)]['success']), end='\r')
		if parsed_json[str(steam_appid)]['success'] == False:
			continue
		
		file = open('LastGame'+str(id_thread)+'.txt', 'w')
		file.write(str(steam_appid))
		file.close()

		dict_game = dict()

		info_dict = dict()

		dict_game.update({str(steam_appid):info_dict})

		#get Characteristics
		list_data = list()
		try:
			list_data.append(parsed_json[str(steam_appid)]['data']['type'])
		except:
			pass
		try:
			list_data.append(parsed_json[str(steam_appid)]['data']['name'])
		except:
			continue
		try:
			list_data.append(parsed_json[str(steam_appid)]['data']['required_age'])
		except:
			pass
		#list_data.append(parsed_json[str(steam_appid)]['data']['controller_support'])
		try:
			list_data.append(parsed_json[str(steam_appid)]['data']['is_free'])
		except:
			pass
		try:
			info_dict.update({'Data':list_data})
		except:
			pass

		#mkdir to game
		try:
			os.mkdir(r'Games/' + str(parsed_json[str(steam_appid)]['data']['name']))
		except:
			pass

		print('Coletando informações do jogo ' + str(parsed_json[str(steam_appid)]['data']['name']) + ' appid ' + str(steam_appid) + ' Thread ' + str(id_thread))

		#get detailed_description
		try:
			detailed_description = parsed_json[str(steam_appid)]['data']['detailed_description']
			info_dict.update({'DetailedDescription':detailed_description})
		except:
			info_dict.update({'DetailedDescription':'nao tem'})
		#get about_the_game
		try:
			about_the_game = parsed_json[str(steam_appid)]['data']['about_the_game']
			info_dict.update({'AboutTheGame':about_the_game})
		except:
			info_dict.update({'AboutTheGame':'nao tem'})

		#get short_description
		try:
			short_description = parsed_json[str(steam_appid)]['data']['short_description']
			info_dict.update({'ShortDescription':short_description})
		except:
			info_dict.update({'ShortDescription':'nao tem'})

		#get supported_languages
		try:
			supported_languages = parsed_json[str(steam_appid)]['data']['supported_languages']
			info_dict.update({'SupportedLanguages':supported_languages})
		except:
			info_dict.update({'SupportedLanguages':'nao tem'})

		#get header_image
		try:
			header_image = parsed_json[str(steam_appid)]['data']['header_image']
			info_dict.update({'HeaderImage':header_image})
		except:
			#print('Não possui imagem de cabeçalho!\n')
			info_dict.update({'HeaderImage':'Não possui imagem de cabeçalho!'})

		#get website
		try:
			website = parsed_json[str(steam_appid)]['data']['website']
			info_dict.update({'Website':website})
		except:
			#print('Não possui website!\n')
			info_dict.update({'HeaderImage':'Não possui website!'})

		#get requiriments
		#Windowns
		try:
			pc_requirements = parsed_json[str(steam_appid)]['data']['pc_requirements']
			info_dict.update({'PcRequirements':pc_requirements})
		except:
			#print('Não possui requirimentos para Windowns\n')
			info_dict.update({'HeaderImage':'Não possui requirimentos para Windowns'})

		#MAC
		try:
			mac_requirements = parsed_json[str(steam_appid)]['data']['mac_requirements']
			info_dict.update({'MacRequirements':mac_requirements})
		except:
			#print('Não possui requirimentos para MAC\n')
			info_dict.update({'HeaderImage':'Não possui requirimentos para MAC'})

		#Linux
		try:
			linux_requirements = parsed_json[str(steam_appid)]['data']['linux_requirements']
			info_dict.update({'LinuxRequirements':linux_requirements})
		except:
			#print('Não possui requirimentos para Linux\n')
			info_dict.update({'LinuxRequirements':'Não possui requirimentos para Linux'})

		#get developers
		list_developers = list()
		try:
			for developer in parsed_json[str(steam_appid)]['data']['developers']:
				list_developers.append(developer)
			info_dict.append({'Developers':list_developers})
		except:
			#print('Não possui Desenvolvedores cadastrados\n')
			info_dict.update({'Developers':'Não possui Desenvolvedores cadastrados'})

		#get price_overview
		dict_price = {}
		try:
			dict_price = {'currency':parsed_json[str(steam_appid)]['data']['price_overview']['currency'], 'initial':parsed_json[str(steam_appid)]['data']['price_overview']['initial'], 'final':parsed_json[str(steam_appid)]['data']['price_overview']['final'], 'final_formatted':parsed_json[str(steam_appid)]['data']['price_overview']['final_formatted']}
			info_dict.update({'Prices':dict_price})
		except:
			#print('Preço Não Encontrado, ou jogo gŕatis')
			info_dict.update({'Prices':'Preço Não Encontrado, ou jogo gŕatis'})

		# get platforms
		list_platforms = list()
		try:
			for platform in parsed_json[str(steam_appid)]['data']['platforms'].keys():
				if(parsed_json[str(steam_appid)]['data']['platforms'][str(platform)] == True):
					list_platforms.append(platform)
			info_dict.update({'Platforms':list_platforms})
		except:
			#print('Não possui plataformas cadastradas\n')
			info_dict.update({'Platforms':'Não possui plataformas cadastradas'})


		#get metacritic
		list_metacritic = list()
		try:
			for info in parsed_json[str(steam_appid)]['data']['metacritic'].values():
				list_metacritic.append(info)
			info_dict.update({'Metacritic':list_metacritic})
		except:
			#print('Não possui nota no metacritic\n')
			info_dict.update({'Metacritic':'Não possui nota no metacritic'})

		#get categories
		list_categories = list()
		try:
			for categorie in parsed_json[str(steam_appid)]['data']['categories']:
				list_categories.append(categorie['description'])
			info_dict.update({'Categories':list_categories})
		except:
			info_dict.update({'Categories':'Nao tem'})

		#get genres
		list_genres = list()
		try:
			for genre in parsed_json[str(steam_appid)]['data']['genres']:
				list_genres.append(genre['description'])
			info_dict.update({'Genres':list_genres})
		except:
			info_dict.update({'Genres':'Nao tem'})

		#get screenshots
		list_screenshots = list()
		try:
			for link in parsed_json[str(steam_appid)]['data']['screenshots']:
				try:
					dict_links = {'path_thumbnail':str(link['path_thumbnail']), 'path_full':str(link['path_full'])}
					list_screenshots.append(dict_links)
				except:
					continue
			info_dict.update({'Screenshots':list_screenshots})
		except:
			info_dict.update({'Screenshots':'Não possui'})

		#get movies
		list_movies = list()
		try:
			for link in parsed_json[str(steam_appid)]['data']['movies']:
				try:
					dict_links = {'name':str(link['name']), 'thumbnail':str(link['thumbnail']), '480':str(link['webm']['480']), 'max':str(link['webm']['max'])}
					list_movies.append(dict_links)
				except:
					continue
			info_dict.update({'Movies':list_movies})
		except:
			info_dict.update({'Movies':'Não possui'})
		
		#get recommendations
		try:
			recommendations = parsed_json[str(steam_appid)]['data']['recommendations']['total']
			info_dict.update({'Recommendations':recommendations})
		except:
			recommendations = 0
			print('Jogo não possui recomendações')
			info_dict.update({'Recommendations':'Jogo não possui recomendações'})

		#get release_date
		try:
			dict_date = {'coming_soon':parsed_json[str(steam_appid)]['data']['release_date']['coming_soon'], 'date':str(parsed_json[str(steam_appid)]['data']['release_date']['date'])}
			info_dict.update({'ReleaseDate':dict_date})
		except:
			print('Não foi encontrada a data de lançamento')
			info_dict.update({'ReleaseDate':'Não foi encontrada a data de lançamento'})

		try:
			file = open(r'Games/' + str(parsed_json[str(steam_appid)]['data']['name']) + '/info.json', 'w')
			final_json = json.dumps(dict_game)
			file.write(final_json)
			file.close()
		except:
			continue

		crawler_reviews(str(steam_appid), str(parsed_json[str(steam_appid)]['data']['name']), str(recommendations))