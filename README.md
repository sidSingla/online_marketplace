This Flask app is a barebones for the online market place.
Products are stored in and fetched from the sqlite db.

To run the web-server, run "python3 api.py"
Following APIs are supported - 

1. API to fetch the items and their prices available in the inventory.
API to get all the products can be accessed by - 
curl -XGET localhost:5000/get?product=all

API to get a specific product can be accessed by -
curl -XGET localhost:5000/get?product=Winter_Caps

2. API to purchase a specific product. The count of the product item will be decreased in the database.
curl -XGET localhost:5000/purchase?product=Winter_Caps

3. API to view the purchased items.
curl -XGET localhost:5000/checkcart

4. API to checkout the cart. This is when the customer has finished shopping and pays the money. 
The API will show the final cart with the final cost. The cart will get cleared.
curl -XGET localhost:5000/checkout

The API calls can be made using curl command or using postman.
