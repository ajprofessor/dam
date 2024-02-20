# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Profesor(models.Model):
    _name = 'dam.profesor'
    _description = 'Profesores'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)

    asignaturas = fields.One2many('dam.asignatura', 'profesor')
