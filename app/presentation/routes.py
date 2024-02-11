from flask import jsonify, request
from app.service_layer.service import FinanceService
from app import app

@app.route('/getAllVehiclesFinance', methods=['GET'])
def get_all_vehicle_finances():
    vehicle_finances = FinanceService.get_all_vehicle_finance()
    return jsonify(vehicle_finances)

@app.route('/getAllVehiclesFinance/<int:id>', methods=['GET'])
def get_vehicle_finance(id):
    vehicle_finance = FinanceService.get_vehicle_finance(id)
    if vehicle_finance:
        return jsonify(vehicle_finance)
    else:
        return jsonify({'error': 'vehicle_finance not found'}), 404

@app.route('/addVehicleFinance', methods=['POST'])
def add_vehicle_finance():
    data = request.json
    id = data.get('id')
    additionalservice = data.get('additionalservice')
    addson = data.get('addson')
    price = data.get('price')


    if not id:
        return jsonify({'error': 'Name is required'}), 400

    vehicle_finance = FinanceService.add_product(id, additionalservice,addson,price)
    return jsonify(vehicle_finance), 201

@app.route('/deleteVehicleFinance/<int:id>', methods=['DELETE'])
def delete_vehicle_finance(id):
    deleted = FinanceService.delete_product(id)
    if deleted:
        return jsonify({'message': 'Product deleted successfully'})
    else:
        return jsonify({'error': 'Product not found'}), 404
