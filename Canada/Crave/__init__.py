#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crave Add-on for Kodi
Canadian streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.crave'
ADDON_NAME = 'Crave'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()