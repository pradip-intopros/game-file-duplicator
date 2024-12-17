# Game File Duplicator

A desktop application for duplicating and renaming game files with prefix changes.

## Features
- Easy-to-use graphical interface
- File and folder selection dialogs
- Automatic file duplication with prefix renaming
- Support for prefab and TypeScript files

## Download
Download the latest release from the [Releases](../../releases) page.

## Development
To build from source:

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python duplicate_ui.py
   ```

## Building
To build the executable:
```bash
pyinstaller duplicate_app.spec
```

## Versioning
Version information is stored in `.version` file. Current version: 1.0.0
