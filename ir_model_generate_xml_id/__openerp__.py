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

{
    'name': "IR Model - Create XML-ID with XML (MMS)",
    'version': "0.1",
    'author': "MADSACK Media Store <consulting@mms-service.de>",
    'license': 'AGPL-3',
    'category': "Tools",
    'summary': "Generating XML-ID",
    "description": """Generating a XML-ID for any record, which has no XML-ID.

    Call the function generate_xml_id(self, module, name, model, filter).

    Example:
    <!-- xml_id: account.journal_bank -->
    <function model="ir.model.data" name="generate_xml_id">
        <!--module--><value>account</value>
        <!--name--><value>journal_bank</value>
        <!--model--><value>account.journal</value>
        <!--filter--><value eval="[('name', '=', 'Bank')]"/>
    </function>

    """,
    'depends': [
        'base',
    ],
    'data': [
    ],
    'installable': True,
}
