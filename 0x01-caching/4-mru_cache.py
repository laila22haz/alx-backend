#!/usr/bin/env python3
"""LIFO caching"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """class FIFO"""
    def __init__(self):
        """init fuction"""
        super().__init__()
        self.dq = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard_key = self.dq.pop(0)
                del self.cache_data[discard_key]
                print("DISCARD:", discard_key, end="\n")
            self.cache_data[key] = item
            self.dq.insert(0, key)

    def get(self, key):
        """get funtion"""
        if key is not None and key in self.cache_data:
            self.dq.remove(key)
            self.dq.append(key)
            return self.cache_data[key]
        return None
