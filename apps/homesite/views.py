from django.shortcuts import render

def about_page_view(request, *args, **kwargs):
    context = {}
    return render(request, "homesite/about.html", context)


def contact_page_view(request, *args, **kwargs):
    context = {}
    return render(request, "homesite/contact.html", context)


def home_page_view(request, *args, **kwargs):
    context = {}
    return render(request, "homesite/home.html", context)
