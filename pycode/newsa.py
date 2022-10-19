#
# import pprint
# import requests
#
#
# secret = "4622d33bb0ba4108b976f32bee7476f9"
#
# # Define the endpoint
# url = 'https://newsapi.org/v2/everything?'
#
# # Specify the query and
# # number of returns
# parameters = {
# 	'q': 'merkel', # query phrase
# 	'pageSize': 100, # maximum is 100
# 	'apiKey': secret # your own API key
# }
#
# # Make the request
# response = requests.get(url,
# 						params = parameters)
#
# # Convert the response to
# # JSON format and pretty print it
# response_json = response.json()
# pprint.pprint(response_json)
#
# from newsapi import NewsApiClient
# import pycountry
# secret = "4622d33bb0ba4108b976f32bee7476f9"
#
# # you have to get your api key from newapi.com and then paste it below
# newsapi = NewsApiClient(api_key=secret)
#
# qr = input("Keyword: ")
# try:
# 	input_countries = []
#
# 	while True:
# 		input_countries.append(input("Country:  \n (ctrl+c when finished)"))
#
# # if the input is not-integer, just print the list
# except:
# 	print(f"Selected countries: {input_countries}")
#
# countries = {}
#
# # iterate over all the countries in
# # the world using pycountry module
# for country in pycountry.countries:
#
# 	# and store the unique code of each country
# 	# in the dictionary along with it's full name
# 	countries[country.name] = country.alpha_2
#
# # now we will check that the entered country name is
# # valid or invalid using the unique code
# codes = [countries.get(country.title(), 'Unknown code')
# 		for country in input_countries]
#
# # now we have to display all the categories from which user will
# # decide and enter the name of that category
# option = input("Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
#
# # now we will fetch the new according to the choice of the user
# top_headlines = newsapi.get_top_headlines(q=qr ,
#
# 	# getting top headlines from all the news channels
# 	category=f'{option.lower()}',language='en', country=f'{codes[0].lower()}')
#
# # fetch the top news inder that category
# Headlines = top_headlines['articles']
#
# # now we will display the that news with a good readability for user
# if Headlines:
# 		for articles in Headlines:
# 			b = articles['title'][::-1].index("-")
# 			if "news" in (articles['title'][-b+1:]).lower():
# 				print(
# 					f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
# 			else:
# 				print(
# 					f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
# 	else:
# 		print(
# 			f"Sorry no articles found for {input_countries}!")
#
# all_articles = newsapi.get_everything(q='Biden',
#                                       domains='lemonde.fr',
#                                       sort_by='relevancy')
#
# all_articles.fromkeys(articles)
# all_articles.keys()
#
# import pandas as pd
# df=pd.DataFrame(all_articles.get("articles"))
# df.content
#
#
