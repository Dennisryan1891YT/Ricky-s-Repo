#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YouTube TV Add-on for Kodi
Live TV streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.youtube.tv'
ADDON_NAME = 'YouTube TV'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()