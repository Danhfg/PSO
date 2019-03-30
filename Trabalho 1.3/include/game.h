#include "graph.h"
#include "rand.h"
#include "score.h"

enum MARK{
	GAME_STOP = -1,
	GAME_PAUSE = 0,
	GAME_RUN = 1
};


class Game{
        
    private:
        int m_penal[24][17];
        color m_color[24][17];///////////////////////
        Context* m_graph;

        Context* nextGraph;/////////////////
        MARK mark;//////////////////////////
    
    public:
        int x;
        int y;//��ǰ�����λ�ã������ƶ�������ת�ɹ���ſ����������ֵ

    private:
        Score s;
    
    private:
        //�ָ����ã������̽����һ��λ���Ƿ�Ϸ������Ϸ���ָ���壩
        bool recoverPenal();
        //�Ƿ���½(�Ƿ������±�)
        bool isAttachBottom();
        //�Ƿ��������
        bool isAttachLeft();
        //�Ƿ������ұ�
        bool isAttachRight();
        //�����ȡ������״
        char getShape();
        //�÷��������������鸳ֵ
        bool setPenal();
        //���鶯����Ҫ�����������Ϣ����
        bool erasePenal();
    
    public:
        Game();
        ~Game();

        //�����������ķ���
        void createCube();
        //�ƶ��ķ���,�ƶ��Ĺ����ж�m_penal�ĸı�
        void move(int dir);
        //��ת�ķ���������
        void roll();
        //����ֹͣ
        void stop();
        //��������
        void erase();
        //�����������ͼ������׹��
        void down(int level);

        void printNextCube(Context* m_graph);
        void gameInit();

        MARK getMark();
        void setMark( MARK );

        void printHelep();

};
