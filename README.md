# 📊 Análise de Propriedades Rurais pelo CAR

Este script Python realiza a análise de propriedades rurais usando dados do Cadastro Ambiental Rural (CAR). Ele lê shapefiles, processa as informações e gera um mapa interativo com camadas sobrepostas e um gráfico de uso do solo.

![Exemplo de Mapa Interativo](https://raw.githubusercontent.com/TiagolGoulart/AnaliseCAR/main/map.png)

## 📋 Pré-requisitos

- Python 3.x
- Bibliotecas Python:
  - `geopandas`
  - `pandas`
  - `matplotlib`
  - `folium`
  - `Pillow`
  - `base64`

Para instalar as bibliotecas necessárias, você pode usar o seguinte comando:

`bash
pip install geopandas pandas matplotlib folium Pillow base64`

## 📁 Dados
Os dados utilizados neste script estão disponíveis no site do SICAR e podem ser baixados de acordo com a preferência de estado de análise:

[SICAR - Downloads](https://www.car.gov.br/publico/estados/downloads)

## 🚀 Instruções de Uso
Baixe e extraia os dados do SICAR para o estado desejado.
Organize os shapefiles nas pastas apropriadas, seguindo a estrutura esperada pelo script.
Execute o script e insira o código do CAR no formato indicado quando solicitado.

## 🗂️ Estrutura do Script
Leitura dos shapefiles.
Filtragem dos dados com base no código do CAR fornecido.
Criação de um mapa interativo usando Folium.
Adição de camadas ao mapa com diferentes cores e transparências.
Geração de um gráfico de uso do solo e adição ao mapa.
Salvamento do mapa como um arquivo HTML.

## 💻 Exemplo de Execução

Execute o código python analiseCAR.py  
Quando solicitado, insira o código do CAR no formato **UF-XXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX**
