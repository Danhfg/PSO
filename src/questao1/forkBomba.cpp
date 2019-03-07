/**
 * @file	forkBomba.cpp
 * @brief	Implementa a
 * @since	01.03.2019
 * @version 0.0.3
 */ 

#include <iostream>
using std::cout;
using std::endl;
using std::cerr;

#include <thread>
using std::thread;

#include <exception>
using std::exception;

/// BIBLIOTECAS UNIX/LINUX
#include <unistd.h>  		/// fork()		
#include <sys/time.h> 		/// pid_t
#include <sys/resource.h> 	/// rlimit

void forkBomb(){
	
	while(true){
		try{	
			fork();
		}
		catch( exception &e){
			cerr << "Erro na criação de processo..." << endl;
		}
	}			

}

int main(){

	thread thread1(forkBomb); /// Criando e iniciando a thread1 que contém o fork bomba
	struct rlimit limiteProcessos;

	getrlimit(RLIMIT_NPROC, &limiteProcessos);
	limiteProcessos.rlim_cur = 3;
	setrlimit(RLIMIT_NPROC, &limiteProcessos);	/// Modificando a quantidade de processos filhos para 3

	thread1.join(); /// Sincronizando esta thread com a thread Main

	return 0;
}
