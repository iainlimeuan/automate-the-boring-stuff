from re import L
import sys, requests, webbrowser, bs4

print('Searching...')

res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

links = bs4.BeautifulSoup(res.text, 'html.parser')

openLinks = links.select('.package-snippet')

numOpen = min(5, len(links))

# Range starts at 0 by default.
# Note that the 'href' attribute value in the returned elements do not
# have the initial https://pypi.org part, so that part has to be concatenated
# to the href attribute value.

for i in range(numOpen): 
    urlToOpen = 'https://pypi.org' + openLinks[i].get('href')
    print('Opening ' + urlToOpen)
    webbrowser.open(urlToOpen)





