use ecom;
select city,category,sum(quantity*price_per_unit) as total_sale from orders
group by city,category with rollup;