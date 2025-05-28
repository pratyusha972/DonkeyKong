matrix = [[]]
for i in range(0,79):
	matrix[0].append("X")
for i in range(1,29):	
	matrix.append([])
	matrix[i].append("X")
	for j in range(1,78):
		matrix[i].append(" ")
	matrix[i].append("X")
matrix.append([])	 
for i in range(0,79):
	matrix[29].append("X")
for i in range(10,21):
	matrix[2][i]="X"
for i in range(1,60):
	matrix[5][i]="X"
for i in range(20,79):
	matrix[9][i]="X"
for i in range(1,46):
	matrix[13][i]="X"
for i in range(30,79):
	matrix[17][i]="X"
for i in range(1,68):
	matrix[21][i]="X"
for i in range(40,79):
	matrix[25][i]="X"
matrix[1][10]="X"
matrix[1][20]="X"
matrix[1][13]="Q"
for i in range (2,5):
	matrix[i][17]="H"
for i in range (5,9):
	matrix[i][56]="H"
for i in range (9,13):
	matrix[i][24]="H"
for i in range (13,17):
	matrix[i][35]="H"
for i in range (17,21):
	matrix[i][64]="H"
for i in range (21,25):
	matrix[i][44]="H"
for i in range (25,29):
	matrix[i][70]="H"


