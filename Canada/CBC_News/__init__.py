#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
CBC News Add-on for Kodi
Live news streaming from CBC - REQUIRES AUTHENTICATION
Users must sign in with CBC account to watch live news
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

CBC_NEWS_API = "https://api.cbcnews.ca"

def load_auth_token():
    """Load authentication token"""
    return ADDON.getSetting('cbc_news_token')

def save_auth_token(token):
    """Save authentication token"""
    ADDON.setSetting('cbc_news_token', token)

def show_login_dialog():
    """Show login dialog for CBC News"""
    keyboard = xbmc.Keyboard('', 'Enter CBC Email')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        email = keyboard.getText()
        keyboard2 = xbmc.Keyboard('', 'Enter Password', hidden=True)
        keyboard2.doModal()
        
        if keyboard2.isConfirmed():
            password = keyboard2.getText()
            return authenticate_cbc(email, password)
    
    return False

def authenticate_cbc(email, password):
    """Authenticate with CBC service"""
    try:
        auth_data = {'email': email, 'password': password}
        response = requests.post(
            f"{CBC_NEWS_API}/auth/login",
            json=auth_data,
            timeout=10
        )
        
        if response.status_code == 200:
            token = response.json().get('token')
            if token:
                save_auth_token(token)
                xbmcgui.Dialog().notification('CBC News', 'Login Successful!')
                return True
        else:
            xbmcgui.Dialog().notification('CBC News', 'Login Failed')
    except Exception as e:
        xbmcgui.Dialog().notification('Error', f'Failed: {str(e)}')
    
    return False

def check_authentication():
    """Check if user is authenticated"""
    token = load_auth_token()
    
    if not token:
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('CBC News', 'You must sign in with your CBC account.\nDo you want to sign in now?')
        return ret and show_login_dialog()
    
    return True

def add_menu_items():
    """Add main menu items"""
    items = [
        {'label': 'Live News', 'action': 'live'},
        {'label': 'News Categories', 'action': 'categories'},
        {'label': 'Sign In', 'action': 'signin'},
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
        
        if action == 'signin':
            show_login_dialog()
        elif action == 'live':
            if check_authentication():
                xbmcgui.Dialog().notification('CBC News', 'Loading live news...')
        else:
            add_menu_items()

if __name__ == '__main__':
    main()