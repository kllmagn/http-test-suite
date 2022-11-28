def parse_config(config_path:str) -> dict:
    '''Считывает конфигурационный файл и возвращает словарь с данными'''
    conf = {}
    try:
        file = open(config_path, 'r')
    except (FileNotFoundError, PermissionError):
        return conf
    text = file.read().split() # Считываем файл и разбиваем на слова
    i = 1
    for word in text:
        if word in ['thread_limit', 'port', 'cpu_count']:
            conf[word] = int(text[i])
        elif word in ['document_root', 'host']:
            conf[word] = text[i]
        i += 1
    return conf
