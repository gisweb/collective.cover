# -*- coding: utf-8 -*-

from collective.cover.testing import INTEGRATION_TESTING
from plone import api

import unittest


class LayoutTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

        with api.env.adopt_roles(['Manager']):
            self.folder = api.content.create(self.portal, 'Folder', 'folder')

        self.cover = api.content.create(
            self.folder, 'collective.cover.content', 'cover')
