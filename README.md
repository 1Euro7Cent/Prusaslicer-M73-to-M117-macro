# Prusaslicer M73 conversion to M117 macro
Fork of original PrusaSlicer M73 percentage and time conversion to M117 for LCD character display for standard Marlin firmware.
Prettified with Days, Hours, Minutes readout.

# Installation instructions

### 1. Install python and remember the installation directory 
This version was tested with python 3. If you just want to run Python for this, i recommend downloading and extracting:
https://sourceforge.net/projects/portable-python/

### 2. Copy script.py and remember storage location

### 3. Configuration in PrusaSlicer 
Go to: `Print settings` > `Output options` > `Post-processing scripts`

### If using Python 3.x installed:
Add line: `"[python directory]\python.exe"  "[script directory]\script.py";`

### If using Python 3.7.x portable:
Add line: `"[python directory]\Portable Python-3.7.9\Python-Launcher.exe"  "[script directory]\script.py";`

# Why does this exist
https://forum.duet3d.com/topic/14675/using-prusaslicers-m73-progress-to-run-macro

https://github.com/MarlinFirmware/Marlin/issues/18648#issuecomment-659171081

https://github.com/prusa3d/PrusaSlicer/issues/4593#issue-668668940

https://github.com/prusa3d/PrusaSlicer/issues/3758#issue-574312749

https://github.com/prusa3d/PrusaSlicer/issues/1867#issuecomment-467792575

https://github.com/prusa3d/PrusaSlicer/issues/1739#issue-404985794 

<!--
https://github.com/prusa3d/PrusaSlicer/issues/1317#issuecomment-429428291

pull Marlin

https://github.com/MarlinFirmware/Marlin/pull/15549

extra

https://github.com/MarlinFirmware/Marlin/issues?q=m73
-->
