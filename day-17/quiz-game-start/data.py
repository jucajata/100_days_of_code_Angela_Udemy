'''
Prompt en ChatGPT para obtener preguntas:

Escribe 20 preguntas acerca de _________ en una lista de diccionarios, 
cada diccionario tendrá dos keys, una llamada "text" y otra llamada "answer", 
cada texto de la pregunta irá en "text" y cada respuesta True o False estará en "answer". 

Por favor que sean preguntas que tengan respuestas "True" o "False" en tipo string, y 
poniendo preguntas de "True" o "False" en orden aleatorio
'''

question_data = [
    {"text": "¿La inteligencia artificial generativa se basa en la capacidad de generar contenido nuevo y original?", "answer": "True"},
    {"text": "¿Los modelos generativos pueden crear imágenes, texto, música y otros tipos de datos?", "answer": "True"},
    {"text": "¿La inteligencia artificial generativa se limita solo a la creación de imágenes?", "answer": "False"},
    {"text": "¿Los modelos generativos pueden ser utilizados en la creación de contenido artístico?", "answer": "True"},
    {"text": "¿Los GAN son un tipo de modelo de inteligencia artificial generativa?", "answer": "True"},
    {"text": "¿Las redes neuronales generativas pueden aprender a imitar cualquier tipo de datos?", "answer": "True"},
    {"text": "¿Los modelos generativos necesitan datos de entrada para generar nuevos contenidos?", "answer": "True"},
    {"text": "¿Los modelos generativos pueden ser utilizados en la producción de música?", "answer": "True"},
    {"text": "¿Los modelos generativos son incapaces de generar contenido realista?", "answer": "False"},
    {"text": "¿La inteligencia artificial generativa solo puede generar contenido aleatorio?", "answer": "False"},
    {"text": "¿Los modelos generativos pueden ser utilizados en la generación de textos literarios?", "answer": "True"},
    {"text": "¿La inteligencia artificial generativa se basa en el aprendizaje supervisado exclusivamente?", "answer": "False"},
    {"text": "¿Los modelos generativos pueden ser utilizados en la creación de videojuegos?", "answer": "True"},
    {"text": "¿La inteligencia artificial generativa se utiliza solo en aplicaciones de entretenimiento?", "answer": "False"},
    {"text": "¿Los modelos generativos pueden ser utilizados en la creación de diseños de moda?", "answer": "True"},
    {"text": "¿La inteligencia artificial generativa puede generar contenido basado en patrones aprendidos de grandes conjuntos de datos?", "answer": "True"},
    {"text": "¿Los modelos generativos pueden ser utilizados en la creación de efectos especiales para películas?", "answer": "True"},
    {"text": "¿La inteligencia artificial generativa no puede ser utilizada en la creación de contenido científico?", "answer": "False"},
    {"text": "¿Los modelos generativos pueden ser utilizados en la creación de paisajes y entornos virtuales?", "answer": "True"},
    {"text": "¿Los modelos generativos pueden generar contenido de manera completamente autónoma sin intervención humana?", "answer": "True"}
]
