There's a frood who really knows where his towel is
---------------------------------------------------

1.0a6 (unreleased)
^^^^^^^^^^^^^^^^^^

- Add ``short_name`` to all tiles.  Use this as title in the tile
  list.  This can be translated.
  [maurits]

- Fix possible problem getting the ``css_class`` when the default
  configuration is used.  The code tried to treat this as a dictionary
  instead of a simple string.
  [maurits]

- Add offset as a configuration option to the collection tile.
  (fixes `#298`_). [warpr]

- Add ``cover-(type)-tile`` class to all tile templates (fixes issue
  `#189`_). [warpr]

- Support text from Dexterity items for the bodycontent and richtext
  tiles (fixes `#323`_). [maurits]

- Leaving layout editing tab after making changes now shows a confirmation
  dialog (fixes `#314`_). [rristow]

- Show a link to the related collection on compose view of the collection tile
  (closes `#260`_). [agnogueira, hvelarde]

- Increase test coverage. [tcurvelo]

- Remove bundles from portal_javascript (closes `#303`_). [jpgimenez]

- Remove upgrade steps from unsupported versions (closes `#295`_). [fulv]

- Depend on collective.js.bootstrap(closes `#201`_). [tcurvelo]

- Remove code from Image and Link tiles (closes `#301`_). [fulv]

- Catalan translation added. [lpmayos]


1.0a5 (2013-10-02)
^^^^^^^^^^^^^^^^^^

- Added Norwegian translation. [espenmn]

- Install IRelatedItems behavior to avoid 'ReferenceException: Invalid target
  UID' (fixes `#294`_). [hvelarde]

- Implement link integrity on Rich Text tile references (closes `#35`_).
  [jpgimenez]

- Register new alternate view for covers; the new view behaves like a standard
  content type view displaying object's title, description and viewlets on
  Plone's main_template main slot (closes `#271`_). [hvelarde]

- Fixes content-search in content chooser to correctly get the first
  page of results (closes `#276`_). [marcosfromero]

- Added any content type support for banner tile. If it has an `image`
  or `getImage` attribute, displays that image. And always adds
  a link (closes `#241`_). [marcosfromero]

- Prevent unnecesary page reloads when saving or canceling edit overlay
  in tiles (closes `#274`_). [marcosfromero]

- On collection tile, return a thumbnail only if the item has an image field
  and the field is visible (closes `#278`_). [cleberjsantos, hvelarde]

- Added Cover as Linkable in TinyMCE settings (closes `#259`_).
  [marcosfromero]

- Default CSS class for tiles (closes `#262`_). [marcosfromero]

- When adding a tile, display configuration icon only for configurable
  tiles (closes `#204`_). [marcosfromero]

- Auto add a column when adding a row (closes `#212`_).
  [marcosfromero]

- Remove dependency on plone.batching to avoid ``IndexError: multiple_pages``
  on Plone 4.2. [jpgimenez]

- Move CSS to registry_css (closes `#244`_). [agnogueira]

- Collection tile now fulfills the configured image size (fixes `#239`_).
  [cleberjsantos]

- Friendly layout for tile configuration (closes `#133`_). [agnogueira]


1.0a4 (2013-07-27)
^^^^^^^^^^^^^^^^^^

- Add Finnish translation. [datakurre]

- Add Italian translation. [gborelli]

- Package documentation was updated. [hvelarde]

- 'buttons.cancel' in prepOverlay closeselector has to be in quotes to
  avoid unrecognized expression javascript errors [ericof]

- Refactor collection tile to include header and footer fields and fix tile's
  i18n. (closes `#118`_) [hvelarde]

- Add simple Chinese translations (zh_CN). [Adam tang]

- Add banner tile that will replace image and link tiles; add deprecation
  warning to image and link tiles as they will be removed from package on
  next release; an upgrade step is provided for unregistering them to
  avoid further addition on covers. (closes `#218`_). [hvelarde]

- Make carousel tile configurable and avoid NoneType error by checking if
  carousel is empty (fixes `#203`_). [hvelarde]

- Refactor image tile to use original image and scales, when possible.
  [ericof, hvelarde]

- Add border to carousel tile dot. (closes `#206`_). [hvelarde]

- Upgrade to plone.app.blocks 1.1 [ericof]

