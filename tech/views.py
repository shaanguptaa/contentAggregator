from django.shortcuts import render
import feedparser
from tech.models import TechSite, TechArticle


def get_articles(rss, source):
    try:
        tech_articles = TechArticle.objects.get(source=source)
        tech_articles.delete()
    except Exception:
        pass

    feed = feedparser.parse(rss)
    articles = []
    for entry in feed['entries']:
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

        tech_article = TechArticle(title=entry.title, url=entry.link, source=source)
        tech_article.save()

    return articles


# Create your views here.
def index(request):
    sites = []
    for site in TechSite.objects.all():
        sites.append({'name': site.name, 'url': site.url, 'articles': get_articles(site.rss_link, site.name)})
    return render(request, 'tech.html', {'sites': sites})
