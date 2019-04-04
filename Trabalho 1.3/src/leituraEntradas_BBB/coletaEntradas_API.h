#include "ADC_API.h"
#include "GPIOIN_API.h"

#include <thread>
#include <fstream>

#include <iostream>

bool le_Potenciometro = true;
bool le_LDR = true;


void coletaBotao( bool &conteudoBotao ){

    while(true){
            
        conteudoBotao = buttonIsPressed();
        std::this_thread::sleep_for (std::chrono::milliseconds(500));

    }

}


void coletaPotenciometro( int &conteudoPotenciometro){

    while(true){

        conteudoPotenciometro << getValuePotenciometro();
        std::this_thread::sleep_for (std::chrono::milliseconds(125));
        le_Potenciometro = !le_Potenciometro;     
    }

}

void coletaLDR( int &conteudoLDR ){

    while(true){

        conteudoLDR << getValueLDR();
        std::this_thread::sleep_for (std::chrono::milliseconds(250));        
        le_LDR = !le_LDR;
    }

}


void escrevendoEmArquivoBBBInputs(){


    std::ofstream inputs;
    bool conteudoBotao;
    int conteudoPotenciometro;
    int conteudoLDR;



        std::thread tBotao( coletaBotao, std::ref(conteudoBotao) );
        std::thread tPotenciometro( coletaPotenciometro, std::ref(conteudoPotenciometro) );
        std::thread tLDR( coletaLDR,  std::ref(conteudoLDR) );

        tBotao.join();
        tPotenciometro.join();
        tLDR.join();

    while(true){

        inputs.open("inputs.in");
    
        if( inputs.is_open() != 0){ /// Verificando se o arquivo foi aberto
            
            if( le_Potenciometro == true ){
                if( conteudoPotenciometro < 500)    /// Movendo à esquerda
                    inputs << 'a';
                 else                               /// Movendo à direita
                    inputs << 'd';   
            }        
            else if ( le_LDR == true ){
                if( conteudoLDR > 10 )
                    inputs << 's';
            }    
            else        
                inputs << 'w';
                
        }

        std::cout << "Botao:" << tBotao.joinable() << std::endl;
        std::cout << "Potenciometro:" << tPotenciometro.joinable() << std::endl;
        std::cout << "LDR:" << tLDR.joinable() << std::endl;

        
    }    
}
