from app import db
from sqlalchemy.orm import validates
from datetime import datetime

class UserResourcePermission(db.Model):
  __tablename__ = "user_resource_permissions"
  
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  
  # Foreign Keys to store User, Permission & Tournament
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), nullable=False)
  tournament_id = db.Column(db.Integer, db.ForeignKey('tournaments.id'))
  
  # Relationship Mapping
  user = db.relationship(
    'User',
    back_populates='resource_permissions'
  )
  # Matches parent model User. It defines resource_permission
  
  permission = db.relationship(
    'Permission',
    back_populates='user_resource_permissions'
  )
  
  tournament = db.relationship(
    'Tournament',
    back_populates='user_resource_permissions'
  )

  # Validation
  @validates('user_id', 'permission_id', 'tournament_id')
  def validates_ids(self, key, value):
    if value is None:
      return value
    if not isinstance(value, int):
      raise ValueError(f"{key} must be an integer")
    return value  
  
  def __repr__(self):
    return (
      f"<UserResourcePermission id={self.id} "
      f"user_id={self.user_id} "
      f"permission_id={self.permission_id} "
      f"tournament_id={self.tournament_id}>"
    )
  