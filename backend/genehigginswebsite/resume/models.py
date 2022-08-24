from django.db import models
from django import forms
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class ResumePage(Page):
    name = models.TextField(
        blank=False,
        max_length=250,
    )
    address = models.CharField(
        blank=True,
        max_length=500,
    )

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        FieldPanel(
            "address",
            classname="howdy",
            widget=forms.Textarea,
        ),
    ]