from dataclasses import Field
from pyexpat import features
from re import T, template
from tabnanny import verbose
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel , PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page):
    templates = 'home/home_page.html' # Choose the template to conect the model to
    banner_titles = models.CharField(max_length=255 , blank=False , null=True) # Add new field to the model
    banner_subtitle = RichTextField(features=["bold", "italic"]) # Add a subtitle to the banner
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    ) # Add image choose field
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    ) # Add Call To Action Field Where we can choose a page to redirect to when we click on banner

    max_count = 1 # To have only one home page in the site

    content_panels = Page.content_panels + [
        FieldPanel("banner_titles"),
        FieldPanel("banner_subtitle"),
        PageChooserPanel("banner_cta"),
        ImageChooserPanel("banner_image")
    ] # to show the field in the admin panel

    class Meta: # class to give information about the information
        verbose_name = "Home Page" # To change the page Title
        verbose_name_plural = "Home Pages"