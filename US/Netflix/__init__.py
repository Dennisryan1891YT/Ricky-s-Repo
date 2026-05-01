#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Netflix Add-on for Kodi
Streaming entertainment service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.netflix'
ADDON_NAME = 'Netflix'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()