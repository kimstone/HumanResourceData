from django.shortcuts import render

def index_page_view(request, *args, **kwargs):
    context = {}
    return render(request, "staff/index.html", context)
