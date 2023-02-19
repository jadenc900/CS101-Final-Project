# import website package 
# call app function in views.py

from website import create_app

app = create_app()

# only runs the server when the file is run directly, not just if it is imported
if __name__ == '__main__' : 
    app.run(debug = True) # any change made, will rerun the server   


