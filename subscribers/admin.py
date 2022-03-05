from wagtail.contrib.modeladmin.options import ModelAdmin , modeladmin_register
from .models import Subscriber

class SubscriberAdmin(ModelAdmin):

    model = Subscriber
    menu_lable = "Subscriber"
    menu_icon = "group"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email" , "user_name",)
    search_fields = ("email" , "user_name",)

modeladmin_register(SubscriberAdmin)