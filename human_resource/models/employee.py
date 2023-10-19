from odoo import models, fields, api


class Employee(models.Model):
    _name = 'human_resource.employee'

    employee_id = fields.Integer(string='Mã Nhân viên', required=True, help="Nhập mã nhân viên.")
    full_name = fields.Char(string='Họ và Tên', help="Nhập họ và tên đầy đủ của nhân viên.")
    date_of_birth = fields.Date(string='Ngày Sinh', help="Nhập ngày sinh của nhân viên.")
    citizen_id = fields.Char(string='Số CMND', help="Nhập số CMND của nhân viên.")
    job_position = fields.Char(string='Chức vụ', help="Nhập chức vụ của nhân viên.")
    address = fields.Text(string='Địa chỉ', help="Nhập địa chỉ thường trú của nhân viên.")
    email = fields.Char(string='Email', help="Nhập địa chỉ email của nhân viên.")
    mobile = fields.Char(string='Số Điện thoại di động', help="Nhập số điện thoại di động của nhân viên.")
    bank_account = fields.Char(string='Số Tài khoản ngân hàng', help="Nhập số tài khoản ngân hàng của nhân viên.")
    image = fields.Binary(string='Hình ảnh', help="Tải lên hình ảnh của nhân viên.")
    department_code = fields.Char(string='Mã Bộ phận', help="Nhập mã bộ phận của nhân viên.")
    contract_code = fields.Char(string='Mã Hợp đồng', help="Nhập mã hợp đồng của nhân viên.")
    project_code = fields.Char(string='Mã Dự án', help="Nhập mã dự án của nhân viên.")
    remaining_paid_leave = fields.Float(string='Ngày nghỉ phép có lương còn lại')
    remaining_unpaid_leave = fields.Float(string='Ngày nghỉ không lương còn lại')

    @api.model
    def create(self, vals):
        employee = super(Employee, self).create(vals)

        employee_id = employee.employee_id

        employment_contract = self.env['human_resource.employment_contract'].create({
            'employee_id': employee_id,
            'contract_code': employee.contract_code,
            'employee_name': employee.full_name
        })

        return employee

