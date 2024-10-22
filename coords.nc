%
O01
G21 				(micron unit)
G90 				(abs)
G54
G00 X126.0 Y182.0	(move to coords: 127, 177, 25)
G00 Z12.0
M03 S4500			(Start spindle with 8000 rpm)
G91 				(relative)
G00 X-1500
(Spin and move 0.5mm down each step)
G02 I1500 Z-500 F20.0
G02 I1500 Z-500 F20.0

G02 I1500 Z-500 F20.0
G02 I1500 Z-500 F20.0

G02 I1500 Z-500 F20.0
G02 I1500 Z-500 F20.0

G02 I1500 Z-500 F20.0
G02 I1500 Z-500 F20.0

G00 Z100.0
M05 				(Stop spindle)

G90 				(absolute)
M30 				(end)
%