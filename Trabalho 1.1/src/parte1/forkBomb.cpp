/**
 * @file  forkBomb.cpp
 * @brief Contém a implementação de um fork boma
 */ 

#include <unistd.h> /// fork()
#include <iostream>

int main(void)
{
    while(1) fork();
    return 0;
}
