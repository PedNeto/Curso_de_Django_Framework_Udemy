# Generated by Django 4.1.3 on 2022-12-26 02:29

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="funcionario",
            name="imagem",
            field=stdimage.models.StdImageField(
                force_min_size=False,
                upload_to=core.models.get_file_path,
                variations={"thumb": {"crop": True, "height": 480, "width": 480}},
                verbose_name="Imagem",
            ),
        ),
    ]
