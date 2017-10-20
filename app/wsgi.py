import sys
sys.path.insert(0, './app/')

from routes import application

if __name__ == "__main__":
	application.run()