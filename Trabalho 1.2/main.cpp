#include <iostream>
#include <string>
#include <fstream>
#include <vector>

int main(){

	double totalCPU = 0;
	std::string percent;
	std::vector<double> percentVector;

	std::system("ps aux --sort=-%cpu | awk '{ print $3 }' > cpu.log" );

	std::ifstream cpuLog;
	cpuLog.open("cpu.log");

	if( cpuLog.is_open() ){

		cpuLog >> percent;

		while( cpuLog >> percent ){

			percentVector.push_back( std::stod(percent) );	
		}

		for( auto& n: percentVector){
			totalCPU += n;
		}

		std::cout << totalCPU << std::endl;

	}
	
	return 0;
}