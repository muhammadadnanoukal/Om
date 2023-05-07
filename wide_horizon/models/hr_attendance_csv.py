from odoo import models, fields, api


class HrAttendanceCSV(models.Model):
    _inherit = 'hr.attendance'
    reg_number = fields.Char(string="Registration Number")
    emp = fields.Char(string="Employee", compute="_compute_emp")

    @api.depends('employee_id')
    def _compute_emp(self):
        for rec in self:
            rec.emp = None
            if rec.reg_number:
                rec.employee_id = self.env['hr.employee'].search([('registration_number', '=', rec.reg_number)])


class HrEmployeeCSV(models.Model):
    _inherit = 'hr.employee'

    def name_get(self):
        result = []
        for rec in self:
            name = '[' + str(rec.registration_number) + '] ' + rec.name
            result.append((rec.id, name))
        return result
