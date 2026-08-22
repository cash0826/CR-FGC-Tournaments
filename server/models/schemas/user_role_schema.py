from marshmallow import Schema, fields, validate

class UserRoleSchema(Schema):
  id = fields.Int(dump_only=True)
  
  # POST/PUT
  user_id = fields.Int(required=True)
  role_id = fields.Int(required=True)
  
  # Single-object relationships (belongs to)
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
  