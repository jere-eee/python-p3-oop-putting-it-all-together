#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size) -> None:
        self.brand = brand
        self.size = size
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        self._brand = brand
        
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self._size = size
    
    def cobble(self):
        self.condition = "New"
        print('Your shoe is as good as new!')
    