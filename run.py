from app import app
from flask_sqlalchemy import SQLAlchemy


#app = Flask(__name__)
#app.config['SQLAlCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)



if __name__ == "__main__":

    app.run(debug=True)
