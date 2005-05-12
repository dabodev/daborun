; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
AppName=Dabo Runtime Engine
AppVerName=DaboRun 0.3.3
AppPublisher=Ed Leafe
AppPublisherURL=http://dabodev.com
AppSupportURL=http://dabodev.com
AppUpdatesURL=http://dabodev.com
DefaultDirName={pf}\Dabo Runtime
DefaultGroupName=Dabo Runtime Engine
AllowNoIcons=yes
Compression=lzma
SolidCompression=yes
OutputBaseFilename=DaboRuntimeSetup

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\projects\daborun\dist\daborun.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\projects\daborun\dist\*"; Excludes: "Output\*, *.iss"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "C:\cleanprojects\dabo\*"; DestDir: "{app}\dabo"; Flags: ignoreversion recursesubdirs
;Source: "C:\cleanprojects\dabo\icons\*.png"; DestDir: "{app}\dabo"; Flags: ignoreversion recursesubdirs
Source: "C:\cleanprojects\dabodemo\*"; DestDir: "{app}\demo"; Flags: ignoreversion recursesubdirs
Source: "C:\cleanprojects\daboide\*"; DestDir: "{app}\ide"; Flags: ignoreversion recursesubdirs
Source: "C:\Python24\msvcr71.dll"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\Dabo Runtime Engine"; Filename: "{app}\daborun.exe"
Name: "{group}\{cm:UninstallProgram,Dabo Runtime Engine}"; Filename: "{uninstallexe}"
Name: "{userdesktop}\Dabo Runtime Engine"; Filename: "{app}\daborun.exe"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\Dabo Runtime Engine"; Filename: "{app}\daborun.exe"; Tasks: quicklaunchicon

