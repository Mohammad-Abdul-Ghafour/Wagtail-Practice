import imp
from django.db import models
from django.shortcuts import render

from wagtail.core.models import Page ,Orderable
from wagtail.core.fields import RichTextField , StreamField
from wagtail.admin.edit_handlers import FieldPanel , PageChooserPanel , StreamFieldPanel , InlinePanel , MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.contrib.routable_page.models import RoutablePageMixin , route

from streams import blocks

class HomePageCarouselBanner(Orderable):

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    carousel_title = models.CharField(max_length=60,blank=False,null=True)
    carousel_subtitle = models.TextField(max_length=250,blank=False,null=True)
    carousel_link = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        ImageChooserPanel("carousel_image"),
        FieldPanel("carousel_title"),
        FieldPanel("carousel_subtitle"),
        PageChooserPanel("carousel_link"),
    ]

class HomePage(RoutablePageMixin, Page):
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
            ("card" , blocks.CardsBlock()),
        ],
        null=True,
        blank=True
    ) # Add A Stream Field NOTE: It Takes A List Of Tuples

    max_count = 1 # To have only one home page in the site

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_titles"),
                FieldPanel("banner_subtitle"),
                PageChooserPanel("banner_cta"),
                ImageChooserPanel("banner_image"),      
            ],
            heading="Banner Options"
        ),
        MultiFieldPanel(
            [
                InlinePanel("carousel_images",max_num=5 , min_num=1, label="Image"),
                # InlinePanel("carousel_title", label="Image"),
                # InlinePanel("carousel_subtitle", label="Image"),
                # InlinePanel("carousel_subtitle", label="Image"),
            ],
            heading="Carousel Images"
        ),
        StreamFieldPanel("content"),
    ] # to show the field in the admin panel

    class Meta: # class to give information about the information
        verbose_name = "Home Page" # To change the page Title
        verbose_name_plural = "Home Pages"

    @route(r'^subscribe/$')
    def the_subscribe_page(self,request,*args,**kwargs):
        context = self.get_context(request,*args,**kwargs)
        context["test"] = "Hello world"
        return render(request,"home/subscribe.html",context)