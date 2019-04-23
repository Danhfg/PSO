#include "../../include/Jogo/Rand.h"

#include <ctime>
#include <stdlib.h>
#include <iostream>

using namespace std;

//ʹ���������һ������ķ�ʽ����ÿ�ζ�ȥsrand,��������ε��úܽӽ�ʱֵ�ͻ�
//һ������ʱ���ϵ�ܴ󣩶�srandһ�ξͲ�������������ˡ�
Rand::Rand(){
    srand(unsigned(time(0)));
}

int 
Rand::randNum(int x,int y){
    int randNum;
    double random(double,double);
    randNum = int(random(x,y));
    return randNum;
}

double 
random(double start,double end){
    return start + (end - start)*rand()/(RAND_MAX + 1.0);
}

/*
int main()
{
    Rand a;
    for(int i = 0;i < 50;i++)
    cout<<a.randNum(1,100)<<endl;
}
*/
