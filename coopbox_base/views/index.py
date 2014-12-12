from django.shortcuts import render, redirect
from django.views.generic import View
from coopbox_base import urls
from django.conf.urls import url


class Index(View):

    def get(self, request):
        if request.REQUEST.get('change'):
            urls.urlpatterns += url(r'^abc$', 'coopbox_base.views.index.index'),
            return redirect('index')
        return render(request, 'coopbox_base/index.jinja', {'caller': index, 'urls': urls.urlpatterns})

index = Index.as_view()
