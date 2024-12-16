class Book:
    def __init__(self, title, page_count):
        if not title:
            raise ValueError("Title cannot be empty.")
        if not isinstance(page_count, int) or page_count <= 0:
            raise ValueError("Page count must be a positive integer.")

        self._title = title
        self._page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not value:
            raise ValueError("Title cannot be empty.")
        self._title = value

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
            return
        if value <= 0:
            raise ValueError("Page count must be a positive integer.")
        self._page_count = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
