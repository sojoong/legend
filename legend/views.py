# forms
from django.http import HttpResponseRedirect
from django.template import RequestContext
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
from django.templatetags.static import static

#internationalization
from django.utils.translation import ugettext as _, activate
from django.utils.translation import ugettext


from django.shortcuts import render, redirect, render_to_response
from work.models import Article


def index(request):
    pre_function(request)

    rooms = Room.objects.all()
    return render(request, 'Sunshine/html/index.html', {'rooms': rooms})

def booking(request):
    pre_function(request)

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
        initial = {}
        parameters = ['checkInDate', 'checkOutDate', 'numberOfPeople', 'room']

        for parameter in parameters:
            if parameter in request.GET:
                initial[parameter] = request.GET[parameter]

        form = RoomReservationForm(auto_id=True, initial=initial)

    return render(request, 'Sunshine/html/booking.html', {'reservation_form': form})


def banquet_reservation(request):
    pre_function(request)

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
    pre_function(request)

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
    if request.method == 'GET':
        last_news = get_last_news()
        return render(request, 'Sunshine/html/contact.html', {'last_news':last_news})

    return render(request, 'Sunshine/html/contact.html')

def fullwidth(request):
    pre_function(request)

    return render(request, 'Sunshine/html/fullwidth.html')

def gallery(request):
    pre_function(request)

    return render(request, 'Sunshine/html/gallery.html')

def news(request):
    pre_function(request)

    articles = Article.objects.order_by('date').reverse()
    if request.method == 'GET':
        page = int(request.GET.get("page",1))
        if page < 1:
            page = 1
        max_page = len(list(articles)) / 6 + 1
        cur_page_articles = []
        count=0
        last_news = []
        for article in articles:
            count+=1
            if(count < 4):
                last_news.append(article)
            if(count>page*6):
                break
            if(count>6*(page-1)):
                cur_page_articles.append(article)
        return render(request, 'Sunshine/html/news.html',
                      {'articles': cur_page_articles,'page_no': page,'max_page':max_page,'last_news':last_news})
    return render(request, 'Sunshine/html/404.html')

def get_last_news():
    articles = Article.objects.order_by('date').reverse()
    count=0
    last_news = []
    for article in articles:
        count+=1
        if(count < 4):
            last_news.append(article)
        else:
            break
    return last_news

def write(request):
    pre_function(request)

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
    pre_function(request)

    return render(request, 'Sunshine/html/room-details.html')

def room_list(request):
    pre_function(request)

    return render(request, 'Sunshine/html/room-list.html')

def room_reservation_ok(request):
    pre_function(request)

    return render(request, 'Sunshine/html/room-reservation-ok.html')

def single_news(request):
    pre_function(request)

    if request.method == 'GET':
        # url = static('notice-data/test.m3u8')
        # print url
        articleID = request.GET.get("articleID",None)
        if articleID != None:
            article = Article.objects.filter(articleID=articleID).first()
            last_news = get_last_news()
            return render(request, 'Sunshine/html/single-news.html', {'article':article,'last_news':last_news})
    return render(request, 'Sunshine/html/404.html')


def change_language(request):

    if (not 'django_language' in request.session) or request.session['django_language'] == 'ko':
        request.session['django_language'] = 'en'
        activate('en')
    else:
        request.session['django_language'] = 'ko'
        activate('ko')

    return HttpResponseRedirect('/')
    #return render_to_response('Sunshine/html/index.html', {})

def pre_function(request):
    if (not 'django_language' in request.session) or request.session['django_language'] == 'ko':
        activate('ko')
    else:
        activate('en')
