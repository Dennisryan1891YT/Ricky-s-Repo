#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Apple TV+ Add-on for Kodi
Apple streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.apple.tv.plus'
ADDON_NAME = 'Apple TV+'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()