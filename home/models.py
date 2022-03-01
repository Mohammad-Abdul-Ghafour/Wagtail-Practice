from dataclasses import Field
from re import template
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    templates = 'home/home_page.html' # Choose the template to conect the model to
    banner_title = models.CharField(max_length=255 , blank=False , null=True) # add new field to the model

    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ] # to show the field in the admin panel
