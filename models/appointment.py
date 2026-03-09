# -*- coding: utf-8 -*-
from odoo import fields, models


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Inherit to get activity features
    _description = 'Hospital Appointment'

  #patient id is many to 1 so we use Many2one avatar user here.
    patient_id = fields.Many2one(
        'hospital.patient',
        string='Patient',
        required=True,
        ondelete='cascade',
    )

    doctor_id = fields.Many2one('res.users', String='Doctor')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.lines', 'appointment_id', string='Pharmacy Lines')

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

    prescription = fields.Html(string="Prescription")

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


class AppointmentPharmacyLines(models.Model):
    _name = 'appointment.pharmacy.lines'
    _description = 'Appointment Pharmacy Lines'

    product_id = fields.Many2one('product.product')
    price_unit= fields.Float(string='Unit Price')
    qty = fields.Float(string='Quantity')

    appointment_id = fields.Many2one('hospital.appointment', string='Appointment')