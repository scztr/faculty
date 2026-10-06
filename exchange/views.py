from django.shortcuts import render

from .models import ExchangeProgram


def exchange_list(request):
    prog = ExchangeProgram.objects.all()
    return render(request, "exchange/exchange_list.html", {"programs": prog})