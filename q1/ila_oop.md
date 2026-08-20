# ILA 3-1: Applying the Four Pillars of OOP

## Sari-Sari Store Inventory System

### 1. Encapsulation
Encapsulation can be used by creating a Product class that keeps the product's data, such as name, price, and quantity, together with methods that control how the data is changed. For example, methods such as addStock() and removeStock() can update the quantity instead of allowing other parts of the program to change it directly. This protects the product's data and keeps related properties and behaviors organized in one object.

### 2. Abstraction
Abstraction can be applied by providing simple methods that hide the details of how inventory operations are performed. For example, the store can use a method such as sellProduct() without needing to know all the internal steps for checking stock, calculating the total price, and updating the quantity. This makes the program easier to use and allows the complicated implementation details to remain inside the appropriate class.

### 3. Inheritance
Inheritance can be used if the store has different types of products that share common properties and behaviors. A general Product class could contain properties such as name, price, and quantity, while classes such as FoodProduct and NonFoodProduct could inherit these properties and add their own specific information or methods. This reduces repeated code and makes it easier to add new product types to the inventory system.

### 4. Polymorphism
Polymorphism allows different product classes to respond differently to the same method. For example, a getDescription() or calculatePrice() method could be defined in the Product class and implemented differently by FoodProduct and NonFoodProduct. This allows the inventory system to work with different types of products through a common interface while still performing the behavior appropriate for each product.

## Reflection
Among the four pillars of Object-Oriented Programming, I think encapsulation would be the most useful for improving the sari-sari store inventory system. It keeps important product information such as price and stock quantity protected and allows the program to control how these values are changed. This can help prevent invalid changes, such as setting the stock to a negative number. Encapsulation also keeps the data and the methods that manage it together, making the inventory system easier to organize and maintain.
