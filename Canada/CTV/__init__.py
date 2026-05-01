#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CTV Add-on for Kodi
Canadian Television Network streaming
Live TV and on-demand content from CTV
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

CTV_API = "https://www.ctv.ca/api"
CTV_LIVE_URL = "https://www.ctv.ca/live"

def get_live_channels():
    """Fetch live CTV channels"""
    try:
        channels = [
            {'name': 'CTV', 'url': 'https://stream.ctv.ca/live/ctv'},
            {'name': 'CTV 2', 'url': 'https://stream.ctv.ca/live/ctv2'},
            {'name': 'CTV News', 'url': 'https://stream.ctv.ca/live/ctvnews'},
        ]
        return channels
    except Exception as e:
        xbmcgui.Dialog().notification('Error', f'Failed to load channels: {str(e)}')
        return []

def add_menu_items():
    """Add main menu items"""
    items = [
        {'label': 'Live TV', 'action': 'live'},
        {'label': 'On Demand', 'action': 'ondemand'},
        {'label': 'Search', 'action': 'search'},
    ]
    
    for item in items:
        url = f"{PLUGIN_URL}?action={item['action']}"
        xbmcplugin.addDirectoryItem(HANDLE, url, xbmcgui.ListItem(item['label']), True)
    
    xbmcplugin.endOfDirectory(HANDLE)

def show_live_channels():
    """Display live CTV channels"""
    channels = get_live_channels()
    
    for channel in channels:
        item = xbmcgui.ListItem(channel['name'])
        item.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(HANDLE, channel['url'], item, False)
    
    xbmcplugin.endOfDirectory(HANDLE)

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        add_menu_items()
    else:
        params = dict(item.split('=') for item in sys.argv[2][1:].split('&'))
        action = params.get('action')
        
        if action == 'live':
            show_live_channels()
        elif action == 'ondemand':
            xbmcgui.Dialog().notification('CTV', 'On Demand coming soon')
        elif action == 'search':
            xbmcgui.Dialog().notification('CTV', 'Search coming soon')
        else:
            add_menu_items()

if __name__ == '__main__':
    main()