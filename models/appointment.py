# -*- coding: utf-8 -*-
from odoo import fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True,
        ondelete='cascade',
    )
    appointment_time = fields.Datetime(string='Appointment Time')
    booking_date = fields.Date(
        string='Booking Date',
        default=fields.Date.context_today,
    )
    priority = fields.Selection([
        ('0', 'Low'),
        ('1', 'Normal'),
        ('2', 'High'),
        ('3', 'Very High'),
    ], string='Priority', default='1')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In Consultation'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', default='draft', required=True)

    def action_test(self):
        return {
            "effect": {
                "fadeout": "slow",
                "message": 'Click Successfull by naem ullah',
                "type": "rainbow_man",
            }
        }