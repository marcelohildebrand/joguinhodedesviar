# Navegador Web Simples

Um aplicativo desktop simples que abre páginas web em uma janela dedicada.

## Requisitos para Desenvolvimento

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

## Instalação para Desenvolvimento

1. Clone este repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Executando em Modo Desenvolvimento

```bash
python app.py
```

## Criando o Executável

Para criar um executável único:

```bash
pyinstaller --onefile --windowed app.py
```

O executável será criado na pasta `dist`.

## Uso

1. Execute o arquivo `Navegador Web.exe` da pasta `dist`
2. O navegador abrirá automaticamente com a página inicial configurada
3. Use normalmente como um navegador web

## Personalização

Para mudar a URL inicial, edite o arquivo `app.py` e altere a URL na linha:
```python
url='https://www.google.com'
``` 