# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # call the connectToMySQL function with the target schema
        results = connectToMySQL('first_flask').query_db(query)
        # create empty list to append instance of friends
        friends = []
        # iterate over db results and create instances of friends with cls
        for friend in results:
            friends.append( cls(friend) )
        return friends
    
    @classmethod
    def save(cls,data) :
        query = "INSERT INTO users ( first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW() );"
        return connectToMySQL('first_flask').query_db( query, data )