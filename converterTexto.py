import pyttsx3

# Iniciar a biblioteca
engine = pyttsx3.init()

# Converter texto para fala
engine.say('Hello World!')
engine.say('Como você está no momento?')

# Executar a aplicação
engine.runAndWait()
