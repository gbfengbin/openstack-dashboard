from horizon import tabs
from django.utils.translation import ugettext_lazy as _
import logging
from horizon import exceptions
from openstack_dashboard.dashboards.admin.flows \
    import tabs as flows_tabs
    
from openstack_dashboard import api


class IndexView(tabs.TabbedTableView):
    tab_group_class = flows_tabs.MypanelTabs
    template_name = 'admin/flows/index.html'

    def get_data(self):
#         try:
#             flows = api.neutron.list_myextensions()(self.request)
#         except Exception:
#             flows = []
#             msg = _('Network list can not be retrieved.')
#             exceptions.handle(self.request, msg)
        return []
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            context["version"] = 'version'
        except Exception:
            exceptions.handle(self.request,
                _('Unable to retrieve version information.'))

        return context