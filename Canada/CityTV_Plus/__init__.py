#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CityTV+ Add-on for Kodi
Premium CityTV streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.citytv.plus'
ADDON_NAME = 'CityTV+'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()