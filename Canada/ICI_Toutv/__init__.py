#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ICI Tou.tv Add-on for Kodi
French-language Quebec streaming - REQUIRES AUTHENTICATION
Users must sign in with Tou.tv account to access content
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

TOUTV_API = "https://api.tou.tv"
TOUTV_AUTH = "https://www.tou.tv/auth"

def load_auth_token():
    """Load authentication token"""
    return ADDON.getSetting('toutv_token')

def save_auth_token(token):
    """Save authentication token"""
    ADDON.setSetting('toutv_token', token)

def show_login_dialog():
    """Show login dialog for Tou.tv"""
    keyboard = xbmc.Keyboard('', 'Entrez votre email Tou.tv')
    keyboard.doModal()
    
    if keyboard.isConfirmed():
        email = keyboard.getText()
        keyboard2 = xbmc.Keyboard('', 'Entrez votre mot de passe', hidden=True)
        keyboard2.doModal()
        
        if keyboard2.isConfirmed():
            password = keyboard2.getText()
            return authenticate_toutv(email, password)
    
    return False

def authenticate_toutv(email, password):
    """Authenticate with Tou.tv service"""
    try:
        auth_data = {'email': email, 'password': password}
        response = requests.post(
            f"{TOUTV_AUTH}/login",
            json=auth_data,
            timeout=10
        )
        
        if response.status_code == 200:
            token = response.json().get('token')
            if token:
                save_auth_token(token)
                xbmcgui.Dialog().notification('ICI Tou.tv', 'Connexion réussie!')
                return True
        else:
            xbmcgui.Dialog().notification('ICI Tou.tv', 'Connexion échouée')
    except Exception as e:
        xbmcgui.Dialog().notification('Erreur', f'Échoué: {str(e)}')
    
    return False

def check_authentication():
    """Check if user is authenticated"""
    token = load_auth_token()
    
    if not token:
        dialog = xbmcgui.Dialog()
        ret = dialog.yesno('ICI Tou.tv', 'Vous devez vous connecter avec votre compte Tou.tv.\nVoulez-vous vous connecter maintenant?')
        return ret and show_login_dialog()
    
    return True

def add_menu_items():
    """Add main menu items"""
    items = [
        {'label': 'Contenu en vedette', 'action': 'featured'},
        {'label': 'Tous les shows', 'action': 'shows'},
        {'label': 'Films', 'action': 'movies'},
        {'label': 'Connexion', 'action': 'signin'},
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
        elif action == 'featured':
            if check_authentication():
                xbmcgui.Dialog().notification('ICI Tou.tv', 'Chargement du contenu...')
        else:
            add_menu_items()

if __name__ == '__main__':
    main()