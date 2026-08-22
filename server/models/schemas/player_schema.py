from marshmallow import Schema, fields, validate

class PlayerSchema(Schema):
  id = fields.Int(dump_only=True)
  
  player_id = fields.Int(required=True, dump_only=True)
  match_id = fields.Int(required=True)
  
  match = fields.Nested(
    'MatchSchema',
    only=('id',),
    dump_only=True
  )
  
  attendee = fields.Nested(
    'TournamentAttendeeSchema',
    only=('id', 'user'),
    dump_only=True
  )