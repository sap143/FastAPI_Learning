from fastapi import FastAPI,Query,Path,Body
from pydantic import BaseModel,Field
#from pydantic.types import UrlStr

class Item(BaseModel):
	name:str
	description:str | None=Field(default=None,title="The description of the item",max_length=300)
	price:float=Field(gt=0,description="The price must be greater than Zero")
	tax:float | None=None
	tag:set[str]
class User(BaseModel):
	username:str
	full_name:str

class Image(BaseModel):
	name:str
	url:str


app=FastAPI()

@app.get("/")
async def index():
	return {"Hello":"Salman"}



#@app.put("/items/{item_id}")
#async def create_item(item_id:int,item:Item,q:str|None=None):
	#result={"item_id":item_id,**item.dict()}
	#if q:
		#result.update({'q':q})
	#return result


#@app.get("/items/{item_id}")
#async def read_lines(item_id:int=Path(title="the ID of the item to get"),q:str|None=Query(default=None,alias="item-query")):
	#result={'item_id':item_id}
	#if q:
		#result.update({'q':q})
	#return result
#@app.get("/items/{item_id}")
#async def read_items(*,item_id:int=Path(title="The ID of the item to get",gt=0,le=100),q:str):
	#result={'irem_id':item_id}
	#if q:
		#result.update({'q':q})
	#return result

#@app.put("/items/{item_id}")
#async def read_it(*,item_id : int=Path(title="This is title for path variable",ge=0,le=100),q : str | None=None,item : Item | None=None,):
	
	#results={"item_id":item_id}
	#if q:
		#results.update({'q':q})
	#if item:
		#results.update({'item':item})
	#return results


#@app.put("/items/{item_id}")
#async def read_it(item_id:int,item:Item=Body(embed=True)):
	#results={'item_id':item_id,'item':item}
	#return results


@app.post("/images/multiple")
async def image_store(*,images:list[Image]):
	for image in images:
		print("Hello")
	return images


@app.get("/items/")
async def create_list(q:list[int]=Query(default=...,)):
	query_item={"q":q}
	return query_item





