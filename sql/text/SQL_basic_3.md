# SQL入門


```python
# 最初に実行してください
!apt-get install sqlite3
```

前回に引き続き、今回も以下のような家計簿テーブルを作成します。


```python
import sqlite3 # SQLite3ライブラリをインポート

# "sample1.db"という名前のSQLiteデータベースに接続する
con = sqlite3.connect("sample1.db")

# カーソルを作成する
cursor = con.cursor()

# "expense"テーブルを作成するSQLクエリを定義する
sample_query = """
CREATE TABLE IF NOT EXISTS expense (
  id INTEGER PRIMARY KEY,
  date TEXT,
  category TEXT,
  amount INTEGER,
  memo TEXT
);
"""

# SQLクエリを実行する
cursor.execute(sample_query)
```




    <sqlite3.Cursor at 0x7f93d1757640>




```python
# sample1.dbに作成されたテーブルの構造を表示する
!sqlite3 sample1.db ".schema"
```

    CREATE TABLE expense (
      id INTEGER PRIMARY KEY,
      date TEXT,
      category TEXT,
      amount INTEGER,
      memo TEXT
    );
    

前回に引き続き、今回も以下のサンプルデータを追加します。


```python
add_query = """
INSERT INTO expense (id, date, category, amount, memo) VALUES
  (1, '2022-05-21', 'food', 1000, 'lunch'),
  (2, '2022-07-10', 'shopping', 5000, ''),
  (3, '2022-09-07', 'food', 1200, 'dinner'),
  (4, '2022-03-30', 'travel', 8000, ''),
  (5, '2022-02-14', 'food', 800, 'breakfast'),
  (6, '2022-04-05', 'shopping', 1500, ''),
  (7, '2022-06-18', 'travel', 5000, ''),
  (8, '2022-08-21', 'shopping', 2000, ''),
  (9, '2022-12-25', 'food', 1500, 'dinner'),
  (10, '2022-11-05', 'travel', 3000, ''),
  (11, '2022-04-12', 'food', 600, 'snack'),
  (12, '2022-07-28', 'shopping', 2500, ''),
  (13, '2022-09-10', 'travel', 4000, ''),
  (14, '2022-02-17', 'food', 1200, 'lunch'),
  (15, '2022-08-06', 'shopping', 3500, ''),
  (16, '2022-06-30', 'food', 1000, 'breakfast'),
  (17, '2022-11-21', 'travel', 6000, ''),
  (18, '2022-12-18', 'shopping', 1800, ''),
  (19, '2022-03-15', 'food', 1500, 'dinner'),
  (20, '2022-01-22', 'travel', 2000, ''),
  (21, '2022-05-23', 'shopping', 2000, ''),
  (22, '2022-06-05', 'food', 800, 'snack'),
  (23, '2022-07-12', 'travel', 5000, ''),
  (24, '2022-08-14', 'food', 1500, 'dinner'),
  (25, '2022-09-01', 'shopping', 3000, ''),
  (26, '2022-10-06', 'travel', 4000, ''),
  (27, '2022-11-11', 'food', 1000, 'lunch'),
  (28, '2022-12-24', 'shopping', 5000, ''),
  (29, '2022-02-28', 'food', 800, 'breakfast'),
  (30, '2022-03-20', 'travel', 6000, '');

"""

# SQLクエリを実行する
cursor.execute(add_query)

con.commit()
```


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM expense"
```

    id|date|category|amount|memo
    1|2022-05-21|food|1000|lunch
    2|2022-07-10|shopping|5000|
    3|2022-09-07|food|1200|dinner
    4|2022-03-30|travel|8000|
    5|2022-02-14|food|800|breakfast
    6|2022-04-05|shopping|1500|
    7|2022-06-18|travel|5000|
    8|2022-08-21|shopping|2000|
    9|2022-12-25|food|1500|dinner
    10|2022-11-05|travel|3000|
    11|2022-04-12|food|600|snack
    12|2022-07-28|shopping|2500|
    13|2022-09-10|travel|4000|
    14|2022-02-17|food|1200|lunch
    15|2022-08-06|shopping|3500|
    16|2022-06-30|food|1000|breakfast
    17|2022-11-21|travel|6000|
    18|2022-12-18|shopping|1800|
    19|2022-03-15|food|1500|dinner
    20|2022-01-22|travel|2000|
    21|2022-05-23|shopping|2000|
    22|2022-06-05|food|800|snack
    23|2022-07-12|travel|5000|
    24|2022-08-14|food|1500|dinner
    25|2022-09-01|shopping|3000|
    26|2022-10-06|travel|4000|
    27|2022-11-11|food|1000|lunch
    28|2022-12-24|shopping|5000|
    29|2022-02-28|food|800|breakfast
    30|2022-03-20|travel|6000|
    

上記の"expense"テーブルは、以下のような構造を持ちます。

- id：自動的に割り当てられる数値型の主キー列。
- date: ：日付を表すテキスト列。YYYY-MM-DD形式で保存される。
- category：支出のカテゴリを表すテキスト列。
- amount：支出金額を表す数値型の列。
- memo：メモを表すテキスト列。

## データのグループ化

テーブルの行をグループ化して集計したいときは、**GROUP BY**を使います。

``` sql
SELECT グループ化の基準列名…, 集計関数
  FROM テーブル名
 (WHERE 絞り込み条件)
  GROUP BY グループ化の基準列名…
