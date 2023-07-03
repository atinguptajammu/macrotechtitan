from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtailcaptcha.models import WagtailCaptchaEmailForm
from django.utils.functional import cached_property
from modelcluster.fields import ParentalKey

class FormField(AbstractFormField):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='form_fields')

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
        ('instagram', blocks.CharBlock(required=False)),
        ('linked_in', blocks.CharBlock(required=False)),
        ('git', blocks.CharBlock(required=False)),
    ])

class HomePage(WagtailCaptchaEmailForm , Page):
    services = RichTextField(blank=True)
    heading = RichTextField(blank=True)
    portfolio = StreamField([('portfolio', PortfolioBlock())], null=True, blank=True,use_json_field=True)
    myteam = StreamField([('myteam', TeamBlock())], null=True, blank=True,use_json_field=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels  + [
        FieldPanel('heading'),
        FieldPanel('services'),
        FieldPanel('myteam'),
        FieldPanel('portfolio'),
    ] + [
        InlinePanel("form_fields", label="Form fields"),
        FieldPanel("thank_you_text", classname="full"),
        MultiFieldPanel(
            [
                FieldRowPanel(
                    [
                        FieldPanel("from_address", classname="col3"),
                        FieldPanel("to_address", classname="col9"),
                    ]
                ),
                FieldPanel("subject"),
            ],
            "Email Notification Config",
        ),
    ]

