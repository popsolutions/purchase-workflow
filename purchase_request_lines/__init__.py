from . import models


def _post_init_update_sequence(env):
    """
    This function is called after the module is installed.
    It updates the sequence of all purchase request lines.
    """
    env["purchase.request.line"].search([])._compute_sequence()
    env.cr.commit()
