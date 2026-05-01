#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
HBO Max Add-on for Kodi
Warner Bros streaming service
HBO originals, movies, and exclusive content
"""

import sys
import xbmcplugin
import xbmcgui
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
PLUGIN_URL = sys.argv[0]
HANDLE = int(sys.argv[1])

def add_menu_items():
    """Add main menu items"""
    items = [
        {'label': 'Featured', 'action': 'featured'},
        {'label': 'HBO Max Originals', 'action': 'originals'},
        {'label': 'Movies', 'action': 'movies'},
        {'label': 'TV Shows', 'action': 'shows'},
        {'label': 'My List', 'action': 'mylist'},
    ]
    
    for item in items:
        url = f"{PLUGIN_URL}?action={item['action']}"
        xbmcplugin.addDirectoryItem(HANDLE, url, xbmcgui.ListItem(item['label']), True)
    
    xbmcplugin.endOfDirectory(HANDLE)

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        add_menu_items()
    else:
        add_menu_items()

if __name__ == '__main__':
    main()