from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger
from flask import flash

class Restaurant: 
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.burgers = []
        
    @classmethod
    def save( cls, data ):
        query = "INSERT INTO restaurants (name, created_at, updated_at) VALUES ( %(name)s, NOW(), NOW());"
        return connectToMySQL('burgers').query_db( query, data )
    
    @classmethod
    def get_restaurant_with_burgers ( cls , data ):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON burgers.restaurant_id = restaurant_id WHERE restaurant_id = %(id)s;"
        results = connectToMySQL('burgers').query_db(query,data)
        # results = list of toppings with burger attached to each
        restaurant = cls (results[0])
        for row_from_db in results:
            # parse burger data to make instanes of burgers and add them to our list
            burger_data = {
                "id": row_from_db["burger.id"],
                "name": row_from_db["burger.name"],
                "bun": row_from_db["bun"],
                "meat": row_from_db["meat"],
                "calories": row_from_db["calories"],
                "created_at": row_from_db["burger.created_at"],
                "updated_at": row_from_db["burger.updated_at"]
            }
            restaurant.burgers.append( burger.Burger (burger_data))
        return restaurant
    