from flask_app.models import author
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # add new book to database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO books(title,num_of_pages) VALUES (%(title)s,%(num_of_pages)s); "
        results = connectToMySQL( DATABASE ).query_db(query,data)
        return results
    
    @classmethod
    def save_fav (cls, data):
        query = "INSERT INTO favorites(user_id,book_id) VALUES (%(user_id)s, %(book_id)s); "
        result = connectToMySQL (DATABASE).query_db(query,data)
        return result
    
    #get all books from database
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL( DATABASE ).query_db(query)
        books = []
        for b in results:
            books.append (cls(b))
        return books
    
    # get one book from database
    @classmethod
    def get_one_book(cls,data):
        query = "SELECT * FROM books WHERE id = %(id)s;"
        results = connectToMySQL ( DATABASE ).query_db(query,data)
        return cls(results[0])
    
    # get books with users who favorited it
    @classmethod
    def get_book_with_users(cls,data):
        query = "SELECT * FROM books left join favorites on books.id = favorites.book_id left join users on users.id = favorites.user_id where books.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        
        if len(result) > 0:
            # current author is set to result of query
            current_book = cls(result[0])
            list_authors = []
            for row in result:
                current_author = {
                    'id':row['users.id'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'created_at':row['users.created_at'],
                    'updated_at':row['users.updated_at'],
                    'book_id':row['book_id']
                }
                a = author.Author( current_author )
                list_authors.append ( a )
            current_book.list_authors = list_authors
            return current_book
        

