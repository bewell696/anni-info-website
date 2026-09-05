# Gmail CLI - Development Integration

A powerful CLI tool for Gmail management and automation, integrated with your ANNI-INFO development workflow.

## 🎯 Purpose

This Gmail CLI enables:
- ✅ Automated email processing for development workflows
- ✅ Gmail API integration with your development tools
- ✅ Email management directly from terminal
- ✅ Webhook integration with your website
- ✅ Email content analysis and processing

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Using setup script
bash setup-gmail.sh

# Or manually
pip3 install -r gmail-cli-requirements.txt
```

### 2. Configure Gmail API

```bash
python3 gmail-cli.py configure
```

This will:
1. Request OAuth 2.0 access
2. Set up authentication
3. Save token to `gmail-token.json`

### 3. Test Connection

```bash
python3 gmail-cli.py test
```

### 4. Start Using

```bash
# Check inbox
python3 gmail-cli.py inbox

# Search emails
python3 gmail-cli.py search --query "invoice" --limit 10

# Mark as read
python3 gmail-cli.py read

# Get specific email
python3 gmail-cli.py get --id "email_id_here"
```

## 📦 Features

### Email Management
- ✅ Check unread messages
- ✅ Search emails with custom queries
- ✅ Mark messages as read/unread
- ✅ Delete/archive emails
- ✅ Get email details

### Statistics
- ✅ Get inbox statistics
- ✅ Track unread counts
- ✅ Label management
- ✅ Activity monitoring

### Integration Ready
- ✅ Webhook support
- ✅ JSON output format
- ✅ Email content parsing
- ✅ Attachment handling
- ✅ Developer-friendly API

## 🔧 Installation

### Prerequisites
- Python 3.10+
- pip package manager
- Gmail account (bewell696@gmail.com)
- Google Cloud Console access

### Setup Commands

```bash
# 1. Navigate to project directory
cd /Users/jagoda/models/hetyner1

# 2. Make setup script executable
chmod +x setup-gmail.sh

# 3. Run setup
bash setup-gmail.sh

# 4. Configure Gmail API
python3 gmail-cli.py configure

# 5. Test connection
python3 gmail-cli.py test
```

## 📋 Available Commands

### Basic Commands
- `python3 gmail-cli.py configure` - Setup OAuth authentication
- `python3 gmail-cli.py test` - Test Gmail API connection
- `python3 gmail-cli.py inbox` - Get unread messages
- `python3 gmail-cli.py read` - Mark all unread as read
- `python3 gmail-cli.py delete --id <email_id>` - Delete specific email

### Search Commands
- `python3 gmail-cli.py search --query "text" --limit 50` - Search emails
- `python3 gmail-cli.py search --query "from:anni-info" --limit 100` - Filter by sender

### Detail Commands
- `python3 gmail-cli.py get --id <email_id>` - Get full email details in JSON

### Stats Commands
- `python3 gmail-cli.py stats` - Get Gmail statistics

## 🔌 Integration Examples

### With Your ANNI-INFO Website

```bash
# Webhook integration for contact form
python3 gmail-cli.py search --query "from:contact-form@anni-info.si" \
  --limit 10 \
  --webhook "https://anni-info.si/api/webhooks/contact"
```

### Automated Processing

```bash
# Process new invoices automatically
python3 gmail-cli.py search --query "subject:invoice" --limit 100
```

### Development Workflows

```bash
# Monitor important emails
python3 gmail-cli.py search --query "from:github.com" --limit 50
```

## 🔐 Security

- **OAuth 2.0 Authentication**: Secure authentication without sharing passwords
- **Token Management**: Local token storage
- **Minimal Permissions**: Only requested necessary Gmail access
- **Secure Storage**: Credentials stored locally

## 📝 Configuration Files

- `gmail-credentials.json` - OAuth credentials (from Google Cloud Console)
- `gmail-token.json` - Session token (auto-generated)
- `.env` - Optional environment variables

## 🎨 Advanced Usage

### Webhook Integration

```bash
# Trigger webhook when new email arrives
python3 gmail-cli.py search --query "subject:urgent" --webhook "https://api.example.com/webhook"
```

### Email Processing Pipeline

```bash
# Get unread emails
python3 gmail-cli.py inbox | while read email_id; do
  # Process each email
  python3 gmail-cli.py get --id "$email_id" | python3 process.py
done
```

### Bulk Operations

```bash
# Archive old emails
python3 gmail-cli.py search --query "after:2023-01-01" --limit 500
# Then archive via API
```

## 🐛 Troubleshooting

### Authentication Issues

```bash
# Reset authentication
rm gmail-token.json
python3 gmail-cli.py configure
```

### API Rate Limits

- Gmail API has rate limits
- Use batching for large operations
- Implement retry logic for failed requests

### Python Dependencies

```bash
# Reinstall dependencies
pip3 install --upgrade google-api-python-client google-auth-oauthlib google-auth-httplib2 click
```

## 📚 API Documentation

- [Gmail API Reference](https://developers.google.com/gmail/api)
- [Google API Python Client](https://github.com/googleapis/google-api-python-client)
- [OAuth 2.0 Setup Guide](https://developers.google.com/identity/protocols/oauth2)

## 🚀 Next Steps

1. ✅ **Configure Gmail API** - Complete OAuth setup
2. ✅ **Test Connection** - Verify API access
3. ✅ **Explore Commands** - Try different Gmail operations
4. ✅ **Integrate with Website** - Connect to ANNI-INFO website
5. ✅ **Set Up Automations** - Create development workflows

## 💡 Integration Ideas

### Invoice Processing
```bash
python3 gmail-cli.py search --query "subject:invoice" --limit 100 --webhook "https://anni-info.si/api/invoices"
```

### Support Ticket System
```bash
python3 gmail-cli.py search --query "from:support@anni-info.si" --limit 50
```

### Development Notifications
```bash
python3 gmail-cli.py search --query "from:github.com/anni-info" --limit 20
```

## 📞 Support

For issues or questions:
- Check error messages for specific issues
- Verify Gmail API configuration
- Ensure all dependencies are installed
- Test with smaller email volumes first

## 🎯 Best Practices

1. **Rate Limiting**: Don't make too many requests in quick succession
2. **Error Handling**: Implement retry logic for failed requests
3. **Token Management**: Keep tokens secure and rotate them periodically
4. **Logging**: Enable detailed logging for debugging
5. **Backup**: Regularly backup important email data

---

**Email:** bewell696@gmail.com
**Project:** ANNI-INFO Development
**Version:** 1.0.0
**Status:** ✅ Ready to Use