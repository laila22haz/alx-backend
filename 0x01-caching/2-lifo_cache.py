#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class FIFO"""
    def __init__(self):
        """init fuction"""
        super().__init__()
        self.key_idexes = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discared = self.key_idexes.pop()
            del self.cache_data[item_discared]
            print("DISCARD:", item_discared, end="\n")
        self.key_idexes.append(key)

    def get(self, key):
        """get funtion"""
        if key is not None:
            return self.cache_data.get(key)
        return None
