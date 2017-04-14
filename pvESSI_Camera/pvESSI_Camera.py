
#######################################################################################
#                                                                                     #
#                               pvESSI Camera                                         #
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  #
#                                                                                     #
#  GITHUB:: https://github.com/SumeetSinha/REAL-ESSI_Utility_Tools                    #
#                                                                                     #
#  Sumeet Kumar Sinha (April,2017)                                                    #
#  Computational Geomechanics Group                                                   #
#  University of California, Davis                                                    #
#  s u m e e t k s i n h a . c o m                                                    #
####################################################################################### 

from paraview.simple import *
LoadPlugin("libpvESSI.so",ns=globals())
from paraview.simple import *

def ResetSession():
    pxm = servermanager.ProxyManager()
    pxm.UnRegisterProxies()
    del pxm
    Disconnect()
    Connect()

ResetSession()
pvESSI(FileName="ShearBox_Sequential.feioutput")
Show()
Render()
viewLayout = GetLayout()
# save screenshot
SaveScreenshot('filepath/filename-%s.png' % time,layout=viewLayout, magnification=3, quality=100)

