from marshmallow import Schema, fields, validate

class EventSchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True, validate=validate.Length(min=1, max=255))
  start = fields.DateTime(required=True)
  registration_deadline = fields.DateTime(required=True)
  game = fields.Str(allow_none=True, validate=validate.Length(max=255))
  platform = fields.Str(allow_none=True, validate=validate.Length(max=255))
  line_up_type = fields.Str(required=True)
  
  tournament_id = fields.Int(required=True)
  
  # Belongs to a single Tournament
  tournament = fields.Nested(
    'TournamentSchema',
    only=('id', 'name', 'start'),
    dump_only=True
  )
  
  # Has Matches, Standings, and Brackets (Nested Relationships)
  matches = fields.List(
    fields.Nested(
      'MatchSchema',
      only=('id', 'player_1', 'player_2'),
      dump_only=True
    )
  )
  
  standings = fields.List(
    fields.Nested(
      'StandingSchema',
      only=('id', 'user', 'points'),
      dump_only=True
    )
  )
  
  brackets = fields.List(
    fields.Nested(
      'BracketSchema',
      only=('id', 'url'),
      dump_only=True
    )
  )
  
  