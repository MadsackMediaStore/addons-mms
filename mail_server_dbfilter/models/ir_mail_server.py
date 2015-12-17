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
from openerp import SUPERUSER_ID
import logging

_logger = logging.getLogger(__name__)

class MailServer(models.Model):
    _inherit = 'ir.mail_server'

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

    def send_email(self, cr, uid, message, mail_server_id=None, smtp_server=None, smtp_port=None, smtp_user=None,
            smtp_password=None, smtp_encryption=None, smtp_debug=False, context=None):

        mail_server = None
        if mail_server_id:
            mail_server = self.browse(cr, SUPERUSER_ID, mail_server_id)
        elif not smtp_server:
            mail_server_ids = self.search(cr, SUPERUSER_ID, [], order='sequence', limit=1)
            if mail_server_ids:
                mail_server = self.browse(cr, SUPERUSER_ID, mail_server_ids[0])

        if mail_server:
            if not mail_server.is_server_active:
                raise Warning(_(
                    "Can not send mail because Database Filter '%s' does not match to current database '%s'.") % (
                    mail_server.dbfilter, cr.dbname))
        else:
            _logger.warning(_(
                'Module "mail_server_dbfilter" does not work with smtp config files. Please uninstall the module.'))

        return super(MailServer, self).send_email(cr, uid, message, mail_server_id=mail_server_id, smtp_server=smtp_server,
            smtp_port=smtp_port, smtp_user=smtp_user, smtp_password=smtp_password, smtp_encryption=smtp_encryption,
            smtp_debug=smtp_debug, context=None)
