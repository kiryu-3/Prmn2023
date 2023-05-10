# SQL入門


```python
# 最初に実行してください
!apt-get install sqlite3
```

## 検索結果の加工

前回、**WHERE句**を使って抽出の条件を指定しました。

``` sql
SELECT 列名1, 列名2, 列名3, …, 列名x
　FROM テーブル名
（WHERE句による修飾）
（そのほかの修飾）
```

今回は他の修飾について学び、検索結果を加工しましょう。

以下のような家計簿テーブルを作成します。


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




    <sqlite3.Cursor at 0x7f5962afb640>




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
    

今回は以下のサンプルデータを追加します。


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

### WHERE句での絞り込み

まずは、WHERE句による絞り込みについてさらに理解を深めていきます。


#### 比較演算子

基本的な**比較演算子**は以下の通りです。  
前回も少し登場しましたよね。

|  比較演算子  |  意味  |
| ---- | ---- |
| **=** | 左右の値が等しい |
| **<** | 左辺は右辺より小さい |
| **>** | 左辺は右辺より大きい |
| **<=** | 左辺は右辺の値以下 |
| **>=** | 左辺は右辺の値以上 |
| **<>** | 左右の値が等しくない |

今回は、5000円以上の出費についてのデータのみ取り出していきます。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE amount >= 5000"
```

    id|date|category|amount|memo
    2|2022-07-10|shopping|5000|
    4|2022-03-30|travel|8000|
    7|2022-06-18|travel|5000|
    17|2022-11-21|travel|6000|
    23|2022-07-12|travel|5000|
    28|2022-12-24|shopping|5000|
    30|2022-03-20|travel|6000|
    

#### NULLの判定

テーブルの中のデータは、何も値が格納されていない状態を意味する  
**NULL**という特別なものになることがあります。

格納データが「不明」であるときに登場します。

今回のデータでいうと、"category"カラムの値が"food"のときは、  
"memo"カラムの値は必ず**NULL**になります。

NULLかどうかを判定するときは、"="演算子や"<>"演算子を利用できません。

NULlであることを判定するためには **IS NULL演算子**、  
NULLでないことを判定するためには **IS NOT NULL 演算子** を使います。


```python
# "memo"カラムの値が空のものは"NULL"値に置き換えます
drop_columns = "UPDATE expense SET memo = NULL WHERE memo = ''"

# SQLクエリを実行する
cursor.execute(drop_columns)

con.commit()
```


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE memo IS NULL"
```

    id|date|category|amount|memo
    2|2022-07-10|shopping|5000|
    4|2022-03-30|travel|8000|
    6|2022-04-05|shopping|1500|
    7|2022-06-18|travel|5000|
    8|2022-08-21|shopping|2000|
    10|2022-11-05|travel|3000|
    12|2022-07-28|shopping|2500|
    13|2022-09-10|travel|4000|
    15|2022-08-06|shopping|3500|
    17|2022-11-21|travel|6000|
    18|2022-12-18|shopping|1800|
    20|2022-01-22|travel|2000|
    21|2022-05-23|shopping|2000|
    23|2022-07-12|travel|5000|
    25|2022-09-01|shopping|3000|
    26|2022-10-06|travel|4000|
    28|2022-12-24|shopping|5000|
    30|2022-03-20|travel|6000|
    


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE memo IS NOT NULL"
```

    id|date|category|amount|memo
    1|2022-05-21|food|1000|lunch
    3|2022-09-07|food|1200|dinner
    5|2022-02-14|food|800|breakfast
    9|2022-12-25|food|1500|dinner
    11|2022-04-12|food|600|snack
    14|2022-02-17|food|1200|lunch
    16|2022-06-30|food|1000|breakfast
    19|2022-03-15|food|1500|dinner
    22|2022-06-05|food|800|snack
    24|2022-08-14|food|1500|dinner
    27|2022-11-11|food|1000|lunch
    29|2022-02-28|food|800|breakfast
    

SQLiteではないですが、[こちらのQiita記事](https://qiita.com/devopsCoordinator/items/9c10410b50f8fcc2ba79)にNULLについて解説があります。

#### パターンマッチングで比較

文字列があるパターンに合致しているかをチェックすることを  
**パターンマッチング**といいます。



SQLではこのパターンマッチングに**LIKE演算子**を使います。

``` sql
式 LIKE パターン文字列
```

検索対象の文字列の中に、指定したパターンが含まれるかどうかを調べます。

LIKE句には、次の2つのワイルドカードがあります。

- **%**：0文字以上の任意の文字列
- **_**（アンダースコア）：任意の1文字

ここでは、2022年12月のデータのみ取り出してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE date LIKE '%-12-%'"
```

    id|date|category|amount|memo
    9|2022-12-25|food|1500|dinner
    18|2022-12-18|shopping|1800|
    28|2022-12-24|shopping|5000|
    

