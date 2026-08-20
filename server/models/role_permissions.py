from app import db
from sqlalchemy.orm import validates
from datetime import datetime

class RolePermission(db.Model):
  __tablename__ = "role_permissions"
  
  id = db.Column(db.Integer, primary_key=True)
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  
  # Foreign Keys to store Role and Permission
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
  permission_id = db.Column(db.Integer, db.ForeignKey('permissions.id'), nullable=False)
  
  # Relationship Mapping
  role = db.relationship(
    'Role',
    back_populates='permissions',
  )
  
  permission = db.relationship(
    'Permission',
    back_populates='role_permissions'
  )
  
  # Validation
  @validates('role_id', 'permission_id')
  def validates_ids(self, key, value):
    if not isinstance(value, int):
      raise ValueError(f"{key} must be an integer")
    return value  
  
  def __repr__(self):
    return f"<RolePermissions id={self.id} role_id={self.role_id} permission_id={self.permission_id}>"