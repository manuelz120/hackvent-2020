/* Dimacs graph format translator to and from a binary, more efficient
   format. Written by Tamas Badics (badics@rutcor.rutgers.edu), 
   using the technique of Marcus Peinado, Boston University. */
/*
   Corrected to number nodes from 1 to n (not 0 to n-1)
   MT
*/

#include "bin2asc.h"

extern const char masks[];
/* ============================================= */
DIMACS_bin_format::DIMACS_bin_format( const char *infile )
{
	read_graph_DIMACS_bin( infile );
	write_graph_DIMACS_ascii( "test.txt" );
}



char DIMACS_bin_format::get_edge(  int i,  int j )
{
	int byte, bit;
	char mask;
	
	bit  = 7-(j & 0x00000007);
	byte = j >> 3;
	
	mask = masks[bit];
	return( (Bitmap[i][byte] & mask)==mask );
}

/* ============================================= */

void DIMACS_bin_format::write_graph_DIMACS_ascii( char *file)
{
	int i,j;
	FILE *fp;
	
	if ( (fp=fopen(file,"w"))==NULL )
	  { printf("ERROR: Cannot open outfile\n"); exit(10); }
	
	fprintf(fp, "%s",Preamble);
	
	for ( i = 0; i<Nr_vert; i++ )
	  {
		  for ( j=0; j<=i; j++ )
			if ( get_edge(i,j) ) fprintf(fp,"e %d %d\n",i+1,j+1 );
	  }
	
	fclose(fp);
}

void DIMACS_bin_format::read_graph_DIMACS_bin( const char *file)
{

	int i, length = 0;
	FILE *fp;
	
	if ( (fp=fopen(file,"r"))==NULL )
	  { printf("ERROR: Cannot open infile\n"); exit(10); }

	if (!fscanf(fp, "%d\n", &length))
	  { printf("ERROR: Corrupted preamble.\n"); exit(10); }

	if(length >= MAX_PREAMBLE)
	  { printf("ERROR: Too long preamble.\n"); exit(10); }
		   
	fread(Preamble, 1, length, fp);
	Preamble[length] = '\0';
	
	if (!get_params())
		  { printf("ERROR: Corrupted preamble.\n"); exit(10); }

	printf("Done reading preamble: %d %d\n", Nr_vert, Nr_edges);

	for ( i = 0
		 ; i < Nr_vert && fread(Bitmap[i], 1, (int)((i + 8)/8), fp)
		 ; i++ );

	printf("Done reading into bitmap\n");

	fclose(fp);

}

int DIMACS_bin_format::get_params(void)
                      /* getting Nr_vert and Nr_edge from the preamble string, 
						 containing Dimacs format "p ??? num num" */
{
	char c, *tmp;
	char * pp = Preamble;
	int stop = 0;
	tmp = (char *)calloc(100, sizeof(char));
	
	Nr_vert = Nr_edges = 0;
	
	while (!stop && (c = *pp++) != '\0'){
		switch (c)
		  {
			case 'c':
			  while ((c = *pp++) != '\n' && c != '\0');
			  break;
			  
			case 'p':
			  sscanf(pp, "%s %hu %u\n", tmp, &Nr_vert, &Nr_edges);
			  stop = 1;
			  break;
			  
			default:
			  break;
		  }
	}
	
	free(tmp);
	
	if (Nr_vert == 0 || Nr_edges == 0)
	  return 0;  // error
	else
	  return 1;
	

}


int main( int argc, const char *argv[] ) {


	const rlim_t kStackSize = 10L * 1024L * 1024L;   // min stack size = 64 Mb
	struct rlimit rl;
	int result;

	result = getrlimit(RLIMIT_STACK, &rl);
	cout<<"max stack size in bytes: "<< rl.rlim_cur <<endl;
	if (result == 0)
	{
		if (rl.rlim_cur < kStackSize)
		{
			rl.rlim_cur = kStackSize;
			result = setrlimit(RLIMIT_STACK, &rl);
			if (result != 0)
			{
				fprintf(stderr, "setrlimit returned result = %d\n", result);
			}
		}
	}
	else
		cerr<<"Could not determine stack size"<<endl;

	cout<<"max stack size in bytes: "<< rl.rlim_cur <<endl;
	new DIMACS_bin_format(argv[1]);
	return 1;
}

