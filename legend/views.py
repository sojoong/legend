from django.shortcuts import render

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
    return render(request, 'Sunshine/html/news.html')

def write(request):
    return render(request, 'Sunshine/html/news_write.html')

def room_details(request):
    return render(request, 'Sunshine/html/room-details.html')

def room_list(request):
    return render(request, 'Sunshine/html/room-list.html')

def single_news(request):
    return render(request, 'Sunshine/html/single-news.html')