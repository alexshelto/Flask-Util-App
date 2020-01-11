#Alexander Shelton
#
#

from src import create_app
from src import db


app = create_app()
app.app_context().push()


#Creating db
with app.app_context():
    db.create_all()



if __name__ == '__main__':
    app.run(debug=True)
