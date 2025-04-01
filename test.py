import google.generativeai as genai

genai.configure(api_key="AIzaSyAQtsgHP5ceRA5Yr2CDGx_sng0cKxhS2uc")

models = genai.list_models()

for model in models:
    print(model.name)
