"""Example calculations route for flask"""
from flask import Blueprint

CALC_ENDPOINTS = Blueprint('calculations', __name__)

@CALC_ENDPOINTS.route('/calculations/add/<first>/<second>')
def add(first, second):
    """Example endpoint to add 2 numbers"""
    return str(int(first) + int(second))
