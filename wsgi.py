from application import app

if __name__ == "__main__":
    app.run()

    
# app.run(debug=True,host='0.0.0.0')

#web: gunicorn -w 4 -b 0.0.0.0 application:app
