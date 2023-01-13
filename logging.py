import logging

# Configurando o logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Criando um handler de arquivo
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Criando um handler de console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Definindo o formato do log
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Adicionando os handlers ao logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Exemplo de uso do logging
logger.debug('Debug message')
logger.info('Info message')
logger.warning('Warning message')
logger.error('Error message')

# Removendo handlers
logger.removeHandler(file_handler)
logger.removeHandler(console_handler)