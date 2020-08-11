  
from django import template

register = template.Library()


@register.filter(name='color')
def set_color(value):
    try:
        value = float(value)
    except ValueError:
        return ''
    if value < 0:
        return '#169206'
        
    elif 1 <= value < 2:
        return '#F8C8C8'
    elif 2 <= value < 5:
        return '#E26F6F'
    elif value >= 5:
        return '#DE4040'
    else:
        return ''