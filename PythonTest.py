from lxml import html
import requests
import csv


page = requests.get('https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1')
tree = html.fromstring(page.content)
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow(["Movie Name" , "Movie Length (min)" , "Movie Type" , "Descreption" , "Director" , "Stars" , "Image URL"])

a = 1
a1 = 0
while a < 8 and a1 < 8: 
 name = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/h4/a/text()' % a)                                              
 time = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/p/time/text()' % a)
 type = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/p/span[1]/text()' % a)
 type1 = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/p/span[3]/text()' % a)
 type2 = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/p/span[5]/text()'  % a)
 type3= tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/p/span[7]/text()'  % a)
 Desc = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/div[2]/text()' % a)
 dir = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/div[3]/span/span/a/text()' % a)
 star = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/div[4]/span[1]/span/a/text()'  % a)
 star1 = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/div[4]/span[2]/span/a/text()' % a)
 star2 = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/div[4]/span[3]/span/a/text()' % a)
 star3 = tree.xpath('//*[@id="main"]/div/div[2]/div[%a]/table/tbody/tr[1]/td[2]/div[4]/span[4]/span/a/text()' % a)
 imurl = tree.xpath('//*[@id="img_primary"]/div/a/div/img/@src')
 ur = [a.split(",")for a in imurl]
 imgu = ur[a1]
 with open('index.csv', 'a') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow([name, time,[ type ,type1, type2,type3] , Desc , dir , [star , star1, star2, star3],imgu])  
 a += 1
 a1 += 1  





a = 1
a1 = 7
while a < 12 and a1 < 17:  
 name = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/h4/a/text()' % a)             
 time = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/p/time/text()' % a)
 type = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/p/span[1]/text()' % a)
 type1 = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/p/span[3]/text()' % a)
 type2 = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/p/span[5]/text()'  % a)
 type3= tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/p/span[7]/text()'  % a)
 Desc = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/div[2]/text()' % a)
 dir = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/div[3]/span/span/a/text()' % a)
 star = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/div[4]/span[1]/span/a/text()'  % a)
 star1 = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/div[4]/span[2]/span/a/text()' % a)
 star2 = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/div[4]/span[3]/span/a/text()' % a)
 star3 = tree.xpath('//*[@id="main"]/div/div[3]/div[%a]/table/tbody/tr[1]/td[2]/div[4]/span[4]/span/a/text()' % a)
 imurl = tree.xpath('//*[@id="img_primary"]/div/a/div/img/@src')
 ur = [a.split(",")for a in imurl]
 imgu = ur[a1]
 with open('index.csv', 'a') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow([name, time,[ type ,type1, type2,type3] , Desc , dir , [star , star1, star2, star3] , imgu])
 a += 1
 a1 += 1

print('Movies Information was downloaded......')


   

      
      