次に、"memo"カラムの値が5文字の文字列であるデータを取り出してみましょう。  
(条件式で _ を5個記述しています)


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE memo LIKE '_____'"
```

    id|date|category|amount|memo
    1|2022-05-21|food|1000|lunch
    11|2022-04-12|food|600|snack
    14|2022-02-17|food|1200|lunch
    22|2022-06-05|food|800|snack
    27|2022-11-11|food|1000|lunch
    

"%"や"_"を含む文字列をLIKE句で探したいときは、少し工夫が必要です。

[こちら](https://bit.ly/3KEWurd)の記事を参考にしてください。

またSQLiteでは、**GROB句**を使ってもLIKE句と同様のことができます。

詳しくは[こちら](https://www.javadrive.jp/sqlite/select/index12.html)の記事を参考にしてください。

#### 指定した値の範囲と比較

ある範囲内に値が収まっているかを判定したいときは、**BETWEEN演算子**を使用します。

``` sql
式 BETWEEN 値1 AND 値2
```

BETWEEN演算子では、データが「値1以上かつ値2以下」の場合に真になります。

ここでは、1000円以上2000円以下の出費が発生したデータのみ取り出してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE amount BETWEEN 1000 AND 2000 "
```

    id|date|category|amount|memo
    1|2022-05-21|food|1000|lunch
    3|2022-09-07|food|1200|dinner
    6|2022-04-05|shopping|1500|
    8|2022-08-21|shopping|2000|
    9|2022-12-25|food|1500|dinner
    14|2022-02-17|food|1200|lunch
    16|2022-06-30|food|1000|breakfast
    18|2022-12-18|shopping|1800|
    19|2022-03-15|food|1500|dinner
    20|2022-01-22|travel|2000|
    21|2022-05-23|shopping|2000|
    24|2022-08-14|food|1500|dinner
    27|2022-11-11|food|1000|lunch
    

#### 指定した値のリストと比較

ある値リストのいづれかにデータが合致するかを判定したいときは、**IN演算子**を使用します。

``` sql
式 IN （値1, 値2, 値3 …）
```

IN演算子を使えば、一度にたくさんの値との比較が可能です。

ここでは、"memo"カラムの値が"lunch"または"snack"に合致する行のみを取り出しましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE memo IN ('lunch', 'snack')"
```

    id|date|category|amount|memo
    1|2022-05-21|food|1000|lunch
    11|2022-04-12|food|600|snack
    14|2022-02-17|food|1200|lunch
    22|2022-06-05|food|800|snack
    27|2022-11-11|food|1000|lunch
    

逆に、値リストのどれとも合致しないことを判定するには、**NOT IN演算子**を使います。

ここでは、"memo"カラムの値が"lunch"または"snack"に合致しない行のみを取り出しましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE memo NOT IN ('lunch', 'snack')"
```

    id|date|category|amount|memo
    3|2022-09-07|food|1200|dinner
    5|2022-02-14|food|800|breakfast
    9|2022-12-25|food|1500|dinner
    16|2022-06-30|food|1000|breakfast
    19|2022-03-15|food|1500|dinner
    24|2022-08-14|food|1500|dinner
    29|2022-02-28|food|800|breakfast
    

#### 論理演算子を使った条件式

1つの条件式ではうまく行を絞り込めない場合、**論理演算子**を使って、  
複数の条件式を組み合わせることができます。

``` sql
WHERE 条件式1 AND 条件式2
WHERE 条件式1 OR 条件式2
WHERE NOT 条件式
```

