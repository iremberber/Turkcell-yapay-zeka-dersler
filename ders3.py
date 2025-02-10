import requests

baseUrl = "http://localhost:3000/products"


def getProducts():
    response = requests.get(baseUrl)
    return response.json()

"""for product in getProducts():
    print(product.get("name"), "/" , product.get("unitPrice")) """


def getProductsByCategory(categoryId):
    response = requests.get(baseUrl + "/?categoryId=" + str(categoryId));
    return response.json()

for product in getProductsByCategory(6):
    print(product.get("name"), "/" , product.get("unitPrice"),"/",product.get("id"))

def createProduct(product):
    response = requests.post(baseUrl,json=product)
    return response.json()

"""productToCreate = {
    "supplierId":2, 
    "categoryId":6,
    "unitPrice":969,
    "name":"Kalem"
}
createProduct(productToCreate)"""

def updateProduct(id, product):
    response = requests.put(baseUrl+"/str(id)",json=product)
    return response.json()

productToUpdate= {
    "supplierId":2, 
    "categoryId":6,
    "unitPrice":969,
    "name":"Kalem"
}



baseUrl = "http://localhost:3000/categories"

def getCategories():
    response = requests.get(baseUrl)
    return response.json()

"""for categorie in getCategories():
    print(categorie.get("name"), "/", categorie.get("description"))"""

def getCategoriesById(id):
    response = requests.get(baseUrl+"/?id="+str(id))
    return response.json()

"""for categorie in getCategoriesById(2):
    print(categorie.get("name"), "/", categorie.get("description"), "/",categorie.get("id"))"""

def createCategories(categorie):
    response = requests.post(baseUrl, json=categorie)
    return response.json()

categorieToCreate =  {
      "id": "22",
      "description": "Sweet and savory",
      "name": "Conditi"
    }
"""createCategories(categorieToCreate)"""

def updateCategorie(id, categorie):
    response = requests.put(baseUrl+"/"+str(id), json=categorie)
    return response.json()

"""categorieToUpdate = {
      "id": "232",
      "description": "Sweet and savoryyyy",
      "name": "Condititi"
    }"""

"""updateCategorie("4", categorieToUpdate)"""

def updateCategorieByPatch(id, categorie):
    response = requests.patch(baseUrl+"/"+str(id), json=categorie)
    return response.json()

categorieToUpdatePatch = {
      "description": "Sweet",
    }

updateCategorieByPatch("4", categorieToUpdatePatch)