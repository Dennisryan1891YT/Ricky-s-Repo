#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CBC Add-on for Kodi
Canadian Broadcasting Corporation streaming
Free access to CBC content
"""

import sys
import xbmcplugin
import xbmcgui
import xbmcaddon
import requests
from urllib.parse import urlencode

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
PLUGIN_URL = sys.argv[0]
HANDLE = int(sys.argv[1])

CBC_API = "https://www.cbc.ca/api"

def add_menu_items():
    """Add main menu items for CBC"""
    items = [
        {'label': 'CBC TV', 'action': 'cbc_tv'},
        {'label': 'CBC News', 'action': 'cbc_news'},
        {'label': 'Featured', 'action': 'featured'},
        {'label': 'Search', 'action': 'search'},
    ]
    
    for item in items:
        url = f"{PLUGIN_URL}?action={item['action']}"
        xbmcplugin.addDirectoryItem(HANDLE, url, xbmcgui.ListItem(item['label']), True)
    
    xbmcplugin.endOfDirectory(HANDLE)

def show_cbc_tv():
    """Display CBC TV shows"""
    shows = [
        {'title': 'The National', 'url': 'https://www.cbc.ca/watch/the-national'},
        {'title': 'Marketplace', 'url': 'https://www.cbc.ca/watch/marketplace'},
        {'title': 'Coronation Street', 'url': 'https://www.cbc.ca/watch/coronation-street'},
    ]
    
    for show in shows:
        item = xbmcgui.ListItem(show['title'])
        item.setProperty('IsPlayable', 'false')
        xbmcplugin.addDirectoryItem(HANDLE, show['url'], item, True)
    
    xbmcplugin.endOfDirectory(HANDLE)

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        add_menu_items()
    else:
        params = dict(item.split('=') for item in sys.argv[2][1:].split('&') if '=' in item)
        action = params.get('action')
        
        if action == 'cbc_tv':
            show_cbc_tv()
        elif action == 'cbc_news':
            xbmcgui.Dialog().notification('CBC', 'CBC News content loading...')
        elif action == 'featured':
            xbmcgui.Dialog().notification('CBC', 'Featured content')
        elif action == 'search':
            xbmcgui.Dialog().notification('CBC', 'Search feature')
        else:
            add_menu_items()

if __name__ == '__main__':
    main()