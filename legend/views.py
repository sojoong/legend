from django.shortcuts import render

# forms
from work.forms import RoomReservationForm

# models
from work.models import RoomReservation


def index(request):
    return render(request, 'Sunshine/html/index.html')

def booking(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RoomReservationForm(request.POST)

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

            reservation = RoomReservation(name=name, phone=phone, email=email, room=room,
                                          checkInDate=checkInDate, checkOutDate=checkOutDate,
                                          numberOfPeople=numberOfPeople, payment=payment,
                                          request=request)

            reservation.save()

            return render(request, "Sunshine/html/room-list.html", {'reservation_form' : form})



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
    return render(request, 'Sunshine/html/news.html')

def room_details(request):
    return render(request, 'Sunshine/html/room-details.html')

def room_list(request):
    return render(request, 'Sunshine/html/room-list.html')

def single_news(request):
    return render(request, 'Sunshine/html/single-news.html')

def complete(request):
    if request.method == "POST":
        form = RoomReservationForm(request.POST)

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

            reservation = RoomReservation(name=name, phone=phone, email=email, room=room,
                                          checkInDate=checkInDate, checkOutDate=checkOutDate,
                                          numberOfPeople=numberOfPeople, payment=payment,
                                          request=request)

            reservation.save()

            return render(request, "Sunshine/html/room-list.html", {'reservation_form' : form})

    return render(request, "Sunshine/html/single-news.html", {'reservation_form' : form})



def write(request):
    return render(request, 'Sunshine/html/news_write.html')