#!/usr/bin/env python

"""Module to generate Real ESSI Input Files from SASSI Input 
"""

__author__ = "Sumeet K. Sinha"
__credits__ = [""]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Sumeet K. Sinha"
__email__ = "sumeet.kumar507@gmail.com"

#! /usr/bin/env python
# import scipy as sp
# import subprocess
import sys
import math
import numpy as np

print "#################################################################################"
print "#                                                                               #"
print "#           Convert SASSI to Real ESSI Simulator Input (.fei) files             #"
print "#  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#"
print "#                                                                               #"
print "#                                                                               #"
print "#  GITHUB:: https://github.com/SumeetSinha/REAL-ESSI_Utility_Tools.git          #"
print "#                                                                               #"
print "#                                                                               #"
print "#  Sumeet Kumar Sinha (Dec,2017)                                                #"
print "#  Computational Geomechanics Group                                             #"
print "#  University of California, Davis                                              #"
print "#  s u m e e t k s i n h a . c o m                                              #"
print "#################################################################################\n\n\n"



def INT(CharList): #return the integer for the char array
	STRING =  (''.join(CharList)).strip();
	if(STRING==''):
		return 0;
	else:
		return int(STRING);

def FLOAT(CharList): #return the float for the char array
	STRING =  (''.join(CharList)).strip();
	if(STRING==''):
		return 0;
	else:
		return float(STRING);

def STRING(CharList): #return the string for the char array
	return  (''.join(CharList)).strip();


## Get the element from the ElementList 
## Each element must have an Id accessible as Id parameter
def GetElement( ElementList, Id):
	for x in ElementList:
		if(x.Id==Id):
			return x;

	print "ERROR : Element with Id " + str (Id) + " not found \n \n ";

	return 

#Defining Node Class
class Node:
	Id    = 0;
	Xcord = 0.0;
	Ycord = 0.0;
	Zcord = 0.0;
	Ux    = 0;
	Uy    = 0;
	Uz    = 0;
	Rx    = 0;
	Ry    = 0;
	Rz    = 0;
	# 1 means fixed and 0 means free

	def __str__(self):
		message = "";
		message = message + "Node No = " + str(self.Id) + "\n";
		message = message + "\t X Coordinate  = " + str(self.Xcord) + "\n"
		message = message + "\t Y Coordinate  = " + str(self.Ycord) + "\n"
		message = message + "\t Z Coordinate  = " + str(self.Zcord) + "\n"
		message = message + "\t Ux constraint = " + str(self.Ux) + "\n"
		message = message + "\t Uy constraint = " + str(self.Uy) + "\n"
		message = message + "\t Uz constraint = " + str(self.Uz) + "\n"
		message = message + "\t Rx constraint = " + str(self.Rx) + "\n"
		message = message + "\t Ry constraint = " + str(self.Ry) + "\n"
		message = message + "\t Rz constraint = " + str(self.Rz) + "\n \n"
		return message;

# Defining Element Class
class Element:
	Id = 0;
	NumNodes =  0;
	NodeList = [0,1,6];
	Type     = " ";
	MaterialId = 0;

	def __str__(self):
		message = "";
		message = message + "Element No         = " + str(self.Id) + "\n";
		message = message + "\t Type            = " + self.Type + "\n";
		message = message + "\t Number of Nodes = " + str(self.NumNodes) + "\n"
		message = message + "\t Node List       = " + str(self.NodeList) + "\n"
		message = message + "\t Material No     = " + str(self.MaterialId) + "\n"
		return message;

# Defining 3-D Beam Class
class BeamElement:
	Id       = 0;
	NodeList = 0;
	IMAT     = 0;
	IMEL     = 0;
	IINC     = 0;
	IB1      = 0;
	IB2      = 0;
	Type     = "BeamElement";

	def __str__(self):
		message = "";
		message = message + "BeamElement Id    = " + str(self.Id)   + "\n";
		message = message + "\t NodeList       = " + str(self.NodeList)  + "\n";
		message = message + "\t IMAT           = " + str(self.IMAT) + "\n";
		message = message + "\t IMEL           = " + str(self.IMEL) + "\n";
		message = message + "\t IINC           = " + str(self.IINC) + "\n";
		message = message + "\t IB1            = " + str(self.IB1)  + "\n";
		message = message + "\t IB2            = " + str(self.IB2)  + "\n";
		return message;

# Defining Brick Element Class
class BrickElement:
	Id     = 0;
	NodeList = [];
	ININT  = 0;
	IMAT   = 0;
	IINC   = 0;
	Type   = "BrickElement";

	def __str__(self):
		message = "";
		message = message + "BrickElement Id   = " + str(self.Id)   + "\n";
		message = message + "\t NodeList       = " + str(self.NodeList)  + "\n";
		message = message + "\t ININT          = " + str(self.ININT)  + "\n";
		message = message + "\t IMAT           = " + str(self.IMAT) + "\n";
		message = message + "\t IINC           = " + str(self.IINC) + "\n";
		return message;

# Defining 3-D Shell Class
class ShellElement:
	Id     = 0;
	NodeList = [];
	IMAT   = 0;
	IINC   = 0;
	TH     = 0;
	Type   = "ShellElement";

	def __str__(self):
		message = "";
		message = message + "ShellElement Id   = " + str(self.Id)   + "\n";
		message = message + "\t NodeList       = " + str(self.NodeList)  + "\n";
		message = message + "\t IMAT           = " + str(self.IMAT) + "\n";
		message = message + "\t IINC           = " + str(self.IINC) + "\n";
		message = message + "\t TH             = " + str(self.TH)  + "\n";
		return message;

# Defining 2-D Quad Class
class Quad2DElement:
	Id     = 0;
	NodeList = [];
	IMAT   = 0;
	IINC   = 0;
	Type   = "Quad2DElement";

	def __str__(self):
		message = "";
		message = message + "Quad2DElement Id  = " + str(self.Id)   + "\n";
		message = message + "\t NodeList       = " + str(self.NodeList)  + "\n";
		message = message + "\t IMAT           = " + str(self.IMAT) + "\n";
		message = message + "\t IINC           = " + str(self.IINC) + "\n";
		return message;


# Defining 3-D InterPile Class
class InterPile3DElement:
	Id     = 0;
	NodeList = [];
	AreaList = [];
	ININT  = 0;
	IMAT   = 0;
	IINC   = 0;
	Type   = "InterPile3DElement";

	def __str__(self):
		message = "";
		message = message + "InterPile3DElement Id = " + str(self.Id)   + "\n";
		message = message + "\t NodeList       = " + str(self.NodeList)  + "\n";
		message = message + "\t AreaList       = " + str(self.AreaList)  + "\n";
		message = message + "\t ININT          = " + str(self.ININT)  + "\n";
		message = message + "\t IMAT           = " + str(self.IMAT) + "\n";
		message = message + "\t IINC           = " + str(self.IINC) + "\n";
		return message;