- Refactor EnabledTilesVocabulary to avoid issues with situations in which
  we have no context/request (HT datakurre). [hvelarde]

- Spanish and Brazilian Portuguese translations were updated. [hvelarde]

- [bugfix] Prevent the configuration view to crash if the widget does not
  provide an 'accesskey'. [frapell]

- Allow editor to add custom class for each tile (closes `#190`_). [jpgimenez]

- Refactor vocabularies and avoid ComponentLookupError when tile is not
  available. [hvelarde]

- Add 'alt' attribute to images in list tile. [ericof]

- Fix image scaling view. [ericof]

- Avoid ComponentLookupError by improved handling of Unauthorized access of
  non-published or deleted objects referenced in the tiles. [ericof]

- Fix translation of Compose and Layout that must be in plone domain. [toutpt]

- Add French translation. [toutpt]


1.0a3 (2013-05-03)
^^^^^^^^^^^^^^^^^^

- Better support for internal and external images (closes `#188`_).
  [jpgimenez]

- Gallery tile now allows sorting of items easily through a widget created for
  that purpose (closes `#198`_). [Quimera]

- A custom permission for the export layout funcionality was added; exporting
  a cover layout to the Plone registry is now an administrative task
  accomplished only by Managers and Site Administrators (closes `#177`_).
  [Quimera]

- Fix a bug in collection tile when the target collection was removed
  (closes `#138`_). [jpgimenez]

- Improve interface and performance of content chooser
  (closes `#168`_ and `#169`_). [jpgimenez]

- Add upgrade step to rename resources in CSS and JS registries
  (fixes `#171`_). [hvelarde]

- An option in the control panel configlet was added in order to select the
  tiles that will be available for cover layout creation; an upgrade step
  is provided to update the registry with the new record (closes `#191`_).
  [hvelarde]

- Tile selection functionality in layout edit view was refactored  to an
  explicit D&D UI (closes `#183`_). [Quimera]

- Apply default configuration to tiles at initialization (closes `#100`_).
  [hvelarde]

- Store basic tile data in unicode format to avoid UnicodeDecodeError
  (closes `#144`_). [hvelarde]

- A new special widgect for the cover creation and layout selection was added;
  the widget draws a preview of the layout in real time using an HTML5 canvas
  element (closes `#179`_). [Quimera]

- Show title of object as alt attribute in image of basic tile. [hvelarde]

- Ensure tile UUID does not start with a number (fixes `#137`_). [hvelarde]

- Implements an original size scale to show the original image. [jpgimenez]

- Improve the way than images are accesed from the original object,
  using the standard images traversal. (issue `#158`_) [jpgimenez]

- Fixed a bug with Plone 4.3 that avoided TinyMCE being displayed for
  RichText. (closes `#157`_). [ericof]


1.0a2 (2013-04-09)
^^^^^^^^^^^^^^^^^^
- Move Galleria's stylesheet and JS init to <head>. [davilima6]

- New tile: `PloneFormGen`_ embedded form. [ericof]

- New tile: Content Body. [ericof]

- Update package documentation. [hvelarde, jpgimenez]

- Package is now compatible with Plone 4.3. [ericof, jpgimenez, hvelarde]

- Remove dependency on plone.principalsource (closes `#152`_). [ericof]

- Support five.grok 1.3.2 and plone.app.dexterity 2.0.x. [ericof]

- Update JQuery UI to version 1.8.16.9 (fixes `#124`_). [hvelarde]

- Fix TinyMCE table conflict (closes `#142`_). [agnogueira]

- News Items can now be added to the carousel tile (fixes `#146`_).
  [jpgimenez]

- Basic tile date field visibility is now configurable. [jpgimenez]

- Refactor carousel tile to use collective.js.galleria (closes `#123`_).
  [jpgimenez]

- Refactor list tile to use adapters to get the contained items uids.
  [jpgimenez]

- Implements a way to ommit fields from tiles edit form and show it at
  configure form. [jpgimenez]

- Refactor of collection tile. [hvelarde]

- List and carousel tiles now support loading images from folderish content.
  [jpgimenez]

- Have the <base> tag to include a slash at the end so relative ajax calls are
  called for the object and not its parent (fixes `#48`_). [frapell]

- In order to be able to load Dexterity items from the import content GS step,
  we need to provide this interface manualy, until a proper fix in Dexterity
  is implemented. [frapell]

