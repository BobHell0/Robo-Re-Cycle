%
O01

G21 (millimetre unit)
G90 (abs)
G00 X0 Y0 Z100.0 
G00 X20.0 Y47.0 Z73.0

M03 S8000 (start spindle with 8000 rpm)
G91 (relative)
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0
G2 I2.0 J0 Z-500 F75.0

G00 Z100.0 (move back up)
M05 (stop spindle)

M30
%