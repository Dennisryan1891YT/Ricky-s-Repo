#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crave Add-on for Kodi
Canadian premium streaming service
Access HBO, Showtime, and exclusive content
"""

import sys
import xbmcplugin
import xbmcgui
import xbmcaddon
import requests

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
PLUGIN_URL = sys.argv[0]
HANDLE = int(sys.argv[1])

CRAVE_API = "https://api.crave.ca"

def add_menu_items():
    """Add main menu items"""
    items = [
        {'label': 'Featured', 'action': 'featured'},
        {'label': 'TV Shows', 'action': 'shows'},
        {'label': 'Movies', 'action': 'movies'},
        {'label': 'HBO Max', 'action': 'hbo'},
        {'label': 'Showtime', 'action': 'showtime'},
        {'label': 'Search', 'action': 'search'},
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
        params = dict(item.split('=') for item in sys.argv[2][1:].split('&') if '=' in item)
        action = params.get('action')
        
        if action:
            xbmcgui.Dialog().notification('Crave', 'Loading content...')
        else:
            add_menu_items()

if __name__ == '__main__':
    main()