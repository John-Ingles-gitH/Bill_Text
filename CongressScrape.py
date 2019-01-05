from bs4 import BeautifulSoup
import requests as req
import time
import re
headers = {'User-Agent': 'Mozilla/5.0'}

def get_link_list(page_link, pages_to_get):
	#Returns a list of urls, one for each Bill/Resolution on a search results page of congress.gov
	
	page_response = req.get(page_link, headers=headers, timeout=5)
	page_content = BeautifulSoup(page_response.content, "html.parser")
	last_page = page_content.find('a',attrs={'class':'last'}).get('href')
	last_page_num = int(re.sub('.*?([0-9]*)$',r'\1',last_page))
	time.sleep(2)#needed to follow congress.gov's crawl limit
	
	#Ensure pages_to_get isn't less than 1 or more than number of available pages
	if pages_to_get == "All":
		pages_to_get = last_page_num
	if pages_to_get <1:
		raise Exception('pages_to_get should not be less than 1')
	if pages_to_get > last_page_num:
		raise Exception('pages_to_get should not exceed '+str(last_page_num))
	
	
		
	def get_next_link():
		#Convert page link to next page link
		#Ex. website.com/page=5 ->website.com/page=6
		last = int(page_link[-1:])
		y=last + 1
		return page_link[:-1]+str(y)

	link_list= []
	counter	= 1
	while(int(re.sub('.*?([0-9]*)$',r'\1', page_link))!=pages_to_get+1):

		page_response = req.get(page_link, headers=headers, timeout=5)
		page_content = BeautifulSoup(page_response.content, "html.parser")	
		
		elems = page_content.find_all('li', attrs={'class':'expanded'})

		for elem in elems:
			span = elem.find('span', attrs={'class':'result-heading'})
			link_list.append(span.a.get('href'))

		page_link = get_next_link()
		print(counter)
		counter+=1
		time.sleep(2)#needed to follow congress.gov's crawl limit

	return link_list

	
link_list = get_link_list('https://www.congress.gov/search?q={%22source%22%3A%22legislation%22}&page=1',3)

for n in range(len(link_list)):
	print(link_list[n])