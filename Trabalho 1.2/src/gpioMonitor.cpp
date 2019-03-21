#include "MonitorarAPI.cpp"

#include <vector>

using namespace std;

int main(int argc, char *argv[]){

	/* aqui faz todas as configurações para os gio de entrada e saída */
	long freeMem, maxMen;
	float percent;
	ifstream infoMem, infoPid;
	ifstream cpuLog;
	string aux;
	power light = off;
	// int monitorarMemoria_ou_CPU;
	// double totalCPU = 0;
	// string percentCPU;
	// vector<double> percentVectorCPU;

	while (true) {

	// 	cout << endl 
	// 		<< "Qual recurso voce deseja monitorar? memoria ou CPU? " 
	// 		<< endl
	// 		<< "Digite 1 caso queira que seja a memoria. Se não, digite 2 para que a CPU seja monitorada... "
	// 		<< endl;

	// 	cin >> 	monitorarMemoria_ou_CPU;

	// 	if( monitorarMemoria_ou_CPU == 1){ /// MONITORANDO O USO DA MEMÓRIA

			system("cat /proc/meminfo | head -2 | awk '{print $2}' > mem.log");
			infoMem.open("mem.log");

			if (infoMem.is_open()) {

				getline(infoMem, aux);
				maxMen = stoi(aux);

				getline(infoMem, aux);
				freeMem = stoi(aux);

				infoMem.close();
				system("rm mem.log");
			}
			else {
				cerr << "Falha na leitura do arquivo que contem as infomacoes sobre a memoria!" << endl;
				system("rm mem.log");
				exit(1); 
			}

		// }
		// else{ /// MONITORANDO O USO DA CPU

		// 	std::system("ps aux --sort=-%cpu | awk '{ print $3 }' > cpu.log" );
		// 	cpuLog.open("cpu.log");

		// 	if( cpuLog.is_open() ){

		// 		cpuLog >> percentCPU;

		// 		while( cpuLog >> percentCPU ){

		// 			percentVectorCPU.push_back( std::stod(percentCPU) );	
		// 		}

		// 		for( auto& n: percentVectorCPU){
		// 			totalCPU += n;
		// 		}
		// 	}
		// 	else {
		// 		cerr << "Falha na leitura do arquivo que contem as infomacoes sobre a CPU!" << endl;
		// 		system("rm cpu.log");
		// 		exit(1); 
		// 	}

		// }


		// if( monitorarMemoria_ou_CPU == 1)
			percent = (float)(maxMen - freeMem) *100 / maxMen;
		// else
		// 	percent = totalCPU;


		if(percent < 25.0f) {
			setVermelho(off);
			setAmarelo(off);
			setVerde(on);
		}
		else if (percent < 50.0f) {
			setVermelho(off);
			setAmarelo(on);
			setVerde(off);
		}
		else if (percent < 75.0f) {
			setVermelho(on);
			setAmarelo(off);
			setVerde(off);
		}
		else {
			if (buttonIsPressed()) {
				system("ps aux --sort=-%mem | head -2 | tail -1 | awk '{print $2}' > killAux.txt");
				infoPid.open("killAux.txt");

				if (infoPid.is_open()) {
					getline(infoPid, aux);
					infoPid.close();
					system("rm killAux.txt");

					string kill = "kill -9 ";
					kill += aux;

					system(kill.c_str());

					// apaga todos
					setVermelho(off);
					setAmarelo(off);
					setVerde(off);

					// 3,5s + 0,5 padrão				
					usleep(3500000);
				}
				else {
					cerr << "Falha na leitura do arquivo de info do PID!" << endl;
					system("rm killAux.txt");
					exit(2);
				}
			}
			else {
				setAll(light);
			    usleep(500000);
				if(light == off)
					light =  on;
				else
					light = off;
			}
		}

		usleep(500000);
	}
	setAll(off);
}