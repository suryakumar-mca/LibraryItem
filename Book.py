from LibraryItem import LibraryItem


class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_details(self):
        print(
            f"The Book details are : Title : {self.title}, Item ID : {self.item_id}, Author : {self.author}")
