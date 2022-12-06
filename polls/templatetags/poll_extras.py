from django import template
from jalali_date import date2jalali

register = template.Library()


@register.filter(name='change_date_to_shamsi')
def change_date_to_shamsi(value):
    return date2jalali(value)


@register.simple_tag
def url_replace(request, field, value):
    dict_ = request.GET.copy()
    dict_[field] = value
    return dict_.urlencode()
