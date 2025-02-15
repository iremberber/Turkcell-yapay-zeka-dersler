select * from categories
select * from customers
select * from employes
Select * from products where category_id=3
Select * from products where category_id=3 or category_id=4
Select * from products where unit_price>56
Select * from products where product_name = 'Carnarvon Tigers'
Select * from products where product_name like '%ef%'
//Başında ve sonunda % varsa bu başı ve sonu önemli değil demek
Select * from products where product_name like 'ix%'
Select * from products where product_name like '%il%x%' //like sık kullanılır

select * from order_details
select sum(quantity*unit_price) from order_details //Toplam satış parası
select avg(quantity*unit_price) from order_details //Ortalama ne kadar para aldık
select max(quantity*unit_price) from order_details //Ortalama ne kadar para aldık
select min(quantity*unit_price) from order_details 

select distinct(city) from customers
//cityler içindeki tekrar edenleri sadece 1 kez yazar.
select distinct(city),company_name from customers

select * from customers
select city from customers group by city //Hangi şehirden kaçar müşterim var? select distinct(city) from customers Bununla aynı
//group by city = şehre göre grupla
select city,count(*) from customers group by city //count = kaç adet
select city,count(*) as adet from customers group by city // adet olarak da göster

--Hangi üründen toplam kaçar dolar satış yapılmış? (ürün id)
--Hangi personel kaçar sipariş almış? (employerid)
--Hangi tedarikçinin kaçar ürünü var (supplierid)

select * from  order_details  order by product_id
select product_id, sum(quantity*(unit_price*(1-discount))) from order_details group by product_id order by 1

select * from orders
select employee_id, count(order_id) from orders group by employee_id

select * from products
select supplier_id, count(product_id) from products group by supplier_id

--Hangi üründen toplam kaçar dolar satış yapmışız?(product_name)

select product_name, sum(order_details.quantity*(order_details.unit_price*(1-order_details.discount))) 
from products inner join order_details on products.product_id = order_details.product_id
group by product_name

--Hangi personel kaçar sipariş almış? (employee name)

select employees.first_name, employees.last_name, count(order_id) as total_order from employees  
inner join orders on employees.employee_id = orders.employee_id
group by employees.first_name, employees.last_name

--Hangi tedarikçinin kaçar ürünü var (supplier name)

select suppliers.company_name, count(products.product_id) as total_product from suppliers
inner join products on suppliers.supplier_id = products.supplier_id
group by suppliers.company_name