ここでは、食費として1200円以上使ったデータを取り出してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE category = 'food' AND amount >= 1200"
```

    id|date|category|amount|memo
    3|2022-09-07|food|1200|dinner
    9|2022-12-25|food|1500|dinner
    14|2022-02-17|food|1200|lunch
    19|2022-03-15|food|1500|dinner
    24|2022-08-14|food|1500|dinner
    

### WHERE句以外での加工

WHERE句以外の修飾について学び、目的に応じてデータを成形してきましょう。

#### 結果の並び替え

SELECT分の最後に**ORDER BY句**を記述すると、  
指定した列の値を基準として並び替えた検索結果を取得することができます。

``` sql
SELECT 列名 FROM テーブル名
　ORDER BY 列名 並び順
```

並び順は、昇順にする場合は**ASC**、 
降順にする場合は**DESC**を指定します。

初期値は昇順です。

では、買い物のデータのみを抽出し、日付順に並び替えてみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE category = 'shopping' ORDER BY date"
```

    id|date|category|amount|memo
    6|2022-04-05|shopping|1500|
    21|2022-05-23|shopping|2000|
    2|2022-07-10|shopping|5000|
    12|2022-07-28|shopping|2500|
    15|2022-08-06|shopping|3500|
    8|2022-08-21|shopping|2000|
    25|2022-09-01|shopping|3000|
    18|2022-12-18|shopping|1800|
    28|2022-12-24|shopping|5000|
    

また、ソートする対象のカラムは複数指定できます。

``` sql
SELECT 列名 FROM テーブル名
　ORDER BY 列名1 並び順, 列名2 並び順
```

複数のカラムを指定した場合には、まず最初のカラムでソートを行い、  
次に最初のカラムで同じ値だったものだけを対象に2番目のカラムでソートを行います。

では、食費のデータのみを抽出し、  
"memo"カラムの値で並び替えたあと、さらに日付順に並び替えてみましょう。 


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE category = 'food' ORDER BY memo DESC, date ASC"
```

    id|date|category|amount|memo
    11|2022-04-12|food|600|snack
    22|2022-06-05|food|800|snack
    14|2022-02-17|food|1200|lunch
    1|2022-05-21|food|1000|lunch
    27|2022-11-11|food|1000|lunch
    19|2022-03-15|food|1500|dinner
    24|2022-08-14|food|1500|dinner
    3|2022-09-07|food|1200|dinner
    9|2022-12-25|food|1500|dinner
    5|2022-02-14|food|800|breakfast
    29|2022-02-28|food|800|breakfast
    16|2022-06-30|food|1000|breakfast
    

また、列名ではなく列番号を指定して並び替えることもできます。


先ほどのコードを列番号で書き換えてみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense WHERE category = 'food' ORDER BY 5 DESC, 2 ASC"
```

    id|date|category|amount|memo
    11|2022-04-12|food|600|snack
    22|2022-06-05|food|800|snack
    14|2022-02-17|food|1200|lunch
    1|2022-05-21|food|1000|lunch
    27|2022-11-11|food|1000|lunch
    19|2022-03-15|food|1500|dinner
    24|2022-08-14|food|1500|dinner
    3|2022-09-07|food|1200|dinner
    9|2022-12-25|food|1500|dinner
    5|2022-02-14|food|800|breakfast
    29|2022-02-28|food|800|breakfast
    16|2022-06-30|food|1000|breakfast
    

#### 取得するデータの数の指定

**LIMIT句**を使用することで、取得するデータの数を指定することができます。

``` sql
SELECT 列名 FROM テーブル名
　(ORDER BY 列名 並び順)
　LIMIT 行数
```

行数が指定された場合には先頭のデータから指定した行数のデータだけを取得します。

ORDER BY 句と LIMIT 句が同時に記述された場合、  
まず ORDER BY 句で並び替えを行った上で、  
 LIMIT 句で指定された数のデータを取得します。

