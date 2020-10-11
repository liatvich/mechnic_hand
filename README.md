 # mechanic hand

We aim to build a generalized process that creates a working simulation from a robot model that is general, can be implemented on any robot, clear and easy to implement as possible

# Simulation steps
Let’s go over each step,
1) After the Mechanical Engineer finishes designing a robotic model in any chosen software, he saves a robot model a .CAD file. 
2) Fusion 360 integration step - our workflow contains additional model processing, we choose to do those processes in ‘Fusion 360’ since it is light and easy to use.
  a. Produce a folder with all the model parts saved as .stl file. Each part file name should indicate the link this file is a part of. 
File name convention is - {link number} {part name}.stl  
Example - 
1 part_name.stl
2 part_name.stl
3 part_name.stl
… 
number indicates which parts are grouped together and controlled by the same armature
multiple parts can be put in the same group if needed
  b. Produce spherical markers at approximate joint locations. 
File name convention is - DBone{link name}_{transformation constraint axis}.stl  
Example - 
DBone1_XYZ.stl
DBone2_XZ.stl
DBone3_YZ.stl
… 
each object marks the start and end locations for armature bones
the combination of X, Y, or Z notes which axis of motion are restricted for the joint
DBone stands for - Device Bone
Blender Add-on: 
The panel purpose is to guide the user each step to the end simulation.

