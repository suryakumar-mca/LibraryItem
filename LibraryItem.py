from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    @abstractmethod
    def display_details(self):
        pass

    @staticmethod
    def is_valid_id(item_id):
        return item_id.isdigit()
