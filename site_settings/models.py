from email import header
from django.db import models
from wagtail.contrib.settings.models import BaseSetting , register_setting
from wagtail.admin.edit_handlers import FieldPanel , MultiFieldPanel

@register_setting(icon="media")
class SocialMediaSettings(BaseSetting):

    facebook = models.URLField(blank=True,null=True,help_text="FaceBook URL")
    twitter = models.URLField(blank=True,null=True,help_text="Teitter URL")
    youtube = models.URLField(blank=True,null=True,help_text="Youtube Channel URL")
    linkedin = models.URLField(blank=True,null=True,help_text="Linkedin URL")

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("facebook"),
                FieldPanel("twitter"),
                FieldPanel("youtube"),
                FieldPanel("linkedin"),
            ],heading="Social Media Settings"
        )
    ]
