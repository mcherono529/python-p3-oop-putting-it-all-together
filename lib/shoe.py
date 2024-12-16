class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size
        self.condition = "New"  
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    def resize(self, new_size):
        self.size = new_size

    def cobble(self):
        self.condition = "New"  
        print("Your shoe is as good as new!")