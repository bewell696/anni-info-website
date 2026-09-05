#!/bin/bash
# Gmail CLI Setup Script for ANNI-INFO Development

echo "🚀 Setting up Gmail CLI for development..."
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10+"
    exit 1
fi

echo "✅ Python version: $(python3 --version)"
echo ""

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed"
    exit 1
fi

echo "✅ pip3 version: $(pip3 --version)"
echo ""

# Install dependencies
echo "📦 Installing required Python packages..."
pip3 install google-api-python-client google-auth-oauthlib google-auth-httplib2 click
echo ""

# Check for credentials file
if [ ! -f "gmail-credentials.json" ]; then
    echo "⚠️  Google credentials file (gmail-credentials.json) not found"
    echo ""
    echo "📋 Setup steps:"
    echo "1. Go to https://console.cloud.google.com/"
    echo "2. Create a new project: anni-info-dev"
    echo "3. Enable Gmail API"
    echo "4. Create OAuth 2.0 credentials"
    echo "5. Download credentials.json to this directory"
    echo ""
    echo "⚠️  First time use: Run 'python3 gmail-cli.py configure'"
else
    echo "✅ Found gmail-credentials.json"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "🚀 Quick start:"
echo "   python3 gmail-cli.py configure    # First time setup"
echo "   python3 gmail-cli.py test          # Test connection"
echo "   python3 gmail-cli.py inbox         # Check inbox"
echo "   python3 gmail-cli.py search        # Search emails"
echo ""
echo "💡 For CLI usage: pip install click"
echo "   cli gmail configure"