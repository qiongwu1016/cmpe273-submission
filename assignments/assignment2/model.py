from datetime import date
from pprint import pprint
import json
from marshmallow import Schema, fields

class DeepLinkSchema(Schema):
    guid = fields.Str()
    bitlink = fields.Str()
    app_uri_path = fields.Str()
    install_url = fields.Str()
    app_guid = fields.Str()
    os = fields.Str()
    install_type = fields.Str()
    created = fields.Str()
    modified = fields.Str()
    brand_guid = fields.Str()

class BitLinkSchema(Schema):
    references = fields.Str()
    link = fields.Str(required=True)
    id = fields.Str()
    long_url = fields.Str(required=True)
    title = fields.Str()
    archived = fields.Bool()
    created_at = fields.Str()
    created_by = fields.Str()
    client_id = fields.Str()
    custom_bitlinks = fields.List(fields.Str())
    tags = fields.List(fields.Str())
    launchpad_ids = fields.List(fields.Str())
    deeplinks = fields.Nested(DeepLinkSchema())





