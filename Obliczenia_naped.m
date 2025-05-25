%% obliczenie sił i momentów (dane wzięte z EXCELA z CFD godnoli)

% Z0 - kąt wychylenia 0 stopni 
dragCalkowityZ0 = 78.4; 
dragPylonZ0 = 73.77; 
dragGondolaZ0 = 2.88; 
DragSkrzydlaZ0=1.78; 

% Z1 - kąt wychylenia 43 stopnie
dragCalkowity_Z1 = 597.66;
dragPylon_Z1 = 336.51;
dragGondola_Z1 = 14.93; 
DragSkrzydla_Z1 = 14.92; 

Fwyp =(dragCalkowity_Z1 - DragSkrzydla_Z1) - (dragCalkowityZ0 - DragSkrzydlaZ0)

r = 0.2; % promień słoneczka
Mobr = Fwyp * r; % potrzebny moment 

%% założone parametry silika i wymagana omega
Msilnika = 1.2; 
ObrSilnika = 3000; 
Omega_docelowa = (80/360)*(60/2)

%% przekładnia planetarna
przelozenie_planetarna = 30; 
Planetarna_M_Output = Msilnika * przelozenie_planetarna;
Planetarna_Omega_Output = ObrSilnika/przelozenie_planetarna;

%% przekładnia łancuchowa
Przelozenie_lancuchowa = 4;
Lancuchowa_M_output = Planetarna_M_Output * Przelozenie_lancuchowa;
Lancuchowa_Omega_output = Planetarna_Omega_Output / Przelozenie_lancuchowa;

%% uzyskana omega
Omega_koncowa = Lancuchowa_Omega_output/60 % omega w obrotach/sekunde
Moment_koncowy = Lancuchowa_M_output