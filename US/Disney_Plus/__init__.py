#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Disney+ Add-on for Kodi
US streaming service
Disney, Pixar, Marvel, Star Wars, National Geographic
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
        {'label': 'Disney', 'action': 'disney'},
        {'label': 'Pixar', 'action': 'pixar'},
        {'label': 'Marvel', 'action': 'marvel'},
        {'label': 'Star Wars', 'action': 'starwars'},
        {'label': 'National Geographic', 'action': 'natgeo'},
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