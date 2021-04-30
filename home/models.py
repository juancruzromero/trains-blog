from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField # Dar la posiblidad de hacer una edición más linda.
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class HomePage(Page): # Podemos importar Banner.
    """HomePage model."""
    template = "home/home_page.html"

    max_count = 1 # Una sola instancia de home page.

    # Escribo en la BBDD
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold","italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    # Lo agrego al admin.
    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta")
    ]

    # TODO: https://www.youtube.com/watch?v=vp8XSkDlMkc&list=PLMQHMcNi6ocsS8Bfnuy_IDgJ4bHRRrvub&index=4

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
