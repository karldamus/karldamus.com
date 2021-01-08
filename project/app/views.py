from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    return render(request, 'contact.html', {})

'''
portfolio
about
blog
contact me

'''

