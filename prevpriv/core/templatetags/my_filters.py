from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
import locale
locale.setlocale( locale.LC_ALL, 'pt-br' )
register = template.Library()


def currency(reais):
    reais =locale.currency( round(float(reais)) , grouping=True)
     #f'{round(float(reais), 2):06.2f}'
    return reais


def percentage(value):
    return f'{0:.1%}'.format(value)


register.filter('percentage', percentage)

register.filter('currency', currency)
