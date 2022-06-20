from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    #add new dojo
    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return result
    
    # get all dojos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        dojos = []
        for d in results:
            dojos.append( cls(d) )
        return dojos
    
    # get one dojo
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)
        return(cls(result[0]))
    
    # get all ninjas from dojo
    @classmethod
    def get_one_with_ninjas (cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;" 
        
        results = connectToMySQL('dojos_and_ninjas').query_db(query,data)

        # validate if query has ninjas
        if len(results) > 0:
            current_dojo = cls(results[0])
            list_ninjas = []
            for row in results:
                current_ninja = {
                    'id' : row['ninjas.id'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'age':row['age'],
                    'created_at':row['ninjas.created_at'],
                    'updated_at':row['ninjas.updated_at'],
                    'dojo_id':row['dojo_id']
                }
                ninja = Ninja(current_ninja)
                list_ninjas.append( ninja )
            current_dojo.list_ninjas = list_ninjas
            return current_dojo