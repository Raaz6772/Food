# Generated by Django 4.2 on 2024-02-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://th.bing.com/th/id/OIP.LFrjAvpM8m1hw9DQE43DQgHaEm?rs=1&pid=ImgDetMain', max_length=500),
        ),
    ]