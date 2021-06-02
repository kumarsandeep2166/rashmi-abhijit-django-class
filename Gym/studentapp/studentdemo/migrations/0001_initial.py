# Generated by Django 2.2 on 2020-07-25 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(max_length=13)),
                ('blood_group', models.CharField(choices=[('o+ve', 'o+ve'), ('o-ve', 'o-ve'), ('A+ve', 'A+ve'), ('A-ve', 'A-+ve'), ('B+ve', 'B+ve'), ('B-ve', 'B-ve'), ('AB+ve', 'AB+ve'), ('AB-ve', 'AB-ve')], max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=5)),
                ('caste', models.CharField(choices=[('Gen', 'GEN'), ('SC', 'SC'), ('ST', 'ST'), ('OBC', 'OBC'), ('Others', 'Others')], max_length=10)),
            ],
        ),
    ]