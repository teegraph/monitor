from app import db
from datetime import datetime


class HistoryCPU(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    utilize = db.Column(db.Float)
