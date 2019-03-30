#ifndef _THREAD_H
#define _THREAD_H

#include <thread>

class Thread{

    private:
        int prioridade;
        std::thread t;

    public:
        Thread(const int prioridadeNova, std::thread &tNova);
        int getPrioridade() const;
        std::thread& getT();

        bool operator<(const Thread &t1);
};



#endif
