# HTML downloader script

import requests
from bs4 import BeautifulSoup

def download(url, fname = "index.html"):
	with open(fname, 'w') as f:
		try:
			content = requests.get(url).content
			soup = BeautifulSoup(content, "lxml")
			html = soup.prettify()
			f.write(html)
			
			return html
		except:
			print("Error")

