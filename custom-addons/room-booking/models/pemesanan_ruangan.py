from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PemesananRuangan(models.Model):
    _name = 'pemesanan.ruangan'
    _description = 'Pemesanan Ruangan'

    nomor_pemesanan = fields.Char(string='Nomor Pemesanan', required=True, unique=True)
    ruangan_id = fields.Many2one('master.ruangan', string='Ruangan', required=True)
    nama_pemesanan = fields.Char(string='Nama Pemesanan', required=True)
    tanggal_pemesanan = fields.Datetime(string='Tanggal Pemesanan', required=True)
    status_pemesanan = fields.Selection([
        ('draft', 'Draft'),
        ('on_going', 'On Going'),
        ('done', 'Done'),
    ], string='Status Pemesanan', default='draft')
    
    catatan = fields.Text(string='Catatan Pemesanan')

    @api.constrains('ruangan_id', 'tanggal_pemesanan')
    def _check_ruangan_availability(self):
        for record in self:
            overlapping_bookings = self.search([
                ('ruangan_id', '=', record.ruangan_id.id),
                ('tanggal_pemesanan', '=', record.tanggal_pemesanan),
                ('id', '!=', record.id) 
            ])
            if overlapping_bookings:
                raise ValidationError("Ruangan ini sudah dipesan pada tanggal yang sama.")

    @api.constrains('nama_pemesanan')
    def _check_unique_nama_pemesanan(self):
        for record in self:
            existing_booking = self.search([
                ('nama_pemesanan', '=', record.nama_pemesanan),
                ('id', '!=', record.id)
            ])
            if existing_booking:
                raise ValidationError("Nama Pemesanan harus unik.")

    def action_set_on_going(self):
        for record in self:
            record.status_pemesanan = 'on_going'

    def action_set_done(self):
        for record in self:
            record.status_pemesanan = 'done'