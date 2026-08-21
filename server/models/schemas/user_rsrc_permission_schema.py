from marshmallow import Schema, fields

class UserResourcePermissionSchema(Schema):
  id = fields.Int(dump_only=True)
  created_at = fields.DateTime(dump_only=True)
  
  # POST/PUT ready
  user_id = fields.Int(required=True)
  permission_id = fields.Int(required=True)
  tournament_id = fields.Int(allow_none=True)
  
  # Belong to a single object (read-only)
  user = fields.Nested(
    'UserSchema',
    only=('id', 'username'),
    dump_only=True
  )
  
  permission = fields.Nested(
    'PermissionSchema',
    only=('id', 'slug'),
    dump_only=True
  )
  
  tournament = fields.Nested(
    'TournamentSchema',
    only=('id', 'name'),
    dump_only=True
  )
  