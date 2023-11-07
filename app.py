# Create a recipes model

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db' #SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Disable tracking modifications for better performance

db = SQLAlchemy(app)

# Define the Recipe model
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# API Routes

# Read all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    recipe_list = [{"id": recipe.id, "name": recipe.name, "ingredients": recipe.ingredients, "instructions": recipe.instructions} for recipe in recipes]
    return jsonify(recipe_list)

# Setting our port
if __name__ == '__main__':
    app.run(debug=True, port=4000) # set the port to 4000