from app import db
from sqlalchemy.orm import validates

class Permission(db.Model):
  __tablename__ = "permissions"
  
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(255), nullable=False)
  slug = db.Column(db.String(255), nullable=False, unique=True)
  category = db.Column(db.String(255))
  description = db.Column(db.Text)
  
  # Join-Table Relationships
  role_permissions = db.relationship(
    'RolePermission',
    back_populates="permission",
    cascade='all, delete-orphan'
  )
  
  user_resource_permissions = db.relationship(
    'UserResourcePermission',
    back_populates="permission",
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
    return f"<Permission id={self.id} slug={self.slug}>"