- Make the cover object to be an Item instead of a Container (fixes `#114`_).
  [frapell]

- Date and subjects fields on basic tile are now Read Only (fixes `#129`_).
  [jpgimenez]

- Fix row height in layout view (closes `#128`_). [Quimera]

- Fix filter feature on content chooser (closes `#121`_). [Quimera]


1.0a1 (2013-01-07)
^^^^^^^^^^^^^^^^^^

- Initial release.

.. _`PloneFormGen`: https://pypi.python.org/pypi/Products.PloneFormGen
.. _`#35`: https://github.com/collective/collective.cover/issues/35
.. _`#48`: https://github.com/collective/collective.cover/issues/48
.. _`#100`: https://github.com/collective/collective.cover/issues/100
.. _`#114`: https://github.com/collective/collective.cover/issues/114
.. _`#118`: https://github.com/collective/collective.cover/issues/118
.. _`#121`: https://github.com/collective/collective.cover/issues/121
.. _`#123`: https://github.com/collective/collective.cover/issues/123
.. _`#124`: https://github.com/collective/collective.cover/issues/124
.. _`#128`: https://github.com/collective/collective.cover/issues/128
.. _`#129`: https://github.com/collective/collective.cover/issues/129
.. _`#133`: https://github.com/collective/collective.cover/issues/133
.. _`#137`: https://github.com/collective/collective.cover/issues/137
.. _`#138`: https://github.com/collective/collective.cover/issues/138
.. _`#142`: https://github.com/collective/collective.cover/issues/142
.. _`#144`: https://github.com/collective/collective.cover/issues/144
.. _`#146`: https://github.com/collective/collective.cover/issues/146
.. _`#152`: https://github.com/collective/collective.cover/issues/152
.. _`#157`: https://github.com/collective/collective.cover/issues/157
.. _`#158`: https://github.com/collective/collective.cover/issues/158
.. _`#168`: https://github.com/collective/collective.cover/issues/168
.. _`#169`: https://github.com/collective/collective.cover/issues/169
.. _`#171`: https://github.com/collective/collective.cover/issues/171
.. _`#177`: https://github.com/collective/collective.cover/issues/177
.. _`#179`: https://github.com/collective/collective.cover/issues/179
.. _`#183`: https://github.com/collective/collective.cover/issues/183
.. _`#188`: https://github.com/collective/collective.cover/issues/188
.. _`#189`: https://github.com/collective/collective.cover/issues/189
.. _`#190`: https://github.com/collective/collective.cover/issues/190
.. _`#191`: https://github.com/collective/collective.cover/issues/191
.. _`#198`: https://github.com/collective/collective.cover/issues/198
.. _`#201`: https://github.com/collective/collective.cover/issues/201
.. _`#203`: https://github.com/collective/collective.cover/issues/203
.. _`#204`: https://github.com/collective/collective.cover/issues/204
.. _`#206`: https://github.com/collective/collective.cover/issues/206
.. _`#212`: https://github.com/collective/collective.cover/issues/212
.. _`#218`: https://github.com/collective/collective.cover/issues/218
.. _`#239`: https://github.com/collective/collective.cover/issues/239
.. _`#241`: https://github.com/collective/collective.cover/issues/241
.. _`#244`: https://github.com/collective/collective.cover/issues/244
.. _`#259`: https://github.com/collective/collective.cover/issues/259
.. _`#260`: https://github.com/collective/collective.cover/issues/260
.. _`#262`: https://github.com/collective/collective.cover/issues/262
.. _`#271`: https://github.com/collective/collective.cover/issues/271
.. _`#274`: https://github.com/collective/collective.cover/issues/274
.. _`#276`: https://github.com/collective/collective.cover/issues/276
.. _`#278`: https://github.com/collective/collective.cover/issues/278
.. _`#281`: https://github.com/collective/collective.cover/issues/281
.. _`#294`: https://github.com/collective/collective.cover/issues/294
.. _`#295`: https://github.com/collective/collective.cover/issues/295
.. _`#298`: https://github.com/collective/collective.cover/issues/298
.. _`#301`: https://github.com/collective/collective.cover/issues/301
.. _`#303`: https://github.com/collective/collective.cover/issues/303
.. _`#314`: https://github.com/collective/collective.cover/issues/314
.. _`#323`: https://github.com/collective/collective.cover/issues/323
