from datetime import datetime
from app.config.db import db

Base = db.Model


class Location(Base):
    __tablename__ = "locations"
    id = db.Column(db.String, primary_key=True, index=True)
    currency = db.Column(db.String)
    language = db.Column(db.String)
    name = db.Column(db.String)
    time_zone = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Audit(Base):
    __tablename__ = "audits"
    id = db.Column(db.String, primary_key=True, index=True)
    location_id = db.Column(db.String, db.ForeignKey("locations.id"))
    code = db.Column(db.String)
    score = db.Column(db.Float)
    approved_audit = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
