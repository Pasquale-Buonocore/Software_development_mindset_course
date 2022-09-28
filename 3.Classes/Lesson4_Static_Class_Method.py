'''
Python classes have different ways to define method:

1. standard method
    when invoked on an object they bind to the instance of the class which called it.

2. class methods 
    Class methods work the same way as regular methods, except that when invoked on an object they bind to the class of the object 
    instead of to the object.

3. static methods 
    They are even simpler: they don't bind anything at all, and simply return the underlying function without any transformations.

'''

class Book():
    def __init__(self, book_name: str, book_total_page: int) -> None:
        self.Name = book_name
        self.TotalPage = book_total_page

    def compute_missing_page(self, page_read: int) -> None:
        print(f"You need to read other {self.TotalPage - page_read} pages to complete the book")

    @classmethod
    def InitializeHarryPotterBook(cls):
        return cls(book_name = 'Harry Potter', book_total_page = 752)
    
    @staticmethod
    def compute_needed_reading_day_to_conclude_book(missing_pages: int, pages_read_per_day: int) -> float:
        return missing_pages/pages_read_per_day

if __name__ == '__main__':
    # Define House of Dragon Book
    Book1 = Book('House Of Dragon', 653)
    Book2 = Book.InitializeHarryPotterBook()

    print(f"The {Book1.Name} is {Book1.TotalPage} page long") 
    print(f"The {Book2.Name} is {Book2.TotalPage} page long") # Use classmethod to store a object initialization


    print(f"I would need other {Book.compute_needed_reading_day_to_conclude_book(50,5)} days of reading to complete the book")