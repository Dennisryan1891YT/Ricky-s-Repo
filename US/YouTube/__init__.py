#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YouTube Add-on for Kodi
Video sharing platform
Watch, search, and subscribe to channels
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
        {'label': 'Trending', 'action': 'trending'},
        {'label': 'Subscriptions', 'action': 'subscriptions'},
        {'label': 'Watch Later', 'action': 'watchlater'},
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
        add_menu_items()

if __name__ == '__main__':
    main()