```

GROUP BY 句の後に指定したカラム名の値が同じものが同じグループとなります。

では、"category"カラムでグループ化を行い、  
グループ毎に含まれるデータの行数を取得してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT category, count(*) FROM expense GROUP BY category"
```

    category|count(*)
    food|12
    shopping|9
    travel|9
    

GROUP BY 句に複数の列をカンマで区切って指定すれば、  
複数の列を基準にしたグループ化をすることができます。

"category"カラムと"memo"カラムでグループ化してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT category,memo, count(*) FROM expense GROUP BY category, memo"
```

    category|memo|count(*)
    food|breakfast|3
    food|dinner|4
    food|lunch|3
    food|snack|2
    shopping||9
    travel||9
    

次に、それぞれの月のデータでグループ化し、  
さらに"category"カラムでグループ化してみようと思います。

支出額の合計を可視化してみます。


```python
!sqlite3 sample1.db ".headers on" \
"SELECT strftime('%Y-%m', date) AS month, category, SUM(amount) AS sum \
 FROM expense \
 GROUP BY month, category"
```

    month|category|sum
    2022-01|travel|2000
    2022-02|food|2800
    2022-03|food|1500
    2022-03|travel|14000
    2022-04|food|600
    2022-04|shopping|1500
    2022-05|food|1000
    2022-05|shopping|2000
    2022-06|food|1800
    2022-06|travel|5000
    2022-07|shopping|7500
    2022-07|travel|5000
    2022-08|food|1500
    2022-08|shopping|5500
    2022-09|food|1200
    2022-09|shopping|3000
    2022-09|travel|4000
    2022-10|travel|4000
    2022-11|food|1000
    2022-11|travel|9000
    2022-12|food|1500
    2022-12|shopping|6800
    

3月に旅行代としての支出が多かったようですね。

### グループ後のデータへの条件の設定

WHERE 句では、グループ化する前の条件を指定することになります。

グループ化した後の条件を指定するときは、**HAVING句**を使います。

ここで、SELECT文の構文を改めて整理しましょう。

``` sql
SELECT 選択列リスト
  FROM テーブル名
 [WHERE 条件式]
 [GROUP BY グループ化列名]
 [HAVING 集計結果に対する条件式]
 [ORDER BY 並び替え列名]
