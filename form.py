from marshmallow import Schema, fields


class FormSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str()
    exp_gre = fields.Int(required=True)
    exp_toefl = fields.Int(required=True)
    cgpa = fields.Float(required=True)
    uni_rate = fields.Int(required=True)
    research = fields.Bool(required=True)
