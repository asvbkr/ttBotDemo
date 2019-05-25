# -*- coding: UTF-8 -*-
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from openapi_client import UserWithPhoto
from ttBotDemo.BotDemo import BotDemo
from .models import Greeting

tt_bot = BotDemo()

if isinstance(tt_bot.info, UserWithPhoto):
    title = 'ТТ-бот: @%s (%s)' % (tt_bot.info.username, tt_bot.info.name)
else:
    title = 'Должна была быть инфа о ТТ-боте, но что-то пошло не так...'


# Create your views here.
@csrf_exempt  # exempt index() function from built-in Django protection
def index(request):
    # type:(WSGIRequest) -> HttpResponse

    request_body = None
    if request.method == "POST":
        request_body = request.body
    if request_body:
        greeting = Greeting()
        greeting.who = ('%s: %s' % (request.method, request.headers.get('User-Agent')))[:Greeting.who_max_len]
        greeting.request_body = request_body
        greeting.save()

        tt_bot.handle_request_body(request_body)
    data = {'title': title, 'info': '%s' % request.method}
    return render(request, "index.html", context=data)


@csrf_exempt  # exempt index() function from built-in Django protection
def db(request):
    # type:(WSGIRequest) -> HttpResponse

    greeting = Greeting()
    greeting.who = ('%s: %s' % (request.method, request.headers.get('User-Agent')))[:Greeting.who_max_len]
    greeting.save()

    # noinspection PyUnresolvedReferences
    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings, 'title': title})
