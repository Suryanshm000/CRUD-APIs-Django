# CRUD-APIs-Django

## Screenshot

<img width="784" alt="image" src="https://github.com/Suryanshm000/CRUD-APIs-Django/assets/65828169/6789a3a6-8091-4f7c-9f3e-d9855ded7ee1">


## API references

**Create a Product**
```
POST
{
name: <string>,
category: <string>,
price: <float>
}

http://127.0.0.1:8000/api/create
```

**Get a single product by id**
```
GET
http://127.0.0.1:8000/api/products/<id>
```

**Get all the products**
```
GET
http://127.0.0.1:8000/api/products
```

**Update a product by id**
```
PUT
http://127.0.0.1:8000/api/products/update/<id>
```

**Delete a product by id**
```
DELETE
http://127.0.0.1:8000/api/products/<id>
```


## Running at localhost

These are the steps to follow in order to run the project on localhost with the help of docker: 
<br>

```
git clone https://github.com/Suryanshm000/CRUD-APIs-Django.git`
```

```
cd CRUD-APIs-Django
```

```
docker-compose build
docker-compose up
```

The *django application* is accessible at *http://127.0.0.1:8000/*
