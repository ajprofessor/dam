# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'dam.alumno'
    _description = 'Alumnos'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)
