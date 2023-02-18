# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def _prepare_production_request_items(self):
        res = super(SaleOrder,self)._prepare_production_request_items()
        for prod_line in res:
            src_order_line = self.env['sale.order.line'].browse(prod_line[2]['sale_line_id'])
            prod_line[2].update({'prepress_proof_id':src_order_line.prepress_proof_id and src_order_line.prepress_proof_id.id})
        return res


    @api.model
    def _check_prepress_proof_validity(self):
        IrDefault = self.env['ir.default'].sudo()
        return IrDefault.get('res.config.settings', 'check_prepress_proof_validity',
                             company_id=self.company_id.id or self.env.user.company_id.id)










