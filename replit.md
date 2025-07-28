# replit.md

## Overview

Walbin is a cryptocurrency-themed landing page featuring "The Whale Robin Hood" concept. This is a static frontend-only website built with vanilla HTML, CSS, and JavaScript that promotes a community-focused cryptocurrency token. The site features a modern, whale-themed design with smooth animations, responsive layout, and social media integration.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

**Frontend-Only Static Website**
- Pure HTML/CSS/JavaScript implementation
- No backend services or database
- Client-side only functionality
- Static hosting compatible

The architecture follows a simple single-page application (SPA) pattern with:
- Semantic HTML structure
- CSS-based animations and responsive design
- Vanilla JavaScript for interactivity
- External CDN dependencies for fonts and icons

## Key Components

### 1. HTML Structure (index.html)
- Semantic HTML5 layout
- Navigation bar with smooth scroll links
- Hero section with animated background
- Sections for About, Tokenomics, and Community
- Meta tags for SEO optimization

### 2. Styling System (styles.css)
- CSS custom properties for theming
- Responsive design with mobile-first approach
- CSS animations and transitions
- Gradient text effects and wave animations
- Modern glassmorphism effects with backdrop-filter

### 3. Interactive Features (script.js)
- Smooth scrolling navigation
- Dynamic navbar styling on scroll
- Contract address copying functionality
- Toast notifications
- Mobile-responsive interactions

### 4. External Dependencies
- Font Awesome 6.0.0 for icons
- Google Fonts (Fredoka One, Poppins)
- All loaded via CDN

## Data Flow

**Static Content Flow:**
1. User loads the page
2. External fonts and icons load from CDNs
3. JavaScript initializes event listeners
4. User interactions trigger smooth scrolling and UI updates
5. Contract address copying uses browser clipboard API

**No server-side data processing** - all functionality is client-side.

## External Dependencies

### CDN Services
- **Font Awesome**: Icon library for UI elements
- **Google Fonts**: Typography (Fredoka One for headings, Poppins for body text)

### Browser APIs
- **Clipboard API**: For copying contract addresses
- **Scroll API**: For smooth scrolling navigation
- **Intersection Observer** (potential future use for scroll animations)

### Social Media Integration
- Telegram links for community access
- External links to social platforms

## Deployment Strategy

**Updated for Replit Deployment:**
- Custom Python HTTP server (server.py) serves static files
- Procfile configured for web deployment
- Health check endpoint responds on / route
- Proper CORS headers for cross-origin requests

**Deployment Requirements:**
- Python 3.11+ environment
- server.py as main entry point
- Health checks on root endpoint (/)
- Port 5000 for HTTP server

**Files Added for Deployment:**
- server.py: Custom HTTP server with proper headers
- Procfile: Deployment configuration
- health_check.py: Health verification script

**Performance Considerations:**
- Optimized for fast loading with minimal dependencies
- CSS and JavaScript are minification-ready
- Images should be optimized before deployment
- CDN usage reduces bundle size

The site is designed to be lightweight, fast-loading, and easily maintainable while providing an engaging user experience for cryptocurrency community building.