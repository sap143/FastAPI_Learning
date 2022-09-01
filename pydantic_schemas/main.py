from fastapi import FastAPI ,APIRouter,Query

from typing import Optional

from schemas import RecipeSearchResults,Recipe,RecipeCreate
# from recipe_data import RECIPE


app=FastAPI(title="Recipe API",openapi_url="/openapi.json")

api_router=APIRouter()

@api_router.get("/",status_code=200)
def root():
    return {"msg":"Salman"}