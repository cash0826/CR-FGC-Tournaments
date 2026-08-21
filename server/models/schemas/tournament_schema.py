from marshmallow import Schema, fields

class TournamentSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  start = fields.DateTime(required=True)
  end = fields.DateTime(allow_none=True)
  in_person = fields.Boolean(allow_none=True)
  location = fields.Str(allow_none=True)
  description = fields.Str(allow_none=True)
  tie_breaking_rule = fields.Str(allow_none=True)
  created_at = fields.DateTime(dump_only=True)
  
  host_id = fields.Int(required=True)
  
  # Belong to a single, nested, Host object (read-only)
  host = fields.Nested(
    'UserSchema',
    only=('id', 'username'),
    dump_only=True
  )
  
  # Nested Relationships
  events = fields.List(
    fields.Nested(
      'EventSchema',
      only=('id', 'name', 'start_time'),
      dump_only=True
    )
  )
  
  tournament_attendance = fields.List(
    fields.Nested(
      'TournamentAttendeeSchema',
      only=('id', 'user'),
      dump_only=True
    )
  )
  
  user_resource_permissions = fields.List(
    fields.Nested(
      'UserResourcePermissionSchema',
      only=('id', 'user', 'permission'),
      dump_only=True
    )
  )
  
  