from db import db
from sqlalchemy.orm import validates

class Bracket(db.Model):
  __tablename__ = 'brackets'
  
  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.Text, nullable=False)
  
  event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
  
  # Relationship
  event = db.relationship(
    'Event',
    back_populates='brackets'
  )
  
  @validates('event_id')
  def validate_int_fields(self, key, value):
    if not isinstance(value, int):
      raise ValueError(f"{key} must be an integer")
    return value
  
  def __repr__(self):
    return f"<Bracket id={self.id} url={self.url}>"
  
  # If you want brackets to group matchs
  # matches = db.relationship(
  #   'Match', 
  #   back_populates='bracket', 
  #   cascade='all, delete-orphan
  # )