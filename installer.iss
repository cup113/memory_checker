; Inno Setup script for Memory Checker
#define MyAppName "Memory Checker"
#define MyAppExeName "main.exe"

[Setup]
AppId={{208D1A1D-1D40-4F7A-9D05-16077BF9456F}}
AppName={#MyAppName}
AppVersion={#APP_VERSION}
DefaultDirName={autopf}\{#MyAppName}
DefaultGroupName={#MyAppName}
OutputDir=output
OutputBaseFilename=MemoryChecker-Setup-{#APP_VERSION}
SetupIconFile=favicon.ico
UninstallDisplayIcon={app}\favicon.ico
Compression=lzma
SolidCompression=yes

[Tasks]
Name: desktopicon; Description: "Create desktop shortcut"; GroupDescription: "Additional icons:"

[Files]
Source: "dist\main.dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "favicon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent
