from app import db
from sqlalchemy.orm import validates

class Role(db.Model):
  __tablename__ = "roles"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  slug = db.Column(db.String(255), nullable=False, unique=True)
  description = db.Column(db.Text)
  is_system_role = db.Column(db.Boolean, nullable=False, default=False)
  
  # Relationships
  user_roles = db.relationship(
    'UserRole',
    back_populates='role',
    cascade='all, delete-orphan'
  )
  
  permissions = db.relationship(
    'RolePermission',
    back_populates='role',
    cascade='all, delete-orphan'
  )
  
  # Slug Validation
  @validates('slug')
  def validate_slug(self, key, value):
    if not isinstance(value, str):
      raise ValueError("Slug must be a string")
    value = value.strip().lower()
    if " " in value:
      raise ValueError("Slug cannot contain spaces")
    return value
  
  def __repr__(self):
    return f"<Role id={self.id} slug={self.slug}"