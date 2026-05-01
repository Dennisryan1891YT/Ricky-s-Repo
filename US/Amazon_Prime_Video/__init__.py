#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Amazon Prime Video Add-on for Kodi
Amazon streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.amazon.prime'
ADDON_NAME = 'Prime Video'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()