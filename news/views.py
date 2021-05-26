from django.shortcuts import render
import feedparser
from news.models import Site, Article


def get_news(rss, source):
    try:
        articles = Article.objects.get(source=source)
        articles.delete()
    except Exception:
        pass

    feed = feedparser.parse(rss)
    news = []
    for entry in feed['entries'][:6]:
        desc = ''
        if 'description' in entry:
            desc = entry.description.split('</a>')[-1]
            desc = desc.split('<')[0]
        elif 'summary' in entry:
            desc = entry.summary.split('</a>')[-1]
            desc = desc.split('<')[0]
        if desc == '':
            desc = entry.title

        published = 'Day, 00 Jan 0000'
        if 'published' in entry:
            published = entry.published
        elif 'pubDate' in entry:
            published = entry.pubDate

        published = published.split(' ')[1:4]
        print(published)

        data = {'heading': entry.title, 'summary': desc, 'date': published[0], 'month': published[1], 'url': entry.link}
        news.append(data)

        date = published[0] + ' ' + published[1] + ' ' + published[2]
        article = Article(heading=entry.title, summary=desc, published_date=date, url=entry.link, source=source)
        article.save()
    return news


# Create your views here.
def index(request):
    sites = []
    chk_boxes = []
    if request.method == 'POST':
        for site in Site.objects.all():
            isChecked = ''
            if request.POST.get(site.short_name + '-news-chkbox'):
                sites.append({'name': site.name, 'url': site.url, 'news_list': get_news(site.rss_link, site.name)})
                isChecked = 'checked'
            chk_boxes.append({'name': site.name, 'shrt_name': site.short_name, 'isChecked': isChecked})
    else:
        for site in Site.objects.all():
            sites.append({'name': site.name, 'url': site.url, 'news_list': get_news(site.rss_link, site.name)})
            chk_boxes.append({'name': site.name, 'shrt_name': site.short_name, 'isChecked': 'checked'})

    return render(request, 'news.html', {'sites': sites, 'chk_boxes': chk_boxes})
