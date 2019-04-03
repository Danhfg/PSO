#include "ADC_API.h"
#include "GPIOIN_API.h"

#include <thread>
#include <fstream>

void coletaBotao( ){

    std::ofstream arqConteudoBotao;

    while(true){
            
        arqConteudoBotao.open("conteudoBotao.dat");

        if( arqConteudoBotao.is_open() != 0) /// Verificando se o arquivo foi aberto
            arqConteudoBotao << buttonIsPressed();

        arqConteudoBotao.close();
        
        std::this_thread::sleep_for (std::chrono::milliseconds(250));      
    }

}


void coletaPotenciometro( ){

    std::ofstream arqConteudoPotenciometro;

    while(true){

        arqConteudoPotenciometro.open("conteudoPotenciometro.dat");

        if( arqConteudoPotenciometro.is_open() != 0) /// Verificando se o arquivo foi aberto
            arqConteudoPotenciometro << getValuePotenciometro();
        
        arqConteudoPotenciometro.close();

        std::this_thread::sleep_for (std::chrono::milliseconds(250));     
    }

}

void coletaLDR( ){

    std::ofstream arqConteudoLDR;

    while(true){

        arqConteudoLDR.open("conteudoLDR.dat");

        if( arqConteudoLDR.is_open() != 0) /// Verificando se o arquivo foi aberto
            arqConteudoLDR << getValueLDR();
        
        arqConteudoLDR.close();

        std::this_thread::sleep_for (std::chrono::milliseconds(250));        
    
    }

}