```

では、月ごと・カテゴリーごとで支出額の合計をグループ化したもののうち、  
5000円以上のものだけを取得してみましょう。


```python
!sqlite3 sample1.db ".headers on" \
"SELECT strftime('%Y-%m', date) AS month, category, SUM(amount) AS sum \
 FROM expense \
 GROUP BY month, category \
 HAVING sum >= 5000"
```

    month|category|sum
    2022-03|travel|14000
    2022-06|travel|5000
    2022-07|shopping|7500
    2022-07|travel|5000
    2022-08|shopping|5500
    2022-11|travel|9000
    2022-12|shopping|6800
    

## テーブルの結合

今までの家計簿テーブルは以下のような形でした。  
（一部カラムについては省略しています）

![](https://imgur.com/REDHKlW.png)

ここで、家計簿テーブルを  
「家計簿テーブル」と「費目テーブル」の2つに分けてみましょう。

![](https://imgur.com/bbMUHSi.png)　![](https://imgur.com/Ylbp27q.png)



見た目的に見やすいのは単一のテーブルで管理している場合です。

しかし、複数のテーブルに分けて管理すると、**安全・確実にデータを管理する**ことができます。

構文は以下のようになっています。

``` sql
SELECT 選択列リスト
  FROM テーブルA
  INNER JOIN テーブルB
    ON テーブルA.カラム名 = テーブルB.カラム名 
```

ではテーブルを結合してみましょう。


```python
# "new_expense"テーブルを作成するSQLクエリを定義する
sample_query = """
CREATE TABLE IF NOT EXISTS new_expense (
  id INTEGER PRIMARY KEY,
  date TEXT,
  categoryId INTEGER,
  amount INTEGER,
  memo TEXT
);
"""

# SQLクエリを実行する
cursor.execute(sample_query)
```




    <sqlite3.Cursor at 0x7f93d1757640>




```python
add_query = """
INSERT INTO new_expense (id, date, categoryId, amount, memo) VALUES
  (1, '2022-05-21', 1, 1000, 'lunch'),
  (2, '2022-07-10', 2, 5000, ''),
  (3, '2022-09-07', 1, 1200, 'dinner'),
  (4, '2022-03-30', 3, 8000, ''),
  (5, '2022-02-14', 1, 800, 'breakfast'),
  (6, '2022-04-05', 2, 1500, ''),
  (7, '2022-06-18', 3, 5000, ''),
  (8, '2022-08-21', 2, 2000, ''),
  (9, '2022-12-25', 1, 1500, 'dinner'),
  (10, '2022-11-05', 3, 3000, ''),
  (11, '2022-04-12', 1, 600, 'snack'),
  (12, '2022-07-28', 2, 2500, ''),
  (13, '2022-09-10', 3, 4000, ''),
  (14, '2022-02-17', 1, 1200, 'lunch'),
  (15, '2022-08-06', 2, 3500, ''),
  (16, '2022-06-30', 1, 1000, 'breakfast'),
  (17, '2022-11-21', 3, 6000, ''),
  (18, '2022-12-18', 2, 1800, ''),
  (19, '2022-03-15', 1, 1500, 'dinner'),
  (20, '2022-01-22', 'travel', 2000, ''),
  (21, '2022-05-23', 2, 2000, ''),
  (22, '2022-06-05', 1, 800, 'snack'),
  (23, '2022-07-12', 3, 5000, ''),
  (24, '2022-08-14', 1, 1500, 'dinner'),
  (25, '2022-09-01', 2, 3000, ''),
  (26, '2022-10-06', 3, 4000, ''),
  (27, '2022-11-11', 1, 1000, 'lunch'),
  (28, '2022-12-24', 2, 5000, ''),
  (29, '2022-02-28', 1, 800, 'breakfast'),
  (30, '2022-03-20', 3, 6000, '');

"""

# SQLクエリを実行する
cursor.execute(add_query)

con.commit()
```


```python
# "categories"テーブルを作成するSQLクエリを定義する
sample_query = """
CREATE TABLE IF NOT EXISTS categories (
  id INTEGER PRIMARY KEY,
  category TEXT
);
"""

