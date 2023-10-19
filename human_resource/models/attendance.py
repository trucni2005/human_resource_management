from odoo import models, fields


class Attendance(models.Model):
    _name = 'human_resource.attendance'
    _description = 'Bảng Chấm Công Nhân Viên'

    employee_id = fields.Many2one('human_resource.employee', string='Nhân Viên', required=True,
                                  help="Nhân viên liên quan đến bản ghi chấm công.")
    checkin_time = fields.Datetime(string='Thời Gian Check-In', required=True, help="Thời gian đến làm việc.")
    checkout_time = fields.Datetime(string='Thời Gian Check-Out', required=True, help="Thời gian kết thúc làm việc.")
    status = fields.Selection([
        ('present', 'Có Mặt'),
        ('absent', 'Vắng Mặt'),
        ('late', 'Đi Trễ'),
        ('early_checkout', 'Về Sớm'),
    ], string='Trạng Thái', help="Trạng thái chấm công.")
    date = fields.Date(string='Ngày', required=True, help="Ngày chấm công.")
