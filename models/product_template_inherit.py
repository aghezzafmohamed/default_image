# -*- coding: utf-8 -*-
import base64

from odoo import models, api, tools


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    @api.model_create_multi
    def create(self, vals_list):
        if not vals_list[0]['image_1920']:
            product_default_image = self.env['ir.config_parameter'].sudo().get_param(
                'res.config.settings.product_default_image')
            if product_default_image:
                vals_list[0]['image_1920'] = product_default_image

        return super(ProductTemplateInherit, self).create(vals_list)