# SQLクエリを実行する
cursor.execute(sample_query)
```




    <sqlite3.Cursor at 0x7f93d1757640>




```python
add_query = """
INSERT INTO categories (id, category) VALUES
  (1, 'food'),
  (2, 'shopping'),
  (3, 'travel');

"""

# SQLクエリを実行する
cursor.execute(add_query)

con.commit()
```


```python
# new_expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM new_expense"
```

    id|date|categoryId|amount|memo
    1|2022-05-21|1|1000|lunch
    2|2022-07-10|2|5000|
    3|2022-09-07|1|1200|dinner
    4|2022-03-30|3|8000|
    5|2022-02-14|1|800|breakfast
    6|2022-04-05|2|1500|
    7|2022-06-18|3|5000|
    8|2022-08-21|2|2000|
    9|2022-12-25|1|1500|dinner
    10|2022-11-05|3|3000|
    11|2022-04-12|1|600|snack
    12|2022-07-28|2|2500|
    13|2022-09-10|3|4000|
    14|2022-02-17|1|1200|lunch
    15|2022-08-06|2|3500|
    16|2022-06-30|1|1000|breakfast
    17|2022-11-21|3|6000|
    18|2022-12-18|2|1800|
    19|2022-03-15|1|1500|dinner
    20|2022-01-22|travel|2000|
    21|2022-05-23|2|2000|
    22|2022-06-05|1|800|snack
    23|2022-07-12|3|5000|
    24|2022-08-14|1|1500|dinner
    25|2022-09-01|2|3000|
    26|2022-10-06|3|4000|
    27|2022-11-11|1|1000|lunch
    28|2022-12-24|2|5000|
    29|2022-02-28|1|800|breakfast
    30|2022-03-20|3|6000|
    


```python
# categoriesテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM categories"
```

    id|category
    1|food
    2|shopping
    3|travel
    

では、結合してみましょう。


```python
# new_expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT new_expense.id, \
        new_expense.date, \
        categories.category, \
        new_expense.amount, \
        new_expense.memo \
 FROM new_expense \
 INNER JOIN categories \
 ON new_expense.categoryId = categories.id; \
"
```

    id|date|category|amount|memo
    1|2022-05-21|food|1000|lunch
    2|2022-07-10|shopping|5000|
    3|2022-09-07|food|1200|dinner
    4|2022-03-30|travel|8000|
    5|2022-02-14|food|800|breakfast
    6|2022-04-05|shopping|1500|
    7|2022-06-18|travel|5000|
    8|2022-08-21|shopping|2000|
    9|2022-12-25|food|1500|dinner
    10|2022-11-05|travel|3000|
    11|2022-04-12|food|600|snack
    12|2022-07-28|shopping|2500|
    13|2022-09-10|travel|4000|
    14|2022-02-17|food|1200|lunch
    15|2022-08-06|shopping|3500|
    16|2022-06-30|food|1000|breakfast
    17|2022-11-21|travel|6000|
    18|2022-12-18|shopping|1800|
    19|2022-03-15|food|1500|dinner
    21|2022-05-23|shopping|2000|
    22|2022-06-05|food|800|snack
    23|2022-07-12|travel|5000|
    24|2022-08-14|food|1500|dinner
    25|2022-09-01|shopping|3000|
    26|2022-10-06|travel|4000|
    27|2022-11-11|food|1000|lunch
    28|2022-12-24|shopping|5000|
    29|2022-02-28|food|800|breakfast
    30|2022-03-20|travel|6000|
    

### 複数テーブルに分ける利点

複数のテーブルに分けて管理すると、安全・確実にデータを管理することができると  
先ほど述べました。

ここでは、実際に分かりやすい例を挙げます。

例えば、古い家計簿テーブルに対して、  
"category"カラムの値をすべて日本語に変更するとしましょう。

以下のように書くことになります。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT category, count(*) FROM expense GROUP BY category"
```

    category|count(*)
    food|12
    shopping|9
    travel|9
    


