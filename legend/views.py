from django.shortcuts import render, redirect
from work.models import Article


def index(request):
    return render(request, 'Sunshine/html/index.html')

def booking(request):
    return render(request, 'Sunshine/html/booking.html')

def contact(request):
    return render(request, 'Sunshine/html/contact.html')

def fullwidth(request):
    return render(request, 'Sunshine/html/fullwidth.html')

def gallery(request):
    return render(request, 'Sunshine/html/gallery.html')

def news(request):
    articles = Article.objects.all()
    return render(request, 'Sunshine/html/news.html', {'articles': articles})

def write(request):
     if request.method == 'POST':
        title = request.POST["title"]
        content = request.POST["content"]
        article = Article(title=title, content=content)
        article.save()
        return redirect('news.html')
     return render(request, 'Sunshine/html/news_write.html')

def room_details(request):
    return render(request, 'Sunshine/html/room-details.html')

def room_list(request):
    return render(request, 'Sunshine/html/room-list.html')

def single_news(request):
    return render(request, 'Sunshine/html/single-news.html')