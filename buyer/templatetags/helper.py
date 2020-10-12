from django import template


register = template.Library()


@register.filter(name='buildFiltersStyle')
def buildFiltersStyle(assistersLength):
    return 'width: {}%'.format((assistersLength * 10) + 30)


@register.filter(name='buildFilterStyle')
def buildFilterStyle(assistersLength):
    return 'float: left; width: calc(100% / {})'.format(assistersLength)


@register.filter(name='buildButtonStyle')
def buildButtonStyle(buttonValue, idMap):
    assisterId = int(buttonValue.split('.')[0])
    filterId = int(buttonValue.split('.')[1])

    if filterId in idMap[assisterId]:
        return 'background-color: #2385e8; color: #ffffff'
    else:
        return 'background-color: #ffffff; color: #222222; border: 1px solid #222222;'


@register.filter(name='determineButtonValue')
def determineButtonValue(assisterId, filterId):
    return '{}.{}'.format(assisterId, filterId)
