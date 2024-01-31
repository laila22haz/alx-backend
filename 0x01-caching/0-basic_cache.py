#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class BasicCache"""
    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get funtion"""
        if key is not None:
            return self.cache_data.get(key)
        return None
