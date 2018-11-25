"""Blueprint for total endpoint

Contains the endpoint that calculates the total sum
"""
import quart

from app.numbers_api import NumbersAPI

total = quart.Blueprint('total', __name__)


def get_api() -> NumbersAPI:
    """Gets and creates the NumbersAPI client"""
    if 'numbers_api' not in quart.g:
        quart.g.numbers_api = NumbersAPI()
    return quart.g.numbers_api


@total.route('')
async def total_endpoint() -> quart.Response:
    """Endpoint, calculates total sum from the numbers api"""
    numbers = await get_api().get()
    return quart.jsonify({"total": sum(numbers)})
