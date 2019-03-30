/**
 * @file    APIGPIO.cpp
 * @brief   Contém as funções que escreve e retorna o valor ou direção de uma porta GPIO
 */

#include <cstring>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <iostream>

using namespace std;

/**
 * @brief   Descobre o valor da porta GPIO especificada
 * @param   gpio    Número da porta GPIO a ser usada
 * @return  Valor na porta GPIO especificada
 */
// int getValue(int gpio) {
//     ifstream valueFile;

//     string path = "/sys/bus/iio/devices/iio:device0" ;

//     valueFile.open(path,ios::in);
//     if(valueFile.fail()) {
//         valueFile.close();
//     }
//     else {
//         int readValue;
//         valueFile >> readValue;

//         valueFile.close();
//         return readValue;
//     }
// }


// int getValuePotenciometro(){
// 	    return getValue(115);
// }


// int getValueADC(){
    // return getValue(115);
// }