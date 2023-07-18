# Generated by Django 4.2.1 on 2023-07-04 17:07

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_homepage_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='footersocialblock',
            field=wagtail.fields.StreamField([('footersocialblock', wagtail.blocks.StructBlock([('socialMedia', wagtail.blocks.StructBlock([('facebook', wagtail.blocks.CharBlock(required=False)), ('twitter', wagtail.blocks.CharBlock(required=False)), ('google', wagtail.blocks.CharBlock(required=False)), ('instagram', wagtail.blocks.CharBlock(required=False)), ('linked_in', wagtail.blocks.CharBlock(required=False)), ('git', wagtail.blocks.CharBlock(required=False))]))]))], blank=True, null=True, use_json_field=True),
        ),
    ]