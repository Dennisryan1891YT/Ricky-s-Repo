#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CBC News Add-on for Kodi
Live news streaming from CBC
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.cbc.news'
ADDON_NAME = 'CBC News'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()