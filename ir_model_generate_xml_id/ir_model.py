# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 MADSACK Media Store GmbH & Co. KG
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

class ir_model_data(models.Model):
    _inherit = 'ir.model.data'

    @api.model
    def generate_xml_id(self, module, name, model, filter):

        ir_model_data = self.search([
            ('module', '=', module),
            ('name', '=', name),
        ])

        if len(ir_model_data) > 0:
            #nothing to do
            return

        record = self.env[model].search(filter)
        if len(record) < 1:
            raise Warning('XML-ID creation failed: No record found for %s.%s on model %s.' % (module, name, model))
            return

        elif len(record) > 1:
            raise Warning('XML-ID creation failed: Too many records found for %s.%s on model %s.' % (module, name, model))
            return

        # len(record) = 1
        ir_model_data = self.search([
            ('model', '=', model),
            ('res_id', '=', record[0].id),
        ])

        if len(ir_model_data) > 0:
            raise Warning('XML-ID %s.%s creation failed: XML-ID "%s" for record %s #%s found.' % (module, name, ir_model_data[0].complete_name, model, str(ir_model_data[0].res_id)))
            return

        values = {
            'module': module,
            'name': name,
            'model': model,
            'res_id': record[0].id,
            'noupdate': True,
        }
        self.create(values)




