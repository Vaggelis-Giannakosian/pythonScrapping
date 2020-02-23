import requests
import re
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

scorepattern = re.compile(r"^(\d+).*")

def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k: k['score'],reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        score = 0
        if len(vote):
            score = scorepattern.search(vote[0].getText()).group(1)


        if int(score) > 100 :
            hn.append({'title': title, 'link': href, 'score': score})
    return sort_stories_by_votes(hn)


hn = create_custom_hn(links, subtext)
print(len(hn))
pprint.pprint(hn)

# print(votes[0].get('id'))
# print(links)
# print(votes)
