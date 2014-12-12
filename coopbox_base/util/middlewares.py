# -*- coding: utf-8 -*-
import logging

log = logging.getLogger(__name__)


class CoopboxMiddleware(object):
    """
    Handle Coop request and response objects.  Works in conjuction with
    coopbox_base.util.context_processors.coopbox_parameters
    """
    def process_response(self, request, response):
        if response.status_code == 200 and request.is_ajax():
            # XXX: force response to be json if successful and is_ajax.
            #      change this to be a bit more sophisticated to avoid
            #      special edge cases ($.load for example).
            response['Content-Type'] = 'application/json'
        return response
