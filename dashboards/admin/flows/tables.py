from django.utils.translation import ugettext_lazy as _

from horizon import tables

 
class MyFilterAction(tables.FilterAction):
    name = "myfilter"


class MyflowsTable(tables.DataTable):
    fix_ip = tables.Column('fix_ip', \
                         verbose_name=_("IP"))
#     id = tables.Column('id', \
#                            verbose_name=_("ID"))
    flows = tables.Column('flows', \
                         verbose_name=_("FLOWS"))
#     bandwidth = tables.Column('bandwidth', \
#                                verbose_name=_("Bandwdth"))
#     def __unicode__(self):
#         return self.fix_ip

    class Meta:
        name = "myflows"
        verbose_name = _("Myflows")
        table_actions = (MyFilterAction,)