/*
 * Definitions.h
 *
 *  Created on: Jul 23, 2010
 *      Author: marco
 */

#ifndef DEFINITIONS_H_
#define DEFINITIONS_H_

#include <cstdio>
#include <cmath>
#include <climits>
#include <cfloat>
#include <cassert>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>

/*
 * Boolean values
 */
#ifndef  BOOL// used in bin reader
#define BOOL	char
#endif

#ifndef Bool
#define Bool uint8_t                    /**< type used for boolean values */
#ifndef TRUE
#define TRUE  1                         /**< boolean value TRUE */
#define FALSE 0                         /**< boolean value FALSE */
#endif
#endif

#define VERSION                500 /**< version number (multiplied by 100 to get integer number) */
#define SUBVERSION               0 /**< sub version number */
#define COPYRIGHT   "Marco"

enum RetCode {
	OKAY = 1,
	PARSEERROR = 2,
	INVALIDDATA = 3,
	MEMORYERROR = 4,
	PARAMETERUNKNOWN = 5,
	PARAMETERWRONGTYPE = 6
};
typedef enum RetCode RETCODE;

/*
 * Long Integer values
 */

#ifndef __STDC_LIMIT_MACROS
#define __STDC_LIMIT_MACROS
#endif
#include <stdint.h>
/* http://en.wikipedia.org/wiki/Stdint.h */


#define ULongint uint_64_t //unsigned long long                         /**< type used for long integer values */
#ifndef ULLONG_MAX
#define ULLONG_MAX	UINT64_MAX //=18446744073709551615  //9223372036854775807ULL*2
#define ULLONG_MIN	0  //(-LLONG_MAX - 1LL)
#endif

#ifndef LLONG_MAX
#define LLONG_MAX	INT64_MAX //=9,223,372,036,854,775,807 //9223372036854775807LL
#define LLONG_MIN	INT64_MIN //(-LLONG_MAX - 1LL)
#endif

#define Longint int64_t  //long long                         /**< type used for long integer values */
#define LONGINT_MAX          LLONG_MAX
#define LONGINT_MIN          LLONG_MIN
#ifndef LONGINT_FORMAT
#if defined(_WIN32) || defined(_WIN64)
#define LONGINT_FORMAT           "I64d"
#else
#define LONGINT_FORMAT           "lld"
#endif
#endif

#define Int int32_t
#ifndef INT_MAX
#define INT_MAX INT32_MAX // 2,147,483,647
#define INT_MIN INT32_MIN // -2,147,483,647
#endif

#define Shortint int16_t
#ifndef SINT_MAX
#define SINT_MAX INT16_MAX // 2,147,483,647
#define SINT_MIN INT16_MIN // -2,147,483,647
#endif


#define fvalue int32_t
#define FVALUE_MAX  INT32_MAX

#define Color int16_t // could be int16_t 32,767 // need -1 as no color sometimes
#define COLOR_MAX INT16_MAX
#define Vertex uint16_t // could be int16_t max 65,535
#define VERTEX_MAX UINT16_MAX


typedef std::vector<Color> ColorMap;
typedef std::set<Vertex> VertexSet;

#ifndef HAVE_BASENAME
#define basename(s) (strrchr((s), '/') == NULL ? (s) : strrchr((s), '/') + 1)
#endif

/*
 * Floating point values
 */

#define Real double                               /**< type used for floating point values */
#define REAL_MAX         (Real)DBL_MAX
#define REAL_MIN        -(Real)DBL_MAX
#define REAL_FORMAT               "lf"

