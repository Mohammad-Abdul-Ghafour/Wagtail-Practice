# Wagtail Practice

## Wagtail Installation

1. First let's make a new directory for our project:
    > mkdir Websites

2. Then to install Wagtail
    1. In our project **`only`**
        > pip install wagtail
    2. To install it on your device **`Globally`** just type the same code in your terminal in the **`Root`**

3. To start your first wagtail project
    > wagtail start mysite

    mysite here is the name of your project

4. Then cd to the project

5. Then enter the shell
    > pipenv shell

6. Then type the following code to extract your dependency to the requirements file for the docker
    > pip install -r requirements.txt

### Add New App To The Project

1. To add new app to the project
    > python manage.py startapp myapp

    Then add the app name to the **`INSTALLED_APPS`** in **`base.py`** file

------------------------------------------

## How To Run Wagtail

1. First we have to migrate
    > python manage.py migrate
2. Then we should create the superuser
    > python manage.py createsuperuser
3. Then we can run the server
    > python manage.py runserver

------------------------------------------

## Install Django Debug Toolbar & Django Shell + Ipython

### Django Debug Toolbar

1. To install Django Debug Toolbar to your project type in the terminal the following code
    > pip install django-debug-toolbar
2. Then in your project folder then settings go to **`dev.py`** file cause this gonna be in the development stage only and add the following to the end of the file

    ```python
        INSTALLED_APPS = INSTALLED_APPS + [
            "debug_toolbar",
        ]
    ```

3. Then in your project folder go to **`urls.py`** and add the following path to the urlpatterns
    > path('__debug__/', include('debug_toolbar.urls'))
4. Then we have to add the following to our middleware in the **`dev.py`**

    ```python
        MIDDLEWARE = MIDDLEWARE + [
            "debug_toolbar.middleware.DebugToolbarMiddleware",
        ]
    ```

5. Last thing we have to add our internal ips also to **`dev.py`**

    ```python
        INTERNAL_IPS = ("127.0.0.1")
    ```

### Django Shell Extension

1. On your terminal type the following
    > pip install django-extensions
2. Then go to **`dev.py`** and just add it to the **`INSTALLED_APPS`**

    ```python
        INSTALLED_APPS = INSTALLED_APPS + [
            "django_extensions",
        ]
    ```

3. Then to enter the shell just run the following on the terminal
    > python manage.py shell_plus

#### Important Codes

* **`__dict__`** : This will give us a dictionary of everything available.

### Ipython

1. On your terminal tyoe the following
    > pip install ipython

2. Then to enter the shell just run the following on the terminal
    > python manage.py shell_plus --ipython

------------------------------------------

## How To Set Site Settings

1. We gonna use **`BaseSetting`** for our class to inherit from.
2. And then we gonna use **`register_setting`** before our class to register it in the settings.

    ```python
    @register_setting(icon="media")
    class SocialMediaSettings(BaseSetting):
        ...
        ...
        ...
        panels = [
            ...
        ]
    ```

3. Then we have to enable the setting so we can get into there from **`base.py`** we go to **`TEMPLATES`** inside **`OPTIONS`** add to the **`context_processors`** the following
    > 'wagtail.contrib.settings.context_processors.settings',
4. Then in **`INSTALLED_APPS`** add the following
    > 'wagtail.contrib.settings',

------------------------------------------

## Routable Page

1. First we have to enable Routable Page from the **`settings`** **`INSTALLED_APPS`**
    > 'wagtail.contrib.routable_page',

2. In the page you needed the route you have to import **`RoutablePageMixin`** & **`route`** from **`wagtail.contrib.routable_page.models`**

------------------------------------------

## Parent Page / Subpage Type Rules

These two attributes allow you to control where page types may be used in your site. It allows you to define rules like **`blog details page`** may only be created under a **`blog list page`**.

Both take a list of model classes or model names. Model names are of the format app_label.ModelName. If the app_label is omitted, the same app is assumed.

1. **`parent_page_types`** : limits which page types this type can be created under.
2. **`subpage_types`** : limits which page types can be created under this type.

By default, any page type can be created under any page type and it is not necessary to set these attributes if that???s the desired behavior.

Setting parent_page_types to an empty list is a good way of preventing a particular page type from being created in the editor interface.

```python
    parent_page_types = ['blog.BlogListPage'] # This means that the page can be created only under blog list page as its parent.
    subpage_types = [] # Empty list means this page has no subpages under it.
```

------------------------------------------

## Advanced StreamField

### StreamField Content Value

In StreamField we know that we have to loop over all elements or blocks inside it, but what if we need to reach one specific block and render only part of it ?

We can use **`Value`** method as the following:

```python
{% for block in page.content %}
    {% if block.block_type == 'person' %}
        <h2>{{ block.value.first_name }} {{ block.value.surname }}</h2>
    {% endif %}
{% endfor %}
```

