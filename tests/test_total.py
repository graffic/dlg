from unittest.mock import patch
from quart.ctx import _AppCtxGlobals
from app.total import get_api
from app.numbers_api import NumbersAPI


@patch('quart.g', _AppCtxGlobals())
def test_get_api_exists():
    from quart import g
    g.numbers_api = 'potato'
    assert get_api() == 'potato'


@patch('quart.g', _AppCtxGlobals())
def test_get_api_does_not_exist_creates_new():
    assert get_api() == NumbersAPI()
