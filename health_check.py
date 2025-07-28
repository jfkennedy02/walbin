#!/usr/bin/env python3
"""
Health check script to verify the server is responding properly.
This can be used by deployment systems to verify the application is healthy.
"""

import requests
import sys
import os

def health_check():
    """Check if the server is responding to health checks."""
    port = os.environ.get('PORT', 5000)
    url = f"http://0.0.0.0:{port}/"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print("✓ Health check passed - Server is responding")
            return True
        else:
            print(f"✗ Health check failed - Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Health check failed - Error: {e}")
        return False

if __name__ == "__main__":
    if health_check():
        sys.exit(0)
    else:
        sys.exit(1)