import os
from logging import getLogger
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.contact.auth import send_contact

log = getLogger(__name__)

class FeaturesPlugin(plugins.SingletonPlugin):

    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True )
    plugins.implements(plugins.IAuthFunctions)		

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'features')

    ## IRoutes
    def before_map(self, map):

        # Add controller for KE EMu specimen records
        map.connect('feature_form', '/features',
                    controller='ckanext.features.controllers.feature:FeatureController',
                    action='form')

        # Add AJAX request handler
        map.connect('feature_ajax_submit', '/features/ajax',
                    controller='ckanext.features.controllers.feature:FeatureController',
                    action='ajax_submit')

        return map

    ## IAuthFunctions
    def get_auth_functions(self):
        return {'features_contact': send_contact}

