from marshmallow import Schema, fields

# These schemas are not used yet
# Only used for data validation and API Documentation
class ItemSchema(Schema):
    # Define fields(columns)
    # dump_only - They are not included when you send a POST req
    id = fields.Str(dump_only=True) # Would only show up when you GET it
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)

class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    # Optional
    name = fields.Str()
    price = fields.Float()
