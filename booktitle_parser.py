from lxml import etree
import sys

# 검색할 booktitle
search_booktitle = sys.argv[1]
if len(sys.argv) != 2:
    print("Insufficient arguments")
    sys.exit()

# DBLP XML 파일 로드
dblp_file = 'bkrankings/dblp.xml'
tree = etree.parse(dblp_file)
root = tree.getroot()

# booktitle 엘리먼트 검색
booktitles = root.xpath(f'//booktitle[text()="{search_booktitle}"]')

# 검색된 booktitle 출력
for booktitle in booktitles:
    # booktitle 엘리먼트의 부모 엘리먼트에 접근하여 논문 정보 가져오기
    paper = booktitle.getparent()
    title = paper.find('title').text
    authors = [author.text for author in paper.xpath('author')]
    year = paper.find('year').text
    
    print(f'Title: {title}')
    print(f'Authors: {", ".join(authors)}')
    print(f'Year: {year}')
    print(f'Booktitle: {search_booktitle}')
    print('-' * 50)

