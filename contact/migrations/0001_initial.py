# Generated by Django 2.2.3 on 2020-03-11 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='留言内容')),
                ('author', models.CharField(max_length=50, verbose_name='作者')),
                ('contact', models.CharField(blank=True, max_length=254, verbose_name='邮箱')),
                ('website', models.URLField(blank=True, verbose_name='网址')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='留言时间')),
            ],
            options={
                'verbose_name': '私信',
                'verbose_name_plural': '私信',
            },
        ),
    ]
