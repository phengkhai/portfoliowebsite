# views.py
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import TemplateView
from django.template import Context, Template
from wordle.models import Post
from .forms import ContactForm

# Wrapper view
class WrapperView(TemplateView):
    template_name = 'base.html'
    model = Post
    form = ContactForm
    def get_context_data(self, **kwargs):
        form = ContactForm()
        context = super(WrapperView, self).get_context_data(**kwargs)
        context = { 'posts' : Post.objects.all,'form':form}
        # In the wrapper template you can show the html of your inline_view with {{ inline_html|safe }}
        return context