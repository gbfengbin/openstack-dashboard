from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.admin import dashboard


class Flows(horizon.Panel):
    name = _("Flows")
    slug = "flows"


dashboard.Admin.register(Flows)
