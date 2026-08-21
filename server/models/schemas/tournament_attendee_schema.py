from marshmallow import Schema, fields, validate

class TournamentAttendeeSchema(Schema):
  id = fields.Int(dump_only=True)
  
  # POST/PUT ready
  user_id = fields.Int(required=True)
  tournament_id = fields.Int(required=True)
  
  user = fields.Nested(
    'UserSchema',
    only=('id', 'username'),
    dump_only=True
  )
  
  tournament = fields.Nested(
    'TournamentSchema',
    only=('id', 'name'),
    dump_only=True
  )