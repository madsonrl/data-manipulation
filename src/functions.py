dataset = []
datasetEstado = []
datasetCidade = []
datasetPorAno = []
listaNomesEstados = []
rankingPIBS = []

def carregaDataset():
    f = open('./src/dataset/pib_municipio_2010_a_2018.txt', 'r', encoding="utf-8-sig")
    for line in f:
        # Split on any whitespace (including tab characters)
        line = line.strip()
        registro = line.split(";")
        dataset.append(registro)


def filtraPorEstado(dataset, estado):
    for registro in dataset:
        if estado == registro[2]:
            datasetEstado.append(registro)

def filtraPorCidade(dataset, cidade):
    for registro in dataset:
        if cidade == registro[3]:
            datasetCidade.append(registro)

def filtraPorAno(dataset, ano):
    for registro in dataset:
        if ano == registro[0]:
            datasetPorAno.append(registro)

def listaEstado(dataset):
    for registro in dataset:
        if registro[2] not in listaNomesEstados:
            listaNomesEstados.append(registro[2])
    
    listaNomesEstados.pop(0)

def mediaPIBPer(dataset):
    soma = 0
    media = 0
    for registro in dataset:
        soma += float(registro[13])
    media = soma/(len(dataset))

    return round(media,2)

def mediaValorAdicionadoBrutoServ(dataset):
    soma = 0
    media = 0
    for registro in dataset:
        soma += float(registro[8])
    media = soma/(len(dataset))

    return round(media,2)

def mediaValorAdicionadoBrutoTotal(dataset):
    soma = 0
    media = 0
    for registro in dataset:
        soma += float(registro[10])
    media = soma/(len(dataset))

    return round(media,2)

def ranking(dataset):
    for estado in listaNomesEstados:
        filtraPorEstado(dataset, estado)
        media =  mediaPIBPer(datasetEstado)
        datasetEstado.clear()
        rankingPIBS.append((estado,media))
    rankingPIBS.sort(key=lambda x: x[1], reverse= True)




carregaDataset()


# listaEstado(dataset)
filtraPorEstado(dataset, 'Amazonas')
filtraPorAno(datasetEstado, '2018')
mediaT = mediaValorAdicionadoBrutoTotal(datasetPorAno)
mediaS = mediaValorAdicionadoBrutoServ(datasetPorAno)
prop = (mediaS*100)/mediaT
print(mediaT, mediaS, round(prop,2),"%")

f = open("demofile2.txt", "a",)
f.writelines(f'{datasetPorAno}')
f.close()

# ranking(datasetPorAno)

# print(rankingPIBS)

# carregaDataset()
# filtraPorAno(dataset, '2018')
# filtraPorCidade(datasetPorAno, 'Manaus')
# print(mediaPIBPer(datasetCidade))

# # listaEstado(dataset)

# print(datasetCidade)




