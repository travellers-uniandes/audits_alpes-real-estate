from app.config.db import db

Base = db.Model


class Location(Base):
    __tablename__ = "locations"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    currency = db.Column(db.String, nullable=False)
    language = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    time_zone = db.Column(db.String, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)


class Audit(Base):
    __tablename__ = "audits"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    code = db.Column(db.String, nullable=False)
    score = db.Column(db.Float, nullable=False)
    approved_audit = db.Column(db.Boolean, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
