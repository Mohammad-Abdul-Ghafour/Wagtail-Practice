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

class LinkStructValue(blocks.StructValue):

    def url(self):
        page_button = self.get('page_buttons')
        url_button = self.get('url_button')
        if page_button:
            return page_button.url
        elif url_button:
            return url_button.url
        return None

class ButtonBlock(blocks.StructBlock):

    page_buttons = blocks.PageChooserBlock(required=False)
    url_button = blocks.URLBlock(required=False)

    class Meta:
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Single Button"
        value_class = LinkStructValue

class DropDownBlock(blocks.StructBlock):

    link_title = blocks.CharBlock(required=True,max_length=40)
    link_page = blocks.PageChooserBlock(required=False)
    link_url = blocks.URLBlock(required=False)

    class Meta:
        template = "streams/drop_down_block.html"
        icon="placeholder"