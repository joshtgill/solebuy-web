from django import template


register = template.Library()


@register.filter(name='buildFiltersStyle')
def buildFiltersStyle(assistersLength):
    return 'width: {}%'.format((assistersLength * 10) + 30)


@register.filter(name='buildFilterStyle')
def buildFilterStyle(assistersLength):
    return 'float: left; width: calc(100% / {})'.format(assistersLength)


@register.filter(name='determineButtonValue')
def determineButtonValue(assisterId, filterId):
    return '{}.{}'.format(assisterId, filterId)
