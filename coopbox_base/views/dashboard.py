from django.shortcuts import render, redirect
from django.views.generic import View
from coopbox_base import urls
from django.conf.urls import url


class Dashboard(View):

    def get(self, request):
        return render(request, 'coopbox_base/dashboard.jinja')

dashboard = Dashboard.as_view()
