from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Link
from .serializers import *
from django.views import View
from django.conf import settings


class ShortenerListView(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class ShortnerCreateView(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class Redirector(View):
    def get(self,request,shortener_link, *args, **kwargs):
        shortener_link = settings.HOST_URL+'/'+self.kwargs['shortener_link']
        redirect_link = Link.objects.filter(shortened_link=shortener_link).first().original_link
        return redirect(redirect_link) 


