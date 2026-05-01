#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hulu Add-on for Kodi
Streaming TV shows and movies
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.hulu'
ADDON_NAME = 'Hulu'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()