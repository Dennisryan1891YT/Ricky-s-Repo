#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CTV Add-on for Kodi
Canadian Television Network streaming
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.ctv'
ADDON_NAME = 'CTV'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()