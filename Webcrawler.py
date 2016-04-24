# Add comment for test
import requests
from bs4 import BeautifulSoup

url="http://www.imdb.com/chart/top"
source_code=requests.get(url)
plain_text=source_code.text
soup = BeautifulSoup(plain_text, "html.parser")
list_soup = soup.findAll('td', {'class': 'titleColumn'})
count=1
file_name = 'book_list.txt'
file_content = ''
for movie_info in list_soup:
    movie_str=str(movie_info.find('a'))
    start = movie_str.find('title',11)
    qudiao = movie_str[start:]
    left = qudiao.find('>')
    right = qudiao.find('<')
    movie = qudiao[left+1:right]
    file_content += '%d\t%s\n'%(count,movie)
    count += 1
f = open(file_name, 'w')
f.write(file_content)
f.close()

