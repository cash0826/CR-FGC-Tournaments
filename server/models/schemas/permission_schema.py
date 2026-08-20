from marshmallow import Schema, fields, validate

class PermissionSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(validate=validate.Length(min=1, max=255))
  slug = fields.Str(validate=validate.Length(min=1, max=255))
  category = fields.Str(allow_none=True)
  description = fields.Str(allow_none=True)
  
  # Nested Relationships (Lists)
  role_permissions = fields.List(
    fields.Nested(
      'RolePermissionSchema', 
      only=("id", "role_id"), 
      dump_only=True
    )
  )
  
  user_resource_permissions = fields.List(
    fields.Nested(
      'UserResourcePermissionSchema', 
      only=('id', 'user_id', 'resource_type', 'resource_id'), 
      dump_only=True
    )
  )
  
  