@ECHO off

SET THISDIR=%~dp0
SET SITE_PACKAGES=%THISDIR%\maya\site-packages

REM Mayaバージョン
SET MAYAVER=2018

REM Environment
SET MAYA_SCRIPT_PATH=%THISDIR%\maya\scripts;%MAYA_SCRIPT_PATH%
SET MAYA_PLUG_IN_PATH=%THISDIR%\maya\plug-ins\%MAYAVER%;%MAYA_PLUG_IN_PATH%
SET PYTHONPATH=%THISDIR%\maya\python;%THISDIR%\library\python;%SITE_PACKAGES%;%PYTHONPATH%
SET XBMLANGPATH=%THISDIR%\maya\icon;%XBMLANGPATH%

REM 英語設定
REM SET MAYA_UI_LANGUAGE=en_US

REM Mayaを直接起動
SET MAYA_EXE=%PROGRAMFILES%\Autodesk\Maya%MAYAVER%\bin\maya.exe
IF EXIST "%MAYA_EXE%" (
    START "launch" "%MAYA_EXE%"
    EXIT /b 0
)

ECHO Mayaが見つかりません。インストールおよびプラグインのセットアップを行なってください。
PAUSE