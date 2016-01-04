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
    'name': "Sale Order - Optinal create invoice line for product (MMS)",
    'version': "0.1",
    'author': "Malte Jansen, MADSACK Media Store <consulting@mms-service.de>",
    'license': 'AGPL-3',
    'category': "Sale",
    'summary': "Disable invoice line creation for certain products.",
    "description": """
        Disable invoice line creation for certain products.
    """,
    'depends': [
        'sale',
    ],
    'data': [
        'views/product_view.xml',
    ],
    'installable': True,
}
