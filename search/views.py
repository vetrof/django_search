from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from realty.models import Realty


class SearchResult(ListView):
    model = Realty
    template_name = 'search.html'
    context_object_name = 'all_realty'

    def get_queryset(self):
        query = self.request.GET.get('q' )
        min_price = self.request.GET.get('min')
        max_price = self.request.GET.get('max')
        category = self.request.GET.get('category')
        queryset = Realty.objects.all()

        if query:
            queryset = queryset.filter(
                Q(info__icontains=query) | Q(name__icontains=query) | Q(adres__icontains=query)
            )

        if min_price:
            queryset = queryset.filter(price__gte=min_price)

        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        if category:
            queryset = queryset.filter(cat=category)

        return queryset



