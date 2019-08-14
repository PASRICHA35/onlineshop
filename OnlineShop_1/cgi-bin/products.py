import base
import json

file = open('data.json')
products = json.load(file)


#print(cart)
#print(products)


print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <style>
        body {
            background-image : url("http://cdn.osxdaily.com/wp-content/uploads/2011/10/NSTexturedFullScreenBackgroundColor.png");
        }
        h1 {
            color : #fff;
        }
    </style>
</head>
<body>
""")

base.header()

print("""
<div class="container">
    <h1 class="text-center">Products</h1>
    <hr>
    <div class="row">
""")

for i in range(len(products)):
    print("""
    <div class="col-md-4">
    <div class="card" style="width: 18rem;margin-bottom:20px; padding:10px;">
      <img src="{}" class="card-img-top" alt="img" height=400>
      <div class="card-body">
        <h5 class="card-title">{}</h5>
        <p class="card-text">Price : {}</p>
        <a href="cart.py?p_id={}" class="btn btn-primary">Add to Cart</a>
      </div>
    </div>
    </div>
    """.format(products[i]['p_image'], products[i]['p_name'], products[i]['p_price'], products[i]['p_id']))

print("""
</div>
</div>
""")

base.footer()