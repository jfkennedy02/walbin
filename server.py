#!/usr/bin/env python3
"""
Simple HTTP server for serving static files.
This is the main entry point for deployment.
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

# Configuration
PORT = int(os.environ.get('PORT', 5000))
HOST = '0.0.0.0'

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='.', **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

def main():
    """Start the HTTP server."""
    httpd = None
    port_used = PORT
    
    try:
        # Try to bind to the preferred port, or find an available one
        for attempt_port in [PORT, PORT + 1, PORT + 2, 8000, 8080, 3000]:
            try:
                httpd = socketserver.TCPServer((HOST, attempt_port), CustomHTTPRequestHandler)
                port_used = attempt_port
                break
            except OSError as e:
                if e.errno == 98:  # Address already in use
                    continue
                else:
                    raise
        
        if httpd is None:
            print("Could not find an available port")
            sys.exit(1)
            
        print(f"Server running at http://{HOST}:{port_used}/")
        print("Press Ctrl+C to stop the server")
        httpd.serve_forever()
        
    except KeyboardInterrupt:
        print("\nServer stopped.")
        if httpd:
            httpd.shutdown()
        sys.exit(0)
    except Exception as e:
        print(f"Error starting server: {e}")
        if httpd:
            httpd.shutdown()
        sys.exit(1)

if __name__ == "__main__":
    main()