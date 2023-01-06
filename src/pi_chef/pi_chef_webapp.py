from flask import Flask, render_template, jsonify, request
import pandas as pd
import sqlite3
import data_controller as dc

app = Flask(__name__)

@app.route('/')
def pi_chef():
    return render_template('base.html', recipes=dc.get_all_recipes())

@app.route('/recipe', methods=['GET'])
def recipe():
    if request.method == 'GET':
        args = request.args
        recipe_id = args.get('recipe_id')
        recipe = dc.get_recipe(recipe_id)
    return jsonify(recipe)

@app.route('/all_recipes', methods=['GET'])
def all_recipes():
    if request.method == 'GET':
        recipes = dc.get_all_recipes()
    return jsonify(recipes)