# -*- coding: utf-8 -*-

from odoo import models
from odoo.exceptions import UserError
from odoo.tools.translate import _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def checkproduct(self):

        for rec in self:
            dict = []

            for line in rec.order_line:

                if line.product_id.id in dict:
                    raise UserError(_('Vous avez ajouté l"article ... en double'))
                dict.append(line.product_id.id)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    _order = 'create_uid desc, id desc'
