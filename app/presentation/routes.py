from flask import Blueprint,jsonify, request
from app.service_layer.service import FinanceService


blueprint = Blueprint('routes', __name__)

@blueprint.route('/getAllFinances', methods=['GET'])
def get_all_vehicle_finances():
    vehicle_finances = FinanceService.get_all_vehicle_finances()

    return jsonify(vehicle_finances)

@blueprint.route('/getFinance/<int:id>', methods=['GET'])
def get_vehicle_finance(id):
    vehicle_finance = FinanceService.get_vehicle_finance(id)
    if vehicle_finance:
        serialized_vehicle_finance = vehicle_finance.serialize()

        return jsonify(serialized_vehicle_finance)
    else:
        return jsonify({'error': 'vehicle_finance not found'}), 404

@blueprint.route('/addFinance', methods=['POST'])
def add_vehicle_finance():
    data = request.json
    id = data.get('id')
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    addon = data.get('addon')
    price = data.get('price')

    if not id:
        return jsonify({'error': 'Name is required'}), 400

    vehicle_finance = FinanceService.add_vehicle_finance(id, brand, model, year, addon, price)
    return jsonify(vehicle_finance), 201



@blueprint.route('/updateFinance', methods=['PUT'])
def update_vehicle_finance():
    data = request.json
    id = data.get('id')
    brand = data.get('brand')
    model = data.get('model')
    year = data.get('year')
    addon = data.get('addon')
    price = data.get('price')

    if not id:
        return jsonify({'error': 'Name is required'}), 400

    vehicle_finance = FinanceService.update_vehicle_finance(id, brand, model, year, addon, price)
    return jsonify(vehicle_finance), 201



@blueprint.route('/deleteFinance/<int:id>', methods=['DELETE'])
def delete_vehicle_finance(id):
    deleted = FinanceService.delete_vehicle_finance(id)
    if deleted:
        return jsonify({'message': 'Vehicle deleted successfully'})
    else:
        return jsonify({'error': 'Vehicle not found'}), 404
