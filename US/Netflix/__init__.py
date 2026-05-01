#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Netflix Add-on for Kodi
US streaming service
Movies, TV shows, and documentaries
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
        {'label': 'TV Shows', 'action': 'shows'},
        {'label': 'Movies', 'action': 'movies'},
        {'label': 'My List', 'action': 'mylist'},
        {'label': 'New & Popular', 'action': 'trending'},
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