from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)

    

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
# do not serialize the password, its a security breach
        }

#class Favorite(db.Model):
  #  id = db.Column(db.Integer, primary_key=True)
   # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #user = db.relationship("User")
    #planet = db.relationship("Planet")
    #person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    #person = db.relationship("Person")
    

    #def __repr__(self):
        #return '<id %r>' % self.id

    #def serialize(self):
      #  return {
       #     "id": self.id,
        #    "user_id": self.user_id,
         #   "planet_id": self.planet_id,
          #  "person_id": self.person_id,
           
            # do not serialize the password, its a security breach
        #}
