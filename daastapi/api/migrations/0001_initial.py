# Generated by Django 4.2.3 on 2023-11-15 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=128, unique=True)),
                ('current_rev', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentRevision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(db_index=True, max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (10, 'Imported'), (15, 'Contribution'), (99, 'Rejected'), (100, 'Approved'), (200, 'Published')], db_index=True)),
                ('revision_number', models.IntegerField(null=True)),
                ('timestamp', models.DateField(db_index=True)),
                ('content', models.JSONField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revisions', to='api.document')),
            ],
        ),
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('url_format', models.CharField(help_text='The format of the url with a placeholder for the entity key', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Transcription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_number', models.IntegerField()),
                ('language_code', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('is_translation', models.BooleanField()),
                ('document_rev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.documentrevision')),
            ],
        ),
        migrations.CreateModel(
            name='EntityDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.CharField(max_length=255, null=True)),
                ('entity_key', models.CharField(db_index=True, max_length=255)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.document')),
                ('entity_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='api.entitytype')),
            ],
        ),
        migrations.AddConstraint(
            model_name='documentrevision',
            constraint=models.UniqueConstraint(fields=('document', 'revision_number'), name='unique_doc_rev_number'),
        ),
    ]
