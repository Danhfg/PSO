#include <iostream>
using std::cout;
using std::endl;

#include <sys/types.h> /// pid_t
#include <unistd.h> /// fork()
#include <dirent.h> /// readdir()

#include <thread>
using std::thread;

int main(){

	DIR *diretorio = nullptr;
	struct dirent *ent = nullptr;
	int numeroTotalProcessos = 0;
	thread threadBackground;

	diretorio = opendir("/proc");

	while( true ){
		
		if( !diretorio)		/// Verificando se a abertura foi feita corretamente
			return -1;

		while ( (ent = readdir(diretorio) )!= nullptr ){ /// Fazendo leitura de processos
			cout << ent->d_name << endl;
			++numeroTotalProcessos;
		}

		cout << "Total de processos:" 
			 << numeroTotalProcessos 
			 << endl 
			 << endl 
			 << endl;
	}	
	return 0;

}
