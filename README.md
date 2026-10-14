# Django ORM Practical Exercise

## College Canteen – Food Order Tracker

### Problem Statement

Your college canteen wants to develop a Django application to manage food orders. Create a Django model to store order details and use Django ORM to perform database operations.

### Task 1: Create the Model

Create a Django model named `FoodOrder` with the following fields:

| S. No. | Field Name    | Data Type    |
| -----: | ------------- | ------------ |
|      1 | customer_name | CharField    |
|      2 | food_item     | CharField    |
|      3 | quantity      | IntegerField |
|      4 | price         | IntegerField |
|      5 | is_delivered  | BooleanField |

### Task 2: Insert the Following Data

Insert the following five food orders into the database.

| S. No. | Customer Name | Food Item    | Quantity | Price (₹) | Is Delivered |
| -----: | ------------- | ------------ | -------: | --------: | ------------ |
|      1 | Arun          | Pizza        |        2 |       250 | Yes          |
|      2 | Priya         | Burger       |        1 |       120 | No           |
|      3 | Karthik       | Sandwich     |        3 |       180 | Yes          |
|      4 | Divya         | Pizza        |        1 |       125 | No           |
|      5 | Sanjay        | French Fries |        2 |       160 | No           |

