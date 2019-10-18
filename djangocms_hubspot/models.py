# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class HubspotForm(models.Model):
    name = models.CharField(
        max_length=300,
        help_text=_('Name of the form. This is just to identify the form when you want to place it into a page.'),
        blank=False,
        null=False,
    )

    embed_code = models.TextField(
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Hubspot form')
        verbose_name_plural = _('Hubspot forms')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class HubspotCTA(models.Model):
    name = models.CharField(
        max_length=300,
        help_text=_('Name of the CTA. This is just to identify the CTA when you want to place it into a page.'),
        blank=False,
        null=False,
    )

    embed_code = models.TextField(
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('Hubspot CTA')
        verbose_name_plural = _('Hubspot CTAs')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class HubspotFormPluginModel(CMSPlugin):
    form = models.ForeignKey(
        'HubspotForm',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.form.name


@python_2_unicode_compatible
class HubspotCTAPluginModel(CMSPlugin):
    cta = models.ForeignKey(
        'HubspotCTA',
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.cta.name
