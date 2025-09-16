from LibraryItem import LibraryItem


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_details(self):
        print(
            f"The Magazine details are : Title : {self.title}, Item ID : {self.item_id}, Issue Number : {self.issue_number}")
