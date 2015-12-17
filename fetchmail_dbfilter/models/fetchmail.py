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

from openerp import models, fields, api, _
from openerp.exceptions import Warning
import logging

_logger = logging.getLogger(__name__)

class FetchmailServer(models.Model):
    _inherit = 'fetchmail.server'

    def compute_default_dbfilter(self):
        return self.env.cr.dbname

    @api.one
    def compute_dbfilter_active(self):
        if not self.dbfilter or self.dbfilter == self.env.cr.dbname:
            self.is_server_active = True
        else:
            self.is_server_active = False

        return self.is_server_active;

    dbfilter = fields.Char('Database Filter', default=compute_default_dbfilter)

    is_server_active = fields.Boolean('Server Active on Current Database', compute=compute_dbfilter_active)

    @api.cr_uid_ids_context
    def connect(self, cr, uid, server_id, context=None):
        if isinstance(server_id, (list, tuple)):
            server_id = server_id[0]

        server = self.browse(cr, uid, server_id, context)

        if context and context.get('fetchmail_cron_running', False) and not server.is_server_active:
            raise Warning(_(
                "Can not Connect to server because Database Filter '%s' does not match to current database '%s'.") % (
                server.dbfilter, cr.dbname))
        return super(FetchmailServer, self).connect(
            cr, uid, server_id=server_id, context=context)

