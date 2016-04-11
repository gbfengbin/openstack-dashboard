# __author__ = 'fb'
from neutron.api import extensions
from neutron import manager
from neutron.api.v2 import base
from neutron import wsgi
from neutron.openstack.common import jsonutils
import json
# from neutron.db.l3_db import L3_NAT_dbonly_mixin
from neutron.plugins.common import constants as plugin_constants

class MyextensionController(wsgi.Controller):
    
    def l3plugin(self):
        if not hasattr(self, '_l3plugin'):
            self._l3plugin = manager.NeutronManager.get_service_plugins()[
                plugin_constants.L3_ROUTER_NAT]
        return self._l3plugin

    def index(self, request):
        self.l3plugin()
        data = self._l3plugin.get_flows(request.context, '192.168.1.23')
#         data = {'ip':"192.168.1.1",'bandwidth':3.0,'request':'%s'%request}
        data_string = json.dumps(data)
        return data_string

class Myextension(extensions.ExtensionDescriptor):
    # The name of this class should be the same as the file name
    # The first letter must be changed from lower case to upper case
    # There are a couple of methods and their properties defined in the
    # parent class of this class, ExtensionDescriptor you can check them

    @classmethod
    def get_name(cls):
        # You can coin a name for this extension
        return "My Extension"

    @classmethod
    def get_alias(cls):
        # This alias will be used by your core_plugin class to load
        # the extension
        return "my-extensions"

    @classmethod
    def get_description(cls):
        # A small description about this extension
        return "An extension defined by myself. Haha!"

    @classmethod
    def get_namespace(cls):
        # The XML namespace for this extension
        return "http://docs.openstack.org/ext/myextension/api/v1.0"

    @classmethod
    def get_updated(cls):
        # Specify when was this extension last updated,
        # good for management when there are changes in the design
        return "2014-08-07T00:00:00-00:00"

    @classmethod
#     def get_resources(cls):
#         # This method registers the URL and the dictionary  of
#         # attributes on the neutron-server.
#         exts = []
#         plugin = manager.NeutronManager.get_plugin()
#         resource_name = 'myextension'
#         collection_name = '%ss' % resource_name
#         params = RESOURCE_ATTRIBUTE_MAP.get(collection_name, dict())
#         controller = base.create_resource(collection_name, resource_name,
#                                           plugin, params, allow_bulk=False)
#         ex = extensions.ResourceExtension(collection_name, controller)
#         exts.append(ex)
#         return exts
    def get_resources(self):
        resources = []
        resource = extensions.ResourceExtension('myextensions',
                                                MyextensionController())
        resources.append(resource)
        return resources
#     def get_extended_resources(self, version):
#         if version == "2.0":
#             return RESOURCE_ATTRIBUTE_MAP
#         else:
#             return {}
    def get_request_extensions(self):
        request_exts = []

#         def _goose_handler(req, res):
#             #NOTE: This only handles JSON responses.
#             # You can use content type header to test for XML.
#             data = jsonutils.loads(res.body)
#             data['FOXNSOX:googoose'] = req.GET.get('chewing')
#             res.body = jsonutils.dumps(data)
#             return res
# 
#         req_ext1 = extensions.RequestExtension('GET', '/dummy_resources/:(id)',
#                                                _goose_handler)
#         request_exts.append(req_ext1)

        def _bands_handler(req, res):
            #NOTE: This only handles JSON responses.
            # You can use content type header to test for XML.
            data = jsonutils.loads(res.body)
            data['myextension'] = 'Pig Bands!'
            res.body = jsonutils.dumps(data)
            return res

        req_ext2 = extensions.RequestExtension('GET', '/dummy_resources/:(id)',
                                               _bands_handler)
        request_exts.append(req_ext2)
        return request_exts

# RESOURCE_ATTRIBUTE_MAP = {
#     'myextensions': {
#         'ip': {'allow_post': False, 'allow_put': False,
#                'is_visible': True},
# #         'name': {'allow_post': True, 'allow_put': True,
# #                           'is_visible': True},
#         'flows': {'allow_post': True, 'allow_put': False,
#                       'validate': {'type:string': None},
# #                       'required_by_policy': True,
#                       'is_visible': True}
#         }
#     }