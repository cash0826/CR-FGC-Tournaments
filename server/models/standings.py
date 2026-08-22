from app import db
from sqlalchemy.orm import validates

class Standing(db.Model):
  __tablename__ = 'standings'
  
  id = db.Column(db.Integer, primary_key=True)
  
  # Statistics
  # Includes player and event relationships
  player_id = db.Column(db.Integer, db.ForeignKey('tournament_attendees.id'), nullable=False)
  points = db.Column(db.Integer, nullable=False)
  event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
  
  #  Relationships
  player = db.relationship(
    'TournamentAttendee',
    foreign_keys=[player_id]
  )
  
  event = db.relationship(
    'Event',
    back_populates='standings'
  )
  
  @validates('player_id', 'event_id', 'points')
  def validate_int_fields(self, key, value):
    if not isinstance(value, int):
      raise ValueError(f"{key} must be an integer")
    if key == "points" and value < 0:
      raise ValueError("points cannot be negative")
    return value
      
  def __repr__(self):
    return f"<Standing player={self.player_id} points={self.points}>"