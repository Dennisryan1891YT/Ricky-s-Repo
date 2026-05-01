#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CBC Gem Add-on for Kodi
Premium CBC streaming service - REQUIRES AUTHENTICATION
Users must sign in with CBC Gem account to access content
"""

import sys
import xbmcplugin
import xbmcgui
import xbmcaddon
import requests
import json
from urllib.parse import urlencode

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
PLUGIN_URL = sys.argv[0]
HANDLE = int(sys.argv[1])

CBC_GEM_API = "https://api.gem.cbc.ca"
CBC_GEM_AUTH_URL = "https://www.cbcgem.ca/auth"

def load_auth_token():
    """Load saved authentication token from Kodi settings"""
    return ADDON.getSetting('cbc_gem_token')

def save_auth_token(token):
    """Save authentication token to Kodi settings"""
    ADDON.setSetting('cbc_gem_token', token)

def show_login_dialog():
    """Show CBC Gem login configuration dialog"""
    keyboard = xbmc.Keyboard('', 'Enter CBC Gem Email')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        email = keyboard.getText()
        
        keyboard2 = xbmc.Keyboard('', 'Enter CBC Gem Password', hidden=True)
        keyboard2.doModal()
        
        if keyboard2.isConfirmed():
            password = keyboard2.getText()
            return authenticate_cbc_gem(email, password)
    
    return False

def authenticate_cbc_gem(email, password):
    """Authenticate with CBC Gem service"""
    try:
        auth_data = {
            'email': email,
            'password': password,
            'deviceId': ADDON.getSetting('device_id') or 'kodi-device'
        }
        
        response = requests.post(
            f"{CBC_GEM_AUTH_URL}/login",
            json=auth_data,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            token = data.get('token')
            if token:
                save_auth_token(token)
                xbmcgui.Dialog().notification('CBC Gem', 'Login Successful!')
                return True
        else:
            xbmcgui.Dialog().notification('CBC Gem', 'Login Failed - Invalid credentials')
            return False
    except Exception as e:
        xbmcgui.Dialog().notification('Error', f'Authentication failed: {str(e)}')
        return False

def check_authentication():
    """Check if user is authenticated, show login if not"""
    token = load_auth_token()
    
    if not token:
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('CBC Gem', 'You must sign in with your CBC Gem account.\nDo you want to sign in now?')
        
        if ret:
            if show_login_dialog():
                return True
            else:
                return False
        return False
    return True

def get_gem_content():
    """Fetch CBC Gem content (requires authentication)"""
    token = load_auth_token()
    
    if not token:
        return []
    
    try:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(
            f"{CBC_GEM_API}/content",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json().get('items', [])
        elif response.status_code == 401:
            ADDON.setSetting('cbc_gem_token', '')
            xbmcgui.Dialog().notification('CBC Gem', 'Session expired. Please login again.')
            return []
    except Exception as e:
        xbmcgui.Dialog().notification('Error', f'Failed to load content: {str(e)}')
    
    return []

def show_settings_menu():
    """Show CBC Gem settings menu"""
    items = [
        {'label': 'Sign In / Sign Out', 'action': 'auth'},
        {'label': 'Account Settings', 'action': 'account'},
        {'label': 'Device Info', 'action': 'device'},
    ]
    
    for item in items:
        url = f"{PLUGIN_URL}?action={item['action']}"
        xbmcplugin.addDirectoryItem(HANDLE, url, xbmcgui.ListItem(item['label']), True)
    
    xbmcplugin.endOfDirectory(HANDLE)

def add_menu_items():
    """Add main menu items"""
    if not check_authentication():
        xbmcgui.Dialog().notification('CBC Gem', 'Please sign in to continue')
        return
    
    items = [
        {'label': 'Featured', 'action': 'featured'},
        {'label': 'Browse All Shows', 'action': 'shows'},
        {'label': 'Movies', 'action': 'movies'},
        {'label': 'My Watchlist', 'action': 'watchlist'},
        {'label': 'Settings', 'action': 'settings'},
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
        
        if action == 'auth':
            show_login_dialog()
        elif action == 'settings':
            show_settings_menu()
        elif action == 'featured':
            if check_authentication():
                content = get_gem_content()
                for item in content:
                    list_item = xbmcgui.ListItem(item.get('title', 'Unknown'))
                    xbmcplugin.addDirectoryItem(HANDLE, '', list_item, False)
                xbmcplugin.endOfDirectory(HANDLE)
        else:
            add_menu_items()

if __name__ == '__main__':
    main()