```python
update_query = """
UPDATE expense
SET category = 
    CASE 
        WHEN category = 'food' THEN '食費'
        WHEN category = 'shopping' THEN '日用品費'
        WHEN category = 'travel' THEN '旅費'
        ELSE category
    END;
"""

# SQLクエリを実行する
cursor.execute(update_query)

con.commit()
```


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT category, count(*) FROM expense GROUP BY category"
```

    category|count(*)
    旅費|9
    日用品費|9
    食費|12
    

1行ずつ条件に合致するかを調べて書き換えることになります。

もし家計簿テーブルが何万行もあったりしたら、明らかに大変です。

では次に、複数テーブルに分けた場合を考えてみましょう。

「費目テーブル」の値を更新するだけで、同様のことができます。


```python
update_query = """
UPDATE categories
SET category = 
    CASE 
        WHEN category = 'food' THEN '食費'
        WHEN category = 'shopping' THEN '日用品費'
        WHEN category = 'travel' THEN '旅費'
        ELSE category
    END;
"""

# SQLクエリを実行する
cursor.execute(update_query)

con.commit()
```


```python
# categoriesテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM categories"
```

    id|category
    1|食費
    2|日用品費
    3|旅費
    

### 内部結合

結合条件を満たす行だけを抽出し、それ以外の行を除外する  
結合方法を**内部結合**といいます。

2つのテーブルに共通するデータだけが結合されます。

これまでやってきたのは内部結合です。  

内部結合が何なのかを分かりやすくするために、「費目テーブル」を以下のように変更します。

![](https://imgur.com/bbMUHSi.png)　![](https://imgur.com/HzXNgQ3.png)

結合結果は以下のようになります。

![](https://imgur.com/YAvfUUF.png)

「費目テーブル」の"ID"カラムの値の中に、  
「家計簿テーブル」の"categoryID"カラムの値が存在しなかった場合は、  
データは取得されません。

### 外部結合

一方のテーブルに存在する行でもう一方のテーブルに存在しない場合の  
結合方法を、**外部結合**といいます。

外部結合の場合は一致しない場合もデータとして取得します。

外部結合が何なのかを分かりやすくするために、「費目テーブル」を以下のように変更します。

![](https://imgur.com/bbMUHSi.png)　![](https://imgur.com/HzXNgQ3.png)

結合結果は以下のようになります。

![](https://imgur.com/AZTV68v.png)

「費目テーブル」の"ID"カラムの値の中に、  
「家計簿テーブル」の"categoryID"カラムの値が存在しなかった場合は、  
内容がすべてNULLな行を生み出して結合します。

構文は以下のようになっています。

``` sql
SELECT 選択列リスト
  FROM テーブルA
  LEFT OUTER JOIN テーブルB
    ON テーブルA.カラム名 = テーブルB.カラム名 
```

ではやってみましょう。


```python
# "new_categories"テーブルを作成するSQLクエリを定義する
sample_query = """
CREATE TABLE IF NOT EXISTS new_categories (
  id INTEGER PRIMARY KEY,
  category TEXT
);
"""

# SQLクエリを実行する
cursor.execute(sample_query)
```




    <sqlite3.Cursor at 0x7f93d1757640>




```python
add_query = """
INSERT INTO new_categories (id, category) VALUES
  (1, 'food'),
  (2, 'shopping');
"""

# SQLクエリを実行する
cursor.execute(add_query)

con.commit()
```


```python
# new_categoriesテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM new_categories"
```

    id|category
    1|food
    2|shopping
    

ではテーブルを結合してみましょう。


```python
# new_categoriesテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT new_expense.id, \
        new_expense.date, \
        new_categories.category, \
        new_expense.amount, \
        new_expense.memo \
 FROM new_expense \
 LEFT OUTER JOIN new_categories \
 ON new_expense.categoryId = new_categories.id; \
