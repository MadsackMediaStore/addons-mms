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

{
    'name': 'Mail Server - DB Filter (MMS)',
    'description': 'Makes sure sending mails via mail.server can only be done on a certain database. Do not use this module if you using smtp-config in files.',
    'version': '0.1',
    'author': 'MADSACK Media Store GmbH & Co. KG',
    'license': 'AGPL-3',
    'website': 'http://www.mms-service.de',
    'depends': [
        'fetchmail',
    ],
    'category': 'Tools',
    'summary': 'Makes sure sending mail via mail.server can only be done on a certain database',
    'data': [
        'views/ir_mail_server_view.xml',
    ],
    'demo': [],
    'installable': True,
}