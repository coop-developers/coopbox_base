# -*- coding: utf-8 -*-
import logging

log = logging.getLogger(__name__)

def coopbox_parameters(request):
    parameters = {}
    if request.is_ajax():
        log.debug("Ajax identified")
        parameters['is_json'] = True
    else:
        log.debug("Not ajax")

    return {'coopbox_parameters__': parameters}
