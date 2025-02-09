****************
collective.cover
****************

.. contents:: Table of Contents

Life, the Universe, and Everything
----------------------------------

``collective.cover`` is a package that allows the creation of elaborate covers
for website homepages, especially for news portals, government sites and
intranets that require more resources than a simple page or collection can
offer. However, despite offering rich resources to build a cover,
``collective.cover`` also provides a very easy mechanism for managing its
contents, built around a drag-and-drop interface.

``collective.cover`` is based on `Blocks`_ and `Tiles`_, like `Deco`_, the new
layout composition system for Plone.

.. TODO: explain why we need cover instead of just using Deco itself.

.. TODO: add a comparison between Deco and collective.cover

Use cases
^^^^^^^^^

Suppose you are running The Planet, a news site that has a bunch of editors
focused on getting news on different topics, like Economy, Health or Sports.

If you are the main publisher of the site, you may want to delegate the
construction of the cover page of the Economy section to the people working on
that content area, but you might not want them messing around the Sports
section as well.

Also, suppose you have the final game of the World Cup and the match is going
to be defined on penalties: you may want to prepare a couple of cover pages
and publish the right one focused on the team that won in the end.

These are the kind of issues we want to solve with this package; we are still
far from it, but that is the idea.

Mostly Harmless
---------------

.. Warning::
   ``collective.cover`` is currently not compatible with standard Plone tiles;
   this will be addressed in a future realease of the package. See issues
   `#81`_ and `#112`_ for more information.

.. image:: https://secure.travis-ci.org/collective/collective.cover.png?branch=master
    :target: http://travis-ci.org/collective/collective.cover

.. image:: https://coveralls.io/repos/collective/collective.cover/badge.png?branch=master
    :target: https://coveralls.io/r/collective/collective.cover

Got an idea? Found a bug? Let us know by `opening a support ticket`_.

Don't Panic
-----------

Installation
^^^^^^^^^^^^

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        collective.cover

    [versions]
    ...
    plone.app.blocks = 1.1.1
    plone.app.drafts = 1.0a2
    plone.app.jquery = 1.7.2
    plone.app.tiles = 1.0.1
    plone.tiles = 1.2

#. If you are using Plone 4.2.x you need to add the following also::

    [versions]
    ...
    collective.js.jqueryui = 1.8.16.9
    plone.app.jquerytools = 1.5.6

After updating the configuration you need to run ''bin/buildout'', which will
take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``collective.cover`` and click the 'Activate' button.

.. Note::

    You may have to empty your browser cache and save your resource registries
    in order to see the effects of the product installation.

Not entirely unlike
-------------------

Over the years there have been some packages designed to solve the problem of
creating section covers in Plone. We have used and have taken ideas from the
following:

`CompositePack`_
    Very old; the legacy code is so complex that is not maintainable anymore.
    It has (arguably) the best user interface of all. Layouts can not be
    created TTW. Viewlets are just page templates associated with content
    types; you can drag&drop viewlets around the layout. Publishers love it.

`CMFContentPanels`_
    Code is very old, but still maintained (at least works in Plone 4). Allows
    to create complex layouts TTW and use any layout as a template. Easy to
    extend and edit (but is terrible to find a content to use). Needs a lot of
    memory to work and aggressive cache settings.

`Collage`_
    Allows the creation of layouts TTW but it has (arguably) the worst user
    interface of all. It is easily extended and there are several add-ons
    available that provide new functionality for it.

Home Page Editor of the Brazilian Chamber of Deputies Site
    Strongly based on `Collage`_, this package was presented at the `World
    Plone Day 2012 Brasilia`_. It allows editing of home pages and the
    definition of permissions on blocks of content. Available only for Plone 3
    and not openly published… yet.

`collective.panels`_
    A new package that lets site editors add portlets to a set of new
    locations: above and below page contents, portal top and footer. The
    package comes with a number of flexible layouts that are used to position
    the portlets, and locations can be fixed to the nearest site object, to
    facilitate inheritance. In ``collective.cover`` (this package), we don't
    want to use portlets at all.

.. _`#112`: https://github.com/collective/collective.cover/issues/112
.. _`#218`: https://github.com/collective/collective.cover/issues/218
.. _`#81`: https://github.com/collective/collective.cover/issues/81
.. _`Blocks`: https://github.com/plone/plone.app.blocks
.. _`CMFContentPanels`: http://plone.org/products/cmfcontentpanels
.. _`Collage`: http://plone.org/products/collage
.. _`collective.panels`: https://github.com/collective/collective.panels
.. _`CompositePack`: http://plone.org/products/compositepack
.. _`Deco`: https://github.com/plone/plone.app.deco
.. _`opening a support ticket`: https://github.com/collective/collective.cover/issues
.. _`see and comment on our mockups online`: https://simples.mybalsamiq.com/projects/capas/grid
.. _`Tiles`: https://github.com/plone/plone.app.tiles
.. _`Using tiles to provide more flexible Plone layouts`: http://davisagli.com/blog/using-tiles-to-provide-more-flexible-plone-layouts
.. _`World Plone Day 2012 Brasilia`: http://colab.interlegis.leg.br/wiki/WorldPloneDay