では、全体のデータの内、出費が多かった行ベスト5を取り出してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense ORDER BY amount DESC LIMIT 5"
```

    id|date|category|amount|memo
    4|2022-03-30|travel|8000|
    17|2022-11-21|travel|6000|
    30|2022-03-20|travel|6000|
    2|2022-07-10|shopping|5000|
    7|2022-06-18|travel|5000|
    

旅行に結構お金を使っているようですね。

#### 取得を開始する位置の指定

データの取得を行う最初の位置を指定するには、**OFFSET 句**を使用します。

``` sql
SELECT 列名 FROM テーブル名
　(ORDER BY 列名 並び順)
　LIMIT 行数
　OFFSET 開始位置
```

LIMIT 句の後に取得するデータの行数、そして OFFSET 句の後にデータを取得する開始位置を指定します。



OFFSET句は省略することができます。

``` sql
SELECT 列名 FROM テーブル名
　(ORDER BY 列名 並び順)
　LIMIT 開始位置 行数
```

OFFSET句を使用しない場合は、開始位置を指定した後に取得する行数を指定します。

では、全体のデータの内、出費が多かった行の6位～10位を取り出してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT * FROM expense ORDER BY amount DESC LIMIT 5 OFFSET 5"
```

    id|date|category|amount|memo
    23|2022-07-12|travel|5000|
    28|2022-12-24|shopping|5000|
    13|2022-09-10|travel|4000|
    26|2022-10-06|travel|4000|
    15|2022-08-06|shopping|3500|
    

#### 重複データを除外して取得

**DISTINCTキーワード**をSELECT分の選択リストの前に記述すると、  
内容が重複している部分は取り除いて取得できます。

``` sql
SELECT DISTINCT 列名 …
　FROM テーブル名
```

ここでは、どのような種類の支出があったか一覧で取得しましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db "SELECT DISTINCT category FROM expense"
```

    food
    shopping
    travel
    

複数のカラムを指定することもできます。

``` sql
SELECT DISTINCT 列名1, 列名2 …
　FROM テーブル名
```

"memo"カラムも追加してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db "SELECT DISTINCT category, memo FROM expense"
```

    food|lunch
    shopping|
    food|dinner
    travel|
    food|breakfast
    food|snack
    

### 式や関数を使った加工

式や関数を用いて、様々な処理を行うことができます。

#### カラム値に対して四則演算

SELECTの後ろには、今まで選択する列のリストを置いてきました。

ほかにも、**固定値**や**計算式**を指定することもできます。

SQLiteで使用できる算術演算子は以下の通りです。

- +（加算）
- -（減算）
- *（乗算）
- /（除算）
- %（剰余）

ここでは、支出額のカラムに1000円を引いたカラムを取得してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT id,\
        amount,\
        amount-1000\
   FROM expense\
   WHERE category = 'food'"
```

    id|amount|amount-1000
    1|1000|0
    3|1200|200
    5|800|-200
    9|1500|500
    11|600|-400
    14|1200|200
    16|1000|0
    19|1500|500
    22|800|-200
    24|1500|500
    27|1000|0
    29|800|-200
    

固定値や計算式がそのまま表の列名になってしまいます。  

列名を変えるときは**AS演算子**を使います。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
"SELECT *,\
        amount-1000 AS substracted_amount\
   FROM expense\
   WHERE category = 'food'"
```

    id|date|category|amount|memo|substracted_amount
    1|2022-05-21|food|1000|lunch|0
    3|2022-09-07|food|1200|dinner|200
    5|2022-02-14|food|800|breakfast|-200
    9|2022-12-25|food|1500|dinner|500
    11|2022-04-12|food|600|snack|-400
    14|2022-02-17|food|1200|lunch|200
    16|2022-06-30|food|1000|breakfast|0
    19|2022-03-15|food|1500|dinner|500
    22|2022-06-05|food|800|snack|-200
    24|2022-08-14|food|1500|dinner|500
    27|2022-11-11|food|1000|lunch|0
    29|2022-02-28|food|800|breakfast|-200
    

#### カラム値に応じて異なる結果を返す

**CASE演算子**は、列の値や条件式を評価し、  
その結果に応じて値を自由に変換することができます。

``` sql
CASE 評価する列や式 WHEN 値1 THEN 値1の時に返す値  
　　　　　　　　　　WHEN 値2 THEN 値2の時に返す値
　　　　　　　　　　ELSE デフォルト値
 END
```

