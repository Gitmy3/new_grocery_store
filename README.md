# new_grocery_store
This is my new Grocery Store consisting of Food Products and Toiletries.   

I have defined two new routes 'delete_category' and 'delete_product' which accept the respective IDs' of the category or product to be deleted. Inside these routes, we first retrieve the category or product by its ID using SQLAlchemy's 'get_or_404' method to handle not-found errors gracefully. 
