import requests
from bs4 import BeautifulSoup
import os, os.path, csv 


url = "http://www.espn.com/college-sports/football/recruiting/databaseresults/_/sportid/24/class/2006/sort/school/starsfilter/GT/ratingfilter/GT/statuscommit/Commitments/statusuncommit/Uncommited"
respondez = requests.get(url)

soup =BeautifulSoup(respondez.text,"html.parser")

blah_List = []

#print (soup)
#soup gives us the full template of the html file

for blah in soup.find_all("tr"):
	if "oddrow" in blah["class"] or "evenrow" in blah["class"]:
		name = blah.find("div", class_="name").a.get_text()
		#print (name)
		hometown = blah.find_all("td")[1].get_text()
		#print(hometown)
		school = hometown[hometown.find(",")+4:]
		#print (school)
		city = hometown[:hometown.find(",")+4]
		#print (city)
		position = blah.find_all("td")[2].get_text()
		#print (position)
		grade = blah.find_all("td")[4].get_text()
		#print (grade)
		blah_List.append([name, school, city, position, grade])
		#print (blah_List)


with open("footballers.csv",'a', encoding= 'utf-8') as toWrite:
	writer = csv.writer(toWrite)
	writer.writerows(blah_List)

print("ESPN College Football listings fetched. ")
