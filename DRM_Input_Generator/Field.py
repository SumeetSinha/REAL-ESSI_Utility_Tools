
###########################################################################################################################
#                                                                                                                         #
#  Generate_DRM :: Python Script to generate DRM Field Motion                                                             #
#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                                      #
#                                                                                                                         #
#                                                                                                                         #
#  GITHUB:: GITHUB:: https://github.com/SumeetSinha/REAL-ESSI_Utility_Tools.git                                           #
#                                                                                                                         #
#                                                                                                                         #
#  Sumeet Kumar Sinha (September,2016)                                                                                    #
#  Computational Geomechanics Group                                                                                       #
#  University of California, Davis                                                                                        #
#  s u m e e t k s i n h a . c o m                                                                                        #
########################################################################################################################### 

import math;


def getField (x,y,z,t):
	displacement = [0,0,0];
	acceleration = [0,0,0];
	w = 2*math.pi*1;
	v = 1000;
	k = w/v
	displacement[0] = math.sin(w*t -k*z);
	acceleration[0] = -1*w*w*math.sin(w*t -k*z);

	return displacement, acceleration;
