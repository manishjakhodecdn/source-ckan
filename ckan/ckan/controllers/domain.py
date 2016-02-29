import re

import ckan.controllers.group as group
import ckan.plugins as plugins


class DomainController(group.GroupController):
    ''' The organization controller is for Organizations, which are implemented
    as Groups with is_organization=True and group_type='domain'. It works
    the same as the group controller apart from:
    * templates and logic action/auth functions are sometimes customized
      (switched using _replace_group_org)
    * 'bulk_process' action only works for organizations

    Nearly all the code for both is in the GroupController (for historical
    reasons).
    '''

    group_types = ['domain']

    def _guess_group_type(self, expecting_name=False):
        return 'domain'

    def _replace_group_org(self, string):
        ''' substitute domain for group if this is an domain'''
        return re.sub('^group', 'domain', string)

    def _update_facet_titles(self, facets, group_type):
        for plugin in plugins.PluginImplementations(plugins.IFacets):
            facets = plugin.domain_facets(
                facets, group_type, None)
