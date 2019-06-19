import subprocess

def listaDeProcessos():
    """ Executa o comando de terminal para pegar a lista de processos

    Returns:
    str:Lista de processos

    """
    comandoListaDeProcesso = "ps -eo user,pid,stat"
    return subprocess.check_output(comandoListaDeProcesso, stderr=subprocess.STDOUT, shell=True).decode("utf-8")
    

def Main():
	print( listaDeProcessos()[0] )




if __name__ == '__main__': 
    Main() 