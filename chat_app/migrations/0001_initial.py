# Generated by Django 5.0 on 2023-12-12 18:11

import chat_app.models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import model_utils.fields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to=chat_app.models.user_directory_path, verbose_name='File')),
                ('upload_date', models.DateTimeField(auto_now_add=True, verbose_name='Upload date')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Uploaded_by')),
            ],
        ),
        migrations.CreateModel(
            name='MessageModel',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('text', models.TextField(blank=True, verbose_name='Text')),
                ('read', models.BooleanField(default=False, verbose_name='Read')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL, verbose_name='Recipient')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_user', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='message', to='chat_app.uploadedfile', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ('-created',),
            },
            managers=[
                ('all_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DialogsModel',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='User1')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='User2')),
            ],
            options={
                'verbose_name': 'Dialog',
                'verbose_name_plural': 'Dialogs',
                'unique_together': {('user1', 'user2'), ('user2', 'user1')},
            },
        ),
    ]