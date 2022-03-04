from dataclasses import Field
from pyexpat import features
from re import T, template
from tabnanny import verbose
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField , StreamField
from wagtail.admin.edit_handlers import FieldPanel , PageChooserPanel , StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

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
    content = StreamField(
        [
            ("title_and_text" , blocks.TitleAndTextBlock()), # ("The name of the stream field you can name it any thing but once you did you can't change it cause wagtail use it", Add out block from streams)
            ("full_richtext" , blocks.RichTextBlock()),
        ],
        null=True,
        blank=True
    ) # Add A Stream Field NOTE: It Takes A List Of Tuples

    max_count = 1 # To have only one home page in the site

    content_panels = Page.content_panels + [
        FieldPanel("banner_titles"),
        FieldPanel("banner_subtitle"),
        PageChooserPanel("banner_cta"),
        ImageChooserPanel("banner_image"),
        StreamFieldPanel("content")
    ] # to show the field in the admin panel

    class Meta: # class to give information about the information
        verbose_name = "Home Page" # To change the page Title
        verbose_name_plural = "Home Pages"