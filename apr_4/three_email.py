from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def fetching_url():

	html = urlopen("http://clickaces.com/contact/")
	bsobj = BeautifulSoup(html.read(), "html.parser")
	emails = bsobj.findAll(text=re.compile(r"[\w\.-]+@[\w\.-]+"))
	# emails = bsobj.findAll(text=re.compile(r"[A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)"))

	for email in emails:
		print(email)

fetching_url()


import ssl
context = ssl._create_unverified_context()
context=context