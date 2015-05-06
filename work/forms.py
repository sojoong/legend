# -*- coding: utf-8 -*-
# decoding
import sys

from django import forms

# Models
from work.models import Room
from work.models import RoomReservation

reload(sys)
sys.setdefaultencoding("utf-8")

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class RoomReservationForm(forms.Form):
    class Meta:
            model = RoomReservation

    error_css_class = "error"

    ROOMS = [(-1, '객실 타입 선택')]
    # ROOMS += [(index, '%s / %s평 / 인원: %s명' % (room.type, room.space, room.numberOfPeople))
     #                 for index, room in enumerate(Room.objects.all(), start=1)]
    ROOMS += [('%s' % room.type, '%s' % room.type) for index, room in enumerate(Room.objects.all(), start=1)]

    GUESTS = ((-1, '인원 수 선택'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('5+', '5+'))
    PAYMENT = ((-1, '결제 방식 선택'), ('현금', '현금'), ('신용카드', '신용카드'), ('계좌이체', '계좌이체'))

    # Personal Data
    name = forms.CharField(max_length=30, error_messages={'required': '이름을 입력해주세요'})
    phone = forms.CharField(max_length=32, help_text='"-"없이 입력해주세요', error_messages={'required': '연락 가능한 번호를 입력해주세요'},
                            widget=forms.TextInput(attrs={'placeholder': ' \'-\' 없이 입력해주세요'}))
    email = forms.EmailField(widget=forms.EmailInput, max_length=32, error_messages={'required': '이메일을 입력해주세요'})

    # Stay Data
    room = forms.ChoiceField(widget=forms.Select, choices=ROOMS, error_messages={'required': '객실 타입을 선택해주세요'})
    checkInDate = forms.DateField(widget=forms.DateInput(format = '%y/%m/%d'), error_messages={'required': '체크인 시간을 선택해주세요'},
                                  input_formats=('%y/%m/%d',))
    checkOutDate = forms.DateField(widget=forms.DateInput(format = '%y/%m/%d'), error_messages={'required': '체크아웃 시간을 선택헤주세요'},
                                  input_formats=('%y/%m/%d',))
    numberOfPeople = forms.ChoiceField(widget=forms.Select, choices=GUESTS, error_messages={'required': '이용 인원 수를 선택해주세요'})
    payment = forms.ChoiceField(widget=forms.Select, choices=PAYMENT, error_messages={'required': '결제수단을 선택해주세요'})
    request = forms.CharField(max_length=255, error_messages={'required': '기타 요구사항을 입력해주세요'}, required=False)
