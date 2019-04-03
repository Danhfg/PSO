#ifndef _BBB_IN
#define _BBB_IN

#include <string>

class BBB_IN{

    private:
    
        std::string nomeDaEntrada;
    
    public:

        BBB_IN(std::string nome){
            this->nome = nome;
        }

        virtual int getValue() = 0;

};



#endif