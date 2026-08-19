from config import db, bcrypt
from datetime import datetime
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
# No marshmallow extensions since schemas will be in a separate folder

class User(db.Model):
  __tablename__= "users"
  
  # Core Identity
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255), unique=True, nullable=False, index=True)
  username = db.Column(db.String(50), unique=True, nullable=False, index=True)
  full_name = db.Column(db.String(255), nullable=False)
  _password_hash = db.Column(db.String(255), nullable=False)
  
  # Profile Information
  date_of_birth = db.Column(db.Date, nullable=True)
  bio = db.Column(db.Text, nullable=True)
  profile_pic_url = db.Column(db.String(500), nullable=True)
  
  # Contact Info + Gamer IDs
  contact_number = db.Column(db.String(50), nullable=True)
  x_user = db.Column(db.String(255), nullable=True)
  discord_user = db.Column(db.String(255), nullable=True)
  twitch_tv_user = db.Column(db.String(255), nullable=True)
  xbox_user = db.Column(db.String(255), nullable=True)
  steam_user = db.Column(db.String(255), nullable=True)
  epic_games_user = db.Column(db.String(255), nullable=True)
  battle_net_user = db.Column(db.String(255), nullable=True)
  riot_games_user = db.Column(db.String(255), nullable=True)
  
  # Timestamps
  created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow, 
                         onupdate=datetime.utcnow, nullable=False)
  
  # --------------
  # Relationships
  # --------------
  
  # User → Roles (global RBAC). Many to Many 
  roles = db.relationship(
    'UserRole',
    back_populates='user',
    cascade='all, delete-orphan'
  )
  
  # User → Resource‑Scoped Permissions. Many to Many
  resource_permissions = db.relationship(
    'UserResourcePermission',
    back_populates='user',
    cascade='all, delete-orphan'
  )
  
  # User → Tournament Host. One to Many
  hosted_tournaments = db.relationship(
    'Tournament',
    back_populates='host',
    foreign_keys='Tournament.host_id'
  )
  
  # User → Tournament Attendees. Many to Many
  tournament_attendance = db.relationship(
    'TournamentAttendee',
    back_populates="user",
    cascade='all, delete-orphan'
  )
  
  # User → Standings (rankings). One to Many.
  standings = db.relationship(
    'Standings',
    back_populates='user',
    cascade="all, delete-orphan"
  )
  
  # Email validation
  @validates('email')
  def validate_email(self, key, address):
    if not isinstance (address, str):
      raise ValueError('Email must be a string')
    address = address.lower().strip()
    if not address:
      raise ValueError("Email cannot be empty")
    if '@' not in address:
      raise ValueError('Email must have @ in the address')
    return address
  
  # Password Hash Constraint
  @hybrid_property
  def password_hash(self):
    raise AttributeError('Password hashes may not be viewed')
  
  # Password Hash Setter
  @password_hash.setter
  def password_hash(self, password):
    if not isinstance(password, str) or len(password.strip()) < 8:
      raise ValueError("Password must be a string of at least 8 characters.")
    password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
    self._password_hash = password_hash.decode('utf-8')
  
  # Password Authenticator
  def authenticate(self, password):
    return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
  
  # --------------
  # Methods
  # --------------
  
  def has_role(self, slug: str) -> bool:
    """Check if user has a global role by slug."""
    return any(ur.role.slug == slug for ur in self.roles)
  
  def has_permission(self, permission_slug: str) -> bool:
    """Check global RBAC permission."""
    for ur in self.roles:
      for rp in ur.role.permissions:
        if rp.permission.slug == permission_slug:
          return True
    return False

  def has_resource_permission(self, permission_slug: str, resource_type: str, resource_id: int) -> bool:
    """Check scoped permission (tournament/event/match)."""
    for rp in self.resource_permissions:
      if (
        rp.permission.slug == permission_slug and
        rp.resource_type == resource_type and
        rp.resource_id == resource_id
      ):
        return True
    return False

  def __repr__(self):
    return f"<User id={self.id} username={self.username or 'N/A'}>"