#define DEFAULT_INFINITY         1e+20  /**< default value considered to be infinity */
#define DEFAULT_EPSILON          1e-09  /**< default upper bound for floating points to be considered zero */
#define DEFAULT_SUMEPSILON       1e-06  /**< default upper bound for sums of floating points to be considered zero */
#define DEFAULT_FEASTOL          1e-06  /**< default feasibility tolerance for constraints */
#define DEFAULT_DUALFEASTOL      1e-09  /**< default feasibility tolerance for reduced costs */
#define DEFAULT_BARRIERCONVTOL   1e-10  /**< default convergence tolerance used in barrier algorithm */
#define DEFAULT_BOUNDSTREPS       0.05  /**< default minimal relative improve for strengthening bounds */
#define DEFAULT_PSEUDOCOSTEPS    1e-01  /**< default minimal variable distance value to use for pseudo cost updates */
#define DEFAULT_PSEUDOCOSTDELTA  1e-04  /**< default minimal objective distance value to use for pseudo cost updates */
#define MAXEPSILON               1e-03  /**< maximum value for any numerical epsilon */
#define MINEPSILON               1e-20  /**< minimum value for any numerical epsilon */
#define INVALID                  1e+99  /**< floating point value is not valid */
#define UNKNOWN                  1e+98  /**< floating point value is not known (in primal solution) */

#define REALABS(x)        (fabs(x))
#define EPSEQ(x,y,eps)    (REALABS((x)-(y)) <= (eps))
#define EPSLT(x,y,eps)    ((x)-(y) < -(eps))
#define EPSLE(x,y,eps)    ((x)-(y) <= (eps))
#define EPSGT(x,y,eps)    ((x)-(y) > (eps))
#define EPSGE(x,y,eps)    ((x)-(y) >= -(eps))
#define EPSZ(x,eps)       (REALABS(x) <= (eps))
#define EPSP(x,eps)       ((x) > (eps))
#define EPSN(x,eps)       ((x) < -(eps))
#define EPSFLOOR(x,eps)   (floor((x)+(eps)))
#define EPSCEIL(x,eps)    (ceil((x)-(eps)))
#define EPSFRAC(x,eps)    ((x)-EPSFLOOR(x,eps))
#define EPSISINT(x,eps)   (EPSFRAC(x,eps) <= (eps))

#ifndef SQR
#define SQR(x)        ((x)*(x))
#define SQRT(x)       (sqrt(x))
#endif

#ifndef ABS
#define ABS(x)        ((x) >= 0 ? (x) : -(x))
#endif

#ifndef MAX
#define MAX(x,y)      ((x) >= (y) ? (x) : (y))     /**< returns maximum of x and y */
#define MIN(x,y)      ((x) <= (y) ? (x) : (y))     /**< returns minimum of x and y */
#endif

#ifndef MAX3
#define MAX3(x,y,z) ((x) >= (y) ? MAX(x,z) : MAX(y,z))  /**< returns maximum of x, y, and z */
#define MIN3(x,y,z) ((x) <= (y) ? MIN(x,z) : MIN(y,z))  /**< returns minimum of x, y, and z */
#endif

/*
 * Pointers
 */

#ifndef NULL
#define NULL ((void*)0)                 /**< zero pointer */
#endif

/*
 * Strings
 */

#define MAXSTRLEN             1024 /**< maximum string length in  */
#if defined(_WIN32) || defined(_WIN64)
#define snprintf _snprintf
#define vsnprintf _vsnprintf
#define strcasecmp _stricmp
#define strncasecmp _strnicmp
#endif

/*
 * Memory settings
 */

#define HASHSIZE_NAMES      131101 /**< size of hash table in name tables */
#define HASHSIZE_CUTPOOLS   131101 /**< size of hash table in cut pools */
#define HASHSIZE_CLIQUES    131101 /**< size of hash table in clique tables */
#define HASHSIZE_PARAMS       4099 /**< size of hash table in parameter name tables */
#define HASHSIZE_VBC        131101 /**< size of hash map for node -> nodenum mapping used for VBC output */

/*#define BMS_NOBLOCKMEM*/

/*
 * Global debugging settings
 */

/*#define DEBUG*/

/*
 * Defines for handling  return codes
 */

#define ABORT() assert(FALSE)

