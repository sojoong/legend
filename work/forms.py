# -*- coding: utf-8 -*-
# decoding
import sys

from django import forms

# Models
from work.models import Room
from work.models import Hall
from work.models import RoomReservation
from work.models import BanquetReservation
from work.models import RestaurantReservation

#internationalization
from django.utils.translation import ugettext_lazy as _


reload(sys)
sys.setdefaultencoding("utf-8")

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class RoomReservationForm(forms.Form):
    class Meta:
        model = RoomReservation

    error_css_class = "error"

    ROOMS = [('-1', '객실 종류 선택')]
    ROOMS += [('%s' % room.type, '%s' % room.type) for index, room in enumerate(Room.objects.all(), start=1)]

    GUESTS = (('-1', '인원 수 선택'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('5+', '5+'))
    PAYMENT = (('-1', '결제 방식 선택'), ('현금', '현금'), ('신용카드', '신용카드'), ('계좌이체', '계좌이체'))

    # Personal Data
    name = forms.CharField(max_length=30, error_messages={'required': '이름을 입력해주세요'})
    phone = forms.CharField(max_length=32, help_text='"-"없이 입력해주세요', error_messages={'required': '연락 가능한 번호를 입력해주세요'},
                            widget=forms.TextInput(attrs={'placeholder': ' ex) 010-1234-5678'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput, max_length=32, error_messages={'required': '이메일을 입력해주세요'}, required=False)

    # Stay Data
    room = forms.ChoiceField(widget=forms.Select, choices=ROOMS, error_messages={'required': '객실 타입을 선택해주세요'})
    checkInDate = forms.DateField(widget=forms.DateInput(format = '%y/%m/%d'), error_messages={'required': '체크인 시간을 선택해주세요'},
                                  input_formats=('%y/%m/%d',))
    checkOutDate = forms.DateField(widget=forms.DateInput(format = '%y/%m/%d'), error_messages={'required': '체크아웃 시간을 선택헤주세요'},
                                  input_formats=('%y/%m/%d',))
    numberOfPeople = forms.ChoiceField(widget=forms.Select, choices=GUESTS, error_messages={'required': '이용 인원 수를 선택해주세요'})
    payment = forms.ChoiceField(widget=forms.Select, choices=PAYMENT, error_messages={'required': '결제수단을 선택해주세요'})
    request = forms.CharField(max_length=255, error_messages={'required': '기타 요구사항을 입력해주세요'}, required=False)

    def clean(self):
        cleaned_data = super(RoomReservationForm, self).clean()
        numberOfPeople = cleaned_data.get("numberOfPeople")
        payment = cleaned_data.get("payment")
        room = cleaned_data.get("room")
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")


        if numberOfPeople == '-1':
            msg = _("투숙인원을 선택해주세요")
            self.add_error('numberOfPeople', msg)

        if payment == '-1':
            msg = "결제방식을 선택해주세요"
            self.add_error('payment', msg)

        if room == '-1':
            msg = "객실 종류를 선택해주세요"
            self.add_error('room', msg)

        if phone == '' and email == '':
            msg = "연락처를 입력해주세요"
            self.add_error('phone', msg)
            self.add_error('email', msg)


class BanquetReservationForm(forms.Form):
    class Meta:
        model = BanquetReservation

    error_css_class = "error"

    HALLS = [('-1', '연회장 종류 선택')]
    HALLS += [('%s' % hall.type, '%s' % hall.type) for index, hall in enumerate(Hall.objects.all(), start=1)]

    # Personal Data
    name = forms.CharField(max_length=30, error_messages={'required': '이름을 입력해주세요'})
    phone = forms.CharField(max_length=32, help_text='"-"없이 입력해주세요', error_messages={'required': '연락 가능한 번호를 입력해주세요'},
                            widget=forms.TextInput(attrs={'placeholder': ' ex) 010-1234-5678'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput, max_length=32, error_messages={'required': '이메일을 입력해주세요'}, required=False)

    # Hall Data
    hall = forms.ChoiceField(widget=forms.Select, choices=HALLS, error_messages={'required': '연회장 종류를 선택해주세요'})
    reservationDate = forms.DateField(widget=forms.DateInput(format = '%y/%m/%d'), error_messages={'required': '체크인 시간을 선택해주세요'},
                                  input_formats=('%y/%m/%d',))
    reservationTime = forms.CharField(max_length=30, error_messages={'required': '예약 시간을 선택해주세요'},
                            widget=forms.TextInput(attrs={'placeholder': ' ex) 오후 4시 30분 or 16시 30분'}))
    numberOfPeople = forms.IntegerField(error_messages={'required': '인원을 입력해주세요'})
    request = forms.CharField(max_length=255, error_messages={'required': '기타 요구사항을 입력해주세요'}, required=False)

    def clean(self):
        cleaned_data = super(BanquetReservationForm, self).clean()
        hall = cleaned_data.get("hall")
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")

        if hall == '-1':
            msg = "연회장 종류를 선택해주세요"
            self.add_error('hall', msg)

        if phone == '' and email == '':
            msg = "연락처를 입력해주세요"
            self.add_error('phone', msg)
            self.add_error('email', msg)


class RestaurantReservationForm(forms.Form):
    class Meta:
        model = RestaurantReservation

    error_css_class = "error"

    # Personal Data
    name = forms.CharField(max_length=30, error_messages={'required': '이름을 입력해주세요'})
    phone = forms.CharField(max_length=32, help_text='"-"없이 입력해주세요', error_messages={'required': '연락 가능한 번호를 입력해주세요'},
                            widget=forms.TextInput(attrs={'placeholder': ' ex) 010-1234-5678'}), required=False)
    email = forms.EmailField(widget=forms.EmailInput, max_length=32, error_messages={'required': '이메일을 입력해주세요'}, required=False)

    # Restaurant Data
    reservationDate = forms.DateField(widget=forms.DateInput(format = '%y/%m/%d'), error_messages={'required': '체크인 시간을 선택해주세요'},
                                  input_formats=('%y/%m/%d',))
    reservationTime = forms.CharField(max_length=30, error_messages={'required': '예약 시간을 선택해주세요'},
                            widget=forms.TextInput(attrs={'placeholder': ' ex) 오후 4시 30분 or 16시 30분'}))
    numberOfPeople = forms.IntegerField(error_messages={'required': '인원을 입력해주세요'})
    request = forms.CharField(max_length=255, error_messages={'required': '기타 요구사항을 입력해주세요'}, required=False)

    def clean(self):
        cleaned_data = super(RestaurantReservationForm, self).clean()
        phone = cleaned_data.get("phone")
        email = cleaned_data.get("email")

        if phone == '' and email == '':
            msg = "연락처를 입력해주세요"
            self.add_error('phone', msg)
            self.add_error('email', msg)