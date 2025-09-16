from Book import Book
from Magazine import Magazine
from Library import Library

Dusty_philips = Book("OOPS in Python", "101", "Dusty")
Sport_Star = Magazine("SportStar", "201", "Sept_2025")


Mini_Library = Library("Mini_Library")

Mini_Library.add_item(Dusty_philips)
Mini_Library.add_item(Sport_Star)

Mini_Library.list_all_items()
