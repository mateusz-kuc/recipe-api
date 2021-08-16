from flask import Flask,  request, jsonify
import requests
from recipe_app.models import Products, Recipes, Ingredients

from recipe_app import app, db


@app.route('/get_products', methods=['GET'])
def get_products():
    products = Products.query.all()
    output = []

    for product in products:
        element_data = {}
        element_data['id'] = product.id
        element_data['name'] = product.name
        element_data['kcal'] = product.kcal
        element_data['unit'] = product.unit
        element_data['sugar'] = product.sugar
        element_data['saturated_fat'] = product.saturated_fat
        element_data['unsaturated_fat'] = product.unsaturated_fat
        output.append(element_data)

    return jsonify({'products': output})

@app.route('/get_product/<string:product>', methods=['GET'])
def get_product(product):
    result = Products.query.filter_by(name=product).first()
    if not result:
        return jsonify({'message' : 'No product found!'})
    element_data = {}
    element_data['id'] = result.id
    element_data['name'] = result.name
    element_data['kcal'] = result.kcal
    element_data['unit'] = result.unit
    element_data['sugar'] = result.sugar
    element_data['saturated_fat'] = result.saturated_fat
    element_data['unsaturated_fat'] = result.unsaturated_fat

    return jsonify({'product': element_data})

@app.route('/add_product', methods=['POST'])
def add_product():

    data = request.get_json()
    data = data["product"]
    try:
        add_product = Products(name=data['name'], kcal = data['kcal'],unit = data['unit'],sugar = data['sugar'],saturated_fat = data['saturated_fat'],unsaturated_fat = data['unsaturated_fat'])
        db.session.add(add_product)
        db.session.commit()

        return jsonify({'message' : 'New product created!'})
    except:
        return jsonify({'message': "New product haven't been created. Something went wrong "})

@app.route('/delete_product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Products.query.filter_by(id=id).first()

    if not product:
        return jsonify({'message': 'No product found!'})

    db.session.delete(product)
    db.session.commit()

    return jsonify({'message': 'The product has been deleted!'})
# !!!!!!
#brak obsługi błędów
@app.route('/update_product/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    data = data["product"]
    product = Products.query.filter_by(id=id).first()
    if data["name"]!="":
        product.name = data["name"]
    if data["kcal"] != "":
        product.kcal = data["kcal"]
    if data["unit"]!="":
        product.unit = data["unit"]
    if data["sugar"]!="":
        product.sugar = data["sugar"]
    if data["unsaturated_fat"]!="":
        product.unsaturated_fat = data["unsaturated_fat"]
    if data["saturated_fat"]!="":
        product.saturated_fat = data["saturated_fat"]

    db.session.commit()
    return jsonify({'message': 'The product has been updated!'})


# Recipes
def get_recipe(result):
    element_data = {}
    element_data['id'] = result.id
    element_data['name'] = result.name
    element_data['recipe_description'] = result.recipe_description
    element_data['instructions'] = result.instructions
    element_data['is_vegan'] = result.is_vegan
    element_data['is_vegetarian'] = result.is_vegetarian
    element_data['is_gluten_free'] = result.is_gluten_free
    element_data['is_lactose_free'] = result.is_lactose_free
    return element_data
@app.route('/get_recipe_by_name/<string:recipe>', methods=['GET'])
def get_recipe_by_name(recipe):
    result = Recipes.query.filter_by(name=recipe).first()
    if not result:
        return jsonify({'message' : 'No recipe found!'})

    recipe = get_recipe(result)
    return jsonify({'recipe': recipe})

@app.route('/get_recipe_by_id/<string:id>', methods=['GET'])
def get_recipe_by_id(id):
    result = Recipes.query.filter_by(id=id).first()
    if not result:
        return jsonify({'message' : 'No recipe found!'})

    recipe = get_recipe(result)
    return jsonify({'recipe': recipe})

@app.route('/add_recipe', methods=['POST'])
def add_recipe():

    data = request.get_json()
    data = data["recipe"]
    try:
        add_recipe = Recipes(name=data['name'], recipe_description = data['recipe_description'],instructions = data['instructions'],is_vegan = data['is_vegan'],is_vegetarian = data['is_vegetarian'],is_gluten_free = data['is_gluten_free'],is_lactose_free = data['is_lactose_free'])
        db.session.add(add_recipe)
        db.session.commit()
        return jsonify({'message': 'New recipe created!'})
    except:
        return jsonify({'message': "New recipe haven't been created! Something went wrong"})

@app.route('/delete_recipe/<int:id>', methods=['DELETE'])
def delete_recipe(id):
    recipe = Recipes.query.filter_by(id=id).first()

    if not recipe:
        return jsonify({'message': 'No recipe found!'})

    db.session.delete(recipe)
    db.session.commit()

    return jsonify({'message': 'The recipe has been deleted!'})


@app.route('/update_recipe/<int:id>', methods=['PUT'])
def update_recipe(id):
    data = request.get_json()
    data = data["recipe"]
    recipe = Recipes.query.filter_by(id=id).first()
    if data["name"]!="":
        recipe.name = data["name"]
    if data["recipe_description"] != "":
        recipe.recipe_description = data["recipe_description"]
    if data["instructions"]!="":
        recipe.instructions = data["instructions"]
    if data["is_vegan"]!="":
        recipe.is_vegan = data["is_vegan"]
    if data["is_vegetarian"]!="":
        recipe.is_vegetarian = data["is_vegetarian"]
    if data["is_gluten_free"]!="":
        recipe.is_gluten_free = data["is_gluten_free"]
    if data["is_lactose_free"]!="":
        recipe.is_lactose_free = data["is_lactose_free"]

    db.session.commit()
    return jsonify({'message': 'The recipe has been updated!'})


# Ingredients
@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():

    data = request.get_json()
    data = data["ingredient"]
    try:
        add_ingredient = Ingredients(quantity= data["quantity"],recipe_id= data["recipe_id"],product_id=data["product_id"])
        db.session.add(add_ingredient)
        db.session.commit()

        return jsonify({'message' : 'New ingredient was added to recipe !'})
    except:
        return jsonify({'message': "New ingredient haven't been add to recipe. Something went wrong "})


@app.route('/delete_ingredient/<int:id>', methods=['DELETE'])
def delete_ingredient(id):
    ingredient = Ingredients.query.filter_by(id=id).first()

    if not ingredient:
        return jsonify({'message': 'No ingredient found!'})

    db.session.delete(ingredient)
    db.session.commit()

    return jsonify({'message': 'The ingredient has been deleted!'})

@app.route('/update_ingredient/<int:id>', methods=['PUT'])
def update_ingredient(id):
    data = request.get_json()
    data = data["ingredient"]
    ingredient = Ingredients.query.filter_by(id=id).first()
    if data["quantity"]!="":
        ingredient.quantity = data["quantity"]
    db.session.commit()
    return jsonify({'message': 'The ingredient has been updated!'})

