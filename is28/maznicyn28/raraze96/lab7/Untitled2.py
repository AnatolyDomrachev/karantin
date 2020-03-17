def vvod_dannyh():
 x = [];
 for i in range(0,5):
  x.append(int(input()));
  y = [];
 for i in range(0,5):
  y.append(int(input()));
  z = [];
 for i in range(0,5):
  z.append(int(input()));
 return x,y,z
def raschet(x,y,z):
 xmin = x[0];
 ymin = y[0];
 zmin = z[0];
 for i in range(1,5):
  if (x[i] < xmin):
   xmin = x[i];
 for i in range(1,5):
  if (y[i] < ymin):
   ymin = y[i];
 for i in range(1,5):
  if (z[i] < zmin):
   zmin = z[i];
 ming = xmin;ind = "x";mass = x;
 if (ymin > ming):
  ming = ymin; ind = "y";mass = y;
 if (zmin > ming):
  ming = zmin; ind = "z";mass = z;
  
  
 return mass,ind
def vyvod_resultata():
 print(mass , " - " , ind);

x,y,z = vvod_dannyh();
mass,ind = raschet(x,y,z);
vyvod_resultata();
   