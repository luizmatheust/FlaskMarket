from market import app

# Verifica se o arquivo run.py foi executado diretamente e não sendo importado.
if __name__ == '__main__':
    app.run(debug=True)