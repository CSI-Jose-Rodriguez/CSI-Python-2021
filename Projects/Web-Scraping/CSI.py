import requests
import bs4
res = requests.get('https://www.sanignacio.pr')
res.raise_for_status()
SanIgnaciopr = bs4.BeautifulSoup(res.text, 'html.parser')
elems = SanIgnaciopr.select('title')
type(SanIgnaciopr)
print(len(elems))
type(elems[0])
print(str(elems[0]))
print(elems[0].getText())