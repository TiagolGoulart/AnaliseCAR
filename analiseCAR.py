import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import folium
from folium.plugins import FloatImage
from io import BytesIO
import base64
from folium import LayerControl
from PIL import Image


# Leia o shapefile
app1 = gpd.read_file('data/UF/APPS/APPS_1.shp')
app2 = gpd.read_file('data/UF/APPS/APPS_2.shp')
app3 = gpd.read_file('data/UF/APPS/APPS_3.shp')
app4 = gpd.read_file('data/UF/APPS/APPS_4.shp')
areaConsolidada = gpd.read_file('data/UF/AREA_CONSOLIDADA/AREA_CONSOLIDADA_1.shp')
areaImovel = gpd.read_file('data/UF/AREA_IMOVEL/AREA_IMOVEL_1.shp')
areaPousio = gpd.read_file('data/UF/AREA_POUSIO/AREA_POUSIO_1.shp')
hidrografia = gpd.read_file('data/UF/HIDROGRAFIA/HIDROGRAFIA_1.shp')
reservaLegal = gpd.read_file('data/UF/RESERVA_LEGAL/RESERVA_LEGAL_1.shp')
servidaoAdministrativa = gpd.read_file('data/UF/SERVIDAO_ADMINISTRATIVA/SERVIDAO_ADMINISTRATIVA_1.shp')
usoRestrito = gpd.read_file('data/UF/USO_RESTRITO/USO_RESTRITO_1.shp')
vegNativa = gpd.read_file('data/UF/VEGETACAO_NATIVA/VEGETACAO_NATIVA_1.shp')

# Preparação dos dados
app1 = app1[app1['cod_tema'] == 'APP_TOTAL']
app2 = app2[app2['cod_tema'] == 'APP_TOTAL']
app3 = app3[app3['cod_tema'] == 'APP_TOTAL']
app4 = app4[app4['cod_tema'] == 'APP_TOTAL']

servidaoAdministrativa = servidaoAdministrativa[servidaoAdministrativa['cod_tema'] == 'AREA_SERVIDAO_ADMINISTRATIVA_TOTAL']


# Exiba as primeiras linhas do GeoDataFrame para verificar se os dados foram carregados corretamente
areaImovel

