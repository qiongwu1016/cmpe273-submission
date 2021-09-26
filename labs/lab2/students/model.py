from marshmallow import Schema, fields

class StudentSchema(Schema):
    id = fields.Int()
    first_name = fields.Str(required=True)
    last_name = fields.Str(Required=True)
    sjsu_id = fields.Str(Required=True)
    email = fields.Str()
    create_timestamp = fields.DateTime(format='timestamp')
    update_timestamp = fields.DateTime(format='timestamp')


