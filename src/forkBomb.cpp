#include <iostream>
using std::cout;
using std::endl;

#include <unistd.h>  		/// fork()		
#include <sys/time.h> 		/// pid_t
#include <sys/resource.h> 	/// rlimit


void forkBomb(){

	while(true)	
		fork();

}

int main(){

	struct rlimit limiteProcessos;
	getrlimit(RLIMIT_NPROC, &limiteProcessos);
	
	cout << limiteProcessos.rlim_cur << endl;	
	fork();
	getrlimit(RLIMIT_NPROC, &limiteProcessos);
	
	cout << limiteProcessos.rlim_cur << endl;	
	

	return 0;
}