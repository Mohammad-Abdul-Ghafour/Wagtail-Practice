from django.db import models

from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import StreamField

from streams import blocks

class FlexPage(Page):

    template = "flex/flex_page.html"

    subtitle = models.CharField(max_length=255,null=True,blank=True)
    content = StreamField(
        [
            ("card" , blocks.CardsBlock()), # ("The name of the stream field you can name it any thing but once you did you can't change it cause wagtail use it", Add out block from streams)
        ],
        null=True,
        blank=True
    ) # Add A Stream Field NOTE: It Takes A List Of Tuples

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
        StreamFieldPanel("content")
    ]

    class Meta :
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
