#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ICI Tou.tv Add-on for Kodi
French-language Quebec streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.ici.toutv'
ADDON_NAME = 'ICI Tou.tv'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()