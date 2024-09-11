// code for spot drilling

%
O01

G21 (millimetre unit)
G90 (abs)
G00 X0 Y0 Z100.0 
G00 X-6.0 Y30.0 Z100.0
G00 X-6.0 Y30.0 Z3.0

M03 S4500 (start spindle with 8000 rpm)
G91 (relative)

G01 Z-4.0 F10.0

G00 Z100.0 (move back up)
M05 (stop spindle)

M30
%
