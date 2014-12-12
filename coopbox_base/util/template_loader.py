import logging
import copy
from django_jinja import loaders
from jinja2 import Template


log = logging.getLogger(__name__)


# XXX: replace with config
BLOCK_IDS = {
    'main': 'ebee4a8063f2dedde170ebd01e6fc77cc4438faf03cb719c1d9e779919cfa1d5',
}

START_BLOCK_MATCH = r'<!-- BLOCK: %(blockname)s %(blockid)s -->'
END_BLOCK_MATCH = r'<!-- ENDBLOCK: %(blockname)s %(blockid)s -->'


class TemplateProxy(object):

    def __init__(self, template):
        self.template = template
        self._inject_proxy()

    def render(self, context):
        context['block_embedded_id__'] = BLOCK_IDS
        rendered = self._old_render(context)
        rendered = unicode(rendered)

        try:
            original_blocks = {}
            for k,v in BLOCK_IDS.iteritems():
                open_match = START_BLOCK_MATCH % {'blockname': k, 'blockid': v}
                close_match = END_BLOCK_MATCH % {'blockname': k, 'blockid': v}
                start_pos = rendered.index(open_match)
                end_pos = rendered.index(close_match)

                original_blocks[k] = rendered[start_pos + len(open_match):end_pos]
        except ValueError:
            return rendered

        rerender_context = copy.copy(context)  # Do only a shallow copy since we are not modifying any existing content
        rerender_context['original_blocks'] = original_blocks
        return global_loader.load_template('coopbox_base/wrap.django.regular.jinja')[0].render(rerender_context)

    def _inject_proxy(self):
        if not isinstance(self.template, Template):
            self._old_render = self.template.render
            self.template.render = self.render

    def get_proxied_template(self):
        return self.template

class LoaderMixin(object):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        template, stuff = super(LoaderMixin, self).load_template(template_name, template_dirs)
        return TemplateProxy(template).get_proxied_template(), stuff


class AppLoader(LoaderMixin, loaders.AppLoader):
    pass

class FileSystemLoader(LoaderMixin, loaders.FileSystemLoader):
    pass

global_loader = AppLoader()
