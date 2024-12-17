import subprocess

def get_version():
    try:
        # Get the latest tag
        result = subprocess.run(['git', 'describe', '--tags', '--abbrev=0'], 
                              capture_output=True, text=True, check=True)
        version = result.stdout.strip()
        # Remove 'v' prefix if present
        if version.startswith('v'):
            version = version[1:]
        return version
    except subprocess.CalledProcessError:
        # Default version if no tag exists
        return '1.0.0'

def generate_version_info():
    version = get_version()
    # Split version into components (e.g., "1.0.1" -> [1, 0, 1, 0])
    version_parts = [int(x) for x in version.split('.') + ['0']]
    version_tuple = tuple(version_parts)

    version_info = f'''VSVersionInfo(
  ffi=FixedFileInfo(
    filevers={version_tuple},
    prodvers={version_tuple},
    mask=0x3f,
    flags=0x0,
    OS=0x40004,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo(
      [
        StringTable(
          u'040904B0',
          [StringStruct(u'CompanyName', u'Game File Duplicator'),
           StringStruct(u'FileDescription', u'Game File Duplicator Tool'),
           StringStruct(u'FileVersion', u'{version}'),
           StringStruct(u'InternalName', u'Game File Duplicator'),
           StringStruct(u'LegalCopyright', u'Copyright (c) 2024'),
           StringStruct(u'OriginalFilename', u'Game File Duplicator.exe'),
           StringStruct(u'ProductName', u'Game File Duplicator'),
           StringStruct(u'ProductVersion', u'{version}')])
      ]
    ),
    VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
  ]
)'''

    with open('file_version_info.txt', 'w') as f:
        f.write(version_info)

if __name__ == '__main__':
    generate_version_info()
