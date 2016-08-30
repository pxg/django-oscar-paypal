from unittest import TestCase

import redis
from django.conf import settings

from paypal.express.gateway import (
    _delete_token,
    _get_token_api_type,
    _set_token_api_type)


class TestRedis(TestCase):

    def setUp(self):
        self.redis = redis.StrictRedis(
            host=settings.PAYPAL_REDIS_HOST,
            port=settings.PAYPAL_REDIS_PORT,
            db=settings.PAYPAL_REDIS_DB,
            charset='utf-8',
            decode_responses=True)

    def test_set_token_api_type_success(self):
        token = 'EC-2U356789SB721815S'

        response = _set_token_api_type(token, 'USD', settings)

        assert response is True
        assert self.redis.get(token) == 'USD'

    def test_get_token_api_type_success(self):
        token = 'EC-8BP68231BP0804219'
        self.redis.set(token, 'GBP')

        response = _get_token_api_type(token, settings)

        assert response == 'GBP'

    def test_delete_token_api_type_success(self):
        token = 'EC-4WS32132GP853923C'
        self.redis.set(token, 'GBP')

        response = _delete_token(token, settings)

        assert response is 1
        assert self.redis.get(token) is None
