#ifndef GENBIN 
#define GENBIN

#include <sys/resource.h>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include "Definitions.h"

#define MAX_PREAMBLE 10000

/* If you change MAX_NR_VERTICES, change MAX_NR_VERTICESdiv8 to be
the 1/8th of it */
//#define NMAX 10000	/* maximum number of vertices handles */
#define MAX_NR_VERTICES		20000	/* = NMAX */
#define MAX_NR_VERTICESdiv8	(20000 / 8) 	/* = NMAX/8 */


using namespace std;

const char masks[ 8 ] = { 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80 };


class DIMACS_bin_format {
public:
	DIMACS_bin_format() {};
	DIMACS_bin_format(const char *infile );
	virtual ~DIMACS_bin_format() {};
	char get_edge(  int i,  int j );
	uint16_t Nr_vert;
	uint32_t Nr_edges;
	void write_graph_DIMACS_ascii( char *file);
private:

	void read_graph_DIMACS_bin( const char *file);
	int get_params(void);

	char Bitmap[MAX_NR_VERTICES][MAX_NR_VERTICESdiv8];

	char Preamble[MAX_PREAMBLE];

};

#endif
