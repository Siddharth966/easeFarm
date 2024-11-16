from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (TypeError, ValueError):
        return None

register = template.Library()

@register.filter
def multiply(value, arg):
    return value * arg