from django.shortcuts import render


def default(request):
    template = "theme/pages/portal.html"
    return render(request, template, {})
