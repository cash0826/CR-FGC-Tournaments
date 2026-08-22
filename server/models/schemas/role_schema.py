from marshmallow import Schema, fields, validate

class RoleSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(validate=validate.Length(min=1, max=255))
  description = fields.Str(allow_none=True)
  is_system_role = fields.Boolean(dump_only=True)
  
  # Nested Relationships
  user_roles = fields.List(
    fields.Nested(
      'UserRoleSchema',
      only=("id", "user"),
      dump_only=True
    )
  )
  
  permissions = fields.List(
    fields.Nested(
      'RolePermissionSchema', 
      only=('id', "permission"),
      dump_only=True
    )
  )