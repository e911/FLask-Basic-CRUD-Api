from flask_io import fields, Schema, post_dump
from .models import User


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    enabled = fields.Boolean(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    created_at = fields.DateTime(dump_only=True)

    @post_dump
    def make_object(self, data):
        return User(**data)
