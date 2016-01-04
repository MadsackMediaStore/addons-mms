# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015 MADSACK Media Store GmbH & Co. KG
#    (<http://www.mms-service.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, api
import pdb

class SaleOrderLine(models.Model):
    _name = "sale.order.line"
    _inherit = "sale.order.line"

    @api.model
    def _prepare_order_line_invoice_line(self, line, account_id=False):
        pdb.set_trace()
        if line and line.product_id and line.product_id.disable_create_invoice_line_from_so:
            return {}

        return super(SaleOrderLine, self)._prepare_order_line_invoice_line(line=line, account_id=account_id)
