from django.shortcuts import render
import feedparser
from tech import __sites


def get_articles(rss):

    feed = feedparser.parse(rss)
    articles = []
    for entry in feed['entries'][:9]:
        # desc = ''
        # if 'description' in entry:
        #     desc = entry.description.split('</a>')[-1]
        #     desc = desc.split('<')[0]
        # elif 'summary' in entry:
        #     desc = entry.summary.split('</a>')[-1]
        #     desc = desc.split('<')[0]
        # if desc == '':
        #     desc = entry.title

        data = {'title': entry.title, 'url': entry.link}
        articles.append(data)
    return articles


# Create your views here.
def index(request):
    sites = []
    for site in __sites:
        sites.append({'name': site.name, 'url': site.url, 'articles': get_articles(site.rss_link)})
    return render(request, 'tech.html', {'sites': sites})
