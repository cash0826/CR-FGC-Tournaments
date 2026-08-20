from marshmallow import Schema, fields

class RolePermissionSchema(Schema):
  id = fields.Int(dump_only=True)
  created_at = fields.DateTime(dump_only=True)

  # Belong to single object (read-only)
  role = fields.Nested(
    'RoleSchema', 
    only=('id', 'name', 'slug'), 
    dump_only=True
  )
  
  permission = fields.Nested(
    'PermissionSchema',
    only=('id', 'name', 'slug', 'category'),
    dump_only=True
  )
  
  