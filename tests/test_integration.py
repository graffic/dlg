from app import build_app
import pytest


@pytest.mark.asyncio
async def test_get():
    app = build_app()
    response = await app.test_client().get('/total')
    assert await response.json == {'total': 500000500000}
