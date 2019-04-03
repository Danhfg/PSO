#include "Game.h"

int main(){
    
    pthread_t t1;
    pthread_mutex_init(&mutex_lock, NULL);
	system("clear");
    Game g;
    //g.createCube();
	g.gameInit();
    pthread_create(&t1,NULL,listenKey,(void*)(&g));

    while(1){
        fflush(stdout);
        usleep(SPEED);
        g.move(DOWN);
    }
	return 0;
}
