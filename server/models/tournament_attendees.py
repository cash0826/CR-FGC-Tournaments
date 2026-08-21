from app import db
from sqlalchemy.orm import validates

class TournamentAttendee(db.Model):
  __tablename__ = 'tournament_attendees'
  
  id = db.Column(db.Integer, primary_key=True)
  
  # Foreign Keys to store User and Tournament
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'), nullable=False)
  
  # Relationship Mapping
  user = db.relationship(
    'User',
    back_populates='tournament_attendance'
  )
  
  tournament = db.relationship(
    'Tournament',
    back_populates='tournament_attendance'
  )
  
  @validates('user_id', 'tournament_id')
  def validate_ids(self, key, value):
    if not isinstance(value, int):
      raise ValueError(f"{key} must be an integer")
    return value
  
  def __repr__(self):
    return (
      f"<TournamentAttendee id={self.id} "
      f"user_id={self.user_id} "
      f"tournament_id={self.tournament_id}>"
    )