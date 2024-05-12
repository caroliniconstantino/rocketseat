from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint('calc_routes', __name__)

estoque = []

@calc_route_bp.route('/calculator/1', methods=['POST'])
def calculator_1():
    calc = Calculator1()
    response = calc.calculate(request)
    
    return jsonify(response), 200

@calc_route_bp.route('/list', methods=['GET'])
def list_products():
    return jsonify(estoque), 200

@calc_route_bp.route('/update', methods=['PUT'])
def update_product():
    product = request.get_json()
    name = product['name']
    for i in range(len(estoque)):
        if estoque[i]['name'] == name:
            estoque[i] = product
            return jsonify({'Produto atualizado': product}), 200

@calc_route_bp.route('/remove', methods=['DELETE'])
def remove_product():
    product = request.get_json()
    name = product['produto']
    product_to_remove = None
    for produto in estoque:
        if produto["produto"] == name:
            product_to_remove = produto
            break
    
    if product_to_remove:
        estoque.remove(product_to_remove)
        return jsonify({'Produto removido': product_to_remove}), 200
    else:
        return jsonify({'Produto não encontrado': name}), 404