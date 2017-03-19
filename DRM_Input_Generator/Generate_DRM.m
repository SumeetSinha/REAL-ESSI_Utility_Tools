
% ###########################################################################################################################
% #                                                                                                                         #
% #  Generate_DRM :: Matlab Scrript to generate DRM Input                                                                   #
% #  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                                      #
% #                                                                                                                         #
% #                                                                                                                         #
% #  GITHUB:: https://github.com/SumeetSinha/gmESSI.git                                                                     #
% #                                                                                                                         #
% #                                                                                                                         #
% #  Sumeet Kumar Sinha (September,2016)                                                                                    #
% #  Computational Geomechanics Group                                                                                       #
% #  University of California, Davis                                                                                        #
% #  s u m e e t k s i n h a . c o m                                                                                        #
% ########################################################################################################################### 

filename = 'DRM_Input.h5';
delete (filename);

% create hdf5 file
fcpl = H5P.create('H5P_FILE_CREATE');
fapl = H5P.create('H5P_FILE_ACCESS');
fileID = H5F.create('DRM_Input.h5','H5F_ACC_TRUNC',fcpl,fapl);

% % datatype id 
% DoubleDatatypeID = H5T.copy('H5T_NATIVE_DOUBLE');
% FloatDatatypeID = H5T.copy('H5T_NATIVE_FLOAT');
% IntDatatypeID = H5T.copy('H5T_NATIVE_INT');

% generate time vector and write time data 
Time = [0.01:0.01:81.92];
Time = Time';

Number_Of_Time_Steps = size(Time,1);

dims = size(Time,1);
dataspaceID = H5S.create_simple(1,dims,[]);
datasetname = 'Time';
datatypeID = H5T.copy('H5T_NATIVE_DOUBLE');
datasetID = H5D.create(fileID,datasetname,datatypeID,dataspaceID,'H5P_DEFAULT');
H5D.write(datasetID,'H5ML_DEFAULT','H5S_ALL','H5S_ALL','H5P_DEFAULT',Time);
H5D.close(datasetID);
H5S.close(dataspaceID);
H5T.close(datatypeID);


% generate elements vector and write element data 
load './DrmInputs/Elements.txt';
dims = size(Elements,1);
dataspaceID = H5S.create_simple(1,dims,[]);
datasetname = 'Elements';
datatypeID = H5T.copy('H5T_NATIVE_INT');
datasetID = H5D.create(fileID,datasetname,datatypeID,dataspaceID,'H5P_DEFAULT');
H5D.write(datasetID,'H5ML_DEFAULT','H5S_ALL','H5S_ALL','H5P_DEFAULT',Elements);
H5D.close(datasetID);
H5S.close(dataspaceID);
H5T.close(datatypeID);


% generate elements vector and write element data 
load './DrmInputs/Nodes.txt';
dims = size(Nodes,1);
NumNodes = size(Nodes,1);
dataspaceID = H5S.create_simple(1,dims,[]);
datasetname = 'DRM Nodes';
datatypeID = H5T.copy('H5T_NATIVE_INT');
datasetID = H5D.create(fileID,datasetname,datatypeID,dataspaceID,'H5P_DEFAULT');
H5D.write(datasetID,'H5ML_DEFAULT','H5S_ALL','H5S_ALL','H5P_DEFAULT',Nodes);
H5D.close(datasetID);
H5S.close(dataspaceID);
H5T.close(datatypeID);


% finding exterior nodes and interior nodes 
load './DrmInputs/InteriorNodes.txt';
Number_Of_Boundary_Nodes = size(InteriorNodes,1);
Number_Of_Exterior_Nodes = NumNodes - Number_Of_Boundary_Nodes;
Is_Boundary_Node = Nodes.*0;

for i = 1:NumNodes
	for j = 1:Number_Of_Boundary_Nodes
		if(Nodes(i)==InteriorNodes(j))
			Is_Boundary_Node(i) = 1;
			break;
		end
	end
end

% writing is boundary node information
dims = size(Is_Boundary_Node,1);
dataspaceID = H5S.create_simple(1,dims,[]);
datasetname = 'Is Boundary Node';
datatypeID = H5T.copy('H5T_NATIVE_INT');
datasetID = H5D.create(fileID,datasetname,datatypeID,dataspaceID,'H5P_DEFAULT');
H5D.write(datasetID,'H5ML_DEFAULT','H5S_ALL','H5S_ALL','H5P_DEFAULT',Is_Boundary_Node);
H5D.close(datasetID);
H5S.close(dataspaceID);
H5T.close(datatypeID);


% writing Number of Boundary Nodes
dims = size(Number_Of_Boundary_Nodes,1);
dataspaceID = H5S.create_simple(1,dims,[]);
datasetname = 'Number of Boundary Nodes';
datatypeID = H5T.copy('H5T_NATIVE_INT');
datasetID = H5D.create(fileID,datasetname,datatypeID,dataspaceID,'H5P_DEFAULT');
H5D.write(datasetID,'H5ML_DEFAULT','H5S_ALL','H5S_ALL','H5P_DEFAULT',Number_Of_Boundary_Nodes);
H5D.close(datasetID);
H5S.close(dataspaceID);
H5T.close(datatypeID);


% writing Number of Exterior Nodes
dims = size(Number_Of_Exterior_Nodes,1);
dataspaceID = H5S.create_simple(1,dims,[]);
datasetname = 'Number of Exterior Nodes';
datatypeID = H5T.copy('H5T_NATIVE_INT');
datasetID = H5D.create(fileID,datasetname,datatypeID,dataspaceID,'H5P_DEFAULT');
H5D.write(datasetID,'H5ML_DEFAULT','H5S_ALL','H5S_ALL','H5P_DEFAULT',Number_Of_Exterior_Nodes);
H5D.close(datasetID);
H5S.close(dataspaceID);
H5T.close(datatypeID);


% writing Accelerations
Accelerations = rand(3*Number_Of_Boundary_Nodes,Number_Of_Time_Steps);
load 'acc.dat';
for i = 1:Number_Of_Boundary_Nodes;
	Accelerations(3*(i-1)+1,:) = zeros(1,Number_Of_Time_Steps);
end

Accelerations(1,:)
dims = size(Accelerations);
dataspaceID = H5S.create_simple(2,dims,[]);
datasetname = 'Accelerations';
datatypeID = H5T.copy('H5T_NATIVE_DOUBLE');
datasetID = H5D.create(fileID,datasetname,datatypeID,dataspaceID,'H5P_DEFAULT');
H5D.write(datasetID,'H5ML_DEFAULT','H5S_ALL','H5S_ALL','H5P_DEFAULT',Accelerations(:)'');

H5D.close(datasetID);
H5S.close(dataspaceID);
H5T.close(datatypeID);



% % writing Displacements
% Displacements = zeros(3*Number_Of_Boundary_Nodes,size(Time,1));
% load 'disp.dat';
% for x = 1:Number_Of_Boundary_Nodes;
% 	Displacements(3*(x-1)+1,:) = disp;
% end
% dims = size(Displacements);
% dataspaceID = H5S.create_simple(2,dims,[]);
% datasetname = 'Displacements';
% datatypeID = H5T.copy('H5T_NATIVE_DOUBLE');
% datasetID = H5D.create(fileID,datasetname,datatypeID,dataspaceID,'H5P_DEFAULT');
% H5D.write(datasetID,'H5ML_DEFAULT','H5S_ALL','H5S_ALL','H5P_DEFAULT',Displacements);
% H5D.close(datasetID);
% H5S.close(dataspaceID);
% H5T.close(datatypeID);





















% close hdf5 file
H5F.close(fileID);
