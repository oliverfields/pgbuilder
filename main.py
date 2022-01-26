from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
	return {
		"message": "Hello world"
	}

async def build():
	return {
		"message": "Hello post"
	}
@app.post('/')
async def get_body(request: Request):
	''' Check post request looks cosher and from viable source, if so try to download file from Dropbox and combine it with pagegen_site from github, then try to build '''

	return await request.json()
