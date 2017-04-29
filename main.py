  from clarifai.rest import ClarifaiApp

  app = ClarifaiApp("PWco1JgPhe9dQGMvCBXb7wU6iPBdxh-MnkAaPJrN", "_J9OaT7VHEDZ0zLiuvyX4pyu2rGxoyBoloHaWAPU")

  # get the general model
  # model = app.models.get("general-v1.3")

  # predict with the model
  model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
