from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
	return {
		"message": "Hello world"
	}

@app.post('/')
async def build():
	return {
		"message": "Hello post"
	}
