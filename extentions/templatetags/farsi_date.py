from django import template
from jalali_date import datetime2jalali, date2jalali

register = template.Library()

months = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند']

@register.filter(name="farsi_date_changer")
def farsi_date_changer(value):
    x = datetime2jalali(value)
    return f'({x.time().hour}:{x.time().minute}) {x.date().day}-{months[x.date().month-1]}-{x.date().year} '

