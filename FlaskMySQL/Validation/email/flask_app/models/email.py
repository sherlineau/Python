from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    # save to database 
    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails(email) VALUES(%(email)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM emails WHERE email =%(email)s"
        results = connectToMySQL(DATABASE).query_db(query,data)
        return results
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        return results
    
    # validate email is in correct format
    @staticmethod
    def validate_email( data ):
        is_valid = True
        # test where field matches pattern
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!")
            is_valid = False
        return is_valid