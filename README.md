# Robo-Re-Cycle
## Problem Definition
The lack of efficient waste management practices have lead to the environmentally damaging disposal of outdated technology such as Hard Disk Drives (HDD). Most often waste ends up in landfill and causes soil/ land pollution with the metals from the HDD/ technology. Our project partner [Veolia](https://www.veolia.com/en) wants a method to dismantle hard disk drives (HDDs) autonomously to create a cost effective solution over landfill. This project will focus on designing and implementing a scalable HDD disassembly system for Veolia. 

This leads us to the question what is the most time efficient, effective, versatile and cost effective machinery/ technology needed to automatically disassemble a HDD? 

## Current Assumptions and Constraints
Our primary goal for this year is to create a system that is able to, from start to end, complete one disassembley action. Specifically, in terms of the hard drive, we aim to be able to remove the top plate the hard drive. The requirements to remove the top plate *manually* were to peel off the label on the plat, remove 7 torx screws, and finally pry off the top plate. 

## What we've got so far
The current solution consists of the following subsystems:

### Milling Machine
To carry out the disassembley actions required to dismantle the hard drive, we are using a milling machine. The particular milling machine we are using is the [Roland MDX-50 Modella](https://www.rolanddg.com.au/products/3d-printers-and-milling-machines/mdx-50-benchtop-cnc-mill). The advantage of a milling machine is that to remove fasteners (screws), we do not need to necessarily apply a tool directly onto the screw head (which requires a high degree of accuracy and dexterity) but instead we can mill around the fastener, allowing for a larger margin of error. Roland's MDX-50 Modella seems to be very reliable in its accuracy and so makes it an attractive choice of milling machine to use for this project.

### Computer Vision System
To locate the fasteners that keep the hard drive in tact, we have opted to use computer vision. The computer vision's primary job is to determine the positions of these fasteners in 2 dimensional space and communicate these positions to the milling machine. The algorithm used to train the computer vision model is YOLOv8 due to the ease of running the algorithm using Python package [ultralytics](https://github.com/ultralytics/ultralytics). 

### G Code Generator
The milling machine is able to read G code, which details an ordered set of instructions for the milling machine to follow. These instructions can be written manually and provided to the machine. To automate this process, a C++ program has been written which is able to write a file with the necessary G code instructions to mill around the fasteners that the computer vision system would have detected. 

### Clamping System
Due to the forces that the milling machine will apply onto the hard drive there is great risk that the hard drive would not stay still unless adaqueate clamping force was provided. 
### Gripper System
The purpose of the gripper system is to remove components that have had all fasteners detached from them. 



## Current documentation and files (likely to import)
- Presentation Slides ([[Term 1](https://docs.google.com/presentation/d/1cy9JzwfEjW_DLN2l6dtpn3kHG1GwHWmRwFtHIFFM_yo/edit?usp=sharing)] | [[Term 2](https://docs.google.com/presentation/d/1I5F65S-NLMF_B2HonFfnrOjBbekZeMwIi9J3JsQ251A/edit?usp=sharing)] 
- [[Google Drive](https://drive.google.com/drive/folders/1G941kPrP4c3bWLbQYe293UxuC4xKIOE8?usp=sharing)] 
