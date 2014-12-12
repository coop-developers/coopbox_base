# -*- coding: utf-8 -*-
import logging

log = logging.getLogger(__name__)

def coopbox_parameters(request):
    """Detect request type and add parameters to the request context,
    thus allowing the page template to decide how rendering should be
    handled
    """
    parameters = {}
    if request.is_ajax():
        log.debug("Ajax identified")
        parameters['is_json'] = True
    else:
        log.debug("Not ajax")

    return {'coopbox_parameters__': parameters}
