## Como usar só o Streamlit:

Clone o repositório, instale Streamlit, e execute: 

    streamlit run /application/main.py

---

## Como usar com PyInstaller e PyWebView:

### 1. Clone o Repositório:

```bash
git clone https://github.com/douglasb78/streamlit_projeto_teste.git
cd streamlit_projeto_teste
```

### 2. Crie um ambiente virtual, ative-o e instale os requisitos:
````bash
python -m venv .venv
.venv\Scripts\activate.bat
pip install -r requirements.txt
````

### 3. Rodando

Para rodar o programa, duas opções:

1. <b>Abrir o arquivo .bat para ativar o ambiente virtual e executar o programa.</b>

2. <b>Empacotar o programa como um .exe para rodar sem a necessidade do Python, usando ``pyinstaller launcher.spec --clean``<br/> O arquivo .exe será gerado na pasta ``dist``. Só copiar a launcher para qualquer lugar e abrir o .exe</b>

