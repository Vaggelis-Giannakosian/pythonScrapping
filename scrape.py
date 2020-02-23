import requests
import re
import pprint
from bs4 import BeautifulSoup


scorepattern = re.compile(r"^(\d+).*")

def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k: k['score'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        score = 0
        if len(vote):
            score = scorepattern.search(vote[0].getText()).group(1)

        if int(score) > 99:
            hn.append({'title': title, 'link': href, 'score': score})
    return sort_stories_by_votes(hn)

hn = []
links = []
subtext = []
for i in range(1,3):
    res = requests.get(f'https://news.ycombinator.com/news?p={i}')
    soup = BeautifulSoup(res.text, 'html.parser')
    links = links + soup.select('.storylink')
    subtext = subtext + soup.select('.subtext')

hn = create_custom_hn(links,subtext)
pprint.pprint(len(hn))
pprint.pprint(hn)


