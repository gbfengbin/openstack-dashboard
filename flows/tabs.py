from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs
import json
import uuid

from openstack_dashboard import api
from openstack_dashboard.dashboards.admin.flows import tables
from dashboards.admin.flows.panel import Flows

class Myflow(object):
    
    def __init__(self,id,ip,flows):
        self.id = id
        self.fix_ip = ip
        self.flows = flows

class MyflowsTab(tabs.TableTab):
    name = _("Myflows Tab")
    slug = "myflows_tab"
    table_classes = (tables.MyflowsTable,)
    template_name = ("horizon/common/_detail_table.html")
    preload = False
# 
#     def has_more_data(self, table):
#         return self._has_more

    def get_myflows_data(self):
        res = []
        id = '1'
        try:
#             marker = self.request.GET.get(
#                         tables.MyflowsTable._meta.pagination_param, None)
            flows = api.neutron.list_myextensions(
                    self.request)
            for inst in flows:
                res.append(Myflow(id,inst['fix_ip'],inst['flows']))
                id = int(id)+1
            
            return res
#             instances, self._has_more = api.nova.server_list(
#                 self.request,
#                 search_opts={'marker': marker, 'paginate': F})
#             myflows = json.loads(flows)
        except Exception:
            self._has_more = False
            error_message = _('Unable to get FLOWS')
            exceptions.handle(self.request, error_message)
  
            return []
#         
#         for flows in myflows:
#             id = '111'
#             res.append(Myflow(id,flows['fix_ip'],flows['flows']))
#         return myflows


class MypanelTabs(tabs.TabGroup):
    slug = "mypanel_tabs"
    tabs = (MyflowsTab,)
    sticky = True