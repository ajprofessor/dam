# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Profesor(models.Model):
    _name = 'dam.profesor'
    _description = 'Profesores'
    _rec_name = 'nombreCompleto'

    nombre = fields.Char(required=True)
    apellidos = fields.Char()
    nombreCompleto = fields.Char(string="Nombre", compute='_obtener_nombreCompleto', store=False)
    dni = fields.Char(string='DNI', required=True)
    email = fields.Char(string='@')

    asignaturas = fields.One2many('dam.asignatura', 'profesor')
    tutorias = fields.One2many('dam.curso', 'tutor')

    @api.constrains('dni')
    def _comprobar_dni(self):
        for r in self:
            if len(r.dni) != 9:
                raise ValidationError("El DNI debe tener 9 caracteres.")

    @api.depends('nombre', 'apellidos')
    def _obtener_nombreCompleto(self):
        for r in self:
            r.nombreCompleto = r.nombre + ('' if r.apellidos is False else (' ' + r.apellidos))