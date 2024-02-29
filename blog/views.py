from django.shortcuts import render
from django.views import generic

from blog.models import Posts


class PostList(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4


class PostDetail(generic.DetailView):
    model = Posts
    template_name = 'post.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class PrivacyView(generic.TemplateView):
    template_name = 'privacy.html'


class TosView(generic.TemplateView):
    template_name = 'tos.html'