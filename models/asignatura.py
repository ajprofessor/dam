# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Asignatura(models.Model):
    _name = 'dam.asignatura'
    _description = 'Asignaturas'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)