では、"memo"カラムの値を変換して取得してみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
" SELECT id, date, category, amount, \
  CASE memo \
    WHEN 'breakfast' THEN '朝食' \
    WHEN 'lunch' THEN '昼食' \
    WHEN 'dinner' THEN '夕食' \
    ELSE 'その他' \
  END AS translated_memo \
FROM expense \
WHERE category = 'food' \
"
```

    id|date|category|amount|translated_memo
    1|2022-05-21|food|1000|昼食
    3|2022-09-07|food|1200|夕食
    5|2022-02-14|food|800|朝食
    9|2022-12-25|food|1500|夕食
    11|2022-04-12|food|600|その他
    14|2022-02-17|food|1200|昼食
    16|2022-06-30|food|1000|朝食
    19|2022-03-15|food|1500|夕食
    22|2022-06-05|food|800|その他
    24|2022-08-14|food|1500|夕食
    27|2022-11-11|food|1000|昼食
    29|2022-02-28|food|800|朝食
    

また、構文はもう一つあります。

``` sql
CASE 
   WHEN 条件1 THEN 条件1の時に返す値  
   WHEN 条件2 THEN 条件2の時に返す値
   ELSE デフォルト値
 END
```

では、書き換えてみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" \
" SELECT id, date, category, amount, \
  CASE \
    WHEN memo = 'breakfast' THEN '朝食' \
    WHEN memo = 'lunch' THEN '昼食' \
    WHEN memo = 'dinner' THEN '夕食' \
    ELSE 'その他' \
  END AS translated_memo \
FROM expense \
WHERE category = 'food' \
"
```

    id|date|category|amount|translated_memo
    1|2022-05-21|food|1000|昼食
    3|2022-09-07|food|1200|夕食
    5|2022-02-14|food|800|朝食
    9|2022-12-25|food|1500|夕食
    11|2022-04-12|food|600|その他
    14|2022-02-17|food|1200|昼食
    16|2022-06-30|food|1000|朝食
    19|2022-03-15|food|1500|夕食
    22|2022-06-05|food|800|その他
    24|2022-08-14|food|1500|夕食
    27|2022-11-11|food|1000|昼食
    29|2022-02-28|food|800|朝食
    

#### 関数の適用

**関数**を使うと、式を使うより高度な処理を手軽に実現できます。

