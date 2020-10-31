from django.db import models


LENGTH_SHORT = 10
LENGTH_MEDIUM = 30
LENGTH_LONG = 50
LENGTH_XLONG = 300


class Pro(models.Model):
    contents = models.CharField(max_length=LENGTH_LONG)


class Con(models.Model):
    contents = models.CharField(max_length=LENGTH_LONG)


class AssisterFilterId(models.Model):
    assisterId = models.IntegerField()
    filterId = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=LENGTH_LONG)
    price = models.FloatField()
    imageFileName = models.CharField(max_length=LENGTH_LONG)
    pros = models.ManyToManyField(Pro)
    cons = models.ManyToManyField(Con)
    assisterFilterIds = models.ManyToManyField(AssisterFilterId)
    prosSummary = models.CharField(max_length=LENGTH_XLONG)
    consSummary = models.CharField(max_length=LENGTH_XLONG)


class Filter(models.Model):
    contents = models.CharField(max_length=LENGTH_MEDIUM)


class Assister(models.Model):
    name = models.CharField(max_length=LENGTH_MEDIUM)
    prompt = models.CharField(max_length=LENGTH_LONG)
    filters = models.ManyToManyField(Filter)
    decisive = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=LENGTH_MEDIUM)
    iconFileName = models.CharField(max_length=LENGTH_MEDIUM)
    assisters = models.ManyToManyField(Assister)
    products = models.ManyToManyField(Product)
