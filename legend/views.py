# forms
from work.forms import RoomReservationForm
from legend.settings import DATA_DIR
# models
from work.models import RoomReservation
from work.models import Room
from django.shortcuts import render, redirect
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

            return redirect("room-list")



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

