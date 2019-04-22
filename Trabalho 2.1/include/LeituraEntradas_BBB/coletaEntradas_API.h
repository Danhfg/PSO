#include "ADC_API.h"
#include "GPIOIN_API.h"

#include <unistd.h>
#include <thread>
#include <fstream>

#include <iostream>

#define MINSPEED 1000000
#define FRAMEWAIT 16000
#define BDELAY 200000

bool le_Potenciometro = true;
bool le_LDR = true;


void 
coletaBotao( bool &conteudoBotao ){

    while(true){
            
        conteudoBotao = buttonIsPressed();

        fflush(stdout);
        // usleep(FRAMEWAIT);  Aparentemente desnecessario

    }

}


void 
coletaPotenciometro( int &conteudoPotenciometroAtual){

    int conteudoPotenciometroAntigo;

    while(true){

        conteudoPotenciometroAtual = getValuePotenciometro();

        if( abs(conteudoPotenciometroAntigo - conteudoPotenciometroAtual) > 100 ){

            le_Potenciometro = true;    
            conteudoPotenciometroAntigo = conteudoPotenciometroAtual;
        }
        else{
            le_Potenciometro = false;
        }

        fflush(stdout);
        //usleep(FRAMEWAIT);  Aparentemente desnecessario
    }

}

void 
coletaLDR( int &conteudoLDR_Atual ){

    int conteudoLDR_Antigo;

    while(true){

        conteudoLDR_Atual = getValueLDR();

        if( abs(conteudoLDR_Antigo - conteudoLDR_Atual) > 100 ){
            conteudoLDR_Antigo = conteudoLDR_Atual;
            le_LDR = true;
        }
        else{
            le_LDR = false;
        }    
        
        fflush(stdout);
        
        int velocidade = MINSPEED - conteudoLDR_Atual* 200;
        usleep(velocidade); 
    }

}


void 
escrevendoEmArquivoBBBInputs(){

    std::ofstream inputs;
    bool conteudoBotao;
    int conteudoPotenciometro;
    int conteudoLDR;

    std::thread thread_Botao( coletaBotao, std::ref(conteudoBotao) );
    std::thread thread_Potenciometro( coletaPotenciometro, std::ref(conteudoPotenciometro) );
    std::thread thread_LDR( coletaLDR,  std::ref(conteudoLDR) );

    sched_param schBotao, schLDR, schPotenciometro;

    int prioridadeBotao, prioridadeLDR, prioridadePotenciometro;

    pthread_getschedparam(thread_Potenciometro.native_handle(), &prioridadePotenciometro, &schPotenciometro);
    schPotenciometro.sched_priority = 3;

    pthread_getschedparam(thread_LDR.native_handle(), &prioridadeLDR, &schLDR);
    schLDR.sched_priority = 2;

    pthread_getschedparam(thread_Botao.native_handle(), &prioridadeBotao, &schBotao);
    schBotao.sched_priority = 1;


    while(true){

        inputs.open("inputs.in");
    
        if( inputs.is_open() != 0){ /// Verificando se o arquivo foi aberto

            // std::cout << "Botao:" << thread_Botao.joinable() << std::endl;
            // std::cout << "Potenciometro:" << thread_Potenciometro.joinable() << std::endl;
            // std::cout << "LDR:" << thread_LDR.joinable() << std::endl;
            // std::cout << "LDR " << le_LDR << " Pot " << le_Potenciometro << std::endl << std::endl;

            if( le_Potenciometro == true ){     /// LENDO POTENCIOMETRO
                if( conteudoPotenciometro < 500)    /// Movendo à esquerda
                    inputs << 'a';
                 else                               /// Movendo à direita
                    inputs << 'd';   
            }        
            else if ( le_LDR == true ){         /// LENDO LDR
                if( conteudoLDR > 10 )
                    inputs << 's';
            }    
            else{                               /// LENDO Botão  
                if(conteudoBotao == true)
                    inputs << 'w';
            }                                
                
        }

        inputs.close();
    }    

    thread_Botao.join();
    thread_Potenciometro.join();
    thread_LDR.join();

}
