from odoo import http
from odoo.http import request

class RoomBookingController(http.Controller):

    @http.route('/api/room_booking/status/<string:nomor_pemesanan>', type='json', auth='public')
    def track_status(self, nomor_pemesanan):
        pemesanan = request.env['pemesanan.ruangan'].sudo().search([('nomor_pemesanan', '=', nomor_pemesanan)], limit=1)
        if not pemesanan:
            return {'error': 'Pemesanan tidak ditemukan'}
        return {'status': pemesanan.status_pemesanan}
