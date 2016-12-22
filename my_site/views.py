from django.http import HttpResponse, Http404
import datetime
# from django import template
# from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render


def return_date(request):
    # time = "The time is %s." % datetime.datetime.now()  # string formatting, datetime object converted to string by %s
    # templates should be stored in templates folder
    # temp = get_template('return_date_template.html')  # give absolute template path
    context = Context({"time_now": datetime.datetime.now(), "test": "test-test"})
    # html = temp.render(context)
    # return HttpResponse(html)

    # all the above code is replaced using render function
    return render(request, 'return_date_template.html', context)    # shortcut to return template


def added_time(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    future_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    context = Context({'n': offset, 'future_time': future_time})
    return  render(request, 'added_time_template.html', context)
