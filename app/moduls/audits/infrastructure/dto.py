from app.config.db import db

Base = db.Model

list_estates_estate = db.Table(
    "list_estates_estates",
    db.Model.metadata,
    db.Column("id", db.String, db.ForeignKey("list_estates.id")),
    db.Column("estate_id", db.String, nullable=False),
    db.Column("code", db.String, nullable=False),
    db.Column("name", db.String, nullable=False),
    db.ForeignKeyConstraint(
        ["estate_id", "code", "name"],
        ["estate.estate_id", "estate.code", "estate.name"]
    )
)


class Estate(Base):
    __tablename__ = "estate"
    estate_id = db.Column(db.String, primary_key=True)
    code = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, primary_key=True)


class List_estates(Base):
    __tablename__ = "list_estates"
    id = db.Column(db.String, primary_key=True)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
    estates = db.relationship('Estate', secondary=list_estates_estate, backref='lists')


class Audit(Base):
    __tablename__ = "audits"
    id = db.Column(db.String, primary_key=True)
    # location_id = db.Column(db.Integer, db.ForeignKey("locations.id"), nullable=False)
    code = db.Column(db.String, nullable=False)
    score = db.Column(db.Float, nullable=False)
    approved_audit = db.Column(db.Boolean, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False)
    updatedAt = db.Column(db.DateTime, nullable=False)
#
#
# class Location(db.Model):
#     __tablename__ = "locations"
#     id = db.Column(db.String, primary_key=True)
#     currency = db.Column(db.String, nullable=False)
#     language = db.Column(db.String, nullable=False)
#     name = db.Column(db.String, nullable=False)
#     time_zone = db.Column(db.String, nullable=False)
#     createdAt = db.Column(db.DateTime, nullable=False)
#     updatedAt = db.Column(db.DateTime, nullable=False)
