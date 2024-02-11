from app.data_access.database import db
from app.data_access.models import Vehicle_Finance


class FinanceService:

    @staticmethod
    def get_all_vehicle_finances():
        return [vehicle_finance.serialize() for vehicle_finance in Vehicle_Finance.query.all()]

    @staticmethod
    def get_vehicle_finance(id):
        return Vehicle_Finance.query.filter_by(id=id).first()

    @staticmethod
    def add_vehicle_finance(id, additionalservice,addson,price):
        new_vehicle = Vehicle_Finance(id=id, additionalservice=additionalservice,addson=addson,price=price)
        db.session.add(new_vehicle)
        db.session.commit()
        return new_vehicle.serialize()

    @staticmethod
    def update_vehicle_finance(id, additionalservice,addson,price):
        vehicle_finance = Vehicle_Finance.query.get(id)
        if vehicle_finance:
            vehicle_finance.id = id
            vehicle_finance.additionalservice = additionalservice
            vehicle_finance.addson = addson
            vehicle_finance.price = price
            db.session.commit()
            return vehicle_finance.serialize()
        else:
            return None

    @staticmethod
    def delete_vehicle_finance(id):
        vehicle_finance = Vehicle_Finance.query.get(id)
        if vehicle_finance:
            db.session.delete(vehicle_finance)
            db.session.commit()
            return True
        else:
            return False

