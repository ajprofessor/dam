# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Asignatura(models.Model):
    _name = 'dam.asignatura'
    _description = 'Asignaturas'
    _rec_name = 'nombre'

    nombre = fields.Char(required=True)
    codigo = fields.Char(string='Código', required=True)
    numAlumnos = fields.Integer(string="Nº alumnos", compute='_obtener_numAlumnos', store=True)
    fechaExamenOrdinaria = fields.Datetime(string='F. Examen Ordinaria')

    profesor = fields.Many2one('dam.profesor', ondelete='set null')
    alumnos = fields.Many2many('dam.alumno')

    @api.onchange('codigo')
    def _comprobar_codigo(self):
        for r in self:
            if len(r.codigo) != 6:
                return {
                    'warning': {
                        'title': "El código no parece válido",
                        'message': "Debería tener 6 caracteres"
                    }
                }

    @api.depends('alumnos')
    def _obtener_numAlumnos(self):
        for r in self:
            r.numAlumnos = len(r.alumnos)
