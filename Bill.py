class Bill:
	'''Contains all the information about a congressional bill'''
	def __init__(self, name, years, congress_num, sponser, sponsers_party,
				num_cosponsers, bill_type, bill_link, path_to_text):
		
		'''
		
		Args:
			name           (str): Name of the Bill
			years          (str): 2 year congressional session
			congress_num   (int): Congress Number
			sponser        (str): Name of person who sponsered the Bill
			sponsers_party (str): Sponser's political party
			num_cosponsers (str): Number of cosponsers
			bill_type      (str): Bill Type (Bill, Resolution, Joint Resolution, etc.)
			bill_link      (str): Url to bill
			path_to_text   (str): file path to saved copy of Bill Text
		
		'''
		self.name = name
		self.years = years
		self.congress_num = congress_num
		self.sponser = sponser
		self.sponsers_party = sponsers_party
		self.num_cosponsers = num_cosponsers
		self.bill_type = bill_type
		self.bill_link = bill_link
		self.path_to_text=path_to_text
	
	def text(self):
		#return text of bill from file
		pass