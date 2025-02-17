# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Swadesh
                                 A QGIS plugin
 Integrates official Indian basemaps from Bhuvan and satellite data from the Bhoonidhi API into QGIS.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-02-19
        copyright            : (C) 2025 by Dhruv Gadhavi
        email                : dxce7qbyg@mozmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Swadesh class from file Swadesh.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .swadesh import Swadesh
    return Swadesh(iface)
