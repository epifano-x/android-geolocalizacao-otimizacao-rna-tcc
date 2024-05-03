import json
import numpy as np

# Criando um array NumPy com valores grandes
array = np.array([0.123456789012345672323890, 0.987232365432109876543210])

# Convertendo o array NumPy para uma lista Python
array_list = array.tolist()

# Serializando a lista em JSON
json_data = json.dumps({"array": array_list}, indent=4)

# Exibindo o JSON resultante
print(json_data)
