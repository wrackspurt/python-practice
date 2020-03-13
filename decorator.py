"""
Task 2
Написать кэширующий декоратор с параметром use_cache, который по умолчанию True. Должен уметь кэшировать любую функцию.
"""


def make_hashable(*args, **kwargs):
    return hash(str(args) + str(kwargs))


def caching(use_cache=True):
    def caching_decorator(f):
        cache = dict()

        def cache_function(*data, **kwdata):
            if use_cache is True:
                new_data = make_hashable(data, kwdata)
                if new_data not in cache:
                    cache[new_data] = f(*data, **kwdata)
                return cache[new_data]
            else:
                print('no cache')
                return f(*data, **kwdata)
        return cache_function
    return caching_decorator
