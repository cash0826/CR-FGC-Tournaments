from app import db
from sqlalchemy.orm import validates
from datetime import datetime

class Match(db.Model):
  __tablename__ = "matches"
  
  id = db.Column(db.Integer, primary_key=True)
  round = db.Column(db.String(50), nullable=True)
  start_time = db.Column(db.DateTime, nullable=True)
  status = db.Column(db.String(50), default='pending', nullable=False)
  # status allowed per validation: pending, in_progress, cancelled, completed
  
  # Foreign Keys
  event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
  player_1_id = db.Column(db.Integer, db.ForeignKey('tournament_attendees.id'), nullable=False)
  player_2_id = db.Column(db.Integer, db.ForeignKey('tournament_attendees.id'), nullable=False)
  winner_id = db.Column(db.Integer, db.ForeignKey('tournament_attendees.id'), nullable=True)
  
  # -------------
  # Relationships
  # -------------
  
  event = db.relationship(
    'Event',
    back_populates='matches'
  )

  player_1 = db.relationship(
    'TournamentAttendee',
    foreign_keys=[player_1_id]
  )
  
  player_2 = db.relationship(
    'TournamentAttendee',
    foreign_keys=[player_2_id]
  )

  winner = db.relationship(
    'TournamentAttendee',
    foreign_keys=[winner_id]
  )
  
  # Validation
  @validates('player_1_id', 'player_2_id', 'event_id')
  def validate_ids(self, key, value):
    if not isinstance(value, int):
      raise ValueError(f"{key} must be an integer")
    return value

  @validates('player_2_id')
  def validate_not_same_player(self, key, value):
    if value == self.player_1_id:
      raise ValueError("player_1 and player_2 cannot be the same attendee")
    return value

  @validates('status')
  def validate_status(self, key, value):
    allowed = {"pending", "in_progress", "completed", "cancelled"}
    if value not in allowed:
      raise ValueError(f"Invalid match status: {value}")
    return value

  def __repr__(self):
    return f"<Match id={self.id} event_id={self.event_id} status={self.status}>"