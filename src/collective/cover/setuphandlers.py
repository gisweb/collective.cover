# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFEditions.interfaces.IModifier import IConditionalTalesModifier
from Products.CMFPlone import interfaces as Plone
from Products.CMFQuickInstallerTool import interfaces as QuickInstaller
from collective.cover.modifiers import modifiers
from zope.interface import implements


class HiddenProfiles(object):

    implements(Plone.INonInstallable)

    def getNonInstallableProfiles(self):
        """Do not show on Plone's list of installable profiles."""
        return [
            u'collective.cover:testfixture',
            u'collective.cover:uninstall',
        ]


class HiddenProducts(object):

    implements(QuickInstaller.INonInstallable)

    def getNonInstallableProducts(self):
        """Do not show on QuickInstaller's list of installable products."""
        return [
        ]


def install_modifiers(context, logger):
    portal_modifier = getToolByName(context, 'portal_modifier')
    for m in modifiers:
        id_ = m['id']
        if id_ in portal_modifier.objectIds():
            continue
        title = m['title']
        modifier = m['modifier'](id_, title)
        wrapper = m['wrapper'](id_, modifier, title)
        enabled = m['enabled']
        if IConditionalTalesModifier.providedBy(wrapper):
            wrapper.edit(enabled, m['condition'])
        else:
            wrapper.edit(enabled)
        portal_modifier.register(m['id'], wrapper)


def import_various(context):
    """Miscellanous steps import handle
    """
    if context.readDataFile('collective.cover_various.txt') is None:
        return

    logger = context.getLogger('collective.cover')
    site = context.getSite()
    install_modifiers(site, logger)
