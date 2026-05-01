#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Apple TV+ Add-on for Kodi
Apple streaming service
Original shows, movies, and documentaries
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
        {'label': 'Apple TV+ Originals', 'action': 'originals'},
        {'label': 'Movies', 'action': 'movies'},
        {'label': 'TV Shows', 'action': 'shows'},
        {'label': 'Up Next', 'action': 'upnext'},
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