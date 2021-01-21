from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# create model
class Products(BaseModel):
    name:str
    description:Optional[str] = None
    amount :int
    tax:float

# create get endpoint
@app.get("/")
async def home():
    return {'message':'Welcome to my firt api'}

# get single items
@app.get('/transaction/{trans_id}')
async def singletransaction(trans_id:int, 
            q: Optional[str] = None):
    return {"trans_id":trans_id,'data':q}

# let's create post request
@app.post('/products/')
async def create_products(products:Products):
    product_dict=products.dict()
    # let add tax and amount together/
    if products.tax:
        netIncome =products.amount-products.tax
        product_dict.update({'net':netIncome})
    return product_dict
