from django.db import models
from wagtail.core.models import Page , StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks

class BlogListPage(Page):
    """ Listing all blog detail pages """

    template = "blog/blog_list.html"

    custom_title = models.CharField(
        max_length=40,
        null=False,
        blank=False,
        help_text="Overwrite the default title",
        )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        context =  super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        return context


class BlogDetailPage(Page):

    template = "blog/blog_detail.html"

    custom_title = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Overwrite the default title",
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    content = StreamField(
        [
            ("title_and_text" , blocks.TitleAndTextBlock()),
            ("full_richtext" , blocks.RichTextBlock()),
            ("card" , blocks.CardsBlock()),
        ],
        null=True,
        blank=True,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
    ]
