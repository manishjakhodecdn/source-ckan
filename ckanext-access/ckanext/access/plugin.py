import os
from logging import getLogger
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.contact.auth import send_contact

log = getLogger(__name__)

class AccessPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True )
    plugins.implements(plugins.IAuthFunctions)		

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'access')
    ## IRoutes
    def before_map(self, map):

        # Add controller for KE EMu specimen records
        map.connect('access_form', '/access_request',
                    controller='ckanext.access.controllers.access:AccessController',
                    action='form')

        # Add AJAX request handler
        map.connect('access_ajax_submit', '/access_request/ajax',
                    controller='ckanext.access.controllers.access:AccessController',
                    action='ajax_submit')

        return map

    ## IAuthFunctions
    def get_auth_functions(self):
        return {'access_contact': send_contact}
