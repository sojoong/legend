from django import forms


class RoomReservationForm(forms.Form):
    # Personal Data
    name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=32)
    email = forms.EmailField(max_length=32)

    # Stay Data
    room = forms.CharField(max_length=32)
    checkInDate = forms.DateField()
    checkOutDate = forms.DateField()
    numberOfPeople = forms.IntegerField()
    payment = forms.CharField(max_length=30)
    request = forms.CharField(max_length=255)