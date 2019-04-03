#include "coletaEntradas_API.h"

void escrevendoEmArquivoBBBInputs(){

    std::thread tBotao( coletaBotao  );
    std::thread tPotenciometro( coletaPotenciometro );
    std::thread tLDR( coletaLDR );
 
    tBotao.join();
    tPotenciometro.join();
    tLDR.join();

}



int main(){

    escrevendoEmArquivoBBBInputs();

    return 0;
}