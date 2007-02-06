; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
AppName=Dabo Runtime Engine
AppVerName=DaboRun 0.7.2
AppPublisher=Ed Leafe
AppPublisherURL=http://dabodev.com
AppSupportURL=http://dabodev.com
AppUpdatesURL=http://dabodev.com/download
DefaultDirName={pf}\Dabo Runtime
DefaultGroupName=Dabo Runtime Engine
AllowNoIcons=yes
Compression=lzma
SolidCompression=yes
OutputBaseFilename=DaboRuntimeSetup
;OutputBaseFilename=DaboRuntimeSetupConsole

[Tasks]
Name: desktopicon; Description: {cm:CreateDesktopIcon}; GroupDescription: {cm:AdditionalIcons}
Name: quicklaunchicon; Description: {cm:CreateQuickLaunchIcon}; GroupDescription: {cm:AdditionalIcons}; Flags: unchecked

[Dirs]
Name: {app}\Common

[UninstallDelete]
Name: {app}\Common; Type: filesandordirs
Name: {app}\dabo\*; Type: filesandordirs
Name: {app}\demo\*; Type: filesandordirs
Name: {app}\ide\*; Type: filesandordirs

[Files]
Source: C:\projects\daborun\dist\daborun.exe; DestDir: {app}; Flags: ignoreversion
Source: C:\projects\daborun\dist\*; Excludes: Output\*, *.iss; DestDir: {app}; Flags: ignoreversion recursesubdirs
Source: C:\cleanprojects\dabo\*; DestDir: {app}\dabo; Flags: ignoreversion recursesubdirs
;Source: "C:\cleanprojects\dabo\icons\*.png"; DestDir: "{app}\dabo"; Flags: ignoreversion recursesubdirs
Source: C:\cleanprojects\demo\*; DestDir: {app}\demo; Flags: ignoreversion recursesubdirs; AfterInstall: LinkDemo
Source: C:\cleanprojects\ide\*; DestDir: {app}\ide; Flags: ignoreversion recursesubdirs; AfterInstall: LinkIDE
Source: C:\Python24\msvcr71.dll; DestDir: {app}; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files
Source: README.txt; DestDir: {app}; Flags: isreadme

[Icons]
Name: {group}\Dabo Runtime Engine; Filename: {app}\daborun.exe; IconFilename: {app}\dabo\icons\daboIcon.ico; Tasks: 
Name: {group}\{cm:UninstallProgram,Dabo Runtime Engine}; Filename: {uninstallexe}
Name: {userdesktop}\Dabo Runtime Engine; Filename: {app}\daborun.exe; Tasks: desktopicon
Name: {userappdata}\Microsoft\Internet Explorer\Quick Launch\Dabo Runtime Engine; Filename: {app}\daborun.exe; Tasks: quicklaunchicon

;;;; PrefEditors isn't working just right yet, so don't add the link
;	CreateShellLink(
;		ExpandConstant('{app}\Common\PrefEditor.lnk'),
;		'Shortcut to the Preference Editor program',
;		ExpandConstant('{app}\daborun.exe'),
;		ExpandConstant('"{app}\ide\PrefEditor.py"'),
;		ExpandConstant('{app}\ide'),
;		'',
;		0,
;		SW_SHOWNORMAL) ;

[Code]
procedure LinkDemo();
begin
	CreateShellLink(
		ExpandConstant('{app}\Common\SimpleFormWithBizobj.lnk'),
		'Shortcut to the SimpleFormWithBizobj demo',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\demo\SimpleFormWithBizobj.py"'),
		ExpandConstant('{app}\demo'),
		'',
		0,
		SW_SHOWNORMAL) ;

	CreateShellLink(
		ExpandConstant('{app}\Common\Dabo Demo.lnk'),
		'Shortcut to the DaboDemo program',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\demo\DaboDemo\DaboDemo.py"'),
		ExpandConstant('{app}\demo\DaboDemo'),
		'',
		0,
		SW_SHOWNORMAL) ;

	CreateShellLink(
		ExpandConstant('{app}\Common\Bubblet.lnk'),
		'Shortcut to the Bubblet game',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\demo\games\bubblet\main.py"'),
		ExpandConstant('{app}\demo\games\bubblet'),
		'',
		0,
		SW_SHOWNORMAL) ;

	CreateShellLink(
		ExpandConstant('{app}\Common\Montana.lnk'),
		'Shortcut to the Montana solitaire game',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\demo\games\montana.py"'),
		ExpandConstant('{app}\demo\games'),
		'',
		0,
		SW_SHOWNORMAL) ;

	CreateShellLink(
		ExpandConstant('{app}\Common\Sizer Tutorial.lnk'),
		'Shortcut to the sizer tutorial',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\demo\tutorial\sizerExample.py"'),
		ExpandConstant('{app}\demo\tutorial'),
		'',
		0,
		SW_SHOWNORMAL) ;

end ;

procedure LinkIDE();
begin
	CreateShellLink(
		ExpandConstant('{app}\Common\App Wizard.lnk'),
		'Shortcut to the Dabo Application Wizard',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\ide\wizards\AppWizard\AppWizard.py"'),
		ExpandConstant('{app}\ide\wizards\AppWizard'),
		'',
		0,
		SW_SHOWNORMAL) ;

	CreateShellLink(
		ExpandConstant('{app}\Common\Class Designer.lnk'),
		'Shortcut to the Dabo Class Designer',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\ide\ClassDesigner.py"'),
		ExpandConstant('{app}\ide'),
		'',
		0,
		SW_SHOWNORMAL) ;

	CreateShellLink(
		ExpandConstant('{app}\Common\Report Designer.lnk'),
		'Shortcut to the Dabo Report Designer',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\ide\ReportDesigner.py"'),
		ExpandConstant('{app}\ide'),
		'',
		0,
		SW_SHOWNORMAL) ;

	CreateShellLink(
		ExpandConstant('{app}\Common\Text Editor.lnk'),
		'Shortcut to the Dabo Editor',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\ide\Editor.py"'),
		ExpandConstant('{app}\ide'),
		'',
		0,
		SW_SHOWNORMAL) ;

	CreateShellLink(
		ExpandConstant('{app}\Common\Connection Editor.lnk'),
		'Shortcut to the Dabo Connection Editor',
		ExpandConstant('{app}\daborun.exe'),
		ExpandConstant('"{app}\ide\CxnEditor.py"'),
		ExpandConstant('{app}\ide'),
		'',
		0,
		SW_SHOWNORMAL) ;

 end ;
 

