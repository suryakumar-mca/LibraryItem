class Library:
    def __init__(self, name):
        self.name = name
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def list_all_items(self):
        for item in self.__items:
            item.display_details()


'''

Saturday_items = []
Saturday_items.append(Dusty_philips)
Saturday_items.append(Sport_Star)
'''
