# Generated by Django 3.1.4 on 2021-10-03 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('birth_year', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('review_title', models.CharField(max_length=50)),
                ('review_text', models.CharField(max_length=4000)),
                ('general_rating', models.PositiveIntegerField()),
                ('attractiveness', models.PositiveIntegerField()),
                ('sociability', models.PositiveIntegerField()),
                ('playfulness', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CatReview',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('cat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat.cat')),
                ('review_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cat.review')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
