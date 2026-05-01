#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
NFB Add-on for Kodi
National Film Board of Canada
Free documentaries and independent films
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

NFB_API = "https://api.nfb.ca"

def get_films():
    """Get films from NFB"""
    try:
        response = requests.get(f"{NFB_API}/films", timeout=10)
        if response.status_code == 200:
            return response.json().get('films', [])
    except:
        pass
    return []

def add_menu_items():
    """Add main menu items"""
    items = [
        {'label': 'Latest Films', 'action': 'latest'},
        {'label': 'Documentaries', 'action': 'documentaries'},
        {'label': 'By Genre', 'action': 'genres'},
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