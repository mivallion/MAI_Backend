import pytest

from utils.cache import LRUCache


@pytest.fixture()
def cache():
    return LRUCache(100)


@pytest.fixture()
def small_cache():
    return LRUCache(1)
