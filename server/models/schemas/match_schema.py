from marshmallow import Schema, fields, validate

class MatchSchema(Schema):
  id = fields.Int(dump_only=True)
  round = fields.Str(allow_none=True, validate=validate.Length(max=50))
  start_time = fields.DateTime(allow_none=True)
  status = fields.Str(
    required=True,
    validate=validate.OneOf(["pending", "in_progress", "completed", "cancelled"])
  )
  
  event_id = fields.Int(required=True)
  player_1_id = fields.Int(required=True)
  player_2_id = fields.Int(required=True)
  winner_id = fields.Int(allow_none=True)
  
  # Belongs to a single Event
  event = fields.Nested(
    'EventSchema',
    only=('id', 'name', 'game'),
    dump_only=True
  )
  
  # Player 1, 2 and winner are from TournamentAttendees
  player_1 = fields.Nested(
    'TournamentAttendeeSchema',
    only=('id', 'user'),
    dump_only=True
  )
  
  player_2 = fields.Nested(
    'TournamentAttendeeSchema',
    only=('id', 'user'),
    dump_only=True
  )
  
  winner = fields.Nested(
    'TournamentAttendeeSchema',
    only=('id', 'user'),
    dump_only=True
  )
  
  
# Note for future change. Consider adding Bracket to relate to Match
# For now, they both belong to a single event but are separate tables