Here we reached the person block under content streamfield and only get the first_name and surname.

To know more about StreamField you can browse them in [wagtail documentation](https://docs.wagtail.org/en/stable/topics/streamfield.html#streamfield)

### StreamField Block Count

Sometimes we need to make a block in StreamField that we can add only number of times so how to do that ?

Simply we can give the StreamField max_num and min_num as the following.

```python
    content = StreamField(
        [

            ("Banner", blocks.Banner()),
            ("Text_With_Right_Image", blocks.TextWithRightImage()),
            ("Text_With_Left_Image", blocks.TextWithLeftImage()),
            ("Text", blocks.AboutUsBlock()),            
            ("Most_Popular_Programs", blocks.Admission()),
            ("YouTube_Video_Block", blocks.YouTubeVideoBlock()),
            ("Calendar", blocks.Calendar()),

        ], max_num = 2,min_num = 1, 
        null = True,
        blank = True,
        
    )
```

In this case we give all block in the **`StreamField`** max and min number, to give a specific block we can add **`block_count`** to it and specify the block as the following.

```python
    content = StreamField(
        [

            ("Banner", blocks.Banner()),
            ("Text_With_Right_Image", blocks.TextWithRightImage()),
            ("Text_With_Left_Image", blocks.TextWithLeftImage()),
            ("Text", blocks.AboutUsBlock()),            
            ("Most_Popular_Programs", blocks.Admission()),
            ("YouTube_Video_Block", blocks.YouTubeVideoBlock()),
            ("Calendar", blocks.Calendar()),

        ],block_counts= {
        'Calendar': {'max_num': 1},
        }
        , 
        null = True,
        blank = True,
        
    )
```

And there are much more to control to the StreamField, you can browse them in [wagtail documentation](https://docs.wagtail.org/en/latest/reference/streamfield/blocks.html).

------------------------------------------

## Sitemaps

1. First we have to enable Sitemaps from the **`settings`** **`INSTALLED_APPS`** for **`django`** and **`wagtail`**

    ```python
        'wagtail.contrib.sitemaps',
        'django.contrib.sitemaps',
    ```

2. Then we have to import wagtail sitemaps views to our project **`urls.py`**
    > from wagtail.contrib.sitemaps.views import sitemap

3. Then add our url to **`urlpatterns`**

    ```python
        path(r'^sitemap.xml$', sitemap)
    ```

------------------------------------------

## Wagtail Localization

### Installing Wagtail Localize

1. Install using pip:

    > pip install wagtail-localize

2. Add **`wagtail_localize`** and **`wagtail_localize.locales`** to your **`INSTALLED_APPS`** setting:

    ```python
    INSTALLED_APPS = [
        # ...
        "wagtail_localize",
        "wagtail_localize.locales",  # This replaces "wagtail.locales"
        # ...
    ]
    ```

### Enabling internationalization

1. To enable internationalization in both Django and Wagtail, set the following settings to True

    ```python
    USE_I18N = True
    WAGTAIL_I18N_ENABLED = True
    USE_L10N = True
    ```

2. Next we need to configure the available languages

    ```python
    WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('en', "English"), # The first option should be the same as the default language (LANGUAGE_CODE)
    ('ar', "Arabic"),
    ]
    ```

3. To allow all of the page trees to be served at the same domain, we need to add a URL prefix for each language.

    ```python
    from django.conf.urls.i18n import i18n_patterns

    urlpatterns = [
        path('django-admin/', admin.site.urls),

        path('admin/', include(wagtailadmin_urls)),
        path('documents/', include(wagtaildocs_urls)),
    ]

    urlpatterns += i18n_patterns(
        path('search/', search_views.search, name='search'),
        path("", include(wagtail_urls)),
    )
    ```

4. After wrapping your URL patterns with i18n_patterns, your site will now respond on URL prefixes. But now it won???t respond on the root path.

    ```python
    MIDDLEWARE = [
    # ... NOTE: After SessionMiddleware 
    'django.middleware.locale.LocaleMiddleware',
    # ... NOTE: Before CommonMiddleware
    ]
    ```

5. Here is a basic example of how to add link to switch between translations of a page.

    ```python
    {% load i18n wagtailcore_tags %}

    {% if page %}
    {% for translation in page.get_translations.live %}
        {% get_language_info for translation.locale.language_code as lang %}
        <a href="{% pageurl translation %}" rel="alternate" hreflang="{{ language_code }}">
            {{ lang.name_local }}
        </a>
    {% endfor %}
    {% endif %}

    # NOTE: Should be at the beginning of the HTML file
    ```

6. Then in the admin site under **`setting`** a **`locales`** tab where we can add new language to our website.

### NOTES

1. The Wagtail Localization started supporting **`ListBlock`** in version 2.16.1 of **`wagtail`** and version 1.1 of **`wagtail-localize`** / 2022-3-11.

2. For the snippets we need to use **`TranslatableMixin`** in its class.

3. If we have **`get_context`** function in one of our classes we need to manually filter the object class according to the language

    eg.

    ```python
    # This is one of the ways to do so.
    if self.locale.__str__() == 'English' :
        context['categories'] = BlogCategory.objects.filter(locale="1")
        context["posts"] = BlogDetailPage.objects.live().public().filter(locale="1")
    elif self.locale.__str__() == 'Arabic':
        context['categories'] = BlogCategory.objects.filter(locale="2")
        context["posts"] = BlogDetailPage.objects.live().public().filter(locale="2")
    ```

### References

* [Wagtail Transifex](https://www.transifex.com/torchbox/wagtail/)
* [Wagtail localization Documentation](https://docs.wagtail.org/en/stable/advanced_topics/i18n.html#id25)

------------------------------------------

## Dynamic Nav Bar (Menus)

### As Snippet

1. We have to create new model for the menus and it will inherit from **`ClusterableModel`**
    > class Menu(ClusterableModel)

2. Then we can create an Orderable Class or we can just use StreamField directly.

3. Then we have to regist the Menus class as snippets.

4. Then inside our menus app we have to create new folder **`templatetags`** and under it create **`menus_tags.py`** file.

5. In **`menus_tags.py`** we have to regist a **`simple_tag`**.

    ```python
    from django import template
    from ..models import Menu

    register = template.Library()

    @register.simple_tag()
    def get_menu(slug):
        return Menu.objects.get(slug=slug)
    ```

### As Setting (@Todo)

------------------------------------------

## Admin Site Customization (@Todo)

------------------------------------------

## Customize Wagtail

### Customize Wagtail Admin UI Colors and Styling

1. First we have to enable wagtail **`Styleguide`**, to do so we have to go to **`dev.py`** in the **`INSTALLED_APPS`** and the following
    > 'wagtail.contrib.styleguide',

    Now in the admin site under setting tab we can see that there is new tab called **`styleguide`**

2. Then we have to create new app and let's call it **`core`** and add it to our **`INSTALLED_APPS`**

3. Then inside the core app we have to create new file and call it **`wagtail_hooks.py`**

4. Then there are many hooks to use but for styling we gonna use the **`insert_global_admin_css`**

    ```python
    from django.utils.html import format_html
    from django.templatetags.static import static

    from wagtail.core import hooks

    @hooks.register('insert_global_admin_css')
    def global_admin_css():
        return format_html('<link rel="stylesheet" href="{}">', static('css/theme.css'))
        # static function here is just to indicate to our static folder
        ## and this link static/css/theme.css will replace what inside the {} in our href
    ```

5. Then we create the css file inside our static and put our style there

There is a lot more hooks, we can find them in their documentation.

[Wagtail Hooks](https://docs.wagtail.org/en/stable/reference/hooks.html?highlight=hooks)

### Customize Wagtail Admin Templates

There is many things that we can customize in wagtail template but we gonna only implement one of them to change the template logo

1. First we need to either to use one of our existing apps or we can create new one for it

2. Then inside the app we create **`templates/wagtailadmin/base.html`**

3. Then inside this **`base.html`** we can override the logo image

    ```python
    {% extends "wagtailadmin/base.html" %}
    {% load static %} # To load our image from the static folder

    {% block branding_logo %}
        <div style="width:100px; background-color:#D5D5D5; height:100px; line-height:115px; border-radius:100% ; text-align:center">
        <img src="{% static 'images/LTUC.png' %}" alt="Custom Project" width="80" />
        </div>
    {% endblock %}
    ```

There is a lot more that we can customize, we can find them in their documentation.

[Customizing Wagtail Admin Templates](https://docs.wagtail.org/en/stable/advanced_topics/customisation/admin_templates.html)

------------------------------------------

## Wagtail Imports

```python
# Models
from wagtail.core import blocks
from wagtail.core.models import (
    Page,
    Orderable,
    TranslatableMixin, # For snippets to make them translatable
)
# Fields
from wagtail.core.fields import (
    RichTextField,
    StreamField,
)
from modelcluster.fields import (
    ParentalKey,
    ParentalManyToManyField,
)
# Admin Panels
from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
    InlinePanel,
)
# Images
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
# Site Settings Models
from wagtail.contrib.settings.models import (
    BaseSetting,
    register_setting,
)
# Routable Page
from wagtail.contrib.routable_page.models import (
    RoutablePageMixin,
    route,
)
# Snippets
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
# Model Admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
# Django Imports
from django.db import models
from django.shortcuts import render
from django import forms
    ## For Localization
    from django.conf.urls.i18n import i18n_patterns

# Customizing Admin UI
from django.utils.html import format_html
from django.templatetags.static import static
from wagtail.core import hooks
```

------------------------------------------
