# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Alumno(models.Model):
    _name = 'dam.alumno'
    _description = 'Alumnos'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)
    apellidos = fields.Char()
    dni = fields.Char(string='DNI', required=True)
    nre = fields.Integer(string='NRE', help='Nº regional de expediente', required=True)
    expediente = fields.Integer(string='EXP', required=True)
    fechaNacimiento = fields.Date(string='F. Nacimiento', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='@')

    asignaturas = fields.Many2many('dam.asignatura')

    @api.constrains('dni')
    def _comprobar_dni(self):
        for r in self:
            if len(r.dni) != 9:
                raise ValidationError("El DNI debe tener 9 caracteres.")

    @api.constrains('nre')
    def _comprobar_nre(self):
        for r in self:
            if r.nre < 1 or r.nre > 10000000:
                raise ValidationError("El NRE debe ser mayor que 0 y menor que 10000000.")

    @api.constrains('expediente')
    def _comprobar_expediente(self):
        for r in self:
            if r.expediente < 1 or r.expediente > 10000:
                raise ValidationError("El número de expediente debe ser mayor que 0 y menor que 10000.")