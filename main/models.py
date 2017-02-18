# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Customer(models.Model):

    chetra_choices = (
        ("awasiya", u'आवासीय'),
        ("angsik_bajar", u'अन्ग्सिक बजार'),
        ("bajar", u'बजार'),
        ("mukhya_bajar", u'मुख्य बजार'),
    )

    batoko_kisim_choices = (
        ("kacchi",u"कच्ची"),
        ("sahayek",u"साहयेक"),
        ("pichbato",u"पीचबाटो"),
        ("mukhya_pichbato",u"मुख्य पिचबाटो")
    )

    ghar_ko_kisim_choices = (
        ("kacchi", u"कच्ची"),
        ("pakki", u"पक्कि")
    )
    internal_identification_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,verbose_name=u"नाम")
    address = models.CharField(max_length=250,verbose_name=u"ठेगाना")
    margh = models.CharField(max_length=100,verbose_name=u"मार्ग")
    house_no = models.CharField(max_length=50,verbose_name=u"घर न.")
    barga_fit = models.CharField(max_length=100,verbose_name=u"वर्ग फिट")
    land_kitta_number = models.CharField(max_length=100,verbose_name=u"जग्गा कि. न.")
    land_area = models.CharField(max_length=100,verbose_name=u"जग्गाको चेत्रफल")
    monthly_fee = models.IntegerField(verbose_name=u"मासिक सुल्क")

    chetra = models.CharField(max_length=100,choices=chetra_choices,default=None,verbose_name="क्षेत्र ")
    batoko_kisim = models.CharField(max_length=100, choices=batoko_kisim_choices, default=None, verbose_name="बाटो को किसिम")
    ghar_ko_kisim = models.CharField(max_length=100, choices=ghar_ko_kisim_choices, default=None, verbose_name="घर को किसिम")

    class Meta():
        verbose_name = u"ग्राहक बिवरण"
        verbose_name_plural = u"ग्राहक बिवरण"

    def __str__(self):
        return self.name


class Payment(models.Model):

    customer = models.ForeignKey("Customer",null=True)
    rasid_number = models.IntegerField(verbose_name=u"रसिद न.",null=True)
    amount = models.IntegerField(verbose_name=u"रकम")
    remarks = models.CharField(max_length=300,verbose_name=u"टिप्पणी")
    date = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta():
        verbose_name = u"भुक्तानी"
        verbose_name_plural = u"भुक्तानी"

    def __str__(self):
        return str(self.rasid_number)