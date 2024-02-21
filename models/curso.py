# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Curso(models.Model):
    _name = 'dam.curso'
    _description = 'Cursos'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)

    delegado = fields.Many2one('dam.alumno', ondelete='set null')
    tutor = fields.Many2one('dam.profesor', ondelete='set null')
    asignaturas = fields.One2many('dam.asignatura', 'curso')
