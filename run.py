from app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
# host está assim para poder acessar o servidor por outros hosts
