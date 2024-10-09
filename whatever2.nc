%
O01

G21 (millimetre unit)
G90 (abs)
G00 X0 Y0 Z100.0 
G00 X26.0 Y30.0 Z100.0

M03 S15000 (start spindle with 8000 rpm)
G91 (relative)
G2 I2.0 J0 Z-500 F35.0
G2 I2.0 J0 Z-500 F35.0
G2 I2.0 J0 Z-500 F35.0
G2 I2.0 J0 Z-500 F35.0
G2 I2.0 J0 Z-500 F35.0
G2 I2.0 J0 Z-500 F35.0
G01 Z-50 F35

G00 Z100.0 (move back up)
M05 (stop spindle)

M30
%
