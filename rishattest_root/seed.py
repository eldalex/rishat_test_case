import sqlite3
#сидим тестовые данные, admin/admin, несколько товаров и заказов.
conn = sqlite3.connect("db.sqlite3")
sql = 'INSERT INTO "main"."auth_user" ("id", "password", "last_login", "is_superuser", "username", "last_name", "email", "is_staff", "is_active", "date_joined", "first_name") VALUES ("1", "pbkdf2_sha256$390000$PUeqzpj0TdJdA1CTr1Rj3G$T67sqapQlaX+Q30x1TgmcUuEw56qB0H23kvzjjoPxP4=", "2022-11-18 13:48:13.426777", "1", "admin", "", "", "1", "1", "2022-11-18 13:47:41.942854", "");'
conn.execute(sql)
sql =  'INSERT INTO "main"."store_discount" ("id", "Discount_name", "Discount_percent") VALUES ("1", "Без скидки", "0"),("2", "10%", "10"),("3", "50%", "50");'
conn.execute(sql)
sql = 'INSERT INTO "main"."store_tax" ("id", "Tax_name", "Tax_percent") VALUES ("1", "Без налога", "0"),("2", "Налог 13%", "13"),("3", "Налог 30%", "30");'
conn.execute(sql)
sql = 'INSERT INTO "main"."store_item" ("id", "name", "description", "price") VALUES ("1", "HDD 1Tb", "Жесткий диск 1 ТБ", "10000"),("2", "Монитор", "Монитор 30", "300000"),("3", "Intel core i9", "Процессор", "50000");'
conn.execute(sql)
sql = 'INSERT INTO "main"."store_order" ("id", "odrer_dt", "order_name", "order_discount_id", "order_tax_id") VALUES ("1", "2022-11-18 14:05:25.912014", "Alex", "2", "1"),("2", "2022-11-18 14:05:42.855715", "Alex2", "2", "2");'
conn.execute(sql)
sql = 'INSERT INTO "main"."store_orderdetail" ("id", "order_dt", "item_count", "detail_binding_id", "item_binding_id") VALUES ("1", "2022-11-18 14:56:03.596810", "3", "1", "3"),("2", "2022-11-18 13:49:36.533076", "2", "1", "2"),("3", "2022-11-18 14:07:46.689137", "2", "2", "1"),("4", "2022-11-18 14:07:58.080728", "3", "2", "2");'
conn.execute(sql)
conn.commit()
conn.close()
