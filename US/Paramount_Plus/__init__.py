#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Paramount+ Add-on for Kodi
Premium Paramount streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.paramount.plus'
ADDON_NAME = 'Paramount+'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()