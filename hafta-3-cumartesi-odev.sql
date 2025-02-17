--INNER JOİN SORULARI
--1
--ikisinde de ortak olarak customer_id bulunuyor. Bu yüzden ordan birleştiriyoruz. 
SELECT customers.contact_name, COUNT(orders.order_id) AS total_orders FROM customers
INNER JOIN orders  ON customers.customer_id = orders.customer_id
GROUP BY customers.contact_name
HAVING COUNT(orders.order_id) >= 5;

--2
--ikisinde de ortak olarak employee_id bulunuyor. Bu yüzden ordan birleştiriyoruz. 
SELECT employees.employee_id, COUNT(orders.order_id) AS total_orders FROM employees 
INNER JOIN orders  ON employees.employee_id = orders.employee_id
GROUP BY employees.employee_id 
HAVING COUNT(orders.order_id) >= 0 ORDER BY total_orders DESC --Burda desc büyükten küçüğe sıralattı.
LIMIT 3; --Limit de sadece 3 tanesinin gelebilmesi için

--3
--ikisinde de ortak olarak product_id bulunuyor. Bu yüzden ordan birleştiriyoruz.
SELECT products.product_name, COUNT(order_details.quantity) AS total_quantity FROM products 
INNER JOIN order_details  ON products.product_id = order_details.product_id
GROUP BY products.product_id
HAVING COUNT(order_details.quantity) >= 0 ORDER BY total_quantity DESC --Burda desc büyükten küçüğe sıralattı.
LIMIT 5;--Limit de sadece 5 tanesinin gelebilmesi için

--4
SELECT customers.contact_name, categories.category_id, categories.category_name FROM customers

--Customer ve orderlarda ortal olan customer_id
INNER JOIN orders ON customers.customer_id=orders.customer_id
--order_detail ile orderda ortak olan order_id
INNER JOIN order_details ON orders.order_id=order_details.order_id
--products ve order details arası ortak olan product_id
INNER JOIN products ON products.product_id=order_details.product_id
--categories ve products arası ortak olan da category id
INNER JOIN categories ON categories.category_id=products.category_id

GROUP BY customers.contact_name, categories.category_id, categories.category_name
ORDER BY customers.contact_name DESC

select distinct customers.contact_name, categories.category_name
from customers
inner join orders on customers.customer_id = orders.customer_id
inner join order_details on orders.order_id = order_details.order_id
inner join products on order_details.product_id = products.product_id
inner join categories on products.category_id = categories.category_id
order by customers.contact_name, categories.category_name
--5

SELECT customers.customer_id, products.product_id, products.product_name ,COUNT(order_details.quantity) AS total_quantity FROM customers

--Customer ve orderlarda ortal olan customer_id
INNER JOIN orders ON customers.customer_id=orders.customer_id
--order_detail ile orderda ortak olan order_id
INNER JOIN order_details ON orders.order_id=order_details.order_id
--products ve order details arası ortak olan product_id
INNER JOIN products ON products.product_id=order_details.product_id

GROUP BY customers.customer_id, products.product_id
HAVING COUNT(order_details.quantity) >= 0 ORDER BY total_quantity DESC --Burda desc büyükten küçüğe sıralattı.

--LEFT JOİN SORULARI

--1
SELECT customers.customer_id, COUNT(orders.order_id) AS total_orders FROM customers
LEFT JOIN orders ON customers.customer_id=orders.customer_id
GROUP BY customers.customer_id
HAVING COUNT(orders.order_id) = 0
--inner dan farkı = inner yazdığımızda boş değerleri bize göstermiyor illa eşleşme istiyor ama left hepsini gösteriyor.

--2
--ikisinde de ortal supplier_id var
SELECT suppliers.supplier_id, COUNT(products.units_on_order) AS total_units_on_order FROM suppliers
LEFT JOIN products  ON suppliers.supplier_id = products.supplier_id
GROUP BY suppliers.supplier_id
HAVING COUNT(products.units_on_order) = 0 ORDER BY total_units_on_order
--Bunu ben yazdım hiç değer vermeyince pair arkadaşlarım nasıl yapmış diye onlardan kopyalayıp çalıştırdım onlarda da boş değer çıktı. Yani tahminimce satış yapmamış  yok.

--3
SELECT employees.first_name, employees.last_name, COUNT(orders.order_id) AS total_order FROM employees
LEFT JOIN orders  ON employees.employee_id = orders.employee_id
GROUP BY employees.employee_id
HAVING COUNT(orders.order_id) = 0 --Bunda da değer çıkmadı

--RIGHT JOIN SORULARI
--Sağ taraftaki tüm değerleri getir, sol tarafta bu değer yoksa ona null değer ata demek.

--1
SELECT customers.customer_id, COALESCE(orders.order_id, 0) AS order_id FROM orders RIGHT JOIN customers ON customers.customer_id = orders.customer_id ORDER BY order_id;
--yazı olarak bir türlü yazdıramadım sürekli hata verdi.

--2
SELECT categories.category_id, products.product_id FROM products RIGHT JOIN categories ON categories.category_id=products.category_id ORDER BY product_id DESC;
--null değer göremedim
