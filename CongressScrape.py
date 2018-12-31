from bs4 import BeautifulSoup
import requests as req
import time
import re
headers = {'User-Agent': 'Mozilla/5.0'}

def get_link_list(page_link, last_page_num):
	if last_page_num == 'All':
		page_response = req.get(page_link, headers=headers, timeout=5)
		page_content = BeautifulSoup(page_response.content, "html.parser")
		last_page = page_content.find('a',attrs={'class':'last'})
		last_page_link = last_page.get('href')
		last_page_num = re.sub('.*?([0-9]*)$',r'\1',last_page_link)
		time.sleep(2)
		
	def get_next_link():
		last = int(page_link[-1:])
		y=last + 1
		return page_link[:-1]+str(y)



	linkList= []
	counter	= 1
	while(int(re.sub('.*?([0-9]*)$',r'\1', page_link))!=last_page_num+1):

		page_response = req.get(page_link, headers=headers, timeout=5)
		page_content = BeautifulSoup(page_response.content, "html.parser")	


		elems = page_content.find_all('li', attrs={'class':'expanded'})

		
		for elem in elems:
			span = elem.find('span', attrs={'class':'result-heading'})
			linkList.append(span.a.get('href'))
		
		

		page_link = get_next_link()
		print(counter)
		counter+=1
		time.sleep(2)

	return linkList

	
linkList = get_link_list('https://www.congress.gov/search?q={%22source%22%3A%22legislation%22}&page=1', 1)

for n in range(len(linkList)):
	print(linkList[n])