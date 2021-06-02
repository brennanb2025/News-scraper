from app import app

if __name__ == '__main__': #on flask run include: -p 5372 after to run it on port 5372.
    app.run(port=5372)
    #if run w/ basicServer.py instead of flask run