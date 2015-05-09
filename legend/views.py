# forms
from work.forms import RoomReservationForm
from work.forms import BanquetReservationForm
from work.forms import RestaurantReservationForm

from legend.settings import DATA_DIR

# models
from work.models import RoomReservation
from work.models import BanquetReservation
from work.models import RestaurantReservation
from work.models import Room
from work.models import Hall


from django.shortcuts import render, redirect, render_to_response
from work.models import Article



def index(request):
    return render(request, 'Sunshine/html/index.html')

def booking(request):
    if request.method == 'POST':
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

        return render(request, 'Sunshine/html/booking.html', {'reservation_form': form,
                                                              'validation': 1})

    else:
        form = RoomReservationForm(auto_id=True)

    return render(request, 'Sunshine/html/booking.html', {'reservation_form': form})


def banquet_reservation(request):
    if request.method == 'POST':
        form = BanquetReservationForm(request.POST, auto_id=True)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            hall = form.cleaned_data['hall']
            reservationDate = form.cleaned_data['reservationDate']
            reservationTime = form.cleaned_data['reservationTime']
            numberOfPeople = form.cleaned_data['numberOfPeople']
            request = form.cleaned_data['request']

            hall_object = Hall.objects.filter(type=hall).first()

            reservation = BanquetReservation(name=name, phone=phone, email=email, hall=hall_object,
                                             reservationDate=reservationDate, reservationTime=reservationTime,
                                             numberOfPeople=numberOfPeople, request=request)

            reservation.save()

            return render_to_response('Sunshine/html/banquet-reservation-ok.html', {'reservation_form': reservation})

        return render(request, 'Sunshine/html/banquet-reservation.html', {'reservation_form': form,
                                                                          'validation': 1})

    else:
        form = BanquetReservationForm(auto_id=True)

    return render(request, 'Sunshine/html/banquet-reservation.html', {'reservation_form': form})

def restaurant_reservation(request):
    if request.method == 'POST':
        form = RestaurantReservationForm(request.POST, auto_id=True)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            reservationDate = form.cleaned_data['reservationDate']
            reservationTime = form.cleaned_data['reservationTime']
            numberOfPeople = form.cleaned_data['numberOfPeople']
            request = form.cleaned_data['request']

            reservation = RestaurantReservation(name=name, phone=phone, email=email,
                                             reservationDate=reservationDate, reservationTime=reservationTime,
                                             numberOfPeople=numberOfPeople, request=request)

            reservation.save()

            return render_to_response('Sunshine/html/restaurant-reservation-ok.html', {'reservation_form': reservation})

        return render(request, 'Sunshine/html/restaurant-reservation.html', {'reservation_form': form,
                                                                          'validation': 1})

    else:
        form = RestaurantReservationForm(auto_id=True)

    return render(request, 'Sunshine/html/restaurant-reservation.html', {'reservation_form': form})

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

        if 'file' in request.FILES:
            file = request.FILES['file']
            filename = file._name
            fp = open('%s/%s_%s' % (DATA_DIR,article.articleID,filename) , 'wb')
            for chunk in file.chunks():
                fp.write(chunk)
            article.image=filename
            article.save()
            fp.close()
        return redirect('/news/')
    return render(request, 'Sunshine/html/news_write.html')

def room_details(request):
    return render(request, 'Sunshine/html/room-details.html')

def room_list(request):
    return render(request, 'Sunshine/html/room-list.html')

def room_reservation_ok(request):
    return render(request, 'Sunshine/html/room-reservation-ok.html')

def single_news(request):
    if request.method == 'GET':
        articleID = request.GET.get("articleID",None)
        if articleID != None:
            article = Article.objects.filter(articleID=articleID).first()
            return render(request, 'Sunshine/html/single-news.html', {'article':article})
    return render(request, 'Sunshine/html/404.html')


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

