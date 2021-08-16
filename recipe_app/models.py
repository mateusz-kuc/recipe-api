from recipe_app import db

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    kcal = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(50), nullable=False)
    sugar = db.Column(db.Float, nullable=False)
    unsaturated_fat = db.Column(db.Float, nullable=False)
    saturated_fat = db.Column(db.Float, nullable=False)
    ingredients = db.relationship('Ingredients', backref='ingredient_product', lazy=True)

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    recipe_description = db.Column(db.Text, nullable = False)
    instructions = db.Column(db.Text, nullable = False)
    is_vegan = db.Column(db.Boolean, nullable = False)
    is_vegetarian = db.Column(db.Boolean, nullable=False)
    is_gluten_free= db.Column(db.Boolean, nullable=False)
    is_lactose_free = db.Column(db.Boolean, nullable=False)
    ingredients = db.relationship('Ingredients', backref='ingredient_recipe', lazy=True)


class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer, nullable = False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
