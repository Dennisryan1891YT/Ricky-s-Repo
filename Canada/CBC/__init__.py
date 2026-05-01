#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CBC Add-on for Kodi
Canadian Broadcasting Corporation streaming
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.cbc'
ADDON_NAME = 'CBC'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()