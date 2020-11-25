from django import template

register = template.Library()


@register.filter(name='buildCategoryIconPath')
def buildCategoryIconPath(category):
    return 'images/{}/icon.png'.format(category.lower())
