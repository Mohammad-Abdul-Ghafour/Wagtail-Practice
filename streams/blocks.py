from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True , help_text="Add your title")
    text = blocks.TextBlock(required=True , help_text="Add your text")

    class Meta:
        template = "streams/title_and_text.html"
        icon = "edit"
        label = "Title & Text"

class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"

class CardsBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True , help_text="Add your title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image",ImageChooserBlock(required=True)),
                ("title",blocks.CharBlock(required=True,max_length=40)),
                ("text",blocks.TextBlock(required=True)),
                ("page_buttons",blocks.PageChooserBlock(required=False)),
                ("url_button",blocks.URLBlock(required=False))
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon="placeholder"
        label="Cards"