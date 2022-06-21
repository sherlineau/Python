from flask_app.models import book
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # add new user to database 
    @classmethod
    def save (cls, data):
        query = "INSERT INTO users(first_name,last_name) VALUES (%(first_name)s, %(last_name)s);"
        result = connectToMySQL( DATABASE ).query_db(query,data)
        return result
    
    @classmethod
    def save_fav (cls, data):
        query = "INSERT INTO favorites(user_id,book_id) VALUES (%(user_id)s, %(book_id)s); "
        result = connectToMySQL (DATABASE).query_db(query,data)
        return result
        
    #get all users from database
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL( DATABASE ).query_db(query)
        authors = []
        for a in result:
            authors.append ( cls(a) )
        return authors
    
    #get one user from database
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL( DATABASE ).query_db(query,data)
        return cls(result[0])
    
    # get one user with books
    @classmethod
    def get_one_with_books(cls,data):
        query =" SELECT * FROM users LEFT JOIN favorites ON users.id = favorites.user_id LEFT JOIN books on books.id = favorites.book_id where users.id = %(id)s;"
        
        result = connectToMySQL(DATABASE).query_db(query,data)
        print(result)
        # validate if query returns anything
        if len(result) > 0:
            # current author is set to result of query
            current_author = cls(result[0])
            list_books = []
            for row in result:
                current_book = {
                    'id':row['books.id'],
                    'title':row['title'],
                    'num_of_pages':row['num_of_pages'],
                    'created_at':row['books.created_at'],
                    'updated_at':row['books.updated_at'],
                    'user_id':row['user_id']
                }
                b = book.Book( current_book )
                list_books.append ( b )
            current_author.list_books = list_books
            return current_author
