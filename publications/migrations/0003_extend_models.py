# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields
import publications.fields


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_initial_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='list',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ['-year', '-month', '-id']},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'ordering': ('order',)},
        ),
        migrations.RenameField(
            model_name='list',
            old_name='list',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='type',
            old_name='type',
            new_name='title',
        ),
        migrations.AddField(
            model_name='publication',
            name='chapter',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='publication',
            name='edition',
            field=models.CharField(blank=True, help_text='The edition of a book -- for example, "Second". This should be an ordinal, and should have the first letter capitalized.', max_length=256),
        ),
        migrations.AddField(
            model_name='publication',
            name='editor',
            field=models.CharField(blank=True, help_text='Name(s) of editor(s), typed as indicated in the LATEX book. If there is also an <author> field, then the <editor> field gives the editor of the book or collection in which the reference appears.', max_length=256),
        ),
        migrations.AddField(
            model_name='publication',
            name='location',
            field=models.CharField(blank=True, help_text="Place of publication, location of conference, or publisher's address.", max_length=256),
        ),
        migrations.AddField(
            model_name='publication',
            name='organization',
            field=models.CharField(blank=True, help_text='The organization that sponsors a conference or that publishes a manual.', max_length=256),
        ),
        migrations.AddField(
            model_name='publication',
            name='school',
            field=models.CharField(blank=True, help_text='The name of the school where a thesis was written.', max_length=256),
        ),
        migrations.AddField(
            model_name='publication',
            name='section',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='series',
            field=models.CharField(blank=True, max_length=256, verbose_name='The name of a series or set of books. When citing an entire book, the <title> field gives its title and an optional <series> field gives the name of a series or multi-volume set in which the book is published.'),
        ),
        migrations.AddField(
            model_name='publication',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('s', 'Submitted'), ('a', 'Accepted'), ('p', 'Published')], default='p', max_length=1),
        ),
        migrations.AlterField(
            model_name='customfile',
            name='file',
            field=models.FileField(upload_to='publications/'),
        ),
        migrations.AlterField(
            model_name='customlink',
            name='url',
            field=models.URLField(verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.CharField(help_text='List of authors separated by commas or <i>and</i>.', max_length=2048),
        ),
        migrations.AlterField(
            model_name='publication',
            name='book_title',
            field=models.CharField(blank=True, help_text='Title of a book, part of which is being cited. See the LATEX book for how to type titles. For book entries, use the <title> field instead', max_length=256),
        ),
        migrations.AlterField(
            model_name='publication',
            name='citekey',
            field=publications.fields.NullCharField(blank=True, help_text='BibTex citation key. Leave blank if unsure.', max_length=512, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='code',
            field=models.URLField(blank=True, help_text='Link to page with code.'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='doi',
            field=publications.fields.NullCharField(blank=True, max_length=128, null=True, unique=True, verbose_name='DOI'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='external',
            field=models.BooleanField(default=False, help_text='If publication was written in another lab, mark as external.'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='publications/images/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='isbn',
            field=publications.fields.NullCharField(blank=True, help_text='Only for a book.', max_length=32, null=True, unique=True, verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='keywords',
            field=models.CharField(blank=True, help_text='List of keywords separated by commas.', max_length=256),
        ),
        migrations.AlterField(
            model_name='publication',
            name='month',
            field=models.IntegerField(blank=True, choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='note',
            field=models.CharField(blank=True, help_text='Any additional information that can help the reader. The first word should be capitalized.', max_length=256),
        ),
        migrations.AlterField(
            model_name='publication',
            name='number',
            field=models.CharField(blank=True, help_text='The number of a journal, magazine, technical report, or of a work in a series. An issue of a journal or magazine is usually identified by its volume and number; the organization that issues a technical report usually gives it a number; and sometimes books are given numbers in a named series.', max_length=128, null=True, verbose_name='Issue number'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='publications/', verbose_name='PDF'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='publications/thumbnails/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='url',
            field=models.URLField(blank=True, help_text='Link to PDF or journal page.', verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='volume',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='year',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='type',
            name='bibtex_types',
            field=models.CharField(default='article', help_text='Possible BibTex types, separated by comma.', max_length=256, verbose_name='BibTex types'),
        ),
        migrations.AlterField(
            model_name='type',
            name='hidden',
            field=models.BooleanField(default=False, help_text='Hide publications from main view.'),
        ),
    ]