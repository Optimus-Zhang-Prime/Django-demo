# Generated by Django 2.1.7 on 2020-01-09 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chunked_upload', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyChunkedUpload',
            fields=[
                ('chunkedupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='chunked_upload.ChunkedUpload')),
            ],
            options={
                'abstract': False,
            },
            bases=('chunked_upload.chunkedupload',),
        ),
    ]
