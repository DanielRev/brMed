# from django.shortcuts import render
# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('currencyApp/index.html')
    context = {
        'latest_question_list': 1,
    }
    return HttpResponse(template.render(context, request))