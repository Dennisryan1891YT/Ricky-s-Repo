#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RiverTV Add-on for Kodi
Canadian streaming platform
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.rivertv'
ADDON_NAME = 'RiverTV'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()