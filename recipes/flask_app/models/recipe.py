from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
#           c reate a recipe
    @classmethod
    def create(cLs,data):
        query = """
        INSERT INTO recipes (name, description, instructions, date, under_30, user_id) 
        VALUES (%(name)s, %(description)s, %(instructions)s, %(date)s, %(under_30)s, %(user_id)s);
        """
        return connectToMySQL(DATABASE).query_db(query,data)
        ## read all           
    @classmethod
    def get_all(cLs):
        query = """
        SELECT * FROM recipes
        JOIN users
        ON users.id = recipes.user_id;
        """
        results = connectToMySQL(DATABASE).query_db(query)
        print("RESULTS========>\n\n", results)
        all_recipes = []
        if results:
            for row in results:
            # create a recipe
                this_recipe = cLs(row)
            # create host of recipe
            # prepare the dict for user 
                user_data ={
                    **row,
                    'id' : row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['updated_at']
              }
                # make the user
                this_cook = user.User(user_data)
                # add new attribute
                this_recipe.cook = this_cook
                all_recipes.append(this_recipe)
        return all_recipes
    #   get by id
    @classmethod
    def get_by_id(cls,data):
        query = """
        SELECT * FROM recipes
        JOIN users
        ON users.id = recipes.user_id
        WHERE recipes.id = %(id)s ;
        """
        results = connectToMySQL(DATABASE).query_db(query,data)
        print("????????", results)
        if results:
            this_recipe = cls(results[0])
            row = results[0]
            user_data ={
                    **row,
                    'id' : row['users.id'],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['updated_at']
            }
            this_user = user.User(user_data)
            this_recipe.cook = this_user
            return this_recipe
        return False
    #      update method
    @classmethod
    def update(cLs,data):
        query = """
        UPDATE recipes
        SET 
        name = %(name)s,
        description = %(description)s,
        instructions = %(instructions)s,
        date = %(date)s,
        under_30 = %(under_30)s
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)
    ##       delete method
    @classmethod
    def delete(cLs,data):
        query = """
        DELETE FROM recipes
        WHERE id = %(id)s;
        """
        return connectToMySQL(DATABASE).query_db(query,data)


#    validator
    @staticmethod
    def vaildator(form_data):
        is_valid =  True
        if len(form_data['name']) < 1:
            is_valid = False
            flash("needs a name")
        if len(form_data['description']) < 1:
            is_valid = False
            flash("needs a description")
        if len(form_data['instructions']) < 1:
            is_valid = False
            flash("needs instructions")
        if len(form_data['date']) < 1:
            is_valid = False
            flash("when was it cooked?")
        if 'under_30' not in form_data:
            is_valid = False
            flash("is it under 30 mintues yes or no")
        return is_valid
