from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community',
}


from ansible.errors import AnsibleFilterError
from ansible.utils.display import Display

display = Display()


def my_filter_test2(input, *args, **kwargs):
    return "unko!" + input
    # raise AnsibleFilterError('hello ansible filter!')


# ---- Ansible filters ----
class FilterModule(object):
    def filters(self):
        return {
            'my_filter_test': my_filter_test2,
        }
