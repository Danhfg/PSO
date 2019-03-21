/**
 * @file	MonitoraAPI.cpp
 * @brief	Contém as funções que modificam o valor e a direção dos leds e do botão
 */

#include <unistd.h>
#include "APIGPIO.cpp"

enum power {
	off = 0,
	on = 1
};

/**
 * @brief	Ativa o led vermelho
 * @param	p	Valor a ser colocado na porta GPIO que está o led vermelho
 */
void setVermelho(power p){
	setDirection( 60, "out" );
	setValue( 60, to_string(p) );
}

/**
 * @brief	Ativa o led amarelo
 * @param	p	Valor a ser colocada na porta GPIO que está o led amarelo
 */
void setAmarelo(power p){
	setDirection( 50, "out" );
	setValue( 50, to_string(p) );
}

/**
 * @brief	Ativa o led verde
 * @param	p	Valor a ser colocada na porta GPIO que está o led verde
 */
void setVerde(power p){
	setDirection( 51, "out" );
	setValue( 51, to_string(p) );
}

/**
 * @brief	Modifica o valor de cada porta de cada led
 * @param	p	Valor a ser colocado nas portas dos leds
 */ 
void setAll(power p){
	setVermelho(p);
	setAmarelo(p);
	setVerde(p);
}

/**
 * @brief	Modifica a direção e o valor da porta GPIO 115 onde está o botão
 * @return	True caso esteja pressionado ou false caso contrário
 */
bool buttonIsPressed(){
	setDirection(115, "in");
	
	if(getValue(115) == 1)
		return true;
	else
		return false;
}