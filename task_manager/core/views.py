from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    title = _('Привет от Хекслета!')
    description = _('Практические курсы по программированию')
    link = 'https://ru.hexlet.io/'
    context = {
        "title": title,
        "description": description,
        "link": link
    }
    return render(request, 'index.html', context)

