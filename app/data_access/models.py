from app.data_access.database import db

class Vehicle_Finance(db.Model):
    __tablename__ = 'vehicle_finance_table'  # Specify the exact table name
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(200), nullable=False)
    model = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    addon = db.Column(db.String(200))
    price = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'addon': self.addon,
            'price': self.price

        }


