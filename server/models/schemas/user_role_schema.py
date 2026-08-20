from marshmallow import Schema, fields, validate

class UserRoleSchema(Schema):
  id = fields.Int(dump_only=True)
  assigned_by = fields.Int(dump_only=True)
  created_at = fields.DateTime(dump_only=True)
  
  # Single-object relationships, not lists (belongs to)
  user = fields.Nested(
    'UserSchema', 
    only=('id', 'username'),
    dump_only=True
  )
  
  role = fields.Nested(
    'RoleSchema', 
    only=('id', 'slug', 'name'),
    dump_only=True
  )
  
  assigned_by_user = fields.Nested(
    'UserSchema',
    only=('id', 'username'),
    dump_only=True
  )
  