from marshmallow import Schema, fields, validate

class StandingSchema(Schema):
  id = fields.Int(dump_only=True)
  
  player_id = fields.Int(required=True)
  points = fields.Int(required=True, validate=validate.Range(min=0))
  event_id = fields.Int(required=True)
  
  player = fields.Nested(
    'TournamentAttendeeSchema',
    only=('id', 'user'),
    dump_only=True
  )
  
  event = fields.Nested(
    'EventSchema',
    only=('id', 'name'),
    dump_only=True
  )