#include "../include/Thread.h"


Thread::Thread(const int prioridadeNova, std::thread &tNova){
    this->prioridade = prioridadeNova;
    this->t.swap(tNova);
}

int 
Thread::getPrioridade() const{
    return this->prioridade;
}

std::thread& 
Thread::getT(){
    return this->t;
}

bool 
Thread::operator<(const Thread &t1){
    return this->prioridade < t1.getPrioridade();
}

