from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(open("krolowiePolscy.html"), features="lxml")

print(soup.prettify())