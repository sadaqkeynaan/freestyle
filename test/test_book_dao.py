import pytest
from book_dao import BookDAO
from book import Book





class Test_Book:          
    # def setup_method(self):
    #     self.book_dao = BookDAO(":memory:")
      
    #     self.book1 = Book(title= "Lost", description= "Beeing lost", author= "Robart")
    #     self.book2 = Book(title= "Found", description= "Beeing found", author= "Ali")
    #     self.book3 = Book(title= "lostandfound", description= "Beeing lostandfound", author= "robart och ali")
    #     self.book_dao.insert_book(self.book1)
    #     self.book_dao.insert_book(self.book2)
    #     self.book_dao.insert_book(self.book3)
        
    # def teardown_method(self):
    #     self.book_dao.close()
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        self.book_dao = BookDAO(":memory:")
        self.book1 = Book(title= "Lost", description= "Beeing lost", author= "Robart")
        self.book2 = Book(title= "Found", description= "Beeing found", author= "Ali")
        self.book3 = Book(title= "lostandfound", description= "Beeing lostandfound", author= "robart och ali")
        self.book_dao.insert_book(self.book1)
        self.book_dao.insert_book(self.book2)
        self.book_dao.insert_book(self.book3)
        yield
        self.book_dao.close()
        
        
    def test_allbook(self):
        self.book_dao.get_all_books()
        Books = self.book_dao.get_all_books()
        assert len(Books) == 3

    def test_add_book(self):
        self.book4 = Book(title= "galaxy", description= "Beeing galaxy fan", author= "sten")
        self.book_dao.insert_book(self.book4)
        Books = self.book_dao.get_all_books()
        assert len(Books) == 4
    
    def test_findtitle(self):
        finder = self.book_dao.find_by_title("Lost")
        assert finder.description == "Beeing lost"

    def test_update(self):
        finder = self.book_dao.find_by_title("Found")
        finder.description = ("Beeing lost")
        self.book_dao.update_book(finder)
        assert finder.description == "Beeing lost"
    
    def test_delete(self):
        finder = self.book_dao.find_by_title("lostandfound")
        self.book_dao.delete_book(finder)
        assert self.book_dao.find_by_title("lostandfound") == None



