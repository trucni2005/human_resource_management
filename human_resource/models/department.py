from odoo import models, fields, api


class Department(models.Model):
    _name = 'human_resource.department'
    _description = 'Bộ phận'

    department_id = fields.Char(string='Mã bộ phận', required=True, help='Nhập mã bộ phận.')
    name = fields.Char(string='Tên Bộ phận', required=True, help='Nhập tên bộ phận.')
    description = fields.Text(string='Mô tả', help='Mô tả về bộ phận.')
    manager_id = fields.Many2one('res.users', string='Quản lý Bộ phận', help='Quản lý của bộ phận.')
    # employees = fields.One2many('human_resource.employee', 'department_id', string='Nhân viên',
    #                             help='Danh sách nhân viên thuộc bộ phận.')
    parent_id = fields.Many2one('human_resource.department', string='Bộ phận cha', help='Bộ phận mẹ (nếu có).')
    child_ids = fields.One2many('human_resource.department', 'parent_id', string='Các bộ phận con',
                                help='Các bộ phận con của bộ phận hiện tại.')

    # Thêm các trường khác tùy theo yêu cầu của bạn.

    @api.onchange('parent_id')
    def _onchange_parent_id(self):
        if self.parent_id:
            return {'domain': {'parent_id': [('id', '!=', self.id)]}}
