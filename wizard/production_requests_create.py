# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero


class ProductionRequestsCreate(models.TransientModel):
    _inherit = 'production.requests.create'

    def _prepare_production_request(self, item):
        res = super(ProductionRequestsCreate, self)._prepare_production_request(item)
        src_order_line = self.env['sale.order.line'].browse(res['sale_line_id'])
        if self.env[
            'sale.order']._check_prepress_proof_validity() and not src_order_line.prepress_proof_id._check_validity_for_product(
                src_order_line.product_id):
            raise ValidationError(
                _("The Prepress proof %s of the product %s is no longer valid,you have to check the status of this Prepress proof!") % (
                src_order_line.prepress_proof_id.name, src_order_line.product_id.display_name))
        res.update({'prepress_proof_id': item.prepress_proof_id and item.prepress_proof_id.id})
        return res

    def _create_production_request(self, production_requests_dict_list):
        production_requests = self.env['mrp.production.request'].create(production_requests_dict_list)
        # TODO:we have to check again if this is good approach
        # we have to pass this argument to context to prevent other modules from updating the prepress proof of the created manufacturing request
        for req in production_requests:
            req.with_context(ignore_update_prepress_proof=True)._onchange_product_id()
        production_requests.action_make_waiting()


class ProductionRequestsCreateItem(models.TransientModel):
    _inherit = 'production.requests.create.item'

    prepress_proof_id = fields.Many2one('prepress.proof', string='Prepress proof', readonly=False)
