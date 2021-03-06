# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_auto_20170109_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='logo',
            field=versatileimagefield.fields.VersatileImageField(default=b'icons/default_server.png', null=True, upload_to=b'server/%Y/%m/', blank=True),
        ),
    ]
