import os
from Acquisition import aq_base
from App.class_init import InitializeClass
from collective.cover.tiles.base import AnnotationStorage
from itertools import izip
from Products.CMFCore.utils import getToolByName
from Products.CMFEditions.interfaces.IArchivist import ArchivistRetrieveError
from Products.CMFEditions.interfaces.IModifier import IAttributeModifier
from Products.CMFEditions.interfaces.IModifier import ICloneModifier
from Products.CMFEditions.Modifiers import ConditionalTalesModifier
from Products.PageTemplates.PageTemplateFile import PageTemplateFile
from ZODB.blob import Blob
from zope.interface import implements


manage_TilesCloneNamedFileBlobsAddForm =  \
    PageTemplateFile('www/CloneNamedFileBlobs.pt', globals(), __name__='manage_CloneNamedFileBlobs')


def manage_addTilesCloneNamedFileBlobs(self, id, title=None, REQUEST=None):
    """Add a clone namedfile blobs modifier.
    """
    modifier = TilesCloneNamedFileBlobs(id, title)
    self._setObject(id, modifier)

    if REQUEST is not None:
        REQUEST['RESPONSE'].redirect(self.absolute_url() + '/manage_main')


class TilesCloneNamedFileBlobs:
    """Modifier to save an un-cloned reference to the blob to avoid it being
    packed away.
    """

    implements(IAttributeModifier, ICloneModifier)

    def __init__(self, id_, title):
        self.id = str(id_)
        self.title = str(title)

    def _blob_file_classes(self):
        blob_file_classes = []
        try:
            from z3c.blobfile.file import File
        except ImportError:
            pass
        else:
            blob_file_classes.append(File)
        try:
            from plone.namedfile.file import NamedBlobFile
        except ImportError:
            pass
        else:
            blob_file_classes.append(NamedBlobFile)
        return tuple(blob_file_classes)

    def getReferencedAttributes(self, obj):
        file_data = {}
        blob_file_classes = self._blob_file_classes()
        # Try to get last revision, only store a new blob if the
        # contents differ from the prior one, otherwise store a
        # reference to the prior one.
        # The implementation is mostly based on CMFEditions's CloneBlobs
        # modifier.
        repo = getToolByName(obj, 'portal_repository')
        try:
            prior_rev = repo.retrieve(obj)
        except ArchivistRetrieveError:
            prior_rev = None

        for tid in obj.list_tiles():
            tile = obj.get_tile(tid)
            for name, field in tile.data.items():
                if isinstance(field, blob_file_classes):
                    if field._blob is None or \
                       field.data is None:
                        continue
                    blob_file = field.open()
                    save_new = True
                    dotted_name = '.'.join([tid, name])
                    if prior_rev is not None:
                        prior_obj = prior_rev.object
                        if tid not in prior_obj.list_tiles():
                            continue
                        prior_tile = prior_obj.get_tile(tid)
                        if prior_tile is None:
                            continue
                        prior_blob = prior_tile.data[name]
                        if prior_blob._blob is not None:
                            prior_file = prior_blob.open()

                            # Check for file size differences
                            if (os.fstat(prior_file.fileno()).st_size ==
                                    os.fstat(blob_file.fileno()).st_size):
                                # Files are the same size, compare line by line
                                for line, prior_line in izip(blob_file,
                                                             prior_file):
                                    if line != prior_line:
                                        break
                                else:
                                    # The files are the same, save a reference
                                    # to the prior versions blob on this
                                    # version
                                    file_data[dotted_name] = prior_blob._blob
                                    save_new = False

                    if save_new:
                        new_blob = file_data[dotted_name] = Blob()
                        new_blob_file = new_blob.open('w')
                        try:
                            blob_file.seek(0)
                            new_blob_file.writelines(blob_file)
                        finally:
                            blob_file.close()
                            new_blob_file.close()

        return file_data

    def reattachReferencedAttributes(self, obj, attrs_dict):
        obj = aq_base(obj)
        annotations = getattr(obj, '__annotations__', None)
        for name, blob in attrs_dict.iteritems():
            tid = name.split('.')[0]
            dataid = 'plone.tiles.data.%s' % tid
            fname = name.split('.')[-1]
            annotations[dataid][fname]._blob = blob

    def getOnCloneModifiers(self, obj):
        """Removes references to blobs.
        """
        blob_file_classes = self._blob_file_classes()
        blob_refs = {}
        for tid in obj.list_tiles():
            tile = obj.get_tile(tid)
            for name, field in tile.data.items():
                if isinstance(field, blob_file_classes):
                    if field._blob is not None and \
                       field.data is not None:
                        blob_refs[id(aq_base(field._blob))] = True
                        # handle scales
                        storage = AnnotationStorage(tile)
                        for scale in storage.values():
                            scale_data = scale.get('data', None)
                            if isinstance(scale_data, blob_file_classes):
                                if scale_data.data is not None:
                                    blob_refs[id(aq_base(scale_data._blob))] = True

        def persistent_id(obj):
            return blob_refs.get(id(obj), None)

        def persistent_load(obj):
            return None

        return persistent_id, persistent_load, [], []


InitializeClass(TilesCloneNamedFileBlobs)


modifiers = (
    {
        'id': 'TilesCloneNamedFileBlobs',
        'title': "Store blobs by reference on collective.cover.content",
        'enabled': True,
        'condition': "python:portal_type == 'collective.cover.content'",
        'wrapper': ConditionalTalesModifier,
        'modifier': TilesCloneNamedFileBlobs,
        'form': manage_TilesCloneNamedFileBlobsAddForm,
        'factory': manage_addTilesCloneNamedFileBlobs,
        'icon': 'www/modifier.gif',
    },
)