#define CALL_ABORT_QUIET(x)  do { if( (x) != OKAY ) ABORT(); } while( FALSE )
//#define CALL_QUIET(x)        do { RETCODE _restat_; if( (_restat_ = (x)) != OKAY ) return _restat_; } while( FALSE )
#define CALL_QUIET(x)
#define ALLOC_ABORT_QUIET(x) do { if( NULL == (x) ) ABORT(); } while( FALSE )
#define ALLOC_QUIET(x)       do { if( NULL == (x) ) return NOMEMORY; } while( FALSE )

#define CALL_ABORT(x) do                                                                                 \
                       {                                                                                      \
                          RETCODE _restat_;                                                              \
                          if( (_restat_ = (x)) != OKAY )                                                 \
                          {                                                                                   \
                             printf("Error <%d> in function call\n", _restat_);                     \
                             ABORT();                                                                     \
                          }                                                                                   \
                       }                                                                                      \
                       while( FALSE )

#define ALLOC_ABORT(x) do                                                                                \
                       {                                                                                      \
                          if( NULL == (x) )                                                                   \
                          {                                                                                   \
                             printf("No memory in function call\n", __FILE__, __LINE__);            \
                             ABORT();                                                                     \
                          }                                                                                   \
                       }                                                                                      \
                       while( FALSE )

#define CALL(x)   do                                                                                     \
                       {                                                                                      \
                          RETCODE _restat_;                                                              \
                          if( (_restat_ = (x)) != OKAY )                                                 \
                          {                                                                                   \
                             printf("Error <%d> in function call\n", _restat_);                     \
                             return _restat_;                                                                 \
                           }                                                                                  \
                       }                                                                                      \
                       while( FALSE )

#define ALLOC(x)  do                                                                                     \
                       {                                                                                      \
                          if( NULL == (x) )                                                                   \
                          {                                                                                   \
                             printf("No memory in function call\n");                                \
                             return NOMEMORY;                                                            \
                          }                                                                                   \
                       }                                                                                      \
                       while( FALSE )

/**
 * Further definitions due to GCP
 * Numbers have been assigned chaotically
 * during the development phase
 * and have not been rearranged since then
 */


#define ASCII_FORMAT	1
#define GZIP_FORMAT	2
#define BIN_FORMAT	3


#define PARTIAL_REPR	1
#define COMPLETE_REPR	0

// For tabu length policy
#define TL_ADAPTIVE 1
#define TL_INTERVAL 2
#define TL_FIXED 3

// For inverse type
#define INV_OLD 1
#define INV_NEW 2
#define INV_NEWOLD 3
#define INV_VERTEX 4
#define VLSN 5

// For solver
#define CONSTRUCTION_HEUR	100
#define RANDOM_RESTART	0
#define FIXED_K_COL	1
#define	SEQUENCE_K_COL	2
#define HYBRID_EA	4
#define	PENALTY_FUNCTION 6
#define HEA_RLF	12
#define X_RLF_SOLVER	5
#define PORUMBELS_EA	110
#define MALAGUTIS_EA	120
#define EX_DSATUR_SOLVER 130

// For Runner
#define BASIC	0
#define TABUCOL	1
#define PARTIALCOL 2
#define TABU_HASH	11
#define TABU_REACTIVE	12
#define TABU_VLSN	26
#define SA_KEMPE 45
#define GLS	50
#define ILS	60
#define	NOVELTY 70
#define	MIN_CONFLICT 71
#define X_RLF_RUNNER 30
#define EX_DSATUR_RUNNER 130

//For Construction Heuristics
//init
#define RANDOM	0
#define ROS	1
#define ROS_FIXED	2
#define RLF	3
#define	RLF_FIXED	4
#define DSATUR	5
#define DSATUR_FIXED	6
#define	FROM_INPUT_FILE	7
#define	RLF_STATIC	9
#define	RLF_REVERSE	11

#define CONFLICT_EDGES
#endif /* DEFINITIONS_H_ */
