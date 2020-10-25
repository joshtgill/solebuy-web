from django import template


register = template.Library()


@register.filter(name='buildButtonStyle')
def buildButtonStyle(buttonValue, filterIdMap):
    assisterId = int(buttonValue.split('.')[0])
    filterId = int(buttonValue.split('.')[1])

    if filterId in filterIdMap[assisterId]:
        return 'border: 3px solid rgb(13, 147, 255);'
    else:
        return 'border: 1px solid rgb(170, 170, 170);'


@register.filter(name='determineButtonValue')
def determineButtonValue(assisterId, filterId):
    return '{}.{}'.format(assisterId, filterId)
