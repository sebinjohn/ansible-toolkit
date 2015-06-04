import ansible.inventory
import ansible.runner
import ansible.callbacks
import ansible.cache

from ansible.runner import Runner
from ansible.utils.template import template_from_file

from utils import get_inventory
from utils_ansible import gather_facts as get_gathered_facts


def show_template(host, path, gather_facts=True):
    inventory = get_inventory()
    setup_cache = get_gathered_facts(host, inventory) if gather_facts else {}

    # Show the template
    runner = Runner(
        inventory=inventory,
        setup_cache=setup_cache,
    )
    host_vars = runner.get_inject_vars(host)
    print template_from_file('.', path, host_vars)