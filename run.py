'''
	author: 		Cameron Wilson
	date:			March 10, 2015
	description:	The main file for the sortable program
'''
import json

with open("products.txt") as product_file:
	product_data = [json.loads(line) for line in product_file.readlines()]

with open("listings.txt") as listing_file:
	listing_data = [json.loads(line) for line in listing_file.readlines()]

output_data = [{"product_name":product["product_name"], "listings":[]} for product in product_data]

model_pname = {product["model"]:product["product_name"] for product in product_data}
model_list = [product["model"] for product in product_data]
with open("debug.txt", "w") as debug_file:
	for listing in listing_data:
		models_in_listing = [model for model in model_list if model in listing["title"]]
		debug_file.write(str(listing) + "\n")
		debug_file.write(str(models_in_listing) + "\n")
		if len(models_in_listing) == 1: #one and only one model found in the listing, it's probably a listing for that product
			#add to the listings for that product:
			[item["listings"].append(listing) for item in output_data if item["product_name"] == model_pname[models_in_listing[0]]]


with open("output.txt", "wb") as output_file:
	for line in output_data:
		json.dump(line, output_file)
		output_file.write("\n")


