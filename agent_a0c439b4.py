import random
import json

data_points = []

for i in range(1000):
    data_point = {
        'id': i,
        'coordinates': [random.uniform(-1000, 1000) for _ in range(3)],
        'details': f'Mock data point {i}'
    }
    data_points.append(data_point)

with open('/media/palmerschallon/ThePod1/mock_data.json', 'w') as f:
    json.dump(data_points, f)