# Defining 2-D InterPile Class
class InterPile2DElement:
	Id     = 0;
	NodeList = [];
	AreaList = [];
	ININT  = 0;
	IMAT   = 0;
	IINC   = 0;
	Type   = "InterPile2DElement";

	def __str__(self):
		message = "";
		message = message + "InterPile2DElement Id = " + str(self.Id)   + "\n";
		message = message + "\t NodeList       = " + str(self.NodeList)  + "\n";
		message = message + "\t AreaList       = " + str(self.AreaList)  + "\n";
		message = message + "\t ININT          = " + str(self.ININT)  + "\n";
		message = message + "\t IMAT           = " + str(self.IMAT) + "\n";
		message = message + "\t IINC           = " + str(self.IINC) + "\n";
		return message;

# Defining 3-D Spring Class
class Spring3DElement:
	Id     = 0;
	NodeList = [];
	IMAT   = 0;
	IINC   = 0;
	Type   = "Spring3DElement";

	def __str__(self):
		message = "";
		message = message + "Spring3DElement Id = " + str(self.Id)   + "\n";
		message = message + "\t NodeList       = " + str(self.NodeList)  + "\n";
		message = message + "\t IMAT           = " + str(self.IMAT) + "\n";
		message = message + "\t IINC           = " + str(self.IINC) + "\n";
		return message;

# Defining 3-D Thick Shell Class
class ThickShellElement:
	Id     = 0;
	NodeList = [];
	IMAT   = 0;
	IINC   = 0;
	TH     = 0;
	Type   = "ThickShellElement";

	def __str__(self):
		message = "";
		message = message + "ThickShellElement Id = " + str(self.Id)   + "\n";
		message = message + "\t NodeList       = " + str(self.NodeList)  + "\n";
		message = message + "\t IMAT           = " + str(self.IMAT) + "\n";
		message = message + "\t IINC           = " + str(self.IINC) + "\n";
		message = message + "\t TH             = " + str(self.TH)  + "\n";
		return message;

# Defining NodalMass
class NodalMass:
	Id     = 0;
	MassList= [];
	Type   = "NodalMass";

	def __str__(self):
		message = "";
		message = message + "NodalMass Id      = " + str(self.Id)   + "\n";
		message = message + "\t MassList       = " + str(self.MassList)  + "\n";
		return message;

# Defining Material Class
class Material:
	Id = 0;
	Constrained_Modulus = 0;
	Shear_Modulus   = 0;
	Density     = 0;
	Damping_P_wave  = 0;
	Damping_S_wave  = 0;

	def __str__(self):
		message = "";
		message = message + "Material No             = " + str(self.Id) + "\n";
		message = message + "\t Constrained_Modulus  = " + str(self.Constrained_Modulus) + "\n";
		message = message + "\t Shear_Modulus        = " + str(self.Shear_Modulus) + "\n"
		message = message + "\t Density              = " + str(self.Density) + "\n"
		message = message + "\t Damping_P_wave       = " + str(self.Damping_P_wave) + "\n"
		message = message + "\t Damping_S_wave       = " + str(self.Damping_S_wave) + "\n"
		return message;


# Defining Material Class
class Geometry_Properies:
	Id = 0;
	Axial_Area   = 0; ## axial area
	Shear_Area_2 = 0; ## shear area associated with shear force in local 2-direction
	Shear_Area_3 = 0; ## shear area associated with shear force in local 3-direction
	Torsional_Inertia  = 0; ## torsional inertia
	Flexural_Inertia_2 = 0; ## flexural inertia about local 2-axis 
	Flexural_Inertia_3 = 0; ## flexural inertia about local 3-axis 


	def __str__(self):
		message = "";
		message = message + "Material No            = " + str(self.Id) + "\n";
		message = message + "\t Axial_Area          = " + str(self.Axial_Area) + "\n";
		message = message + "\t Shear_Area_2        = " + str(self.Shear_Area_2) + "\n"
		message = message + "\t Shear_Area_3        = " + str(self.Shear_Area_3) + "\n"
		message = message + "\t Torsional_Inertia   = " + str(self.Torsional_Inertia) + "\n"
		message = message + "\t Flexural_Inertia_2  = " + str(self.Flexural_Inertia_2) + "\n"
		message = message + "\t Flexural_Inertia_3  = " + str(self.Flexural_Inertia_3) + "\n"
		return message;


def GetNodeNumbers(CharList):
	ID_List = [0,0,0,0,0,0,0,0,0,0,0,0,0,0];
	TheNodeList = [];
	N_1 = 0; N_2 = 0; N_3 = 0;
	Whether_List_Terminated = False; 
	for x in range (0,14):
		ID_List[x] = INT(CharList[x*5:(x+1)*5]); 
	for i in range(0,14):
		N_1 = ID_List[i]; i=i+1;
		if(N_1==0):
			Whether_List_Terminated = True;

		if(i<14):
			N_2 = ID_List[i]; i=i+1;
			if(N_3==0):
				Whether_List_Terminated = True;

		if(i<14):
			N_3 = ID_List[i]; i=i+1;
			if(N_3==0):
				Whether_List_Terminated = True;

		if(N_3==-1):
			for j in range(N_1,N_2,-N_3):
				TheNodeList.append(j);
		else:
			if(N_1>0):
				TheNodeList.append(N_1);
			if(N_2>0):
				TheNodeList.append(N_2);

	return Whether_List_Terminated, TheNodeList




## SASSI House module or input file 
##	- Contains the finite element model for
##		(a) Structure 
##		(b) Excavated Soil
## House_Module = './Example_1/House.dat'
## House_Module = './Example_2/npp_house.in'

House_Module = raw_input("Enter the SASSI House Module input filename : ");
House_Module = House_Module.strip();
try:
    with open(House_Module) as file:
        pass
except IOError as e:
    print "Unable to open file" #Does not exist OR no read permissions

print "\n\n";

############################################################################
# Each nodal point on the structure can have upto 6 dofs (ux uy uz rx ry rz)
# The coordinated could be in 
#	(a) Cartesian coordinate system 
#	(b) Spherical coordinate system 
#	(c) Cylindrical coordinate system
############################################################################

