from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
        
    # query database, get all users
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users
    
    # save new user from form input
    @classmethod
    def save(cls,data) :
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        result = connectToMySQL('users_schema').query_db( query, data )
        
        return result
    
    #retreive single user
    @classmethod
    def get_one(cls,data):
        query = "SELECT * from users WHERE id = %(id)s;"
        result = connectToMySQL('users_schema').query_db( query , data)
        return cls(result[0])
    
    #update user info based on id
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)
    
    # delete user from database
    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM users where id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)