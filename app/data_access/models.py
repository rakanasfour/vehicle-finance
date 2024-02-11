from app.data_access.database import db

class Vehicle_Finance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    additionalservice = db.Column(db.String(50), nullable=False)
    addson = db.Column(db.String(200))
    price = db.Column(db.Integer, nullable=False)
    def serialize(self):
        return {
            'id': self.id,
            'additionalservice': self.additionalservice,
            'addson': self.addson,
            'price': self.price
        }
