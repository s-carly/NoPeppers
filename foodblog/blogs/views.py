from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from blogs.models import Restaurant, Post, Comment

class IndexView(generic.ListView):
    template_name = "blogs/index.html"
    context_object_name = "posts_list"

    def get_queryset(self):
        """Return the last five published posts."""
        return Post.objects.order_by('-pub_date')[:5]


class RestView(generic.DetailView):
    model = Restaurant
    template_name = 'blogs/page.html'

