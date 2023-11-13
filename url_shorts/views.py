from rest_framework import generics
from .models import Link
from .serializers import LinkSerializer
from django.shortcuts import render, redirect
from .models import Link
from .forms import UrlForm
from .shortner import shortner


class LinkListCreateView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


# Create your views here.

def Home(request, token):
    long_url = Link.objects.filter(short_url=token)[0]
    return redirect(long_url.original_url)

def Make(request):
    form = UrlForm(request.POST)
    token = ""
    if request.method == "POST":
        if form.is_valid():
            NewUrl = form.save(commit=False)
            token = shortner().issue_token()
            NewUrl.short_url = token
            NewUrl.save()
        else:
            form = UrlForm()
            token = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'token': token})
