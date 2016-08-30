from django.test import TestCase

from paypal.express.gateway import _get_token_api_type
from paypal.models import ExpressTransaction


class TestGetCurrency(TestCase):

    def setUp(self):
        ExpressTransaction.objects.create(
            token='EC-2U356789SB721815S',
            currency='USD',
            method='DoExpressCheckoutPayment',
            version=119,
            ack='Success',
            raw_request='asdf',
            raw_response='asdf',
            response_time=1)

    def test_get_token_api_type_success(self):
        token = 'EC-2U356789SB721815S'

        assert _get_token_api_type(token) == 'USD'
