from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import (
    MultiFieldPanel,
    FieldPanel,
    # InlinePanel,
    # PageChooserPanel,
    StreamFieldPanel,
    )
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from streams import blocks

# from django_extensions.db.fields import AutoSlugField
# from modelcluster.fields import ParentalKey
# from wagtail.core.models import Orderable
# from wagtail.core import hooks

# ---------------------------------------------------
#                  With Orderable
# ---------------------------------------------------

# class MenuItem(Orderable):
    
#     page = ParentalKey("Menu", related_name="menu_items")
#     link_title = models.CharField(blank=True,null=True,max_length=50)
#     link_page = models.ForeignKey(
#         "wagtailcore.Page",
#         null=True,
#         blank=True,
#         related_name="+",
#         on_delete=models.CASCADE,
#     )
#     open_in_new_tab = models.BooleanField(default=False,blank=True,)

#     content = StreamField(
#         [
#             ("drop_down",blocks.DropDownBlock()),
#         ],
#         null=True,
#         blank=True
#     )

#     panels = [
#         FieldPanel("link_title"),
#         PageChooserPanel("link_page"),
#         FieldPanel("open_in_new_tab"),
#         StreamFieldPanel("content"),
#     ]

# @register_snippet
# class Menu(ClusterableModel):

#     title = models.CharField(max_length=100 , choices=[("LTUC","LTUC"),("ASAC","ASAC"),])
#     slug = models.SlugField(auto_created=True,help_text="Don't Change This Field")
#     # slug = AutoSlugField(populate_from="title",editable=True,help_text="Don't Change This Field")

#     panels = [
#         MultiFieldPanel([
#             FieldPanel("title"),
#             FieldPanel("slug"),
#         ],heading = "Menu"),
#         InlinePanel("menu_items",max_num=4,min_num=1,label="Menu Item")
#         # InlinePanel("menu_items",max_num=4,min_num=1,label="Menu Item")
#     ]

#     def __str__(self):
#         return self.title

# # Menu._meta.get_field("title").default = "Main"
# # Menu._meta.get_field("slug").default = "main"

# ---------------------------------------------------

# ---------------------------------------------------
#                 Without Orderable
# ---------------------------------------------------

@register_snippet
class Menu(ClusterableModel):

    title = models.CharField(max_length=100,choices=[("Main","Main")])
    slug = models.SlugField(auto_created=True,editable=True,help_text="Don't Change This Field")
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        help_text="Add You Navigation Logo"
    )
    content = StreamField(
        [
            ("schools",blocks.DropDownBlock()),
            ("admissions",blocks.DropDownBlock()),
            ("home",blocks.DropDownBlock()),
            ("news_And_Events",blocks.DropDownBlock()),
            ("careers",blocks.DropDownBlock()),
            ("alumni",blocks.DropDownBlock()),
            ("about_Us",blocks.DropDownBlock()),
            ("contact_Us",blocks.DropDownBlock()),
        ],
        null=True,
        blank=True
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("title"),
            FieldPanel("slug"),
            ImageChooserPanel("logo"),
        ],heading = "Menu"),
        StreamFieldPanel("content"),
    ]

    def __str__(self):
        return self.title
