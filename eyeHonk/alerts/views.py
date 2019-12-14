# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render


def home(request):
    return render(request, 'alerts/home.html')


def honk(request):
    return render(request, 'alerts/honk.html')


def settings(request):
    return render(request, 'alerts/settings.html')
