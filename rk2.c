#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float func(float x, float y ) {

	return -2*y;


	}



void plot() {
	
	FILE *pipe = popen("gnuplot -persist \n","w");
	fprintf(pipe,"plot 'rungek2.dat'  \n");
	fprintf(pipe,"exit\n");
	pclose(pipe);





}

int  main()  {


	FILE *file;
	int i,j, Npoints, n;
	float *x, *y, h, h_fi, up_lmt = 2.0, low_lmt =0.0, S;
	Npoints = 50;


	char fname[20];

	x = (float *) malloc((Npoints+2)*sizeof(float));
	y =  (float *) malloc((Npoints+2)*sizeof(float));


	n = Npoints;
	h = (up_lmt - low_lmt)/Npoints;

	for (i = 0; i <= Npoints; i++) {
			
			x[i] = low_lmt + i*h;

			}


	y[0] = 1;
	file = fopen("rungek2.dat", "w");
	fprintf(file, "%f %f\n", x[0], y[0]);


	for (i  = 0; i <= Npoints; i++){

			h_fi = h*func(x[i], y[i]);
			
			y[i + 1] = y[i] + 0.5*h_fi +  0.5*h*func(x[i] + h, y[i] + h_fi) ;

			fprintf(file, "%f %f\n", x[i+1], y[i+1]);

			}


	fclose(file);

   plot();
	}
	
