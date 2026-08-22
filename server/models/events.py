from app import db
from sqlalchemy.orm import validates
from datetime import datetime

class Event(db.Model):
  __tablename__ = 'events'
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  start = db.Column(db.DateTime, nullable=False)
  registration_deadline = db.Column(db.DateTime, nullable=False)
  game = db.Column(db.String(255), nullable=True)
  platform = db.Column(db.String(255), nullable=True)
  line_up_type = db.Column(db.String(255), nullable=False)
  
  # Foreign Key to store Tournament
  tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'), nullable=False)
  
  # Belongs to tournament
  tournament = db.relationship(
    'Tournament',
    back_populates='events'
  )
  
  # Has Matches, Standings, and Brackets
  matches = db.relationship(
    'Match',
    back_populates='event',
    cascade='all, delete-orphan'
  )
  
  standings = db.relationship(
    'Standing',
    back_populates='event',
    cascade='all, delete-orphan'
  )
  
  brackets = db.relationship(
    'Bracket',
    back_populates='event',
    cascade='all, delete-orphan'
  )
  
  @validates('tournament_id')
  def validate_tournament_id(self, key, value):
    if not isinstance(value, int):
      raise ValueError("tournament_id must be an integer")
    return value

  @validates('name')
  def validate_name(self, key, value):
    if not value or not isinstance(value, str):
      raise ValueError("Event name must be a non-empty string")
    return value.strip()
  
  @validates('line_up_type')
  def validate_line_up_type(self, key, value):
    if not value or not isinstance(value, str):
      raise ValueError("line_up_type must be a non-empty string")
    return value.strip()

  def __repr__(self):
    return f"<Event id={self.id} name={self.name}>"