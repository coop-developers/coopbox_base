from django.shortcuts import render
from django.views.generic import View

class Index(View):

    def get(self, request):
        return render(request, 'coopbox_base/index.jinja', {'caller': index})

index = Index.as_view()
