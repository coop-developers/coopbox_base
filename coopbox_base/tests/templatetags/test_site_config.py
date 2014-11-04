import mock
import pytest
from coopbox_base.templatetags import site_config


class FakeConfig(object):

    CONFIG_ENTRY_1 = mock.sentinel.conf_entry_1


@pytest.yield_fixture
def mock_django_config():
    with mock.patch.object(site_config, 'settings', new=FakeConfig):
        yield


def test_site_config_default_behavior_passes_django_config(mock_django_config):
    assert FakeConfig == site_config.site_config()


def test_site_config_lookup_behavior(mock_django_config):
    assert mock.sentinel.conf_entry_1 == \
        site_config.site_config('CONFIG_ENTRY_1')
    assert None == site_config.site_config('NO_SUCH_ENTRY')
