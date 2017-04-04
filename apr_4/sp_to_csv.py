from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

def table_to_csv():

	req = Request('http://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500.html', headers={'User-Agent': 'Mozilla/5.0'})
	webpage = urlopen(req).read()

	bsobj = BeautifulSoup(webpage, "html.parser")
	table = bsobj.find("table",{"id":"quotesFuturesProductTable1"})
	# print(table)
	rows = table.findAll("tr")
	csvFile = open("sp_emini2.csv", 'wt')
	writer = csv.writer(csvFile)

	for row in rows:
		print(row)
		csvRow = []
		for cell in row.findAll(['td','th']):
			print(cell)
			csvRow.append(cell.get_text())
		# print(csvRow)

		writer.writerow(csvRow)


table_to_csv()

