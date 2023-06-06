# Generated by Django 4.2.1 on 2023-06-02 19:29

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='portfolio',
            field=wagtail.fields.StreamField([('portfolio', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('photo', wagtail.images.blocks.ImageChooserBlock(required=True)), ('intro', wagtail.blocks.RichTextBlock())]))], blank=True, null=True, use_json_field=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='services',
            field=wagtail.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='team',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]