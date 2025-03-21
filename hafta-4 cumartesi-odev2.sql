--Her Müşteri İçin En Son 3 Siparişi ve Toplam Harcamalarını Listeleyin 
--Her müşterinin en son 3 siparişini (OrderDate’e göre en güncel 3 sipariş) 
--ve bu siparişlerde harcadığı toplam tutarı gösteren bir sorgu yazın.

select * from order_details
select * from orders
select * from customers

    SELECT 
        o.customer_id, 
        o.order_id,
		od.product_id
    FROM orders o
    INNER JOIN order_details od ON o.order_id = od.order_id
	group by  o.customer_id, od.product_id, o.order_id
	order by o.customer_id, od.product_id