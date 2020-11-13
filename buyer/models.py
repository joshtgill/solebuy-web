from django.db import models


LENGTH_SHORT = 30
LENGTH_MEDIUM = 50
LENGTH_XLONG = 500


class Category(models.Model):
    name = models.CharField(max_length=LENGTH_SHORT)


class Assister(models.Model):
    name = models.CharField(max_length=LENGTH_SHORT)
    prompt = models.CharField(max_length=LENGTH_MEDIUM)
    decisive = models.BooleanField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Filter(models.Model):
    contents = models.CharField(max_length=LENGTH_SHORT)

    assister = models.ForeignKey(Assister, on_delete=models.CASCADE)


class AssisterFilterId(models.Model):
    assisterId = models.IntegerField()
    filterId = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=LENGTH_MEDIUM)
    price = models.FloatField()
    imageFileName = models.CharField(max_length=LENGTH_MEDIUM)
    prosSummary = models.CharField(max_length=LENGTH_XLONG)
    consSummary = models.CharField(max_length=LENGTH_XLONG)
    assisterFilterIds = models.ManyToManyField(AssisterFilterId)
    entryCapacity = models.IntegerField(default=0)
    cameraDescription = models.CharField(max_length=LENGTH_MEDIUM, default='')
    batteryDescription = models.CharField(max_length=LENGTH_SHORT, default='')
    displayDescription = models.CharField(max_length=LENGTH_MEDIUM, default='')
    internalsDescription = models.CharField(max_length=LENGTH_SHORT, default='')
    alternativeProductNames = models.CharField(max_length=LENGTH_MEDIUM, default='')
    ranking = models.IntegerField(default=100)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Pro(models.Model):
    contents = models.CharField(max_length=LENGTH_MEDIUM)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Con(models.Model):
    contents = models.CharField(max_length=LENGTH_MEDIUM)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
