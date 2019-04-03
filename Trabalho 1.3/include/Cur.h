#ifndef CUR_H_
#define CUR_H_

#include<iostream>

using namespace std;

class Cur{
	
	public:
		void saveCur();				// Salvar a posição do cursor
		void moveCur(const int x,const int y);	// Mova a posição do cursor para coordenadas (x, y)
		void resumeCur();		// Restaurar a posição do cursor
};

#endif

