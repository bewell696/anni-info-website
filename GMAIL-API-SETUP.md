# Gmail API Setup Guide - bewell696@gmail.com

## 🎯 Quick Start

1. **Create Google Cloud Project**
2. **Enable Gmail API**
3. **Create OAuth Credentials**
4. **Configure CLI**
5. **Start Using**

## 📋 Step-by-Step Setup

### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click **"Create Project"**
3. Name it: `anni-info-dev`
4. Click **"Create"**

### Step 2: Enable Gmail API

1. In Google Cloud Console, go to **APIs & Services** → **Library**
2. Search for **"Gmail API"**
3. Click **Enable**

### Step 3: Create OAuth 2.0 Credentials

1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **OAuth client ID**
3. Select **Application type:** **Web application**
4. Name it: `Gmail CLI for ANNI-INFO`
5. Add authorized redirect URIs:
   - `http://localhost:8080`
   - `http://localhost:8080/callback`
6. Click **Create**
7. Copy the **Client ID** and **Client Secret**
8. Click **Download JSON** to save as `gmail-credentials.json`

### Step 4: Configure Gmail CLI

```bash
cd /Users/jagoda/models/hetyner1
python3 gmail-cli.py configure
```

This will:
- ✅ Launch browser for OAuth login
- ✅ Request Gmail read/write permissions
- ✅ Generate and save token to `gmail-token.json`

### Step 5: Test Connection

```bash
python3 gmail-cli.py test
```

This should show:
```
✅ Connection successful!
📧 Connected to: bewell696@gmail.com
👤 User ID: [your Gmail ID]
```

### Step 6: Start Using

```bash
# Check inbox
python3 gmail-cli.py inbox

# Search emails
python3 gmail-cli.py search --query "invoice" --limit 10

# Mark as read
python3 gmail-cli.py read
```

## 🔐 OAuth Permissions

The CLI will request these permissions:
- ✅ Read your Gmail messages
- ✅ Modify messages (mark as read, delete, archive)
- ✅ Manage your labels
- ✅ Access your profile information

## 📧 Test with Your Email

### Test Email Flow

1. Send yourself a test email to `bewell696@gmail.com`
2. Run: `python3 gmail-cli.py inbox`
3. You should see your test email appear

### Example Commands

```bash
# Get unread messages
python3 gmail-cli.py inbox

# Search for recent emails
python3 gmail-cli.py search --query "from:me" --limit 20

# Get email details
python3 gmail-cli.py get --id "email_id_here"

# Mark all unread as read
python3 gmail-cli.py read

# Delete specific email
python3 gmail-cli.py delete --id "email_id_here"
```

## 🔧 Advanced Configuration

### Custom Redirect URIs

If you need custom redirect URIs, update the OAuth client settings:

1. Go to **APIs & Services** → **Credentials**
2. Edit your OAuth client
3. Add new redirect URIs if needed

### Token Management

The token is automatically refreshed. To reset authentication:

```bash
# Remove old token
rm gmail-token.json

# Reconfigure
python3 gmail-cli.py configure
```

## 🚀 Integration with ANNI-INFO Website

### Webhook Integration

```bash
# Process contact form emails
python3 gmail-cli.py search --query "from:contact@anni-info.si" \
  --limit 10 \
  --webhook "https://anni-info.si/api/webhooks/contact"
```

### Invoice Processing

```bash
# Process invoices automatically
python3 gmail-cli.py search --query "subject:invoice" \
  --limit 50 \
  --webhook "https://anni-info.si/api/invoices"
```

## 📊 Available Commands

| Command | Description |
|---------|-------------|
| `python3 gmail-cli.py configure` | Setup OAuth authentication |
| `python3 gmail-cli.py test` | Test Gmail API connection |
| `python3 gmail-cli.py inbox` | Get unread messages from inbox |
| `python3 gmail-cli.py search` | Search emails with query |
| `python3 gmail-cli.py read` | Mark all unread as read |
| `python3 gmail-cli.py get --id <id>` | Get specific email details |
| `python3 gmail-cli.py delete --id <id>` | Delete specific email |

## 🐛 Troubleshooting

### Authentication Failed

```bash
# Reset and reconfigure
rm gmail-token.json
python3 gmail-cli.py configure
```

### Permission Denied

1. Make sure you accepted the OAuth permissions
2. Ensure your account has Gmail access
3. Check if any other OAuth sessions are active

### API Errors

```bash
# Test connection again
python3 gmail-cli.py test
```

### Rate Limit Errors

Gmail API has rate limits. Wait a few seconds between requests.

## 🔒 Security Best Practices

1. ✅ **Keep credentials secure**: Don't share `gmail-credentials.json`
2. ✅ **Delete old tokens**: Regularly rotate OAuth tokens
3. ✅ **Use OAuth**: Never store raw passwords
4. ✅ **Limit permissions**: Only request necessary Gmail access
5. ✅ **Monitor activity**: Regularly check Gmail activity

## 📝 Next Steps

1. ✅ **Configure Gmail API** - Complete OAuth setup
2. ✅ **Test Connection** - Verify API access
3. ✅ **Explore Commands** - Try different Gmail operations
4. ✅ **Integrate with Website** - Connect to ANNI-INFO website
5. ✅ **Set Up Automations** - Create development workflows

## 💡 Quick Reference

```bash
# Full setup workflow
python3 gmail-cli.py configure  # First time
python3 gmail-cli.py test        # Test connection
python3 gmail-cli.py inbox       # Check inbox
python3 gmail-cli.py search      # Search emails
```

---

**Email:** bewell696@gmail.com
**Project:** ANNI-INFO Development
**Status:** ✅ Ready for Setup