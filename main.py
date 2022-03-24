# import os
#
# import mux_python
#
# configuration = mux_python.Configuration()
# configuration.username = os.environ['744688ef-5102-47e4-9ae1-a20060af58a1']
# configuration.password = os.environ['rY+dttwhxoF6bTvhg++TKJMR7gOWIoGwqKk5/F8dnwfJmpz7F0ofcWmkoZkMdtygLsnjg0eKFC0']
#
# assets_api = mux_python.AssetsApi(mux_python.ApiClient(configuration))
# input_settings = [mux_python.InputSettings(url='https://muxed.s3.amazonaws.com/leds.mp4')]
# create_asset_request = mux_python.CreateAssetRequest(input=input_settings)
# create_asset_response = assets_api.create_asset(create_asset_request)
#
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
