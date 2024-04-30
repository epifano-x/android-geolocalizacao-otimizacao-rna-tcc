import json
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Carregar dados do arquivo JSON
with open('dados_final.json', 'r') as f:
    data = json.load(f)

# Definir o número máximo de satélites esperado em uma amostra
max_satellites = 0
for sample in data:
    gnss_data = sample.get('gnss_data', {})
    satellites = gnss_data.get('satellites', [])
    max_satellites = max(max_satellites, len(satellites))

# Extrair características e rótulos
X_data = []
y_lat = []
y_lon = []

for sample in data:
    gnss_data = sample.get('gnss_data', {})
    satellites = gnss_data.get('satellites', [])
    num_satellites = len(satellites)
    
    # Extrair características dos satélites
    satellite_features = []
    for i in range(max_satellites):
        if i < num_satellites:
            satellite = satellites[i]
            satellite_features.extend([
                satellite.get('svid', 0),
                satellite.get('constellationType', 0),
                satellite.get('azimuthDegrees', 0),
                satellite.get('elevationDegrees', 0),
                satellite.get('cn0DbHz', 0),
                satellite.get('basebandCn0DbHz', 0),
                satellite.get('carrierFrequencyHz', 0)
            ])
        else:
            # Preencher com valores padrão se não houver dados para o satélite
            satellite_features.extend([0] * 7)
    
    # Extrair características restantes
    altitude = gnss_data.get('altitude', 0)
    accuracy = gnss_data.get('accuracy', 0)
    speed = gnss_data.get('speed', 0)
    
    # Concatenar todas as características
    features = [altitude, accuracy, speed]
    features.extend(satellite_features)
    
    # Adicionar à lista de características
    X_data.append(features)
    
    # Adicionar rótulos
    y_lat.append(gnss_data.get('latitudeDiferenca', 0))
    y_lon.append(gnss_data.get('longitudeDiferenca', 0))

# Converter para arrays numpy
X = np.array(X_data)
y_lat = np.array(y_lat)
y_lon = np.array(y_lon)

# Dividir dados em conjuntos de treinamento e teste
X_train, X_test, y_lat_train, y_lat_test, y_lon_train, y_lon_test = train_test_split(X, y_lat, y_lon, test_size=0.22, random_state=42)

# Definir arquitetura da RNA
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compilar o modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinar o modelo
history = model.fit(X_train, y_lat_train, epochs=100, batch_size=32, validation_data=(X_test, y_lat_test))

# Avaliar o modelo
loss = model.evaluate(X_test, y_lat_test)
print(f'Loss: {loss}')

# Fazer previsões
predictions = model.predict(X_test)

# Calcular métricas de desempenho
mae = mean_absolute_error(y_lat_test, predictions)
print("Mean Absolute Error:", mae)

# Exibir exemplos de previsões e diferenças
num_examples = 10
for i in range(num_examples):
    print("Exemplo", i+1)
    print("Previsão:", predictions[i][0])
    print("Valor Real:", y_lat_test[i])
    print("Diferença:", predictions[i][0] - y_lat_test[i])
    print()

# Plotar gráfico de perda ao longo das épocas
plt.plot(history.history['loss'], label='loss')
plt.plot(history.history['val_loss'], label='val_loss')
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Salvar o modelo
model.save('model_lat.h5')
