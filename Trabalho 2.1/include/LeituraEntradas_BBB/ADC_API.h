/**
 * @file    ADC_API.cpp
 * @brief   Contém as funções que retorna o valoro de uma porta ADC
 */

#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>

using namespace std;

/**
 * Lê porta analógica de entrada AIN
 * @param   ain Número da porta em formato de string
 * @return  Contéudo da porta analógica
 */  
int getValueADC(int ain){
    ifstream valueFile;

    string path = "/sys/bus/iio/devices/iio:device0/in_voltage" + to_string(ain) + "_raw";

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
 * Lê entrada LDR e retorna-a
 * @return  Conteúdo na entrada analógica LDR
 */ 
int getValueLDR(){
    return getValueADC(0);
}


/**
 * Lê entrada Potenciomêtro e retorna-a
 * @return  Conteúdo na entrada analógica Potenciomêtro
 */ 
int getValuePotenciometro(){
    return getValueADC(1);
}

