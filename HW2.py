import urllib.request
import ssl
import re
import matplotlib.pyplot as plt

ssl._create_default_https_context = ssl._create_unverified_context
author=input("Input Author:")
author=author.replace(" ","+")
url = "https://arxiv.org/search/?query=" + author + "&searchtype=author"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = '\"is-size-7\">[\s\S]*?</p>'
pages_pattern="pagination-list\">[\s\S]*?</ul>"
result = re.findall(pattern,html_str)
pages=re.findall(pages_pattern,html_str)
years=[]
announce_year=[]
num_of_papers=[]

print("[Author: "+ author +']')

for r in result:
	date = r.split("announced</span>")[1].split(".")[0].strip()
	years.append(date.split(' ')[1])

#find the number of pages
page_count=len(pages[0].split("<li>"))

for i in range(2,page_count):
	url="https://arxiv.org/search/?query=" + author + "&searchtype=author&start="+str((i-1)*50)
	content=urllib.request.urlopen(url)
	html_str = content.read().decode('utf-8')
	result = re.findall(pattern,html_str)
	for r in result:
		date=r.split("announced</span>")[1].split(".")[0].strip()
		years.append(date.split(' ')[1])

years.sort()


#plot it
announce_year.append(years[0])
num_of_papers.append(0)
for y in years:
	if(y!=announce_year[len(announce_year)-1]):
		announce_year.append(y)
		num_of_papers.append(0)
	num_of_papers[len(announce_year)-1]+=1

print(announce_year)
print(num_of_papers)
plt.bar(announce_year,num_of_papers)
plt.show()
