import sqlite3
import pandas as pd

def get_all_recipes():
    con = sqlite3.connect("data/recipes.db")
    cur = con.cursor()
    df = pd.read_sql_query("SELECT id, name, description, image FROM RECIPE", con)
    recipes = df.to_dict('records')
    return recipes


def get_filtered_recipes(filters):
    con = sqlite3.connect("data/recipes.db")
    cur = con.cursor()
    df = pd.read_sql_query("SELECT id, name, description, image FROM RECIPE", con)
    recipes = df.to_dict('records')
    return recipes


def get_recipe(id):
    con = sqlite3.connect("data/recipes.db")
    cur = con.cursor()
    df = pd.read_sql_query(f"SELECT * FROM RECIPE WHERE id = {id}", con)
    recipe = df.to_dict('records')
    return recipe