NOPT = 0;  ## Operation Mode
HED  = ''; ## Contains information to be printed with output
MAXC = 0;  ## Maximum Number of Columns to be assigned to each block
MAXT = 0;  ## Maximum number of terms assigned to each block
MUSE = 0;  ## Maximum decimal field length to be used for blank common (modified by program so that it
NUMNP= 0;  ## Total number of nodes in the system
NUMGP= 0;  ## Total number of nodes at/below ground/surface which act as interaction nodes
NUMEG = 0; ## Total number of different element groups
NUML  = 0; ## Total number of soil layers
NUMLM = 0; ## Total number of nodes with lumped mass or inertia
NSYMPL= 0; ## Total number of planes/line or symmetry or anti-symmetry (maximum of 2)
NIMP  = 0; ## Method of computing impedance matrix
NDIM  = 0; ## Dimension of analysis
NTPILE= 0; ## Blank, pile impedance method is not used
GRAV  = 0; ## Acceleration of gravity
ZSRFCE= 0; ## Z-coordinate of ground level
N     = 0; ## Plane/line of symmetry/anti-symmetry number
NPLTYP= 0; ## Type of plane/line
NPT_1 = 0; ## First reference nodal point number on this plane/line
NPT_2 = 0; ## Second reference nodal point number on this plane/line
NPT_3 = 0; ## Third reference nodal point number on this plane/line
INTACT= 0; ## Total number of interaction nodes to be entered
INTFCE= 0; ## Total number of interface nodes to be entered
INTMED= 0; ## Total number of intermediate nodes to be entered
INTRNL= 0; ## Total number of internal nodes to be entered

Number_Of_Element_Groups = 0; ## Number of element groups encountered 
NodeList = [];   ## Contains the nodes
ElementList = [];## Contains the elements
InteractionNodes = [] ## Contains the node ids of interaction nodes  (Subtraction Method NIMP=1 or NIMP=3)
InterfaceNodes = [] ## Contains the node ids of interaction nodes    (SKIN Method NIMP=2)
IntermediateNodes = [] ## Contains the node ids of interaction nodes (SKIN Method NIMP=2)
InternalNodes = [] ## Contains the node ids of interaction nodes (SKIN Method NIMP=2)
SoilLayerData = [] ## Contains the Soil Layer Data
MaterialList  = [] ## Contains the Material Data
MaterialMapData ={} ## Locally Mapping the material Data (Only Required for SASSI to ESSI) (! Only for algorithm below)
GeometryList  = [] ## Contains the Geometry Data
GeometryMapData ={} ## Locally Mapping the Geometry Data (Only Required for SASSI to ESSI) (! Only for algorithm below)


NPAR_1 = 0 ; 
NPAR_2 = 0 ; ## Total number of element types
NPAR_3 = 0 ; ## Total number of material types
NPAR_4 = 0 ; ## Number of geometric properties
NPAR_5 = 0 ; ## Material property code
ELGRPID = 0 ; ## Physical group name of elements

