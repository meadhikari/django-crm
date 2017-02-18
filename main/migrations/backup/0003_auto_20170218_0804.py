# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-18 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20170218_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='batoko_kisim',
            field=models.CharField(choices=[(b'kacchi', '\u0915\u091a\u094d\u091a\u0940'), (b'sahayek', '\u0938\u093e\u0939\u092f\u0947\u0915'), (b'pichbato', '\u092a\u0940\u091a\u092c\u093e\u091f\u094b'), (b'mukhya_pichbato', '\u092e\u0941\u0916\u094d\u092f \u092a\u093f\u091a\u092c\u093e\u091f\u094b')], default=None, max_length=100, verbose_name=b'\xe0\xa4\xac\xe0\xa4\xbe\xe0\xa4\x9f\xe0\xa5\x8b \xe0\xa4\x95\xe0\xa5\x8b \xe0\xa4\x95\xe0\xa4\xbf\xe0\xa4\xb8\xe0\xa4\xbf\xe0\xa4\xae'),
        ),
        migrations.AddField(
            model_name='customer',
            name='ghar_ko_kisim',
            field=models.CharField(choices=[(b'kacchi', '\u0915\u091a\u094d\u091a\u0940'), (b'pakki', '\u092a\u0915\u094d\u0915\u093f')], default=None, max_length=100, verbose_name=b'\xe0\xa4\x98\xe0\xa4\xb0 \xe0\xa4\x95\xe0\xa5\x8b \xe0\xa4\x95\xe0\xa4\xbf\xe0\xa4\xb8\xe0\xa4\xbf\xe0\xa4\xae'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='chetra',
            field=models.CharField(choices=[(b'awasiya', '\u0906\u0935\u093e\u0938\u0940\u092f'), (b'angsik_bajar', '\u0905\u0928\u094d\u0917\u094d\u0938\u093f\u0915 \u092c\u091c\u093e\u0930'), (b'bajar', '\u092c\u091c\u093e\u0930'), (b'mukhya_bajar', '\u092e\u0941\u0916\u094d\u092f \u092c\u091c\u093e\u0930')], default=None, max_length=100, verbose_name=b'\xe0\xa4\x95\xe0\xa5\x8d\xe0\xa4\xb7\xe0\xa5\x87\xe0\xa4\xa4\xe0\xa5\x8d\xe0\xa4\xb0 '),
        ),
    ]
