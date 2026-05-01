#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Disney+ Add-on for Kodi
Disney streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.disney.plus'
ADDON_NAME = 'Disney+'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()