# -*- coding: utf-8 -*-
from AccessControl import Unauthorized
from collective.cover import _
from collective.cover.tiles.base import IPersistentCoverTile
from collective.cover.tiles.base import PersistentCoverTile
from plone.app.uuid.utils import uuidToObject
from plone.autoform import directives as form
from plone.tiles.interfaces import ITileDataManager
from plone.uuid.interfaces import IUUID
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFPlone.utils import safe_unicode
from zope import schema
from zope.interface import implements


class IPFGTile(IPersistentCoverTile):

    title = schema.TextLine(
        title=_(u'Title'),
        required=False,
    )

    description = schema.Text(
        title=_(u'Description'),
        required=False,
    )

    form.omitted('uuid')
    uuid = schema.TextLine(title=u'Collection uuid', readonly=True)


class PFGTile(PersistentCoverTile):

    implements(IPersistentCoverTile)

    index = ViewPageTemplateFile("templates/pfg.pt")

    is_editable = True
    is_configurable = True
    short_name = _(u"msg_short_name_pfg", default=u"FormGen")

    def body(self):
        body = ''
        uuid = self.data.get('uuid', None)
        try:
            obj = uuid and uuidToObject(uuid)
            if obj is not None:
                body = obj.restrictedTraverse('fg_embedded_view_p3')()
        except Unauthorized:
            body = ''
        return body

    def populate_with_object(self, obj):
        super(PFGTile, self).populate_with_object(obj)

        data = {
            'title': safe_unicode(obj.Title()),
            'description': safe_unicode(obj.Description()),
            'uuid': IUUID(obj, None),  # XXX: can we get None here? see below
        }

        data_mgr = ITileDataManager(self)
        data_mgr.set(data)

    def accepted_ct(self):
        """ For now we are supporting Document and News Item
        """
        return ['FormFolder']
