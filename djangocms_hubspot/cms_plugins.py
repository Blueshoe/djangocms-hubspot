# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from djangocms_hubspot.forms import HubspotFormPluginForm, HubspotCTAPluginForm
from djangocms_hubspot.models import HubspotFormPluginModel, HubspotCTAPluginModel
from django.utils.translation import gettext_lazy as _


@plugin_pool.register_plugin
class HubspotFormPlugin(CMSPluginBase):
    model = HubspotFormPluginModel
    form = HubspotFormPluginForm
    name = _('Hubspot Form')
    module = _('Hubspot')
    render_template = 'djangocms_hubspot/plugins/form.html'
    cache = True
    text_enabled = True


@plugin_pool.register_plugin
class HubspotCTAPlugin(CMSPluginBase):
    model = HubspotCTAPluginModel
    form = HubspotCTAPluginForm
    name = _('Hubspot CTA')
    module = _('Hubspot')
    render_template = 'djangocms_hubspot/plugins/cta.html'
    cache = True
    text_enabled = True
