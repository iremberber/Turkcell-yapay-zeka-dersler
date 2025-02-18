"""--LEVEL 1
/*1) En Çok Satış Yapan Çalışanı Bulun
Her çalışanın (Employees) sattığı toplam ürün adedini hesaplayarak,
en çok satış yapan ilk 3 çalışanı listeleyen bir sorgu yazınız.
İpucu: Orders, OrderDetails ve Employees tablolarını kullanarak
GROUP BY ve ORDER BY yapısını oluşturun. TOP 3 veya LIMIT ile ilk 3 çalışanı seçin.*/"""

SELECT e.first_name, e.last_name, SUM(od.quantity) AS total_sales
FROM orders o
INNER JOIN order_details od ON o.order_id = od.order_id
INNER JOIN employees e ON e.employee_id = o.employee_id
GROUP BY e.first_name, e.last_name
ORDER BY SUM(od.quantity) DESC
LIMIT 3

"""/*2) Aylık Satış Trendlerini Bulun
Siparişlerin (Orders) hangi yıl ve ayda ne kadar toplam satış geliri oluşturduğunu hesaplayan
ve yıllara göre sıralayan bir sorgu yazınız. İpucu: Orders ve OrderDetails tablolarını kullanın.
Tarih bilgisini yıl ve aya göre gruplayın, toplam satış gelirini hesaplayarak sıralayın.*/"""

SELECT TO_CHAR(order_date, 'YYYY-MM') AS year_month, SUM(od.quantity*(od.unit_price-od.discount)) AS sales_revenue
FROM orders o
INNER JOIN order_details od ON o.order_id = od.order_id
GROUP BY year_month
ORDER BY year_month

"""/*3) En Karlı Ürün Kategorisini Bulun
Her ürün kategorisinin (Categories), o kategoriye ait ürünlerden (Products) yapılan
satışlar sonucunda elde ettiği toplam geliri hesaplayan bir sorgu yazınız.
İpucu: Categories, Products, OrderDetails ve Orders tablolarını birleştirin.
Kategori bazında gelir hesaplaması yaparak en yüksekten en düşüğe sıralayın.*/"""

SELECT c.category_name, SUM(od.quantity*(od.unit_price-od.discount)) AS sales_revenue
FROM categories c
INNER JOIN products p ON c.category_id = p.category_id
INNER JOIN order_details od ON p.product_id = od.product_id
INNER JOIN orders o ON o.order_id = od.order_id
GROUP BY c.category_name
ORDER BY SUM(od.quantity*(od.unit_price-od.discount)) DESC

"""/*4) Belli Bir Tarih Aralığında En Çok Sipariş Veren Müşterileri Bulun
1997 yılında en fazla sipariş veren ilk 5 müşteriyi listeleyen bir sorgu yazınız.
İpucu: Orders ve Customers tablolarını birleştirin. WHERE ile 1997 yılını filtreleyin,
müşteri bazında sipariş sayılarını hesaplayarak sıralayın ve en fazla sipariş veren 5 müşteriyi seçin.*/"""

SELECT c.company_name, COUNT(o.customer_id) AS number_of_orders
FROM customers c
INNER JOIN orders o ON o.customer_id = c.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) = 1997
GROUP BY c.company_name
ORDER BY COUNT(o.customer_id) DESC
LIMIT 5

"""/*5) Ülkelere Göre Toplam Sipariş ve Ortalama Sipariş Tutarını Bulun
Müşterilerin bulunduğu ülkeye göre toplam sipariş sayısını ve ortalama sipariş tutarını hesaplayan bir
sorgu yazınız. Sonucu toplam sipariş sayısına göre büyükten küçüğe sıralayın.
İpucu: Customers, Orders ve OrderDetails tablolarını birleştirin. Ülke bazında GROUP BY kullanarak
toplam sipariş sayısını ve ortalama sipariş tutarını hesaplayın.*/"""

SELECT c.country, AVG(od.quantity*(od.unit_price-od.discount)) AS avg_sales_price, COUNT(o.customer_id) AS number_of_orders
FROM orders o
INNER JOIN order_details od ON o.order_id = od.order_id
INNER JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.country
ORDER BY c.country
