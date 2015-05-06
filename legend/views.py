# forms
from work.forms import RoomReservationForm

# models
from work.models import RoomReservation
from work.models import Room

from django.shortcuts import render, redirect, render_to_response
from work.models import Article



def index(request):
    return render(request, 'Sunshine/html/index.html')

def booking(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomReservationForm(request.POST, auto_id=True)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            room = form.cleaned_data['room']
            checkInDate = form.cleaned_data['checkInDate']
            checkOutDate = form.cleaned_data['checkOutDate']
            numberOfPeople = form.cleaned_data['numberOfPeople']
            payment = form.cleaned_data['payment']
            request = form.cleaned_data['request']

            room_object = Room.objects.filter(type=room).first()

            reservation = RoomReservation(name=name, phone=phone, email=email, room=room_object,
                                          checkInDate=checkInDate, checkOutDate=checkOutDate,
                                          numberOfPeople=numberOfPeople, payment=payment,
                                          request=request)

            reservation.save()

            return render_to_response('Sunshine/html/room-reservation-ok.html', {'reservation': reservation})



    # if a GET (or any other method) we'll create a blank form
    else:
        form = RoomReservationForm(auto_id=True)

    return render(request, 'Sunshine/html/booking.html', {'reservation_form': form})


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

def room_reservation_ok(request):
    return render(request, 'Sunshine/html/room-reservation-ok.html')

def write(request):
    return render(request, 'Sunshine/html/news_write.html')
