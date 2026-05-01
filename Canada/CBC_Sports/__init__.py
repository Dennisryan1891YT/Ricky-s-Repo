#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CBC Sports Add-on for Kodi
Live sports streaming from CBC
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.cbc.sports'
ADDON_NAME = 'CBC Sports'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()