"
```

    id|date|category|amount|memo
    1|2022-05-21|food|1000|lunch
    2|2022-07-10|shopping|5000|
    3|2022-09-07|food|1200|dinner
    4|2022-03-30||8000|
    5|2022-02-14|food|800|breakfast
    6|2022-04-05|shopping|1500|
    7|2022-06-18||5000|
    8|2022-08-21|shopping|2000|
    9|2022-12-25|food|1500|dinner
    10|2022-11-05||3000|
    11|2022-04-12|food|600|snack
    12|2022-07-28|shopping|2500|
    13|2022-09-10||4000|
    14|2022-02-17|food|1200|lunch
    15|2022-08-06|shopping|3500|
    16|2022-06-30|food|1000|breakfast
    17|2022-11-21||6000|
    18|2022-12-18|shopping|1800|
    19|2022-03-15|food|1500|dinner
    20|2022-01-22||2000|
    21|2022-05-23|shopping|2000|
    22|2022-06-05|food|800|snack
    23|2022-07-12||5000|
    24|2022-08-14|food|1500|dinner
    25|2022-09-01|shopping|3000|
    26|2022-10-06||4000|
    27|2022-11-11|food|1000|lunch
    28|2022-12-24|shopping|5000|
    29|2022-02-28|food|800|breakfast
    30|2022-03-20||6000|
    

"category"カラムの値が、"travel"から空になって取得できたことが確認できます。

これで、取得結果から何らかの行が消滅してしまうことが避けられます。



![](https://imgur.com/8TsI5MO.png)　![](https://imgur.com/1ASe8QX.png)

そのほかの結合については、[こちら](https://www.javadrive.jp/sqlite/join/)のページなどを参考にしてください。

## ビュー

データベースのテーブルのクエリ結果を仮想的に表したものを **ビュー(view)** といいます。

SELECT 文などによってテーブルの一部のカラムのデータを閲覧したい場合に、  
再利用しやすくなります。

例えば、複数のテーブルを用意した場合、以下のコードを入力してテーブルを結合しました。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT new_expense.id, \
        new_expense.date, \
        categories.category, \
        new_expense.amount, \
        new_expense.memo \
 FROM new_expense \
 INNER JOIN categories \
 ON new_expense.categoryId = categories.id \
 ORDER BY date; \
"
```

    id|date|category|amount|memo
    5|2022-02-14|食費|800|breakfast
    14|2022-02-17|食費|1200|lunch
    29|2022-02-28|食費|800|breakfast
    19|2022-03-15|食費|1500|dinner
    30|2022-03-20|旅費|6000|
    4|2022-03-30|旅費|8000|
    6|2022-04-05|日用品費|1500|
    11|2022-04-12|食費|600|snack
    1|2022-05-21|食費|1000|lunch
    21|2022-05-23|日用品費|2000|
    22|2022-06-05|食費|800|snack
    7|2022-06-18|旅費|5000|
    16|2022-06-30|食費|1000|breakfast
    2|2022-07-10|日用品費|5000|
    23|2022-07-12|旅費|5000|
    12|2022-07-28|日用品費|2500|
    15|2022-08-06|日用品費|3500|
    24|2022-08-14|食費|1500|dinner
    8|2022-08-21|日用品費|2000|
    25|2022-09-01|日用品費|3000|
    3|2022-09-07|食費|1200|dinner
    13|2022-09-10|旅費|4000|
    26|2022-10-06|旅費|4000|
    10|2022-11-05|旅費|3000|
    27|2022-11-11|食費|1000|lunch
    17|2022-11-21|旅費|6000|
    18|2022-12-18|日用品費|1800|
    28|2022-12-24|日用品費|5000|
    9|2022-12-25|食費|1500|dinner
    

ビューでは結果表をテーブルのように扱うことができます。  

つまり、SELECT文によって取得できたデータをを再利用できるようになるということです。 

### ビューの作成

