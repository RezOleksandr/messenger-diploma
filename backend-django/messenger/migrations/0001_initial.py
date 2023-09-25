# Generated by Django 4.2.1 on 2023-06-19 20:48

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
            name='DocumentTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_file', models.FileField(upload_to='static/messenger/document_templates', verbose_name='Файл шаблону')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Назва шаблону')),
                ('button_text', models.CharField(max_length=255, verbose_name='Текст кнопки')),
            ],
            options={
                'verbose_name': 'Шаблон документів',
                'verbose_name_plural': 'Шаблони документів',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Назва групи')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='Код групи')),
                ('study_year', models.IntegerField(blank=True, null=True, verbose_name='Курс')),
                ('speciality', models.CharField(blank=True, max_length=255, verbose_name='Спеціальність')),
                ('institute', models.CharField(blank=True, max_length=255, verbose_name='Інститут')),
                ('faculty', models.CharField(blank=True, max_length=255, verbose_name='Кафедра')),
                ('degree', models.CharField(blank=True, choices=[('bachelor', 'бакалавр'), ('master', 'магістр')], max_length=255, verbose_name='Ступінь')),
                ('information', models.TextField(blank=True, help_text='Заповнювати у форматі:\nПосилання: https://www.google.com.ua/', verbose_name='Посилання')),
                ('methodological_guide', models.FileField(blank=True, upload_to='static/messenger/methodological_guides', verbose_name='Методичні вказівки')),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500, verbose_name='Про себе')),
                ('photo', models.ImageField(blank=True, upload_to='static/messenger/profile_photos', verbose_name='Фото')),
                ('email_confirmed', models.BooleanField(default=False, verbose_name='Підтвердження пошти')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='Є викладачем')),
                ('patronymic', models.CharField(blank=True, max_length=255, verbose_name='По-батькові')),
                ('diploma_supervisor_1', models.CharField(blank=True, max_length=255, verbose_name='Керівник диплому 1')),
                ('diploma_supervisor_2', models.CharField(blank=True, max_length=255, verbose_name='Керівник диплому 2')),
                ('diploma_topic', models.CharField(blank=True, max_length=255, verbose_name='Тема диплому')),
                ('diploma_reviewer', models.CharField(blank=True, max_length=255, verbose_name='Рецензент')),
                ('diploma_reviewer_position', models.CharField(blank=True, max_length=255, verbose_name='Посада рецензента')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='messenger.group', verbose_name='Група')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Профіль',
                'verbose_name_plural': 'Профілі',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва чату')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='static/messenger/chat_photos', verbose_name='Фото')),
                ('type', models.CharField(choices=[('private', 'приватний'), ('group', 'груповий'), ('diploma', 'дипломний')], default='group', max_length=255, verbose_name='Тип чату')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Творець чату')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='messenger.group', verbose_name='Група')),
                ('users', models.ManyToManyField(related_name='chats', to=settings.AUTH_USER_MODEL, verbose_name='Користувачі')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чати',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст повідомлення')),
                ('file', models.FileField(blank=True, null=True, upload_to='static/messenger/message_files', verbose_name='Файл')),
                ('number', models.PositiveIntegerField(default=0, verbose_name='Номер повідомлення')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Дата надсилання')),
                ('pinned', models.BooleanField(default=False, verbose_name='Закріплено')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messenger.chat', verbose_name='Чат')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач')),
            ],
            options={
                'verbose_name': 'Повідомлення',
                'verbose_name_plural': 'Повідомлення',
                'unique_together': {('chat', 'number')},
            },
        ),
    ]