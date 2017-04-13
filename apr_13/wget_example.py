import wget
import re

def spdrHoldings(string):
    data = []
    file_url = 'http://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Holdings/Export/ExportCsv?symbol='
    etf = wget.download(file_url + string)

    with open(etf,'r',errors='replace') as holdings:
        for line in holdings.readlines()[2:]:
            # print(line)
            #cleaning line a bit and split it
            split_line = line.replace('"','').strip().split(',')[:-1]
#             print(split_line)
#             we have to change volume, check split_line[6]
            # print(split_line[6])
#             converting volume into int
            if "K" in split_line[6]:
                split_line[6] = int(float(re.sub('["".KM]', '', split_line[6])))*1000
            elif "M" in split_line[6]:
                split_line[6] = int(float(re.sub('["".KM]', '', split_line[6])))*1000000
#             coverting last price into int
#             print(split_line[3])
            split_line[3] = int(float(re.sub('[""]', '', split_line[3])))
#             print(split_line[3])

            data.append(list(split_line))
    
        print(data)
        # return data
spdrHoldings("XLF")
