class Bill:
	'''Contains all the information about a congressional bill'''
	def __init__(self, name, years, congress_num, sponsor, sponsors_party,
				num_cosponsors, bill_type, bill_link, path_to_text
				date_introduced):
		
		'''
		
		Args:
			name           (str): Name of the Bill
			years          (str): 2 year congressional session
			congress_num   (int): Congress Number
			sponsor        (str): Name of person who sponsored the Bill
			sponsors_party (str): Sponsor's political party
			num_cosponsors (str): Number of cosponsors
			bill_type      (str): Bill Type (Bill, Resolution, Joint Resolution, etc.)
			bill_link      (str): Url to bill
			path_to_text   (str): File path to saved copy of Bill Text
			date_introduced(str): Date bill was introduced
		
		'''
		self.name = name
		self.years = years
		self.congress_num = congress_num
		self.sponseor = sponsor
		self.sponsors_party = sponsors_party
		self.num_cosponsors = num_cosponsors
		self.bill_type = bill_type
		self.bill_link = bill_link
		self.path_to_text = path_to_text
		self.date_introduced = date_introduced
	
	def text(self):
		#return text of bill from file
		pass