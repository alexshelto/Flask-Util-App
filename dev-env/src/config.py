#Alexander Shelton
#creating enviornment variables for production


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.sqlite' #3 slashes = relative path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='7z5x64367g4cfx85475364h6'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
