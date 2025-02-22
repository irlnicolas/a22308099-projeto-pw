# Generated by Django 4.0.6 on 2024-04-18 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('ano_lancamento', models.IntegerField()),
                ('capa', models.ImageField(blank=True, null=True, upload_to='app/capas')),
            ],
        ),
        migrations.CreateModel(
            name='Banda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('genero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('duracao', models.DurationField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='musicas', to='bandas.album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='banda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albuns', to='bandas.banda'),
        ),
    ]
