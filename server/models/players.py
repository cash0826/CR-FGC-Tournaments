from app import db
from sqlalchemy.orm import validates

class Player(db.Model):
  __tablename__ = "players"
  
  id = db.Column(db.Integer, primary_key=True)
  
  # Foreign Keys
  player_id = db.Column(db.Integer, db.ForeignKey('tournament_attendees.id'),nullable=False) 
  match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
  
  # Relationship
  match = db.relationship(
    'Match',
    back_populates='players'
  )
    
  attendee = db.relationship(
    'TournamentAttendee',
    foreign_keys=[player_id]
  )
  
  # Validation
  @validates('player_id', 'match_id')
  def validate_ids(self, key, value):
    if not isinstance(value, int):
      raise ValueError(f"{key} must be an integer")
    return value
  
  @validates('player_id')
  def validate_unique_player(self, key, value):
    # Prevent duplicate players in the same match
    if self.match is None:
      existing = {p.player_id for p in self.match.players if p.id != self.id}
      if value in existing:
        raise ValueError("Player already added to this match.")
    return value
  
  @validates('player_id')
  def validate_same_tournament(self, key, value):
    if self.match is None:
      return value
    event_tournament_id = self.match.event.tournament_id
    attendee_tournament_id = self.attendee.tournament_id
    if event_tournament_id != attendee_tournament_id:
      raise ValueError("Player must belong to the same tournament as the match.")
    return value
    
def __repr__(self):
    return f"<Player id={self.id} player_id={self.player_id} match_id={self.match_id}>"  

