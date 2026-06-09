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
PrivilegesRequired=lowest

[Tasks]
Name: desktopicon; Description: "Create desktop shortcut"; GroupDescription: "Additional icons:"
Name: autostart; Description: "Start with Windows"; GroupDescription: "Startup options:"

[Files]
Source: "dist\main.dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "favicon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Registry]
Root: HKCU; Subkey: "Software\Microsoft\Windows\CurrentVersion\Run"; ValueType: string; ValueName: "{#MyAppName}"; ValueData: "{app}\{#MyAppExeName}"; Tasks: autostart

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "Launch {#MyAppName}"; Flags: nowait postinstall skipifsilent
