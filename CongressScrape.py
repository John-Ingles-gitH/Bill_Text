from bs4 import BeautifulSoup
import requests as req
import time
import re
headers = {'User-Agent': 'Mozilla/5.0'}

def getBillAttrs(page_link, pages_to_get):
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
		
	def getNextLink():
		#Convert page link to next page link
		#Ex. website.com/page=5 ->website.com/page=6
		last = int(page_link[-1:])
		y=last + 1
		return page_link[:-1]+str(y)

	link_list= []
	name_list=[]
	years_list=[]
	congress_num_list=[]
	sponsor_list=[]
	num_cosponsors_list=[]
	sponsor_party_list=[]
	date_introduced_list=[]
	counter	= 1
	while(int(re.sub('.*?([0-9]*)$',r'\1', page_link))!=pages_to_get+1):

		page_response = req.get(page_link, headers=headers, timeout=5)
		page_content = BeautifulSoup(page_response.content, "html.parser")	
		
		link_elems = page_content.find_all('li', attrs={'class':'expanded'})

		for elem in link_elems:
			span1 = elem.find('span', attrs={'class':'result-heading'})
			span2 = elem.find_all('span', attrs={'class':'result-item'})
			
			#get bill sponsor, cosponsor, and sponsor's party
			for elem2 in span2:
				if elem2.find('strong').text == 'Sponsor:':
					date_introduced=re.sub('.*(\d\d\/\d\d\/\d\d\d\d).*',r'\1',elem2.text).strip()
					date_introduced_list.append(date_introduced)
					sponsor = elem2.find_all('a')[0].text
					sponsor_party=re.sub('.*\[([RD]).+\]',r'\1',sponsor)
					sponsor = re.sub('(.*)\[.*\]',r'\1',sponsor).strip()
					sponsor_party_list.append(sponsor_party)
					sponsor_list.append(sponsor)
					num_cosponsors=int(elem2.find_all('a')[1].text)
					num_cosponsors_list.append(num_cosponsors)
					
			#get bill hyperlink
			link=span1.a.get('href')
			
			#get bill name
			name=span1.a.text
			
			#get session years and congress number
			years=span1.text
			m=re.search('((\d+)st|(\d+)nd|(\d+)rd|(\d+)th)',years, re.IGNORECASE)
			congress_num = m.group(1)[:-2]
			years=years[years.find("(")+1:years.find(")")]
			
			#add each bill attribute to a list
			link_list.append(link)
			name_list.append(name)
			years_list.append(years)
			congress_num_list.append(congress_num)
				
		#iterate page
		page_link = getNextLink()
		print(counter)
		counter+=1
		time.sleep(2)#needed to follow congress.gov's crawl limit

	return link_list, name_list, years_list, congress_num_list, sponsor_list, num_cosponsors_list, sponsor_party_list, date_introduced_list

link_list, name_list, years_list, congress_num_list, sponsor_list, num_cosponsors_list, sponsor_party_list, date_introduced_list = getBillAttrs('https://www.congress.gov/search?q={%22source%22%3A%22legislation%22}&page=1',1)

for n in range(len(link_list)):
	print(link_list[n])
	print(name_list[n])
	print(years_list[n])
	print(congress_num_list[n])
	print(sponsor_list[n])
	print(num_cosponsors_list[n])
	print(sponsor_party_list[n])
	print(date_introduced_list[n])