ここで紹介していない関数は[こちら](https://www.javadrive.jp/sqlite/function/)のページなどを参考にしてください。

##### COUNT関数

カラムごとの行数を取得することができます。

今回は、それぞれのカラムの行数を取得してみましょう。


```python
# "memo"カラムの値が空のものは"NULL"値に置き換えます
drop_columns = "UPDATE expense SET memo = NULL WHERE memo = ''"

# SQLクエリを実行する
cursor.execute(drop_columns)

con.commit()
```


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT COUNT(id), COUNT(date), COUNT(category), COUNT(amount), COUNT(memo) FROM expense"
```

    COUNT(id)|COUNT(date)|COUNT(category)|COUNT(amount)|COUNT(memo)
    30|30|30|30|12
    

"memo"カラムは"category"カラムの値が"food"ではない場合はNULL値になるので、  
行数が極端に少なくなっています。

カラムに " * " を指定すると、全体の行数を取得できます。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT COUNT(*) FROM expense"
```

    COUNT(*)
    30
    

##### SUM関数

指定したカラムの値の合計を求めます。

では、支出額の合計を求めてみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT SUM(amount) FROM expense"
```

    SUM(amount)
    82200
    

##### AVG関数

指定したカラムの平均値を求めます。

では、支出額の平均を求めてみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT AVG(amount) FROM expense"
```

    AVG(amount)
    2740.0
    

次に、食費の支出額の合計と平均を求めてみましょう。


```python
!sqlite3 sample1.db ".headers on" \
"SELECT \
  SUM(amount) AS total, \
  AVG(amount) AS average \
FROM \
  expense \
WHERE \
  category = 'food'"
```

    total|average
    12900|1075.0
    

##### MAX関数

指定したカラムの最大値を求めます。

では、支出額の最大値を求めてみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT MAX(amount) FROM expense"
```

    MAX(amount)
    8000
    

##### MIN関数

指定したカラムの最小値を求めます。

では、支出額の最小値を求めてみましょう。


```python
# expenseテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT MIN(amount) FROM expense"
```

    MIN(amount)
    600
    

次に、食費の支出額の最大値と最小値を求めてみましょう。


```python
!sqlite3 sample1.db ".headers on" \
"SELECT \
  MAX(amount) AS max, \
  MIN(amount) AS min \
FROM \
  expense \
WHERE \
  category = 'food'"
```

    max|min
    1500|600
    

なお、これまで紹介してきた5つの関数は、  
検索結果のデータを集計する**集計関数**です。

##### strftime()関数

SQLiteの**strftime()関数**は、日付/時刻を文字列に変換する関数です。

strftime()関数は、**書式指定子**を使用して、出力される文字列の形式を制御することができます。

書式指定子は、特定の文字列を置換するために使用される特別な文字列です。  
書式指定子には、日付や時刻の各要素を表す略語が含まれています。

strftime()関数を使用すると、日付や時刻を様々な形式で出力することができます。  
具体的には、次のような書式指定子が用意されています。



|  比較演算子  |  意味  |
| ---- | ---- |
| **%Y** | 西暦年（4桁） |
| **%m** | 月（2桁） |
| **%d** | 日（2桁） |
| **%H** | 時間（24時間表記、2桁） |
| **%M** | 分（2桁） |
| **%S** | 秒（2桁） |
| **%j** | 年間の通算日数（3桁） |
| **%w** | 曜日（0-6で表される。0は日曜日） |
| **%W** | 年間の通算週番号（2桁） |
| **%Z** | タイムゾーンの名前 |


これらの書式指定子を組み合わせることで、様々な形式の日付や時刻を出力することができます。

詳細は[こちら](https://www.javadrive.jp/sqlite/function/index6.html#section4)の記事などを参照してください。

ではまず、現在時刻を取得してみましょう。


```python
# 東京の現在時刻を取得する
!sqlite3 sample1.db "SELECT strftime('%Y-%m-%d %H:%M:%S', 'now', 'localtime', '+9 hours');"
```

    2023-04-29 17:01:39
    

次に、家計簿テーブルについて、それぞれの月のデータを表示してみましょう。


```python
!sqlite3 sample1.db ".headers on" \
"SELECT *, strftime('%Y-%m', date) AS month FROM expense;"
```

    id|date|category|amount|memo|month
    1|2022-05-21|food|1000|lunch|2022-05
    2|2022-07-10|shopping|5000||2022-07
    3|2022-09-07|food|1200|dinner|2022-09
    4|2022-03-30|travel|8000||2022-03
    5|2022-02-14|food|800|breakfast|2022-02
    6|2022-04-05|shopping|1500||2022-04
    7|2022-06-18|travel|5000||2022-06
    8|2022-08-21|shopping|2000||2022-08
    9|2022-12-25|food|1500|dinner|2022-12
    10|2022-11-05|travel|3000||2022-11
    11|2022-04-12|food|600|snack|2022-04
    12|2022-07-28|shopping|2500||2022-07
    13|2022-09-10|travel|4000||2022-09
    14|2022-02-17|food|1200|lunch|2022-02
    15|2022-08-06|shopping|3500||2022-08
    16|2022-06-30|food|1000|breakfast|2022-06
    17|2022-11-21|travel|6000||2022-11
    18|2022-12-18|shopping|1800||2022-12
    19|2022-03-15|food|1500|dinner|2022-03
    20|2022-01-22|travel|2000||2022-01
    21|2022-05-23|shopping|2000||2022-05
    22|2022-06-05|food|800|snack|2022-06
    23|2022-07-12|travel|5000||2022-07
    24|2022-08-14|food|1500|dinner|2022-08
    25|2022-09-01|shopping|3000||2022-09
    26|2022-10-06|travel|4000||2022-10
    27|2022-11-11|food|1000|lunch|2022-11
    28|2022-12-24|shopping|5000||2022-12
    29|2022-02-28|food|800|breakfast|2022-02
    30|2022-03-20|travel|6000||2022-03
    

月のデータだけ取得することができました。
