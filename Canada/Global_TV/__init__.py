#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Global TV Add-on for Kodi
Canadian television network streaming
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.globaltv'
ADDON_NAME = 'Global TV'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()