# __author__ = 'fb'
from horizon import forms
from django.utils.translation import ugettext_lazy as _

class MyflowsForms(forms.SelfHandlingForm):
    name = forms.CharField(max_length=255,
                           label=_("Name"),
                           required=False)
    tenant_id = forms.ChoiceField(label=_("Project"))
    # if api.neutron.is_port_profiles_supported():
    #     net_profile_id = forms.ChoiceField(label=_("Network Profile"))
    # admin_state = forms.BooleanField(label=_("Admin State"),
    #                                  initial=True, required=False)
    # shared = forms.BooleanField(label=_("Shared"),
    #                             initial=False, required=False)
    # external = forms.BooleanField(label=_("External Network"),
    #                               initial=False, required=False)