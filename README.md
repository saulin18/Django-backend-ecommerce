
# E-commerce Django


Backend maded in Django for a E-commerce platform. 






## API Reference

#### Get all items

```http
 /orders/
```



#### Get item

```http
 /orders/{id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |

```http
POST /orders/add
```
Just add a order


```http
PUT /orders/deliver/{id}
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to update |


```http
GET /orders/my
```
Get my orders

```http
GET /products
```
Get all


```http
GET /products
```
```http
GET /products/cate/{category}/
```

Get all products with a category in specific

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `category`      | `string` | **Required**. category of item to fetch |

```http
DELETE /products/delete/{id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. id of item to delete |

```http
PUT /products/edit/{id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to update |

```http
GET /products/get/{slug}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `slug`      | `string` | **Required**. slug of item to fetch |

```http
GET /products/get/admin/{id}/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to fetch |

```http
POST /products/post
```
Create a product

```http
POST /products/review/{id}
```
Create a review for a product

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `integer` | **Required**. Id of item to find |

```http
GET /products/search/
```

```http
POST /users/login
```

AUTH IMPLEMENTED WITH JWT

```http
POST /users/refresh/
```

Refresh token

```http
POST /users/register/
```

Create a user

```http
/users/users/
```

Get all users












