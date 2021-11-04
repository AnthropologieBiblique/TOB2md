#!/usr/bin/env python3


import os
import csv
import markdownify
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
import fileinput

def telechargerVersets(livre, chapitre):
	# Téléchargement d'un chapitre de la bible AELF sur aelf.org/bible
	try:
	    url = "http://otremolet.free.fr/otbiblio/bible/"+livre+chapitre+'.html'
	    headers = {}
	    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
	    req = urllib.request.Request(url, headers = headers)
	    resp = urllib.request.urlopen(req)
	    respData = resp.read().decode('utf-8')
	    saveFile = open('temp.html','w')
	    saveFile.write(str(respData))
	    saveFile.close()
	except Exception as e:
	    print(str(e))
	
	# Ouverture du html pour parsing
	file = open('temp.html', 'r')
	contents = file.read()
	soup = BeautifulSoup(contents, 'html.parser')
	
	indiceVerset = re.compile(":([0-9|a-z]{1,3})")
	flag = False
	for data in soup.find_all():
		if data.name == "i":
			if indiceVerset.search(data.getText()) == None:
				pass
			else:
				print(indiceVerset.search(data.getText()).group(1))
		if data.name == "td":
			if data.attrs != {}:
				flag = True
			else:
				if flag == True:
					print(data.getText().replace('\t','').replace('\n',' '))
					flag = False

telechargerVersets("ancien/ecclesiaste%0d/qo","12")
