# src/schemas/usuario_schema.py

from marshmallow import Schema, fields, validate, validates, ValidationError

class UsuarioRegistroSchema(Schema):
    nombre_usuario = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    correo = fields.Email(required=True)
    contrasena = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))

class UsuarioLoginSchema(Schema):
    correo = fields.Email(required=True)
    contrasena = fields.Str(required=True, load_only=True)

class UsuarioRespuestaSchema(Schema):
    id = fields.Int()
    nombre_usuario = fields.Str()
    correo = fields.Email()
    capital_inicial = fields.Float()
    capital_actual = fields.Float()
    moneda = fields.Str()
    creado_en = fields.DateTime()
