#include <iostream>
using std::cout;
using std::endl;

#include <thread>
using std::thread;

#include <unistd.h>  		/// fork()		
#include <sys/time.h> 		/// pid_t
#include <sys/resource.h> 	/// rlimit

void forkBomb(){
	while(true)	
		fork();
}

int main(){

	thread thread1(forkBomb);
	
	struct rlimit limiteProcessos;
	getrlimit(RLIMIT_NPROC, &limiteProcessos);
	
	thread1.join();

	return 0;
}
