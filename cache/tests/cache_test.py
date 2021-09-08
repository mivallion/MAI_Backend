def test_simple_set_get(cache):
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    assert cache.get('Jesse') == 'James'
    cache.rem('Walter')
    assert cache.get('Walter') == ''


def test_empty_cache(cache):
    assert cache.get("Jesse") == ''


def test_over_capacity(small_cache):
    small_cache.set('Jesse', 'Pinkman')
    small_cache.set('Walter', 'White')
    assert small_cache.get("Jesse") == ''
    assert small_cache.get("Walter") == 'White'
