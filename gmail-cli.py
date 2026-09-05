#!/usr/bin/env python3
"""
Gmail CLI - Development Integration for ANNI-INFO
A powerful CLI tool for Gmail management and automation
"""

import click
import os
import json
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

try:
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload
except ImportError as e:
    print(f"Error: Missing required dependencies: {e}")
    print("Install with: pip install google-api-python-client google-auth-oauthlib google-auth-httplib2 click")
    sys.exit(1)

# Default credentials file path
CREDENTIALS_FILE = "gmail-credentials.json"
TOKEN_FILE = "gmail-token.json"
SCOPES = ['https://www.googleapis.com/auth/gmail.modify', 'https://www.googleapis.com/auth/gmail.readonly']

@click.group()
@click.version_option(version='1.0.0')
def gmail():
    """Gmail CLI for development automation and integration"""
    pass

@gmail.command()
def configure():
    """Setup Gmail API OAuth authentication"""
    click.echo("📝 Setting up Gmail API OAuth...")
    
    if not os.path.exists(CREDENTIALS_FILE):
        click.echo(f"❌ Error: {CREDENTIALS_FILE} not found!")
        click.echo("Please create OAuth 2.0 credentials in Google Cloud Console")
        click.echo("1. Go to https://console.cloud.google.com/")
        click.echo("2. Create a new project: anni-info-dev")
        click.echo("3. Enable Gmail API")
        click.echo("4. Create OAuth 2.0 credentials")
        click.echo("5. Download credentials.json to this directory")
        sys.exit(1)
    
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
    creds = flow.run_local_server(port=0)
    
    with open(TOKEN_FILE, 'w') as token:
        token.write(creds.to_json())
    
    click.echo("✅ Authentication successful! Token saved to gmail-token.json")

@gmail.command()
def test():
    """Test Gmail API connection"""
    if not os.path.exists(TOKEN_FILE):
        click.echo("❌ Error: No authentication token found!")
        click.echo("Run 'cli gmail configure' first")
        sys.exit(1)
    
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        
        # Test API call
        user_profile = service.users().getProfile(userId='me').execute()
        email = user_profile['emailAddress']
        
        click.echo(f"✅ Connection successful!")
        click.echo(f"📧 Connected to: {email}")
        click.echo(f"👤 User ID: {user_profile['id']}")
        
    except HttpError as error:
        click.echo(f"❌ API Error: {error}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"❌ Error: {e}")
        sys.exit(1)

@gmail.command()
def inbox():
    """Get unread emails from inbox"""
    if not os.path.exists(TOKEN_FILE):
        click.echo("❌ Error: No authentication token found!")
        sys.exit(1)
    
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        
        # Get unread messages
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=10).execute()
        messages = results.get('messages', [])
        
        if not messages:
            click.echo("📭 No unread messages found")
            return
        
        click.echo(f"📬 Unread messages in inbox: {len(messages)}\n")
        
        for msg in messages:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
            headers = msg_data['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
            
            click.echo(f"📨 Message: {subject}")
            click.echo(f"   From: {sender}")
            click.echo(f"   ID: {msg['id']}")
            click.echo("-" * 50)
    
    except HttpError as error:
        click.echo(f"❌ API Error: {error}")
        sys.exit(1)

@gmail.command()
@click.option('--query', default='', help='Search query')
@click.option('--limit', default=50, help='Maximum results')
def search(query, limit):
    """Search Gmail with custom query"""
    if not os.path.exists(TOKEN_FILE):
        click.echo("❌ Error: No authentication token found!")
        sys.exit(1)
    
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        
        results = service.users().messages().list(
            userId='me', 
            q=query, 
            maxResults=limit
        ).execute()
        
        messages = results.get('messages', [])
        
        if not messages:
            click.echo(f"📭 No results found for query: {query}")
            return
        
        click.echo(f"🔍 Found {len(messages)} messages for query: {query}\n")
        
        for msg in messages[:10]:
            msg_data = service.users().messages().get(userId='me', id=msg['id'], format='metadata').execute()
            headers = msg_data['payload']['headers']
            subject = next((h['value'] for h in headers if h['name'] == 'Subject'), 'No Subject')
            sender = next((h['value'] for h in headers if h['name'] == 'From'), 'Unknown')
            
            click.echo(f"📨 {subject}")
            click.echo(f"   From: {sender}")
            click.echo(f"   ID: {msg['id']}")
            click.echo("-" * 50)
    
    except HttpError as error:
        click.echo(f"❌ API Error: {error}")
        sys.exit(1)

@gmail.command()
@click.argument('email_id')
def get(email_id):
    """Get details of specific email"""
    if not os.path.exists(TOKEN_FILE):
        click.echo("❌ Error: No authentication token found!")
        sys.exit(1)
    
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        
        msg_data = service.users().messages().get(userId='me', id=email_id, format='full').execute()
        
        click.echo(json.dumps(msg_data, indent=2))
    
    except HttpError as error:
        click.echo(f"❌ API Error: {error}")
        sys.exit(1)

@gmail.command()
@click.option('--all', is_flag=True, help='Read all messages')
def read(all):
    """Mark messages as read"""
    if not os.path.exists(TOKEN_FILE):
        click.echo("❌ Error: No authentication token found!")
        sys.exit(1)
    
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        
        # Get unread messages
        results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=50).execute()
        messages = results.get('messages', [])
        
        if not messages:
            click.echo("📭 No messages to mark as read")
            return
        
        unread_count = 0
        for msg in messages:
            service.users().messages().modify(userId='me', id=msg['id'], body={'removeLabelIds': ['UNREAD']}).execute()
            unread_count += 1
        
        click.echo(f"✅ Marked {unread_count} messages as read")
    
    except HttpError as error:
        click.echo(f"❌ API Error: {error}")
        sys.exit(1)

@gmail.command()
@click.option('--id', required=True, help='Email ID to delete')
def delete(email_id):
    """Delete specific email"""
    if not os.path.exists(TOKEN_FILE):
        click.echo("❌ Error: No authentication token found!")
        sys.exit(1)
    
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        
        service.users().messages().trash(userId='me', id=email_id).execute()
        click.echo(f"✅ Deleted email: {email_id}")
    
    except HttpError as error:
        click.echo(f"❌ API Error: {error}")
        sys.exit(1)

@gmail.command()
@click.option('--limit', default=5, help='Number of stats to show')
def stats(limit):
    """Get Gmail statistics"""
    if not os.path.exists(TOKEN_FILE):
        click.echo("❌ Error: No authentication token found!")
        sys.exit(1)
    
    try:
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        service = build('gmail', 'v1', credentials=creds)
        
        # Get unread count
        results = service.users().labels().list(userId='me').execute()
        labels = {label['id']: label['name'] for label in results.get('labels', [])}
        
        unread_count = service.users().labels().get(userId='me', id='UNREAD').execute()['messagesTotal']
        inbox_count = service.users().labels().get(userId='me', id='INBOX').execute()['messagesTotal']
        
        click.echo("📊 Gmail Statistics")
        click.echo("=" * 50)
        click.echo(f"📧 Unread Messages: {unread_count}")
        click.echo(f"📥 Inbox Messages: {inbox_count}")
        click.echo(f"🏷️  Total Labels: {len(labels)}")
        
    except HttpError as error:
        click.echo(f"❌ API Error: {error}")
        sys.exit(1)

if __name__ == '__main__':
    gmail()