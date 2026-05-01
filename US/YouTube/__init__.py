#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YouTube Add-on for Kodi
Video sharing platform
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.youtube'
ADDON_NAME = 'YouTube'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()