#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HBO Max Add-on for Kodi
Premium HBO streaming service
"""

import xbmcplugin
import xbmcgui
import sys

# Add-on metadata
ADDON_ID = 'plugin.video.hbo.max'
ADDON_NAME = 'HBO Max'

def main():
    """Main entry point for the add-on"""
    xbmcplugin.endOfDirectory(int(sys.argv[1]))

if __name__ == '__main__':
    main()