# Entrada do código do CAR a ser analisado
codCar = input('Digite o código do CAR no formato indicado: UF-XXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

# Extraindo informações individuais do CAR
if codCar in app1['cod_imovel'].values:
    appInd = app1[app1['cod_imovel'] == codCar]
elif codCar in app2['cod_imovel'].values:
    appInd = app2[app2['cod_imovel'] == codCar]
elif codCar in app3['cod_imovel'].values:
    appInd = app3[app3['cod_imovel'] == codCar]
else:
    appInd = app4[app4['cod_imovel'] == codCar]

areaConsolidadaInd = areaConsolidada[areaConsolidada['cod_imovel'] == codCar]
areaImovelInd = areaImovel[areaImovel['cod_imovel'] == codCar]
areaPousioInd = areaPousio[areaPousio['cod_imovel'] == codCar]
hidrografiaInd = hidrografia[hidrografia['cod_imovel'] == codCar]
reservaLegalInd = reservaLegal[reservaLegal['cod_imovel'] == codCar]
servidaoAdministrativaInd = servidaoAdministrativa[servidaoAdministrativa['cod_imovel'] == codCar]
usoRestritoInd = usoRestrito[usoRestrito['cod_imovel'] == codCar]
vegNativaInd = vegNativa[vegNativa['cod_imovel'] == codCar]


#CRIANDO O MAPA FOLIUM

# Obter o ponto central da área total
centro = areaImovelInd.geometry.centroid.iloc[0].coords[0][::-1]

# Criar o mapa centralizado no ponto central
m = folium.Map(location=centro, zoom_start=12)

# Adicionar o TileLayer personalizado
tile_url = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'  # URL do provedor de tiles
folium.TileLayer(name= 'Google Satellite',tiles=tile_url, attr='<a href="https://www.google.at/permissions/geoguidelines/attr-guide.html">Map data ©2015 Google</a>').add_to(m)

# Função para adicionar GeoDataFrames ao mapa com coloração e transparência
def adicionar_camadas(gdf, nome, cor):
    folium.GeoJson(
        gdf,
        name=nome,
        style_function=lambda x: {
            'fillColor': cor,
            'color': cor,
            'weight': 1,
            'fillOpacity': 0.4
        }
    ).add_to(m)

# Adicionar as camadas ao mapa
adicionar_camadas(areaImovelInd, 'Área do Imóvel', 'black')
adicionar_camadas(appInd, 'APP', 'green')
adicionar_camadas(areaConsolidadaInd, 'Área Consolidada', 'blue')
adicionar_camadas(areaPousioInd, 'Área de Pousio', 'purple')
adicionar_camadas(hidrografiaInd, 'Hidrografia', 'cyan')
adicionar_camadas(reservaLegalInd, 'Reserva Legal', 'brown')
adicionar_camadas(servidaoAdministrativaInd, 'Servidão Administrativa', 'orange')
adicionar_camadas(usoRestritoInd, 'Uso Restrito', 'red')
adicionar_camadas(vegNativaInd, 'Vegetação Nativa', 'darkgreen')

# Adicionar controle de camadas
folium.LayerControl(collapsed=False).add_to(m)

#print(usoRestritoInd.head())
#print(usoRestritoInd.shape)

# Analisando Reserva Legal e Uso restrito e realizando a soma das áreas 
numlinhas,numColunas = reservaLegalInd.shape

if numlinhas == 0:
    print('Reserva Legal não encontrada')
else:
    reservaLegalInd['num_area_total'] = reservaLegalInd['num_area'].sum()

numlinhas,numColunas = usoRestritoInd.shape

if numlinhas == 0:
    print('Uso Restrito não encontrado')
else:
    usoRestritoInd['num_area_total'] = usoRestritoInd['num_area'].sum()

# Criação do dataframe
carStats = pd.DataFrame({'area_imovel': [0]})

# Criando e preenchendo as colunas do DataFrame
if not areaImovelInd.empty:
    carStats['area_imovel'] = areaImovelInd.iloc[0]['num_area']
else:
    print('Área do imóvel não encontrada')

if not appInd.empty:
    carStats['app'] = appInd.iloc[0]['num_area']
else:
    carStats['app'] = 0

if not areaPousioInd.empty:
    carStats['area_pousio'] = areaPousioInd.iloc[0]['num_area']
else:
    carStats['area_pousio'] = 0

if not reservaLegalInd.empty:
    carStats['reserva_legal'] = reservaLegalInd.iloc[0]['num_area_total']
else:
    carStats['reserva_legal'] = 0

if not servidaoAdministrativaInd.empty:
    carStats['servidao_adm'] = servidaoAdministrativaInd.iloc[0]['num_area']
else:
    carStats['servidao_adm'] = 0

if not usoRestritoInd.empty:
    carStats['uso_restrito'] = usoRestritoInd.iloc[0]['num_area_total']
else:
    carStats['uso_restrito'] = 0

if not vegNativaInd.empty:
    carStats['veg_nativa'] = vegNativaInd.iloc[0]['num_area']
else:
    carStats['veg_nativa'] = 0


# Exiba o resultado
#print(carStats)

# Calcular o percentual de cada uso do solo
area_imovel = carStats['area_imovel'][0]
usos = carStats.columns[1:]
percentuais = carStats[usos].iloc[0] / area_imovel * 100

# Preparar os dados para o gráfico
percentuais_df = percentuais.reset_index()
percentuais_df.columns = ['Uso do Solo', 'Percentual']

# Configurar o gráfico
plt.figure(figsize=(6, 4))
bars = plt.bar(percentuais_df['Uso do Solo'], percentuais_df['Percentual'], color='skyblue')

# Adicionar título e rótulos
plt.title('Uso do Solo em Relação à Área Total do Imóvel')
plt.xlabel('Uso do Solo')
plt.ylabel('Percentual (%)')
plt.xticks(rotation=45)
plt.ylim(0, 100)  # Ajustar o limite do eixo y para 0 a 100%

# Adicionar os valores no topo de cada barra
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}%', ha='center', va='bottom')


# Mostrar o gráfico
#plt.tight_layout()
#plt.show()

# Salvar o gráfico em um objeto BytesIO
img = BytesIO()
plt.tight_layout()
plt.savefig(img, format='png')
img.seek(0)

# Redimensionar a imagem usando PIL
img_pil = Image.open(img)
img_pil = img_pil.resize((400, 266))  # Ajustar o tamanho da imagem
img_byte_arr = BytesIO()
img_pil.save(img_byte_arr, format='PNG')
img_byte_arr.seek(0)
img_base64 = base64.b64encode(img_byte_arr.read()).decode('utf-8')


# Adicionar a imagem como overlay no mapa
img_html = f'data:image/png;base64,{img_base64}'
FloatImage(img_html, bottom=2, left=1).add_to(m)

mapa_url = codCar + '.html'
m.save(mapa_url)
m