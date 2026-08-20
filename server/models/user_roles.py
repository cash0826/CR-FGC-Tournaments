from app import db
from datetime import datetime
from sqlalchemy.orm import validates

class UserRole(db.Model):
  __tablename__ = "user_roles"
  
  id = db.Column(db.Integer, primary_key=True)
  
  # Foreign Keys
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
  
  # Audit trail
  assigned_by = db.Column(db.Integer, db.ForeignKey('users.id', nullable=True))
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  
  # Relationships
  user = db.relationship(
    'User', 
    back_populates='roles', 
    foreign_keys=[user_id]
  )
  
  role = db.relationship(
    'Role', 
    back_populates='user_roles'
  )
  
  assigned_by_user = db.relationship(
    'User', 
    foreign_keys=[assigned_by]
  )
  
  # Validation
  @validates('user_id', 'role_id')
  def validates_ids(self, key, value):
    if not isinstance(value, int):
      raise ValueError(f"{key} must be an integer")
    return value
  
  def __repr__(self):
    return f"<UserRoles id={self.id} user_id={self.user_id} role_id={self.role_id}"