from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class PortfolioBlock(blocks.StructBlock):
    heading = blocks.CharBlock(classname="full title")
    photo = ImageChooserBlock(required=True)
    intro = blocks.RichTextBlock()

class TeamBlock(blocks.StructBlock):    
    photo = ImageChooserBlock(required=True)
    name = blocks.CharBlock(classname="name")
    intro = blocks.RichTextBlock()
    designation = blocks.CharBlock(classname="designation")
    socialMedia = blocks.StructBlock([
        ('instagram', blocks.CharBlock()),
        ('linked_in', blocks.CharBlock()),
        ('git', blocks.CharBlock()),
    ])

class HomePage(Page):
    services = RichTextField(blank=True)
    portfolio = StreamField([('portfolio', PortfolioBlock())], null=True, blank=True,use_json_field=True)
    myteam = StreamField([('myteam', TeamBlock())], null=True, blank=True,use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('services'),
        FieldPanel('myteam'),
        FieldPanel('portfolio'),

    ] 

