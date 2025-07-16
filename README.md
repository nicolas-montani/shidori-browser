# Shidori Browser

A minimal web browser implementation in Python using Tkinter for the GUI. This project demonstrates the fundamental concepts of how web browsers work by implementing basic HTTP/HTTPS requests, HTML parsing, and text rendering.

## Features

- **HTTP/HTTPS Support**: Fetches web pages using HTTP and HTTPS protocols
- **File Protocol Support**: Can load local HTML files using the `file://` protocol
- **Basic HTML Parsing**: Strips HTML tags and displays plain text content
- **Scrollable Interface**: Navigate through content using arrow keys
- **Simple Text Layout**: Basic text rendering with line wrapping

## Requirements

- Python 3.11 or higher
- Tkinter (usually included with Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/nicolas-montani/shidori-browser.git
cd shidori-browser
```

2. Run the browser:
```bash
python3 shidori.py
```

## Usage

The browser currently loads a default page from `https://browser.engineering/examples/xiyouji.html`. To modify the URL, edit the last line in `shidori.py`:

```python
Browser().load(URL("your-url-here"))
```

### Supported URL Schemes

- `http://` - Standard HTTP requests
- `https://` - Secure HTTPS requests  
- `file://` - Local file access

### Controls

- **Down Arrow**: Scroll down
- **Up Arrow**: Scroll up

## Architecture

### Core Components

1. **URL Class**: Handles URL parsing and HTTP/HTTPS requests
   - Parses URLs into components (scheme, host, port, path)
   - Sends HTTP requests and processes responses
   - Supports both HTTP and HTTPS with SSL

2. **HTML Lexer**: Simple text extraction from HTML
   - Removes HTML tags and returns plain text content

3. **Layout Engine**: Basic text positioning
   - Arranges characters in a grid layout
   - Handles line wrapping

4. **Browser Class**: Main application window
   - Creates Tkinter GUI
   - Manages scrolling and rendering
   - Handles user input

## Technical Details

- **Window Size**: 800x600 pixels
- **Character Spacing**: 13px horizontal, 18px vertical
- **Scroll Step**: 100px per arrow key press
- **User Agent**: "Shidori-Browser/1.0"

## Limitations

- Only displays plain text (no images, CSS, or JavaScript)
- No interactive elements (links, forms, etc.)
- Basic error handling
- Single-threaded (blocking requests)
- No caching or history

## Educational Purpose

This browser is designed for educational purposes to demonstrate:
- HTTP protocol implementation
- Basic HTML parsing concepts
- GUI application development with Tkinter
- Network programming with sockets
- SSL/TLS handling

## Contributing

This is a learning project. Feel free to fork and experiment with additional features such as:
- Link navigation
- Basic CSS support
- Image rendering
- Bookmarks
- Multiple tabs

## License

This project is open source. Please check the repository for license details.

## Acknowledgments

Inspired by web browser engineering concepts and educational resources about how browsers work under the hood.