Line_Number = 0;
Card_Number = 1;
Card_Read   = False;
Sub_Card_Number = 1;
with open(House_Module,'r') as f:
	for Each_Line in f:
		Characters = list(Each_Line);
		Line_Number = Line_Number +1;
		Card_Read   = False;

		# print Card_Read
		# print Characters
		# print Card_Number
		# print Sub_Card_Number

		# print Line_Number
		while(not Card_Read):
			if(Characters[0]=='$'):
				pass
				## print "Line_Number " + str(Line_Number) +": Skipping comments";
				Card_Read = True;
				### Now lets start the parsing ###
			elif(Card_Number==1):
				# print "CARD==1 " + str(Characters)
				NOPT = INT(Characters[0:5]);      ## Operation Mode
				HED  = STRING(Characters[8:80]);  ## Contains information to be printed with output
				Card_Read = True;
				Card_Number = 2;
			elif(Card_Number==2):
				# print "CARD==2 " + str(Characters)
				MAXC = INT(Characters[0:10]);  ## Maximum Number of Columns to be assigned to each block
				MAXT = INT(Characters[10:20]); ## Maximum number of terms assigned to each block
				MUSE = INT(Characters[20:30]); ## Maximum decimal field length to be used for blank common (modified by program so that it
				Card_Read = True;
				Card_Number = 3;
			elif(Card_Number==3):
				# print "CARD==3 " + str(Characters)
				NUMNP = INT(Characters[0:5]);   ## Total number of nodes in the system
				NUMGP = INT(Characters[5:10]);  ## Total number of nodes at/below ground/surface which act as interaction nodes
				NUMEG = INT(Characters[10:15]); ## Total number of different element groups
				NUML  = INT(Characters[15:20]); ## Total number of soil layers
				NUMLM = INT(Characters[20:25]); ## Total number of nodes with lumped mass or inertia
				NSYMPL= INT(Characters[29:30]); ## Total number of planes/line or symmetry or anti-symmetry (maximum of 2)
				NIMP  = INT(Characters[34:35]); ## Method of computing impedance matrix
				NDIM  = INT(Characters[39:40]); ## Dimension of analysis
				NTPILE= INT(Characters[44:45]); ## Blank, pile impedance method is not used
				Card_Read   = True;
				Card_Number = 4;
			elif(Card_Number==4):
				# print "CARD==4 " + str(Characters)
				GRAV  = FLOAT(Characters[0:10]);  ## Acceleration of gravity
				Card_Read   = True;
				Card_Number = 5;
			elif(Card_Number==5):
				# print "CARD==5 " + str(Characters)
				ZSRFCE= FLOAT(Characters[0:10]);  ## Z-coordinate of ground level
				Card_Read   = True;
				Card_Number = 6;
			elif(Card_Number==6):
				# print "CARD==6 " + str(Characters)
				if(NSYMPL==0):
					pass
					## print "Line_Number " + str(Line_Number) +": NSYMPS==0 So, skipping Card Number 6";
				else:
					N      = INT(Characters[0:5]);  ##  Plane/line of symmetry/anti-symmetry number
					NPLTYP = INT(Characters[5:10]); ##  Type of plane/line
					NPT_1  = INT(Characters[10:15]);##  First reference nodal point number on this plane/line
					NPT_2  = INT(Characters[15:20]);##  Second reference nodal point number on this plane/line
					NPT_3  = INT(Characters[20:25]);##  Third reference nodal point number on this plane/line
					Card_Read = True;
				Card_Number = 7;
			elif(Card_Number==7):
				# print "CARD==7 " + str(Characters)
				if(NUMNP==0):
					pass
					## print "Line_Number " + str(Line_Number) +": NUMNP==0 So, skipping Card Number 7";
					Card_Number = 8;
					if(NIMP==1 or NIMP==3):
						Card_Number     = 8.1;
						Sub_Card_Number = 8.11;
					elif(NIMP==2):
						Card_Number     = 8.2;
						Sub_Card_Number = 8.21;
				else:

					N_NUM  = INT(Characters[0:5]); 
					NC     = STRING(Characters[5:6]);
					ID_1   = INT(Characters[6:10]);
					ID_2   = INT(Characters[10:15]);
					ID_3   = INT(Characters[15:20]);
					ID_4   = INT(Characters[20:25]);
					ID_5   = INT(Characters[25:30]);
					ID_6   = INT(Characters[30:35]);
					XORD   = FLOAT(Characters[35:45]);
					YORD   = FLOAT(Characters[45:55]);
					ZORD   = FLOAT(Characters[55:65]);
					KN     = INT(Characters[65:70]);
					NPILE  = INT(Characters[70:75]);

					####### Process the node data ######
					New_Node = Node();
					New_Node.Id = N_NUM;
					New_Node.Ux = ID_1;
					New_Node.Uy = ID_2;
					New_Node.Uz = ID_3;
					New_Node.Rx = ID_4;
					New_Node.Ry = ID_5;
					New_Node.Rz = ID_6;
							       # Cyln   Sphr
					x_cord = XORD; # r      r
					y_cord = YORD; # theta  theta
					z_cord = ZORD; # z	   	phi	
					if(NC=='C'):
						x_cord = XORD*math.cos(YORD);
						y_cord = XORD*math.sin(YORD);
						z_cord = ZORD;	
					if(NC=='S'):
						x_cord = XORD*math.cos(YORD)*math.sin(ZORD);
						y_cord = XORD*math.sin(YORD)*math.sin(ZORD);
						z_cord = XORD*math.cos(ZORD);	

					New_Node.Xcord = x_cord;
					New_Node.Ycord = y_cord;
					New_Node.Zcord = z_cord;

					NodeList.append(New_Node); # appending the node to NodeList 

					Card_Read = True;

					if(len(NodeList)==NUMNP):
						Card_Number = 8;
						if(NIMP==1 or NIMP==3):
							Card_Number     = 8.1;
							Sub_Card_Number = 8.11;
						elif(NIMP==2):
							Card_Number     = 8.2;
							Sub_Card_Number = 8.21;

			elif(Card_Number==8.1):
				if(Sub_Card_Number==8.11):
					INTACT =  INT(Characters[0:5]);
					Sub_Card_Number = 8.12;
					Card_Read = True;
				elif(Sub_Card_Number==8.12):
					if(INTACT==0):
						pass
						## print "Line_Number " + str(Line_Number) +": INTACT==0 So, skipping Card Number 8.1"
						Card_Number = 9;
					else:
						Whether_List_Terminated, NodeNumbers = GetNodeNumbers(Characters);
						InteractionNodes = InteractionNodes + NodeNumbers;
						Card_Read = True;
						if(Whether_List_Terminated==True):
							Card_Number = 9;

			elif(Card_Number == 8.2):
				if(Sub_Card_Number==8.21):
					INTFCE =  INT(Characters[0:5]);
					INTMED =  INT(Characters[5:10]);
					INTRNL =  INT(Characters[10:15]);
					Sub_Card_Number = 8.22;
					Card_Read = True;
				elif(Sub_Card_Number==8.22):
					if(INTFCE==0):
						pass
						## print "Line_Number " + str(Line_Number) +": INTFCE==0 So, skipping Card Number 8.22"
						Sub_Card_Number = 8.23;
					else:
						Whether_List_Terminated, NodeNumbers = GetNodeNumbers(Characters);
						InterfaceNodes = InterfaceNodes + NodeNumbers;
						Card_Read = True;
						if(Whether_List_Terminated==True):
							Sub_Card_Number = 8.23;
				elif(Sub_Card_Number==8.23):
					if(INTMED==0):
						pass
						## print "Line_Number " + str(Line_Number) +": INTMED==0 So, skipping Card Number 8.23"
						Sub_Card_Number = 8.24;
					else:
						Whether_List_Terminated, NodeNumbers = GetNodeNumbers(Characters);
						IntermediateNodes = IntermediateNodes + NodeNumbers;
						Card_Read = True;
						if(Whether_List_Terminated==True):
							Sub_Card_Number = 8.24;
				elif(Sub_Card_Number==8.23):
					if(INTRNL==0):
						pass
						## print "Line_Number " + str(Line_Number) +": INTRNL==0 So, skipping Card Number 8.22"
						Card_Number = 9;
					else:
						Whether_List_Terminated, NodeNumbers = GetNodeNumbers(Characters);
						InternalNodes = InternalNodes + NodeNumbers;
						Card_Read = True;
						if(Whether_List_Terminated==True):
							Card_Number = 9;

			elif(Card_Number==9):
				# print "CARD==9 " + str(Characters)
				if(NUML==0):
					pass
					## print "Line_Number " + str(Line_Number) +": NUML==0 So, skipping Card Number 9"
					Card_Number = 10;
					Sub_Card_Number = 10;
				else:
					N_ = FLOAT(Characters[0:5]);
					G_ = FLOAT(Characters[5:15]);
					W_ = FLOAT(Characters[15:25]); 
					Vs_= FLOAT(Characters[25:35]);
					Vp_= FLOAT(Characters[35:45]);
					Ds_= FLOAT(Characters[45:55]);
					Dp_= FLOAT(Characters[55:65]);

					NewSoilLayer = [N_,G_,W_,Vs_,Vp_,Ds_,Dp_];
					SoilLayerData.append(NewSoilLayer);

					## making new materials
					NewMaterial = Material();
					MaterialId   = len(MaterialList)+1;
					NewMaterial.Id = MaterialId;
					NewMaterial.Constrained_Modulus = W_*Vp_**2/GRAV;
					NewMaterial.Shear_Modulus   = W_*Vs_**2/GRAV;
					NewMaterial.Density     = W_/GRAV;
					NewMaterial.Damping_P_wave  = Dp_;
					NewMaterial.Damping_S_wave  = Ds_;
					MaterialList.append(NewMaterial);

					Card_Read = True;

					if(len(SoilLayerData)==NUML):
						Card_Number = 10;
						Sub_Card_Number = 10;

			######### Element Mesh Data
			elif(Card_Number==10):

				if(Sub_Card_Number == 10):

					if(Number_Of_Element_Groups==NUMEG):
						Card_Number=11;
						Sub_Card_Number = 11;
					Number_Of_Element_Groups = Number_Of_Element_Groups + 1;

					# print "CARD==10 " + str(Characters) 
					NPAR_1 = INT(Characters[0:5]);
					Card_Read = True;

					if(NPAR_1== 1): ## Three dimensional solid element
						NPAR_2 = INT(Characters[5:10]);  ## Number of 8-node solid elements
						NPAR_3 = INT(Characters[10:15]); ## Number of material types
						NPAR_4 = INT(Characters[18:20]); ## Material Property Code
						NPAR_5 = INT(Characters[24:25]); ## Incompatible mode code
						ELGRPID = STRING(Characters[30:80]); ## Element Physical Group
						Sub_Card_Number = 10.12;

					elif(NPAR_1== 2): ## Three dimensional beam element
						NPAR_2 = INT(Characters[5:10]);  ## Number of beam elements
						NPAR_3 = INT(Characters[10:15]); ## Number of material types
						NPAR_5 = INT(Characters[15:20]); ## Number of geometry property types
						NPAR_4 = INT(Characters[23:25]); ## Material Property Code
						ELGRPID = STRING(Characters[30:80]); ## Element Physical Group
						Sub_Card_Number = 10.12;

					elif(NPAR_1== 3 or NPAR_1 ==4 or NPAR_1 ==5 or NPAR_1 ==6): ## 3-D Shell Element
						NPAR_2 = INT(Characters[5:10]);  ## Number of shell elements
						NPAR_3 = INT(Characters[10:15]); ## Number of material types
						NPAR_4 = INT(Characters[15:20]); ## Material Property Code
						ELGRPID = STRING(Characters[30:80]); ## Element Physical Group
						Sub_Card_Number = 10.12;

				elif(Sub_Card_Number==10.12):
					# print "CARD==10.12 " + str(Characters)
					if(NPAR_3==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_3==0 So, skipping Card Number 10.12"
						if(NPAR_1==1):
							Sub_Card_Number = 10.13;
						elif(NPAR_1==2):
							Sub_Card_Number = 10.23;
						elif(NPAR_1==3):
							Sub_Card_Number = 10.33;
						elif(NPAR_1==4):
							Sub_Card_Number = 10.43;
						elif(NPAR_1==5):
							Sub_Card_Number = 10.53;
						elif(NPAR_1==6):
							Sub_Card_Number = 10.63;
						# print "New_SubCard " + str ( Sub_Card_Number)
					else:
						N_ = INT(Characters[0:5]);   ## Material Type Number
						M_ = FLOAT(Characters[5:15]);  ## Elastic Modulus/ Constrained Modulus/ P-Wave Velocity
						G_ = FLOAT(Characters[15:25]); ## Poisson's ratio/ Shear Modulus / S-wave 
						W_ = FLOAT(Characters[25:35]); ## Unit weight of material
						Dp_= FLOAT(Characters[35:45]); ## P-wave associated damping ratio
						Ds_= FLOAT(Characters[45:55]); ## S-wave associated damping ratio

						## making new materials
						NewMaterial = Material();
						MaterialId   = len(MaterialList)+1;
						NewMaterial.Id = MaterialId;
						NewMaterial.Density     = W_/GRAV;
						NewMaterial.Damping_P_wave  = Dp_;
						NewMaterial.Damping_S_wave  = Ds_;

						if(NPAR_4==-1):
							NewMaterial.Constrained_Modulus = M_*(1-G_)/(1+G_)/(1-2*G_);
							NewMaterial.Shear_Modulus       = M_/(2*(1+G_));
						elif(NPAR_4==1):
							NewMaterial.Constrained_Modulus = W_*M_**2/GRAV;
							NewMaterial.Shear_Modulus       = W_*G_**2/GRAV;
						elif(NPAR_4==0):
							NewMaterial.Constrained_Modulus = M_;
							NewMaterial.Shear_Modulus       = G_;

						MaterialList.append(NewMaterial);
						MaterialMapData.update({N_:MaterialId})
						NPAR_3 = NPAR_3 - 1;
						Card_Read = True;

						# print NewMaterial

						if(NPAR_3<=0):
							if(NPAR_1==1):
								Sub_Card_Number = 10.13;
							elif(NPAR_1==2):
								Sub_Card_Number = 10.23;
							elif(NPAR_1==3):
								Sub_Card_Number = 10.33;
							elif(NPAR_1==4):
								Sub_Card_Number = 10.43;
							elif(NPAR_1==5):
								Sub_Card_Number = 10.53;
							elif(NPAR_1==6):
								Sub_Card_Number = 10.63;

				elif(Sub_Card_Number == 10.13):
					# print "CARD==10.13 " + str(Characters)
					if(NPAR_2==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_2==0 So, skipping Card Number 9"
						Sub_Card_Number = 10;
					else:
						INEL = INT(Characters[0:5]);
						INP_1= INT(Characters[5:10]);
						INP_2= INT(Characters[10:15]);
						INP_3= INT(Characters[15:20]);
						INP_4= INT(Characters[20:25]);
						INP_5= INT(Characters[25:30]);
						INP_6= INT(Characters[30:35]);
						INP_7= INT(Characters[35:40]);				
						INP_8= INT(Characters[40:45]);	
						ININT= INT(Characters[49:50]);	
						INTYP= INT(Characters[53:55]);	
						IMAT = INT(Characters[55:60]);	
						IINC = INT(Characters[60:65]);

						NewElement = BrickElement();
						NewElement.Id = INEL;
						NewElement.NodeList = [INP_8,INP_5,INP_6,INP_7,INP_4,INP_1,INP_2,INP_3];
						NewElement.ININT = ININT;
						NewElement.IINC = IINC;

						if(INTYP==1):
							IMAT = MaterialMapData[IMAT];		

						NewElement.IMAT = IMAT;
						ElementList.append(NewElement);

						NPAR_2 = NPAR_2 -1;
						Card_Read = True;

						if(NPAR_2<=0):
							Sub_Card_Number = 10;
				elif(Sub_Card_Number == 10.23):
					# print "CARD==10.23 " + str(Characters)
					if(NPAR_5==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_4==0 So, skipping Card Number 10.23"
						Sub_Card_Number = 10.24;
					else:
						N_    = INT(Characters[0:5]);     ## Geometry Type Number
						ELP_1 = FLOAT(Characters[5:15]);  ## Axial Area
						ELP_2 = FLOAT(Characters[15:25]); ## Shear area associated with shear force in local 2-direction
						ELP_3 = FLOAT(Characters[25:35]); ## Shear area associated with shear force in local 3-direction 
						ELP_4 = FLOAT(Characters[35:45]); ## Torsional Inertia
						ELP_5 = FLOAT(Characters[45:55]); ## Flexural inertia about local 2-axis
						ELP_6 = FLOAT(Characters[55:65]); ## Flexural inertia about local 3-axis

						NewGeometry = Geometry_Properies();
						geometryId  = len(GeometryList)+1;
						NewGeometry.Id = geometryId;
						NewGeometry.Axial_Area   = ELP_1;
						NewGeometry.Shear_Area_2 = ELP_2;
						NewGeometry.Shear_Area_3 = ELP_3;
						NewGeometry.Torsional_Inertia  = ELP_4;
						NewGeometry.Flexural_Inertia_2 = ELP_5;
						NewGeometry.Flexural_Inertia_3 = ELP_6;

						GeometryList.append(NewGeometry);
						GeometryMapData.update({N_:geometryId});
						NPAR_5 = NPAR_5 - 1;
						Card_Read = True;

						if(NPAR_5==0):
							Sub_Card_Number = 10.24;

				elif(Sub_Card_Number == 10.24):
					# print "CARD==10.24 " + str(Characters)
					if(NPAR_2==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_2==0 So, skipping Card Number 10.24"
						Sub_Card_Number = 10;
					else:
						INEL = INT(Characters[0:5]);
						INI  = INT(Characters[5:10]);
						INJ  = INT(Characters[10:15]);
						INK  = INT(Characters[15:20]);
						IMAT = INT(Characters[20:25]);
						IMEL = INT(Characters[25:30]);
						IINC = INT(Characters[30:35]);
						IB1  = INT(Characters[39:45]);				
						IB2  = INT(Characters[49:55]);	

						NewElement = BeamElement();
						NewElement.Id = INEL;
						NewElement.NodeList = [INI,INJ,INK];
						NewElement.IB1 = IB1;
						NewElement.IB2 = IB2;
						NewElement.IINC = IINC;
						NewElement.IMEL = GeometryMapData[IMEL];
						NewElement.IMAT = MaterialMapData[IMAT];

						ElementList.append(NewElement);

						NPAR_2 = NPAR_2 -1;
						Card_Read = True;

						if(NPAR_2<=0):
							Sub_Card_Number = 10;

				elif(Sub_Card_Number == 10.33):
					# print "CARD==10.33 " + str(Characters)
					if(NPAR_2==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_2==0 So, skipping Card Number 10.33"
						Sub_Card_Number = 10;
					else:
						INEL = INT(Characters[0:5]);
						INP1 = INT(Characters[5:10]);
						INP2 = INT(Characters[10:15]);
						INP3 = INT(Characters[15:20]);
						INP4 = INT(Characters[20:25]);
						INP5 = INT(Characters[25:30]);
						IMAT = INT(Characters[30:35]);
						IINC = INT(Characters[35:40]);				
						TH   = INT(Characters[40:45]);	

						NewElement = ShellElement();
						NewElement.Id = INEL;
						NewElement.NodeList = [INP1,INP2,INP3,INP4,INP5];
						NewElement.IINC = IINC;
						NewElement.TH   = TH;
						NewElement.IMAT = MaterialMapData[IMAT];

						ElementList.append(NewElement);

						NPAR_2 = NPAR_2 -1;
						Card_Read = True;

						if(NPAR_2<=0):
							Sub_Card_Number = 10;

				elif(Sub_Card_Number == 10.33):
					# print "CARD==10.33 " + str(Characters)
					if(NPAR_2==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_2==0 So, skipping Card Number 10.33"
						Sub_Card_Number = 10;
					else:
						INEL = INT(Characters[0:5]);
						INP1 = INT(Characters[5:10]);
						INP2 = INT(Characters[10:15]);
						INP3 = INT(Characters[15:20]);
						INP4 = INT(Characters[20:25]);
						INP5 = INT(Characters[25:30]);
						IMAT = INT(Characters[30:35]);
						IINC = INT(Characters[35:40]);				
						TH   = INT(Characters[40:45]);	

						NewElement = ShellElement();
						NewElement.Id = INEL;
						NewElement.NodeList = [INP1,INP2,INP3,INP4,INP5];
						NewElement.IINC = IINC;
						NewElement.TH   = TH;
						NewElement.IMAT = MaterialMapData[IMAT];

						ElementList.append(NewElement);

						NPAR_2 = NPAR_2 -1;
						Card_Read = True;

						if(NPAR_2<=0):
							Sub_Card_Number = 10;

				elif(Sub_Card_Number == 10.43):
					# print "CARD==10.43 " + str(Characters)
					if(NPAR_2==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_2==0 So, skipping Card Number 10.43"
						Sub_Card_Number = 10;
					else:
						INEL = INT(Characters[0:5]);
						INP1 = INT(Characters[5:10]);
						INP2 = INT(Characters[10:15]);
						INP3 = INT(Characters[15:20]);
						INP4 = INT(Characters[20:25]);
						INTYP= INT(Characters[25:30]);
						IMAT = INT(Characters[30:35]);				
						IINC = INT(Characters[35:40]);	

						NewElement = Quad2DElement();
						NewElement.Id = INEL;
						NewElement.NodeList = [INP1,INP2,INP3,INP4];
						NewElement.IINC = IINC;

						if(INTYP==1):
							IMAT = MaterialMapData[IMAT];	
						NewElement.IMAT = MaterialMapData[IMAT];

						ElementList.append(NewElement);

						NPAR_2 = NPAR_2 -1;
						Card_Read = True;

						if(NPAR_2<=0):
							Sub_Card_Number = 10;

				elif(Sub_Card_Number == 10.53):
					# print "CARD==10.53 " + str(Characters)
					if(NPAR_2==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_2==0 So, skipping Card Number 10.53"
						Sub_Card_Number = 10;
					else:
						INEL = INT(Characters[0:5]);
						INP_1= INT(Characters[5:10]);
						INP_2= INT(Characters[10:15]);
						INP_3= INT(Characters[15:20]);
						INP_4= INT(Characters[20:25]);
						INP_5= INT(Characters[25:30]);
						INP_6= INT(Characters[30:35]);
						INP_7= INT(Characters[35:40]);				
						INP_8= INT(Characters[40:45]);	
						ININT= INT(Characters[49:50]);	
						IMAT = INT(Characters[50:55]);	
						IINC = INT(Characters[55:60]);

						Characters = list(f.next());
						AX_1 = FLOAT(Characters[0:10]);
						AX_2 = FLOAT(Characters[10:20]);
						AX_3 = FLOAT(Characters[20:30]);
						AX_4 = FLOAT(Characters[30:40]);

						NewElement = InterPile3DElement();
						NewElement.Id = INEL;
						NewElement.NodeList = [INP_1,INP_2,INP_3,INP_4,INP_5,INP_6,INP_7,INP_8];
						NewElement.AreaList = [AX_1, AX_2, AX_3, AX_4];
						NewElement.ININT = ININT;
						NewElement.IINC = IINC;
						NewElement.IMAT = MaterialMapData[IMAT];

						ElementList.append(NewElement);

						NPAR_2 = NPAR_2 -1;
						Card_Read = True;

						if(NPAR_2<=0):
							Sub_Card_Number = 10;

				elif(Sub_Card_Number == 10.63):
					# print "CARD==10.53 " + str(Characters)
					if(NPAR_2==0):
						pass
						## print "Line_Number " + str(Line_Number) +": NPAR_2==0 So, skipping Card Number 10.53"
						Sub_Card_Number = 10;
					else:
						INEL = INT(Characters[0:5]);
						INP_1= INT(Characters[5:10]);
						INP_2= INT(Characters[10:15]);
						INP_3= INT(Characters[15:20]);
						INP_4= INT(Characters[20:25]);
						ININT= INT(Characters[25:30]);
						IMAT = INT(Characters[30:35]);
						IINC = INT(Characters[35:40]);				

						Characters = list(f.next());
						AX_1 = FLOAT(Characters[0:10]);
						AX_2 = FLOAT(Characters[10:20]);

						NewElement = InterPile2DElement();
						NewElement.Id = INEL;
						NewElement.NodeList = [INP_1,INP_2,INP_3,INP_4];
						NewElement.AreaList = [AX_1, AX_2];
						NewElement.ININT = ININT;
						NewElement.IINC  = IINC;
						NewElement.IMAT  = MaterialMapData[IMAT];

						ElementList.append(NewElement);

						NPAR_2 = NPAR_2 -1;
						Card_Read = True;

						if(NPAR_2<=0):
							Sub_Card_Number = 10;

			elif(Card_Number == 11):
				# print "CARD==11 " + str(Characters)
				if(NUMLM==0):
					pass
					## print "Line_Number " + str(Line_Number) +": NUMLM==0 So, skipping Card Number 11"
					Sub_Card_Number = 12;
				else:
					N_     = INT(Characters[0:5]);
					MTYP   = INT(Characters[5:10]);
					Divisor = 1.0;
					if(MTYP==0):
						Divisor = GRAV;
					XMASS_1= FLOAT(Characters[10:20])/Divisor;
					XMASS_2= FLOAT(Characters[20:30])/Divisor;
					XMASS_3= FLOAT(Characters[30:40])/Divisor;
					XMASS_4= FLOAT(Characters[40:50])/Divisor;
					XMASS_5= FLOAT(Characters[50:60])/Divisor;
					XMASS_6= FLOAT(Characters[60:70])/Divisor;

					NewElement = NodalMass();
					NewElement.Id = N_;
					NewElement.MassList = [XMASS_1,XMASS_2,XMASS_3,XMASS_4,XMASS_5,XMASS_6];
					ElementList.append(NewElement);

					NPAR_2 = NPAR_2 -1;
					Card_Read = True;

					if(NPAR_2==0):
						Sub_Card_Number = 12;
			else:
				Card_Read = True;
		# print Line_Number

print "\n\n---------------------- House Parameters-----------------------------\n"
print 'NOPT   = ' + str(NOPT)   + " -- Operation Mode";
print 'HED    = ' + str(HED )   + " -- Information to be printed with output";
print 'MAXC   = ' + str(MAXC)   + " -- Maximum number of columns to be assigned to each block";
print 'MAXT   = ' + str(MAXT)   + " -- Maximum number of terms to be assigned to each block";
print 'MUSE   = ' + str(MUSE)   + " -- Maximum decimal field length";
print 'NUMNP  = ' + str(NUMNP ) + " -- Total number of nodes in the system";
print 'NUMGP  = ' + str(NUMGP ) + " -- Number of nodes at/below ground surface acts as interaction nodes";
print 'NUMEG  = ' + str(NUMEG ) + " -- Total number of differnet element groups";
print 'NUML   = ' + str(NUML  ) + " -- Total number of soil layers";
print 'NUMLM  = ' + str(NUMLM ) + " -- Total number of nodes with lumped mass or inertia";
print 'NSYMPL = ' + str(NSYMPL) + " -- Total number of soil layers";
print 'NIMP   = ' + str(NIMP  ) + " -- Method of computing mass matrix";
print 'NDIM   = ' + str(NDIM  ) + " -- Dimension of analysis";
print 'NTPILE = ' + str(NTPILE) + " -- Impedance method ";
print 'GRAV   = ' + str(GRAV  ) + " -- Gravity";
print 'ZSRFCE = ' + str(ZSRFCE) + " -- Z-coordinate of ground level";
# print 'N      = ' + str(N     ) + " -- "; 
# print 'NPLTYP = ' + str(NPLTYP) + " -- "; 
# print 'NPT_1  = ' + str(NPT_1 ) + " -- "; 
# print 'NPT_2  = ' + str(NPT_2 ) + " -- "; 
# print 'NPT_3  = ' + str(NPT_3 ) + " -- "; 
# print 'INTACT = ' + str(INTACT) + " -- "; 


print '======================== Data Base Created =========================== \n'

#########################################################################################################
#########################################################################################################
## All Database Created from the SASSI Input File
## Lets write the Real-ESSI Input Files

NodeFile     = 'node.fei';
FixitiesFile = 'fixities.fei';
ElementFile  = 'element.fei';
MaterialFile = 'material.fei';
MainFile     = 'main.fei'

## writing down the node file (node.fei) with all the nodes ##
FileNode     = open(NodeFile,'w');
FileFixity   = open(FixitiesFile,'w');
MainFile     = open(MainFile,'w');

## model name ;
MainFile.write("""model name "%2s";\n\n""" % (HED));
## add acceleration field #  	ax =  	ay =  	az =  ;
MainFile.write("add acceleration field #1  	ax = 0*m/s^2   ay = 0*m/s^2  az = %2s*m/s^2; \n\n\n" % (GRAV));

sys.stdout.write("Writing Node (node.fei) file ......");sys.stdout.flush();
for node in NodeList:
	## add node #  at (,,)  with  dofs;
	FileNode.write('add node #%8s  at (%8s*m, %8s*m, %8s*m) with 6 dofs;\n' % (node.Id, round(node.Xcord,4), round(node.Ycord,4), round(node.Zcord,4)));

	ConstrainedDOFs = '';
	if(node.Ux==1):
		ConstrainedDOFs = ConstrainedDOFs + "ux ";
	if(node.Uy==1):
		ConstrainedDOFs = ConstrainedDOFs + "uy ";
	if(node.Uz==1):
		ConstrainedDOFs = ConstrainedDOFs + "uz ";
	if(node.Rx==1):
		ConstrainedDOFs = ConstrainedDOFs + "rx ";
	if(node.Ry==1):
		ConstrainedDOFs = ConstrainedDOFs + "ry ";		
	if(node.Rz==1):
		ConstrainedDOFs = ConstrainedDOFs + "rz ";		
	if(ConstrainedDOFs!=''):
		FileFixity.write('fix node #%8s  dofs %8s;\n' % (node.Id, ConstrainedDOFs));

sys.stdout.write("...... completed \n");sys.stdout.flush();
MainFile.write("""include  "node.fei" ; \n""");
FileNode.close();

##################### Writing Material File #####################
FileMaterial   = open(MaterialFile,'w');
sys.stdout.write("Writing Material (material.fei) file ......");sys.stdout.flush();
for material in MaterialList:

	M = material.Constrained_Modulus;
	G = material.Shear_Modulus;
	Dp = material.Damping_P_wave;
	Ds = material.Damping_S_wave;

	elastic_modulus = G*(3*M-4*G)/(M-G);
	poisson_ratio   = (M-2*G)/(2*M-2*G);
	mass_density    = material.Density;

	# add material #  type linear_elastic_isotropic_3d 	mass_density =  	elastic_modulus =  	poisson_ratio = ;				
	FileMaterial.write('add material #%8s  type linear_elastic_isotropic_3d  mass_density = %8s*kg/m^3   elastic_modulus = %8s*Pa   poisson_ratio = %8s ;\n' % (material.Id, round(mass_density,4), round(elastic_modulus,4), round(poisson_ratio,4)));

sys.stdout.write("...... completed \n");sys.stdout.flush();
MainFile.write("""include  "material.fei" ; \n""");
FileMaterial.close();

##################### Writing Element File #####################
FileElement   = open(ElementFile,'w');
sys.stdout.write("Writing Elements (element.fei) file ......");sys.stdout.flush();
for element in ElementList:

	EleType = element.Type;

	if(EleType == 'BrickElement'):
		nd_1 = element.NodeList[0];
		nd_2 = element.NodeList[1];
		nd_3 = element.NodeList[2];
		nd_4 = element.NodeList[3];
		nd_5 = element.NodeList[4];
		nd_6 = element.NodeList[5];
		nd_7 = element.NodeList[6];
		nd_8 = element.NodeList[7];

		## add element #  type 8NodeBrick using  Gauss points each direction with nodes (, , , , , , , ) use material # ;
		FileElement.write('add element #%8s  type 8NodeBrick with nodes (%8s, %8s, %8s, %8s, %8s, %8s, %8s, %8s) use material #%8s;\n' % (element.Id, nd_1,nd_2,nd_3,nd_4,nd_5,nd_6,nd_7,nd_8, element.IMAT));

	if(EleType == 'BeamElement'):
		nd_1 = element.NodeList[0];
		nd_2 = element.NodeList[1];
		nd_3 = element.NodeList[2];

		# print str(nd_1) + " " + str(nd_2) +  " " + str(nd_3);

		node_1 = GetElement(NodeList,nd_1);
		node_2 = GetElement(NodeList,nd_2);
		node_3 = GetElement(NodeList,nd_3);

		NodeCoord_1 = np.array([node_1.Xcord, node_1.Ycord, node_1.Zcord]);
		NodeCoord_2 = np.array([node_2.Xcord, node_2.Ycord, node_2.Zcord]);
		NodeCoord_3 = np.array([node_3.Xcord, node_3.Ycord, node_3.Zcord]);

		Plane_Vector = np.cross(NodeCoord_1-NodeCoord_3,NodeCoord_2-NodeCoord_3);
		Plane_Vector = np.cross(NodeCoord_1-NodeCoord_2,Plane_Vector); ## Web vector 
		Plane_Vector = Plane_Vector/math.sqrt(Plane_Vector[0]*Plane_Vector[0]+Plane_Vector[1]*Plane_Vector[1]+Plane_Vector[2]*Plane_Vector[2])

		material = MaterialList[element.IMAT-1];
		geometry = GeometryList[element.IMEL-1];

		M = material.Constrained_Modulus;
		G = material.Shear_Modulus;
		E = G*(3*M-4*G)/(M-G);
		Rho = material.Density;

		Area = geometry.Axial_Area;
		Jx   = geometry.Torsional_Inertia;
		Iy   = geometry.Flexural_Inertia_2;
		Iz   = geometry.Flexural_Inertia_3;

		## add element #  type beam_elastic with nodes (, ) cross_section =  	elastic_modulus =  	shear_modulus =  	torsion_Jx =  	bending_Iy =  	bending_Iz =  	mass_density =   	xz_plane_vector = (, ,  ) 	joint_1_offset = (, ,  ) 	joint_2_offset = (, ,  );
		FileElement.write('add element #%8s  type beam_elastic with nodes (%8s, %8s) cross_section = %8s*m^2 	elastic_modulus = %8s*Pa 	shear_modulus = %8s*Pa 	torsion_Jx =  %8s*m^4	bending_Iy = %8s*m^4 	bending_Iz =  %8s*m^4	mass_density = %8s*kg/m^3  xz_plane_vector = (%8s,%8s,%8s) 	joint_1_offset = (0*m,0*m,0*m) 	joint_2_offset = (0*m,0*m,0*m);\n' % (
		element.Id, nd_1,nd_2,Area,E,G,Jx,Iy,Iz,Rho,Plane_Vector[0],Plane_Vector[1],Plane_Vector[2]));


		##### End conditions for node 1
		DOFs = ['ux','uy','uz','rx','ry','rz']; ## all the dofs

		digits = [int(x) for x in str(element.IB1)];
		EndCondition1 = '';
		for i in range(0,len(digits)):
			if(digits[i]==1):
				EndCondition1 = EndCondition1 + DOFs[t] + " ";

		digits = [int(x) for x in str(element.IB2)];
		EndCondition2 = '';
		for i in range(0,len(digits)):
			if(digits[i]==1):
				EndCondition2 = EndCondition2 + DOFs[t] + " ";

		if(EndCondition1 != ''):
			FileFixity.write('free node #%8s  dofs %8s;\n' % (node.Id, EndCondition1));
		if(EndCondition2 != ''):
			FileFixity.write('free node #%8s  dofs %8s;\n' % (node.Id, EndCondition2));

	if(EleType == 'NodalMass'):

		mass     = element.MassList;
		## add mass to node #  	mx =  	my =  	mz =   Imx =  	Imy =  	Imz = ;
		FileElement.write('add mass to node #%8s  	mx = %8s*kg  	my = %8s*kg  	mz = %8s*kg   Imx = %8s*kg*m^2  	Imy = %8s*kg*m^2  	Imz = %8s*kg*m^2 ;\n' % (element.Id, mass[0],mass[1],mass[2],mass[3],mass[4],mass[5]));


	if(EleType == 'ShellElement'):
		nd_1 = element.NodeList[0];
		nd_2 = element.NodeList[1];
		nd_3 = element.NodeList[2];
		nd_4 = element.NodeList[3];
		Thickness = element.TH;

		## add element #  type FourNodeShellANDES with nodes (, , , ) use material #  thickness = ;
		FileElement.write('add element #%8s  type FourNodeShellANDES with nodes ( %8s, %8s , %8s , %8s) use material #%8s  thickness = %8s*m;\n' % (element.Id, nd_1,nd_2,nd_3,nd_4,element.IMAT,Thickness));

MainFile.write("""include  "fixities.fei" ; \n""");
MainFile.write("""include  "element.fei" ; \n""");
MainFile.write("""\n\n check model;\n""");

sys.stdout.write("...... completed \n");sys.stdout.flush();
FileElement.close();
FileFixity.close();

sys.stdout.write("Written Boundary Condition (fixities.fei) \n");sys.stdout.flush();
sys.stdout.write("Written Analysis (main.fei) file \n\n\n");sys.stdout.flush();

sys.stdout.write("Thank You, and Have a great day !!\n");sys.stdout.flush();

