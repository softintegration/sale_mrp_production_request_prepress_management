# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    check_prepress_proof_validity = fields.Boolean(string='Check the validity of Prepress proof',
                                            help='Check this option if you want to check the validity of Prepress proof when creating Manufacturing requests.')

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IrDefault = self.env['ir.default'].sudo()
        IrDefault.set('res.config.settings', "check_prepress_proof_validity", self.check_prepress_proof_validity,
                      company_id=self.company_id.id or self.env.user.company_id.id)
