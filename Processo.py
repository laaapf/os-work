class Processo(object):
    def __init__(self, nome, prioridade, tempoProcesso, nImpressora, nDisco, tamanho):
        self.nome = nome
        self.prioridade = prioridade
        self.estado = "pronto"
        self.tempoProcesso = tempoProcesso
        self.tempoProcessado = 0
        self.nImpressora = nImpressora
        self.nDisco = nDisco
        self.tamanho = tamanho

    def __str__(self):
        if not self.prioridade:
           aux = "Com prioridade"
        else:
            aux = "Sem prioridade" 
        return "\n\tProcesso {}   Estado {}   {}\n\tTamanho do Processo:{}Mbytes\n\tTempo de serviço: {}\n".format(self.nome, self.estado, aux, self.tamanho, self.tempoProcesso)
    
    def recursosDisponiveis(self, lPerifericos,):
        impressoras = 0
        discos = 0
        for p in lPerifericos:
            if(p.tipo == "impressora" and p.disponivel):
                impressoras += 1
            if(p.tipo == "disco" and p.disponivel):
                discos += 1
        if (discos < self.nDisco):
            return "semDisco"
        else: 
            if(impressoras < self.nImpressora):
                return "semImpressora"
            else:
                return "pronto"

    def reservaES(self,lPerifericos):
        if self.tempoProcesso - self.tempoProcessado <=2:
            i = self.nImpressora
            while (i > 0) :
                for periferico in lPerifericos:
                    if(periferico.tipo == "impressora" and periferico.disponivel):
                        periferico.disponivel = False
                        i-=1
        if  self.tempoProcessado == 0:    
            i = self.nDisco
            while (i > 0) :
                for periferico in lPerifericos:
                    if(periferico.tipo == "disco" and periferico.disponivel):
                        periferico.disponivel = False
                        i-=1

    def liberaES(self,n,tipo,lPerifericos):
        while (n > 0) :
            for periferico in lPerifericos:
                if(periferico.tipo == tipo and not periferico.disponivel):
                    periferico.disponivel = True
                    n-=1
            

    def executa(self):
        estadoAntigo = self.estado
        self.estado = "executando"
        return "\tProcesso {}   Estado {} --> Executando\n".format(self.nome, estadoAntigo)

        
    def bloqueia(self):
        estadoAntigo = self.estado
        self.estado = "bloqueado"
        return "\tProcesso {}   Estado {} --> Bloqueado\n".format(self.nome, estadoAntigo)

    def apronta(self):
        estadoAntigo = self.estado
        self.estado = "pronto"   
        return "\tProcesso {}   Estado {} --> Pronto\n".format(self.nome, estadoAntigo)

    def termina(self):
        estadoAntigo = self.estado
        self.estado = "terminado"   
        return "\tProcesso {}   Estado {} --> Terminado\n".format(self.nome, estadoAntigo)