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

#include <system_error>
using std::system_error;

/// BIBLIOTECAS UNIX/LINUX
#include <unistd.h>  		/// fork()		
#include <sys/time.h> 		/// pid_t
#include <sys/resource.h> 	/// rlimit

void forkBomb(){

	while(true){
		try{	
			fork();
		}
		catch( const system_error &e){
			
			cerr << "Erro no fork (EAGAIN: " 
				 << e.code() 
				 << " ) - " 
				 << e.what()
				 << endl;
		}
	}			

}

int main(){

	struct rlimit limiteProcessos;

	getrlimit(RLIMIT_NPROC, &limiteProcessos);

	cout << "(ANTES) - "
		 << "limite atual: "
		 << limiteProcessos.rlim_cur 
		 << " limite maximo: "
		 << limiteProcessos.rlim_max 
		 << endl;	///-> NÃO ESQUECER DE APAGAR DEPOIS!

	limiteProcessos.rlim_cur = 1500;
	setrlimit(RLIMIT_NPROC, &limiteProcessos);	/// Modificando a quantidade de processos filhos para 3

	cout << "(DEPOIS) - "
		 << "limite atual: "
		 << limiteProcessos.rlim_cur 
		 << " limite maximo: "
		 << limiteProcessos.rlim_max 
		 << endl 
		 << endl;		///-> NÃO ESQUECER DE APAGAR DEPOIS!
	
	thread thread1(forkBomb); /// Criando e iniciando a thread1 que contém o fork bomba
	thread1.detach(); /// Sincronizando esta thread com a thread Main
	
	return 0;
}