ビューの作成には**CREATE VIEW文**を使います。

``` sql
CREATE VIEW ビュー名 AS SELECT文
```

では、先ほど得られたデータからビューを作成してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"CREATE VIEW combined_expense \
 AS SELECT new_expense.id, \
        new_expense.date, \
        categories.category, \
        new_expense.amount, \
        new_expense.memo \
    FROM new_expense \
    INNER JOIN categories \
    ON new_expense.categoryId = categories.id; \
"
```

このビューにSELECT文を実行してみましょう。


```python
!sqlite3 sample1.db ".headers on" \
"SELECT strftime('%Y-%m', date) AS month, category, SUM(amount) AS sum \
 FROM combined_expense \
 GROUP BY month, category"
```

    month|category|sum
    2022-02|食費|2800
    2022-03|旅費|14000
    2022-03|食費|1500
    2022-04|日用品費|1500
    2022-04|食費|600
    2022-05|日用品費|2000
    2022-05|食費|1000
    2022-06|旅費|5000
    2022-06|食費|1800
    2022-07|旅費|5000
    2022-07|日用品費|7500
    2022-08|日用品費|5500
    2022-08|食費|1500
    2022-09|旅費|4000
    2022-09|日用品費|3000
    2022-09|食費|1200
    2022-10|旅費|4000
    2022-11|旅費|9000
    2022-11|食費|1000
    2022-12|日用品費|6800
    2022-12|食費|1500
    

テーブルを使った時と同じ結果が得られました。

ビュー自体にデータを保持する機能はなく、あくまで参照元のデータをその都度表示する仕組みです。

そのため、参照元のデータが変更された場合には、ビューの内容も自動的に更新されます。

では、ここでは大みそかに食費の出費があったとして、そのデータを追加します。


```python
add_query = """
INSERT INTO new_expense (id, date, categoryId, amount, memo) VALUES
  (31, '2022-12-31', 1, 5000, 'dinner');
"""

# SQLクエリを実行する
cursor.execute(add_query)

con.commit()
```


```python
!sqlite3 sample1.db ".headers on" \
"SELECT strftime('%Y-%m', date) AS month, category, SUM(amount) AS sum \
 FROM combined_expense \
 GROUP BY month, category"
```

    month|category|sum
    2022-02|食費|2800
    2022-03|旅費|14000
    2022-03|食費|1500
    2022-04|日用品費|1500
    2022-04|食費|600
    2022-05|日用品費|2000
    2022-05|食費|1000
    2022-06|旅費|5000
    2022-06|食費|1800
    2022-07|旅費|5000
    2022-07|日用品費|7500
    2022-08|日用品費|5500
    2022-08|食費|1500
    2022-09|旅費|4000
    2022-09|日用品費|3000
    2022-09|食費|1200
    2022-10|旅費|4000
    2022-11|旅費|9000
    2022-11|食費|1000
    2022-12|日用品費|6800
    2022-12|食費|6500
    

ビュー`combined_expense`が自動で更新されていることが、  
12月の食費のデータから確認できます。

また、ビューはテーブルとよく似ていますが、全く同じというわけではありません。

ビューに対してデータの追加や削除、データの更新といった処理を行うことは、  
基本的にはできなくなっています。注意しましょう。

### ビューの削除

ビューの作成には**DROP VIEW文**を使います。

``` sql
DROP VIEW ビュー名
```

では先ほど作ったビュー`combined_expense`を削除してみましょう。


```python
# sample1.dbに作成されたテーブルの一覧を表示する
!sqlite3 sample1.db ".table"
```

    categories        expense           new_expense     
    combined_expense  new_categories  
    


```python
# sample1.dbに作成されたテーブルの一覧を表示する
!sqlite3 sample1.db "DROP VIEW combined_expense"
```


```python
# sample1.dbに作成されたテーブルの一覧を表示する
!sqlite3 sample1.db ".table"
```

    categories      expense         new_categories  new_expense   
    
