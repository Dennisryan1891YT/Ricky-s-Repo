#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NFB Add-on for Kodi
National Film Board of Canada streaming
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.nfb'
ADDON_NAME = 'NFB'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()