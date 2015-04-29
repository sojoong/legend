# -*- coding: utf-8 -*-
# decoding
import sys

from django import forms

# Models
from work.models import Room

reload(sys)
sys.setdefaultencoding("utf-8")


class RoomReservationForm(forms.Form):
    error_css_class = "error"

    ROOMS = [(-1, '객실 타입 선택')]
    ROOMS += [(index, '%s / %s평 / 인원: %s명' % (room.type, room.space, room.numberOfPeople))
                      for index, room in enumerate(Room.objects.all(), start=1)]

    GUESTS = ((-1, '인원 수 선택'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '5+'))
    PAYMENT = ((-1, '결제 방식 선택'), ('1', '현금'), ('2', '신용카드'), ('3', '계좌이체'))

    # Personal Data
    name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=32)
    email = forms.EmailField(widget=forms.EmailInput, max_length=32)

    # Stay Data
    room = forms.ChoiceField(widget=forms.Select, choices=ROOMS)
    checkInDate = forms.DateField(widget=forms.TextInput(attrs=
                                                         {
                                                             'class': 'datepicker'
                                                         }))
    checkOutDate = forms.DateField(widget=forms.TextInput(attrs=
                                                         {
                                                             'class': 'datepicker'
                                                         }))
    numberOfPeople = forms.ChoiceField(widget=forms.Select, choices=GUESTS)
    payment = forms.ChoiceField(widget=forms.Select, choices=PAYMENT)
    request = forms.CharField(max_length=255)

    def clean(self):
        cleaned_data = super(RoomReservationForm, self).clean()
        name = cleaned_data.get("name")
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")

        # if name is None or phone is None or email is None:
        #     msg = "error"
        #     self.add_error('name', msg)