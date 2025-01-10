from django.shortcuts import render
from dateutil.parser import parse
import feedparser
from news import __sites


def get_news(rss):

    feed = feedparser.parse(rss)
    news = []
    for entry in feed['entries'][:6]:
        desc = entry.title
        if 'description' in entry:
            desc = entry.description.split('</a>')[-1]
            desc = desc.split('<')[0]
        elif 'summary' in entry:
            desc = entry.summary.split('</a>')[-1]
            desc = desc.split('<')[0]

        published = parse(entry.published) if 'published' in entry else parse(entry.pubDate)

        data = {'heading': entry.title, 'summary': desc, 'date': published.day, 'month': published.month, 'publish_date': published, 'url': entry.link}
        news.append(data)
    return news


def index(request):
    sites = []
    chk_boxes = []
    if request.method == 'POST':
        for site in __sites:
            isChecked = ''
            if request.POST.get(site.short_name + '-news-chkbox'):
                sites.append({'name': site.name, 'url': site.url, 'news_list': get_news(site.rss_link)})
                isChecked = 'checked'
            chk_boxes.append({'name': site.name, 'shrt_name': site.short_name, 'isChecked': isChecked})
    else:
        for site in __sites:
            sites.append({'name': site.name, 'url': site.url, 'news_list': get_news(site.rss_link)})
            chk_boxes.append({'name': site.name, 'shrt_name': site.short_name, 'isChecked': 'checked'})

    return render(request, 'news.html', {'sites': sites, 'chk_boxes': chk_boxes})
