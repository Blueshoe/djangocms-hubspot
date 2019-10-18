from django import forms

from django_select2.forms import Select2Widget

from djangocms_hubspot.models import HubspotFormPluginModel, HubspotCTAPluginModel, HubspotForm, HubspotCTA


class HubspotFormPluginForm(forms.ModelForm):
    class Meta:
        model = HubspotFormPluginModel
        fields = '__all__'
        widgets = {
            'form': Select2Widget
        }


class HubspotCTAPluginForm(forms.ModelForm):
    class Meta:
        model = HubspotCTAPluginModel
        fields = '__all__'
        widgets = {
            'cta': Select2Widget
        }
