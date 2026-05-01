#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CBC Gem Add-on for Kodi
Premium CBC streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.cbc.gem'
ADDON_NAME = 'CBC Gem'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()