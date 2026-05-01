#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
YouTube Add-on for Kodi
Video sharing platform - REQUIRES GOOGLE ACCOUNT
Watch, search, and subscribe to channels with Google login
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
YOUTUBE_API = "https://www.googleapis.com/youtube/v3"

CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"
CLIENT_SECRET = "YOUR_GOOGLE_CLIENT_SECRET"
REDIRECT_URI = "urn:ietf:wg:oauth:2.0:oob"

def load_google_token():
    """Load saved Google authentication token"""
    return ADDON.getSetting('google_token')

def save_google_token(token):
    """Save Google authentication token"""
    ADDON.setSetting('google_token', token)

def save_refresh_token(refresh_token):
    """Save Google refresh token"""
    ADDON.setSetting('google_refresh_token', refresh_token)

def load_refresh_token():
    """Load Google refresh token"""
    return ADDON.getSetting('google_refresh_token')

def show_google_login_dialog():
    """Show Google login dialog for YouTube authentication"""
    dialog = xbmcgui.Dialog()
    
    # Show information about Google login
    dialog.notification('YouTube', 'Opening Google Login...', time=3000)
    
    # Get authorization code from user
    keyboard = xbmc.Keyboard('', 'Enter Google Authorization Code (from browser)')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        auth_code = keyboard.getText()
        return authenticate_google_account(auth_code)
    
    return False

def authenticate_google_account(auth_code):
    """Authenticate with Google account using authorization code"""
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
                
                xbmcgui.Dialog().notification('YouTube', 'Google Login Successful!')
                return True
        else:
            xbmcgui.Dialog().notification('YouTube', 'Login Failed - Invalid code')
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
        ret = dialog.yesno('YouTube', 'You must sign in with your Google account.\nDo you want to sign in now?')
        
        if ret:
            return show_google_login_dialog()
        return False
    
    return True

def get_youtube_subscriptions():
    """Get user's YouTube subscriptions (requires authentication)"""
    token = load_google_token()
    
    if not token:
        return []
    
    try:
        headers = {'Authorization': f'Bearer {token}'}
        params = {
            'part': 'snippet',
            'mine': 'true',
            'maxResults': 50
        }
        
        response = requests.get(
            f"{YOUTUBE_API}/subscriptions",
            headers=headers,
            params=params,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json().get('items', [])
        elif response.status_code == 401:
            # Token expired, try to refresh
            if refresh_google_token():
                return get_youtube_subscriptions()
            else:
                ADDON.setSetting('google_token', '')
                xbmcgui.Dialog().notification('YouTube', 'Session expired. Please login again.')
    except Exception as e:
        xbmcgui.Dialog().notification('Error', f'Failed to load subscriptions: {str(e)}')
    
    return []

def show_settings_menu():
    """Show YouTube settings menu"""
    items = [
        {'label': 'Sign In / Sign Out', 'action': 'auth'},
        {'label': 'Account Settings', 'action': 'account'},
        {'label': 'Privacy Settings', 'action': 'privacy'},
    ]
    
    for item in items:
        url = f"{PLUGIN_URL}?action={item['action']}"
        xbmcplugin.addDirectoryItem(HANDLE, url, xbmcgui.ListItem(item['label']), True)
    
    xbmcplugin.endOfDirectory(HANDLE)

def add_menu_items():
    """Add main menu items"""
    if not check_google_authentication():
        xbmcgui.Dialog().notification('YouTube', 'Please sign in to continue')
        return
    
    items = [
        {'label': 'Trending', 'action': 'trending'},
        {'label': 'Subscriptions', 'action': 'subscriptions'},
        {'label': 'Watch Later', 'action': 'watchlater'},
        {'label': 'Your Uploads', 'action': 'uploads'},
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
        elif action == 'subscriptions':
            if check_google_authentication():
                subs = get_youtube_subscriptions()
                for sub in subs:
                    title = sub.get('snippet', {}).get('title', 'Unknown')
                    list_item = xbmcgui.ListItem(title)
                    xbmcplugin.addDirectoryItem(HANDLE, '', list_item, False)
                xbmcplugin.endOfDirectory(HANDLE)
        else:
            add_menu_items()

if __name__ == '__main__':
    main()