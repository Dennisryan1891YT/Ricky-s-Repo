#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YouTube TV Add-on for Kodi
Live TV streaming service - REQUIRES GOOGLE ACCOUNT
Watch live TV channels with Google account authentication
"""

import sys
import xbmcplugin
import xbmcgui
import xbmcaddon
import requests
import json

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
ADDON_NAME = ADDON.getAddonInfo('name')
PLUGIN_URL = sys.argv[0]
HANDLE = int(sys.argv[1])

GOOGLE_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
GOOGLE_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"
YOUTUBE_TV_API = "https://www.googleapis.com/youtubetv/v1"

CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"
CLIENT_SECRET = "YOUR_GOOGLE_CLIENT_SECRET"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

def load_google_token():
    """Load saved Google authentication token"""
    return ADDON.getSetting('google_tv_token')

def save_google_token(token):
    """Save Google authentication token"""
    ADDON.setSetting('google_tv_token', token)

def save_refresh_token(refresh_token):
    """Save Google refresh token"""
    ADDON.setSetting('google_tv_refresh_token', refresh_token)

def load_refresh_token():
    """Load Google refresh token"""
    return ADDON.getSetting('google_tv_refresh_token')

def show_google_login_dialog():
    """Show Google login dialog for YouTube TV authentication"""
    dialog = xbmcgui.Dialog()
    
    # Show information about Google login
    dialog.notification('YouTube TV', 'Opening Google Login...', time=3000)
    
    # Get authorization code from user
    keyboard = xbmc.Keyboard('', 'Enter Google Authorization Code (from browser)')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        auth_code = keyboard.getText()
        return authenticate_google_account(auth_code)
    
    return False

def authenticate_google_account(auth_code):
    """Authenticate with Google account for YouTube TV"""
    try:
        # Exchange auth code for tokens
        token_data = {
            'code': auth_code,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'redirect_uri': REDIRECT_URI,
            'grant_type': 'authorization_code'
        }
        
        response = requests.post(
            GOOGLE_TOKEN_URL,
            data=token_data,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            access_token = data.get('access_token')
            refresh_token = data.get('refresh_token')
            
            if access_token:
                save_google_token(access_token)
                if refresh_token:
                    save_refresh_token(refresh_token)
                
                xbmcgui.Dialog().notification('YouTube TV', 'Google Login Successful!')
                return True
        else:
            xbmcgui.Dialog().notification('YouTube TV', 'Login Failed - Invalid code')
            return False
    except Exception as e:
        xbmcgui.Dialog().notification('Error', f'Authentication failed: {str(e)}')
        return False

def refresh_google_token():
    """Refresh expired Google access token"""
    refresh_token = load_refresh_token()
    
    if not refresh_token:
        return False
    
    try:
        token_data = {
            'refresh_token': refresh_token,
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
            'grant_type': 'refresh_token'
        }
        
        response = requests.post(
            GOOGLE_TOKEN_URL,
            data=token_data,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            access_token = data.get('access_token')
            if access_token:
                save_google_token(access_token)
                return True
    except Exception as e:
        pass
    
    return False

def check_google_authentication():
    """Check if user is authenticated with Google account"""
    token = load_google_token()
    
    if not token:
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('YouTube TV', 'You must sign in with your Google account.\nDo you want to sign in now?')
        
        if ret:
            return show_google_login_dialog()
        return False
    
    return True

def get_live_channels():
    """Get live TV channels (requires authentication)"""
    token = load_google_token()
    
    if not token:
        return []
    
    try:
        headers = {'Authorization': f'Bearer {token}'}
        params = {
            'part': 'snippet',
            'maxResults': 100
        }
        
        response = requests.get(
            f"{YOUTUBE_TV_API}/channels",
            headers=headers,
            params=params,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json().get('items', [])
        elif response.status_code == 401:
            # Token expired, try to refresh
            if refresh_google_token():
                return get_live_channels()
            else:
                ADDON.setSetting('google_tv_token', '')
                xbmcgui.Dialog().notification('YouTube TV', 'Session expired. Please login again.')
    except Exception as e:
        xbmcgui.Dialog().notification('Error', f'Failed to load channels: {str(e)}')
    
    return []

def get_epg_guide():
    """Get electronic program guide"""
    token = load_google_token()
    
    if not token:
        return []
    
    try:
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.get(
            f"{YOUTUBE_TV_API}/epg",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json().get('programs', [])
    except Exception as e:
        pass
    
    return []

def show_settings_menu():
    """Show YouTube TV settings menu"""
    items = [
        {'label': 'Sign In / Sign Out', 'action': 'auth'},
        {'label': 'Account Settings', 'action': 'account'},
        {'label': 'DVR Settings', 'action': 'dvr'},
        {'label': 'Parental Controls', 'action': 'parental'},
    ]
    
    for item in items:
        url = f"{PLUGIN_URL}?action={item['action']}"
        xbmcplugin.addDirectoryItem(HANDLE, url, xbmcgui.ListItem(item['label']), True)
    
    xbmcplugin.endOfDirectory(HANDLE)

def add_menu_items():
    """Add main menu items"""
    if not check_google_authentication():
        xbmcgui.Dialog().notification('YouTube TV', 'Please sign in to continue')
        return
    
    items = [
        {'label': 'Live TV', 'action': 'live'},
        {'label': 'Guide', 'action': 'guide'},
        {'label': 'Recorded Shows', 'action': 'recorded'},
        {'label': 'Favorites', 'action': 'favorites'},
        {'label': 'Search', 'action': 'search'},
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
            show_google_login_dialog()
        elif action == 'settings':
            show_settings_menu()
        elif action == 'live':
            if check_google_authentication():
                channels = get_live_channels()
                for channel in channels:
                    title = channel.get('snippet', {}).get('title', 'Unknown')
                    list_item = xbmcgui.ListItem(title)
                    list_item.setProperty('IsPlayable', 'true')
                    xbmcplugin.addDirectoryItem(HANDLE, '', list_item, False)
                xbmcplugin.endOfDirectory(HANDLE)
        elif action == 'guide':
            if check_google_authentication():
                programs = get_epg_guide()
                xbmcgui.Dialog().notification('YouTube TV', f'Loading {len(programs)} programs...')
        else:
            add_menu_items()

if __name__ == '__main__':
    main()