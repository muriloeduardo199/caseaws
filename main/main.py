
import pandas as pd






def teste():

    """Faz a leitura do arquivo csv e retira partes dos dados e gera dois arquivos csv"""


    doc = pd.read_csv('./arquivo_exemplo.csv',  encoding="ISO-8859-1", sep = ';')
    master_df = pd.DataFrame(doc)
    data= master_df.iloc[:, 7].to_csv('cpf.csv', index=False)
    date=pd.to_datetime(master_df.iloc[:, 24], infer_datetime_format=True).to_csv('datas.csv', index= False)
    print(teste())

    return data, date





