from django.shortcuts import render
from django.views.generic import ListView
from .models import Quote

# Create your views here.
class QuotesView(ListView):  # Rename to QuotesView for consistency
    template_name = "quotes.html"
    model = Quote

    # Uncomment if you have related models
    # def get_queryset(self):
    #     query_set = super().get_queryset()
    #     return query_set.select_related('quote_category')
