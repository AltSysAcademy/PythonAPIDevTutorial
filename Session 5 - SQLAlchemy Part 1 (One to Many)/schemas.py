from marshmallow import Schema, fields

# Rename to PlainItemSchema, and then remove the store_id
# ID change to integer
class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    
class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()

    # For idempotency (When we add new items)
    store_id = fields.Int()
#####
class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
