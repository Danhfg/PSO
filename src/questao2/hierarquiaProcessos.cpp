/**
 * @file	hierarquiaProcessos.cpp
 * @brief	Implementa a
 * @since	01.03.2019
 * @version 0.0.2
 */ 

#include <iostream>
using std::cout;
using std::endl;
using std::cerr;

#include <string>
using std::string;

#include <thread>
using std::thread;

/// BIBLIOTECA UNIX/LINUX
#include <sys/types.h> /// pid_t
#include <unistd.h> /// fork()
#include <dirent.h> /// readdir()

void quantidadeDeProcessos(){
	
	int numeroTotalProcessos = 0;
	DIR *diretorio = nullptr;
	struct dirent *ent = nullptr;
	
	diretorio = opendir("/proc");

	while( true ){
			
		if( !diretorio)		/// Verificando se a abertura foi feita corretamente
			break;

		while ( (ent = readdir(diretorio) )!= nullptr ){ /// Fazendo leitura de processos
			
			if( string(ent->d_name)[0] >= '0' && string(ent->d_name)[0] <= '9'  ){
				
		//		cout << "Name:" << ent->d_name << "    "
		//			<<	"Ino:" << ent->d_ino << "    "
		//			<<	"Off:" << ent->d_off << "    "
		//			<<	"Reclen:" << ent->d_reclen << "    "
		//			<<	"Type:" << ent->d_type << "    "
		//			<< endl;
				
				++numeroTotalProcessos;
			}

		}

		cout << "Total de processos: " 
			<< numeroTotalProcessos 
			<< endl
			<< endl;
	}

}

void processo(int ppid){

	// TODO

}

int main(int argc, char* argv[] ){

	if( argc != 2){ 	
		cerr << "Indique o pid do processo..." << endl;
		exit(1);
	}

	thread thread1(quantidadeDeProcessos);
	thread thread2( processo, atoi(argv[1]) );

	thread1.detach();

	return 0;

}
