# -*- coding: utf-8 -*-
# Copyright 2020 Akretion (http://www.akretion.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
# pylint: disable=W8106
# pylint: disable=consider-merging-classes-inherited

import logging

from odoo.exceptions import AccessError
from odoo.tools.translate import _

from odoo.addons.base_rest.components.service import to_bool
from odoo.addons.component.core import Component

_logger = logging.getLogger(__name__)


class GithubModuleService(Component):
    _inherit = "base.rest.service"
    _name = "github.module.service"
    _collection = "github.module"
    _usage = "module"

    def get_github_module_information(self):
        modules = self.env["odoo.module"].search([])
        return
