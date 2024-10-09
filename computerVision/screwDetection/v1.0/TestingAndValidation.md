# Testing and Validating V1.0

In the zip file *TestingAndValidation.zip*, there are 16 separated directories 
named predict, predict2, predict3, ..., predict16. Each of these directories have 
photographs of the hard drive taken by a Samsung Galaxy A14 camera, at an angle of 
30 degrees, 340 mm away. Through random experimentation and adjustment, it was 
discovered that the most dominant factor in the performance of the model was the 
level of zoom applied. 

Prediction sets 1 to 5 showed little encouraging results. In particular the middle 
(hidden) screw was often missed or had a very low confidence score associated with
it. It was only the last image in set 6, where a more zoomed in photograph was used 
for the model, when more promising results occured. From set 7 and onwards, 
different zooms were experimented with. Using 1.5x, 2x, 2.5x and 3x zoom in set 7, 
it was decided that 2.5x zoom was sufficient for adaquete screw detection. 

This decision was further validated using sets 10 to 16. Each set includes 30 
photos with the camera positioned in the same spot, now using a 2.5x zoom. The 
differences between each set is the position of the bedroom lamp on what area 
of the hard drive it is shining. Set 16 had the best results, with no screw misses
(although occasionally the model thought a certain box was both a screw AND a hole).
This particular set was achieved by positioning the bedroom lamp such that the 
light reflected off the front of the hard drive.