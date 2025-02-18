#--LEVEL 2-Mid
#AR_GE -> CTE (Common Table Expressions) ve PIVOT

#1) Her Çalışanın En Çok Satış Yaptığı Ürünü Bulun
#Her çalışanın (Employees) sattığı ürünler içinde en çok sattığı (toplam adet olarak) ürünü bulun
#ve sonucu çalışana göre sıralayın.*/

WITH total_sales AS (
    SELECT e.employee_id, e.first_name, e.last_name, p.product_name, SUM(od.quantity) AS amount_of_product_sold
    FROM order_details od
    INNER JOIN products p ON p.product_id = od.product_id
    INNER JOIN orders o ON o.order_id = od.order_id
    INNER JOIN employees e ON e.employee_id = o.employee_id
    GROUP BY e.employee_id, e.first_name, e.last_name, p.product_name
),

most_sold_product AS (
    SELECT employee_id, first_name, last_name, product_name, amount_of_product_sold,
        RANK() OVER (PARTITION BY employee_id ORDER BY amount_of_product_sold DESC) AS line
    FROM total_sales
)

SELECT employee_id, first_name, last_name, product_name, amount_of_product_sold
FROM most_sold_product
WHERE line = 1
ORDER BY employee_id;

#2) Bir Ülkenin Müşterilerinin Satın Aldığı En Pahalı Ürünü Bulun
#Belli bir ülkenin (örneğin "Germany") müşterilerinin verdiği siparişlerde satın aldığı en pahalı ürünü
#(UnitPrice olarak) bulun ve hangi müşterinin aldığını listeleyin.

WITH ordered_products_prices_by_country AS (
    SELECT o.order_id, c.customer_id, c.company_name, p.product_name, od.unit_price, o.ship_country
    FROM customers c
    INNER JOIN orders o ON o.customer_id = c.customer_id
    INNER JOIN order_details od ON od.order_id = o.order_id
	INNER JOIN products p ON p.product_id = od.product_id
    WHERE o.ship_country = 'Spain' --Ülke ismini dilediğiniz gibi değiştirebilirsiniz.
),

highest_priced_product_by_country AS (
    SELECT order_id, customer_id, company_name, product_name, unit_price, ship_country,
        RANK() OVER (PARTITION BY ship_country ORDER BY unit_price DESC) AS ranking
    FROM ordered_products_prices_by_country
)

SELECT order_id, customer_id, company_name, product_name,unit_price, ship_country
FROM highest_priced_product_by_country
WHERE ranking = 1

#3) Her Kategoride (Categories) En Çok Satış Geliri Elde Eden Ürünü Bulun
#Her kategori için toplam satış geliri en yüksek olan ürünü bulun ve listeleyin.

with sales_per_product as (
    select
        p.category_id,
        p.product_id,
        sum(od.unit_price * od.quantity) as totalsales
    from order_details od
    inner join products p on od.product_id = p.product_id
    group by p.category_id, p.product_id
)
select
    cat.category_name,
    p.product_name,
    s.totalsales
from sales_per_product s
inner join products p on s.product_id = p.product_id
inner join categories cat on s.category_id = cat.category_id
where s.totalsales = (
    select max(totalsales)
    from sales_per_product sp
    where sp.category_id = s.category_id
)


#5)  Çalışanların Sipariş Sayısına Göre Kendi Departmanındaki Ortalamanın Üzerinde Olup Olmadığını Belirleyin
#Her çalışanın aldığı sipariş sayısını hesaplayın ve kendi departmanındaki çalışanların ortalama sipariş sayısıyla karşılaştırın.
#Ortalama sipariş sayısının üstünde veya altında olduğunu belirten bir sütun ekleyin.
WITH total_ship AS (
    SELECT
        ship_via,
        employee_id,
        COUNT(*) AS total_ship_by_employee
    FROM orders
    GROUP BY ship_via, employee_id
), #-- Her çalışan için ship sayısı

avarage AS (
    SELECT
        ship_via,
        AVG(total_ship_by_employee) AS avarage_ship
    FROM total_ship
    GROUP BY ship_via
) #-- Her ship_viaların ortalaması

SELECT
    t.ship_via,
    t.employee_id,
    t.total_ship_by_employee,
    a.avarage_ship,
    CASE  #--https://www.w3schools.com/sql/sql_case.asp Bi duruma uygun yazı yazdırma when-else durumu bu linkte güzel anlatılıyor.
        WHEN t.total_ship_by_employee > a.avarage_ship THEN 'Üstünde'
        ELSE 'Altında'
    END AS tekrar_durumu
FROM total_ship t
INNER JOIN avarage a ON t.ship_via = a.ship_via
ORDER BY t.ship_via, t.employee_id;