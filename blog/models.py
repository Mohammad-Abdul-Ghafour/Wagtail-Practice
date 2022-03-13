import locale
from xml.dom.minidom import TypeInfo
from django.db import models
from django.shortcuts import render
from django import forms

from wagtail.core.models import TranslatableMixin

from modelcluster.fields import (
    ParentalKey,
    ParentalManyToManyField,
)

from wagtail.core.models import (
    Page,
    StreamField,
    Orderable,
)
from wagtail.admin.edit_handlers import (
    StreamFieldPanel,
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import (
    RoutablePageMixin,
    route,
)
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

from streams import blocks

class BlogCategory(TranslatableMixin,models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text="A slug to identify the posts"
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug")
    ]

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

register_snippet(BlogCategory)

class BolgAuthorsOrderable(Orderable):

    page = ParentalKey("blog.BlogDetailPage",related_name="blog_authors")
    author = models.ForeignKey(
        "blog.BlogAuthor",
        on_delete=models.CASCADE,
    )

    panels = [
        SnippetChooserPanel("author")
    ]

class BlogAuthor(TranslatableMixin,models.Model):

    name = models.CharField(max_length=100,null=False,blank=False)
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    email = models.EmailField(null=True,blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                ImageChooserPanel("image")
            ],heading="Name & Image"
        ),
        MultiFieldPanel(
            [
                FieldPanel("email")
            ],heading="Email"
        )
    ]

    def __str__(self):
        return self.name

    class Meta(TranslatableMixin.Meta):
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"

register_snippet(BlogAuthor)

class BlogListPage(RoutablePageMixin,Page):
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
        context['revers_link'] = self.reverse_subpage('last_posts')
        # print(self.get_translations)
        # print(self.locale)
        # print(type(self.locale))
        # print(self.locale.__str__())
        # if request.GET.get(locale,None):
        #     locale = request.GET.get('locale')
        #     context['categories'] = BlogCategory.objects.filter(locale=[locale])

        if self.locale.__str__() == 'English' :
            print('hello')
            context['categories'] = BlogCategory.objects.filter(locale="1")
            context["posts"] = BlogDetailPage.objects.live().public().filter(locale="1")
        elif self.locale.__str__() == 'Arabic':
            context['categories'] = BlogCategory.objects.filter(locale="2")
            context["posts"] = BlogDetailPage.objects.live().public().filter(locale="2")
        return context
    
    @route(r'^latest/$' , name="last_posts")
    def latest_blog_posts(self,request,*args,**kwargs):
        context = self.get_context(request,*args,**kwargs)
        context['posts']= context['posts'][:1]
        context['author']= BlogAuthor.objects.all()
        return render(request,"blog/latest_posts.html", context)

    def get_sitemap_urls(self,request):
        # return [] "This Will remove the blog and latest page from sitemap"
        sitemap = super().get_sitemap_urls(request)
        sitemap.append(
            {
                "location": self.full_url + self.reverse_subpage('last_posts') ,
                "lastmod": (self.last_published_at or self.latest_revision_created_at),
                "priority":0.9, # To add a priority to the page
            }
        )
        return sitemap


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

    categories = ParentalManyToManyField("blog.BlogCategory",blank=True,)

    content = StreamField(
        [
            ("title_and_text" , blocks.TitleAndTextBlock()),
            ("full_richtext" , blocks.RichTextBlock()),
            ("card" , blocks.CardsBlock()),
            ("button", blocks.ButtonBlock()),
        ],
        null=True,
        blank=True,
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
        MultiFieldPanel(
            [
                InlinePanel("blog_authors" , label="Author",min_num=1,max_num=5)
            ],
            heading="Author(s)"
        ),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        )
    ]

class ArticleBlogPage(BlogDetailPage):

    template = "blog/article_blog_page.html"

    subtitle = models.CharField(max_length=100,blank=True,null=True)
    intro_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Intro Image"
    )

    content_panels = BlogDetailPage.content_panels + [
        FieldPanel("subtitle"),
        ImageChooserPanel("intro_image")
    ]