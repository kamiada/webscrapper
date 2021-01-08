from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open("krolowiePolscy.html"), features="lxml")

# print(soup.prettify())  #prints everything what is in the document

finalWriter = csv.writer(open("dataFromKrolowiePolscy.csv", "w")) #the output file should be open before the rest of the code is run to write into it

finalWriter.writerow(["Name", "The beginning of the reign", "The end of the reign", "Parents"]) #first row - column names

filtered_table = soup.find_all('table', class_="wikitable")
for tr in filtered_table:
  trs = tr.find_all('tr')
  for tr2 in trs:
    tds = tr2.find_all('td')
    try:
      names = str(tds[1].get_text())
      theBeginning = str(tds[5].get_text())
      theEnd = str(tds[6].get_text())
      parents = str(tds[7].get_text())
    except:
      print("bad tr string: {}".format(tds))
      continue
    finalWriter.writerow([names, theBeginning, theEnd, parents]) #oh boy, it works