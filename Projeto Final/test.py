import subprocess

def listaDeProcessos():
    """ Executa o comando de terminal para pegar a lista de processos

    Returns:
    str:Lista de processos

    """
    comandoListaDeProcesso = "ps -eo user,pid,stat"
    return subprocess.check_output(comandoListaDeProcesso, stderr=subprocess.STDOUT, shell=True).decode("utf-8")
    

def capturaConsumoDeMemoria():
    """ Executa o comando de terminal para pegar o consumo de memória

    Returns:
    str:Porcentagem do consumo de memória atual

    """
    comandoConsumoDeMemoria =  "free | grep Mem | awk '{print $3/$2 * 100.0}'"
    return subprocess.check_output(comandoConsumoDeMemoria, stderr=subprocess.STDOUT, shell=True).decode("utf-8")
    

def Main():
	print( str(float(capturaConsumoDeMemoria())) )




if __name__ == '__main__': 
    Main() 