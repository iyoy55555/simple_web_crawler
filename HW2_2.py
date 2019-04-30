import urllib.request
import ssl
import re
 
ssl._create_default_https_context = ssl._create_unverified_context
author_name=input("Input Author:")
author=author_name.replace(" ","+")
url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = '\"authors\">[\s\S]*?</p>'

result = re.findall(pattern,html_str)
co_workers=[]
for r in result:
	author=r.split("<a href=")[1].split("</a>")[0].strip()
	if(author.split(">")[1] != author_name):
		co_workers.append(author.split(">")[1])

co_workers.sort()
count=0;
for i in range(len(co_workers)):
	if(i==0):
		count+=1
	else:
		if(co_workers[i]==co_workers[i-1]):
			count+=1
		else:
			print(co_workers[i-1]+":"+str(count)+" times")
			count=1
