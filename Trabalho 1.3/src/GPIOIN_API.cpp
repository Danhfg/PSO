/**
 * @file    GPIOIN_API.cpp
 * @brief   Contém as funções que retorna o valor ou direção de uma porta GPIO
 */

#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

/**
 * @brief   Descobre o valor da porta GPIO especificada
 * @param   gpio    Número da porta GPIO a ser usada
 * @return  Valor na porta GPIO especificada
 */
int getValue(int gpio) {
    ifstream valueFile;

    string path = "/sys/class/gpio/gpio" + to_string(gpio) + "/value";

    valueFile.open(path,ios::in);
    if(valueFile.fail()) {
        valueFile.close();
    }
    else {
        int readValue;
        valueFile >> readValue;

        valueFile.close();
        return readValue;
    }
}


/**
 * @brief   Descobre a direção da porta GPIO especificada
 * @param   gpio    Número da porta GPIO a ser usada
 * @return  Direção da porta GPIO especificada
 */
string getDirection(int gpio) {
    ifstream directionCheck;

    string path = "/sys/class/gpio/gpio" + to_string(gpio) + "/direction";

    directionCheck.open(path, ios::in|ios::binary);
    if(directionCheck.fail()) {
        directionCheck.close();
    }
    else {
        string readValue;
        directionCheck >> readValue;

        return readValue;
    }
}

/**
 * @brief   Modifica a direção da porta GPIO especificada
 * @param   gpio    Número da porta GPIO a ser usada
 * @param   direction   Direção a ser colocada na porta
 * @return  True caso foi possível modificar a direção ou false caso contrário
 */
bool setDirection(int gpio, string direction) {
    ofstream directionFile;

    string path = "/sys/class/gpio/gpio" + to_string(gpio) + "/direction";

    directionFile.open(path, ios::out);
    if(directionFile.fail()) {
        directionFile.close();
        return false;
    }
    else {
        directionFile << direction;
        directionFile.close();
        return true;
    }
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
