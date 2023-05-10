# SQL入門


```python
# 最初に実行してください
!apt-get install sqlite3
```

## データモデル

**データモデル**とは、現実世界の対象やシステム内で扱うデータを、  
コンピュータ上で扱いやすい形式に変換するための手法です。

データモデルに従って、データを整理・蓄積・処理することで、  
複数種類・大量のデータを効率的に扱うことができます。



以下のようなデータモデルが存在します。

### リレーショナルデータモデル

リレーショナルデータモデルは、テーブルと呼ばれる2次元的な表を使って、データを表現します。


テーブルは、行と列から構成されており、  
行はデータの個々のレコード、列はデータの属性を表します。

![](https://imgur.com/rXiVfp6.png)

### 他のデータモデル

リレーショナルデータモデル以外にも、以下のようなデータモデルが存在します。

・**階層型データモデル**  
→ データを階層構造で表現するモデルで、木構造のような形式でデータを組織化する。  
　 主に、古いシステムで使われる。

・**ネットワーク型データモデル**  
→ データを複数の集合体（レコード）とポインタで繋ぎ合わせたグラフ構造で表現するモデル。  
　 リレーショナルデータモデルよりも複雑な構造を持つため、扱いが難しい。

・**オブジェクト指向データモデル**  
→ オブジェクト指向プログラミングの考え方をデータベースに適用したモデル。  
　 現在のアプリケーション開発において、最もポピュラーなデータモデルの一つ。

・**NoSQLデータモデル**  
→ リレーショナルデータモデルに縛られない柔軟性の高いデータモデル。  
　 主に、大規模なWebサービスやソーシャルメディア等のWebアプリケーションで使用されている。

## データベース

**データベース**（**DB**）は、データを保管し、整理、保存、そして検索するための電子的な仕組みです。

データベースは、データの整合性を保ちながら、データの追加、変更、削除を行うことができます。  
また、**クエリ言語**を使用して、保存されているデータを検索することができます。

### リレーショナルデータベース

**リレーショナルデータベース**（**RDB**）は、リレーショナルデータモデルに基づいて構築されたデータベースのことを指します。  



リレーショナルデータベースは、その使いやすさなどから、 最も広く使われているデータベースです。  

データを表形式で管理するため、各テーブル間にリレーションシップ（関連）を設定することで、  
複数のテーブルから必要なデータを一括して取得できます。

## データベース管理システム

**データベース管理システム**（**DBMS**）は、データベースを操作するためのソフトウェアです。

DBMSにクエリ言語で書かれた命令文を送信することで、  
データベースに対する操作を実行することができます。

### リレーショナルデータベース管理システム

リレーショナルデータベース管理システム（**RDBMS**）は、  
RDBを採用しているDBMSのことを指します。

RDBに基づいているため、企業や組織にとって信頼性と柔軟性を兼ね備えた  
データ管理システムとして、広く利用されています。



今回は、このRDBMSについてのみ触れていきます。  
このほかのDBMSについては、[こちら](https://bit.ly/40SHXPz)の記事を参考にしてください。

RDBMSには様々な製品が存在します。  
ここでは主要のものについて、特徴を以下に説明します。



1. **SQLite**：単一ユーザー向け。軽量で初学者が使いやすい。Pythonと相性がいい。

2. **MySQL**：オープンソースのRMDBSで、最も広く使用されている。PHPと相性がいい。

3. **PostgreSQL**：MySQLと同様複数ユーザー向けだが、より機能が豊富で、複雑である。  
　 　　　　　大規模なデータベースを扱うときによく使われる。




そのほか有償ではありますが、**Microsoft SQL server** や **oracle** といったRDBMSが存在します。

Google ColabにはSQLiteを使用するためのライブラリが用意されているため、  
ここでは**SQLite**を使って基本的な文法を学習します。

### SQL

**SQL**は、RDBMSでデータを操作するために、最も一般的に使用される標準的なクエリ言語です。

SQLは、Structured Query Language（構造化問い合わせ言語）の略称です。  
「エスキューエル、シークエル」などといわれます。

SQLをRDMBSに送信することで、データベースファイル内の情報を  
検索、追加、更新、削除することができます。

#### 標準SQL

標準SQLは、国際規格化機構（**ISO**）と国際電気標準会議（**IEC**）によって共同で定められた、  
SQLの標準仕様を指します。

各種RDBMSは基本的には標準SQLに沿うように設計されています。

## 実践編

ここまで用語の解説が続いたので、いよいよSQLを体験してみようと思います。

学生の情報を管理する、Userテーブルを作成してみようと思います。


```python
import sqlite3 # SQLite3ライブラリをインポート

# "sample1.db"という名前のSQLiteデータベースに接続する
con = sqlite3.connect("sample1.db")

# カーソルを作成する
cursor = con.cursor()

# "User"テーブルを作成するSQLクエリを定義する
sample_query = """
CREATE TABLE IF NOT EXISTS User (  -- 存在しないときのみテーブルを作成
  UserId INTEGER, -- ユーザーID
  Name TEXT, -- ユーザー名
  Age INTEGER, -- 年齢
  Department TEXT, -- 所属学科
  Email TEXT -- メールアドレス
);
"""

# SQLクエリを実行する
cursor.execute(sample_query)
```




    <sqlite3.Cursor at 0x7f21b0fff1c0>



### テーブルの一覧の確認

データベースに存在するテーブルの一覧を表示したいときは、以下のコマンドを実行します。

``` SQL
.tables
```

では実行してみましょう。


```python
# sample1.dbに作成されたテーブルの一覧を表示する
!sqlite3 sample1.db ".table"
```

    User
    

User テーブルが作成されていることが確認できました。

「**!**」は、Google Colaboratoryでコマンドラインコマンドを実行するために使われる  
マジックコマンドの1つです。

コマンドラインツールに直接コマンドを渡しています。

### テーブルの構造の確認

テーブルの構造を**スキーマ**(**schema**)といいます。

具体的には、テーブルやカラム、インデックス、トリガーなどの定義を含みます。

データベースに存在するテーブルの構造を表示したいときは、以下のコマンドを実行します。

``` SQL
.schema
```

では実行してみましょう。


```python
# sample1.dbに作成されたテーブルの構造を表示する
!sqlite3 sample1.db ".schema"
```

    CREATE TABLE User (  -- 存在しないときのみテーブルを作成
      UserId INTEGER, -- ユーザーID
      Name TEXT, -- ユーザー名
      Age INTEGER, -- 年齢
      Department TEXT, -- 所属学科
      Email TEXT -- メールアドレス
    );
    

UserテーブルのCREATE文が表示されました。

### コメント

SQLにおけるコメントの記述方法には、2つのルールがあります。

① ハイフン2つ「--」から行末まではコメントとして扱われる。  
② 「/\*」から「\*/」まではコメントとして扱われる

### テーブルの作成

テーブルを作成するには、**CREATE TABLE**文を使います。  
基本形は以下の通りです。

``` sql
CREATE TABLE テーブル名 (
  列名1　列1の型名,
  列名2　列2の型名,
  ...
　列名X　列Xの型名
)
```


#### カラムのデータ型

**カラムのデータ型**は、そのカラムに格納できる値の型を指定するものです。

SQLiteでは、以下の5つのデータ型がサポートされています。

1. **INTEGER**  
→ 整数値を表現するためのデータ型。  
　 8バイト以下の整数はすべてINTEGER型として格納される。  

2. **REAL**  
→  浮動小数点数を表現するためのデータ型。  
　 8バイト以下の浮動小数点数はすべてREAL型として格納される。

3. **TEXT**  
→  文字列を表現するためのデータ型。  
　  Unicode文字列を格納することができる。

4. **BLOB**  
→ バイナリデータを表現するためのデータ型。  
　 画像、音声、動画など、様々な種類のデータを格納することができる。

5. **NUMERIC**  
→ INTEGER型とREAL型のいずれかに自動的に変換される汎用的なデータ型。  
　 整数または浮動小数点数のどちらかに自動的に変換される。

#### 値のデータ型

**値のデータ型**は、実際にそのカラムに格納される値の型を表します。

SQLiteでは、以下の5つのデータ型がサポートされています。

1. **INTEGER**  
→ 整数値を表現するためのデータ型。  
　 8バイト以下の整数はすべてINTEGER型として格納される。  

2. **REAL**  
→  浮動小数点数を表現するためのデータ型。  
　 8バイト以下の浮動小数点数はすべてREAL型として格納される。

3. **TEXT**  
→  文字列を表現するためのデータ型。  
　  Unicode文字列を格納することができる。

4. **BLOB**  
→ バイナリデータを表現するためのデータ型。  
　 画像、音声、動画など、様々な種類のデータを格納することができる。

5. **NULL**  
→ 何も値がないことを表す特殊なデータ型。  
　 データベースに値が存在しない場合や、値が不明な場合に使用される。

例えば、TEXT型のカラムにINTEGERやREALのデータ型の値が格納された場合、  
TEXT型に変換されてから格納されます。

また、NUMERIC型のカラムに TEXT 型の値が格納された場合、  
INTEGER 型または REAL 型に変換を試みます。  
成功すればそのデータ型で格納されますが、失敗すれば TEXT 型のまま格納されます。

カラムに格納された値のデータ型の確認方法などは、  
[こちら](https://www.javadrive.jp/sqlite/type/index2.html)のページなどを参照してください。

#### テーブルの更新

テーブル定義の内容を変更するには、**ALTER TABLE**文を使います。  


まず、テーブル名を変更するには、以下のようなALTER TABLE文を使用します。

``` sql
ALTER TABLE テーブル名 RENAME TO 新しいテーブル名;
```

では、"User"テーブルを"Student"テーブルに変更してみましょう。


```python
# "User"テーブルを作成するSQLクエリを定義する
sample_query = """
CREATE TABLE IF NOT EXISTS User (  -- 存在しないときのみテーブルを作成
  UserId INTEGER, -- ユーザーID
  Name TEXT, -- ユーザー名
  Age INTEGER, -- 年齢
  Department TEXT, -- 所属学科
  Email TEXT -- メールアドレス
);
"""

# SQLクエリを実行する
cursor.execute(sample_query)

# "User"テーブルを"Student"テーブルに名前変更
change_tablename = "ALTER TABLE User RENAME TO Student;"

# SQLクエリを実行する
cursor.execute(change_tablename)

# 変更を確定させる
con.commit()
```


```python
# sample1.dbに作成されたテーブルの一覧を表示する
!sqlite3 sample1.db ".table"
```

    Student
    

次に、カラム名を変更するには、以下のようなALTER TABLE文を使用します。

``` sql
ALTER TABLE テーブル名 COLUMN 変更前の列名 TO 変更後の列名;
```


```python
# "UserId"カラムを"Gakuseki"カラムに名前変更
change_columsnname = "ALTER TABLE Student RENAME COLUMN UserId TO Gakuseki;"

# SQLクエリを実行する
cursor.execute(change_columsnname)

# 変更を確定させる
con.commit()
```


```python
# sample1.dbに作成されたテーブルの構造を表示する
!sqlite3 sample1.db ".schema"
```

    CREATE TABLE IF NOT EXISTS "Student" (  -- 存在しないときのみテーブルを作成
      Gakuseki INTEGER, -- ユーザーID
      Name TEXT, -- ユーザー名
      Age INTEGER, -- 年齢
      Department TEXT, -- 所属学科
      Email TEXT -- メールアドレス
    );
    

次に、カラムを追加するには、以下のようなALTER TABLE文を使用します。

``` sql
ALTER TABLE テーブル名 ADD COLUMN 列名 データ型;
```


```python
# "Password"カラムを追加
add_columns = "ALTER TABLE Student ADD COLUMN Password TEXT;"

# SQLクエリを実行する
cursor.execute(add_columns)

con.commit()
```


```python
# sample1.dbに作成されたテーブルの構造を表示する
!sqlite3 sample1.db ".schema"
```

    CREATE TABLE IF NOT EXISTS "Student" (  -- 存在しないときのみテーブルを作成
      Gakuseki INTEGER, -- ユーザーID
      Name TEXT, -- ユーザー名
      Age INTEGER, -- 年齢
      Department TEXT, -- 所属学科
      Email TEXT -- メールアドレス
    , Password TEXT);
    

なお、2023年4月現在、カラムの削除はできないようです。

#### テーブルの削除

作成済みのテーブルを削除するには、DROP TABLE文を使います。


```python
# sample1.dbに作成されたテーブルの一覧を表示する
!sqlite3 sample1.db ".table"
```

    Student
    


```python
# "Student"テーブルを削除
drop_columns = "DROP TABLE Student;"

# SQLクエリを実行する
cursor.execute(drop_columns)

con.commit()
```


```python
# sample1.dbに作成されたテーブルの一覧を表示する
!sqlite3 sample1.db ".table"
```

#### 制約

制約とは、データベースに保存されるデータの整合性を保つために設定される条件のことです。  



制約は、CREATE TABLE文でテーブルを定義する際に、  
列定義の後ろに指定することが可能です。

``` sql
CREATE TABLE テーブル名 (
  列名　型　制約の指定 ,
  ...
)
```

SQLiteには、以下のような制約があります。

1. **DEFAULT制約**  
→ 指定したカラムがデータが挿入されなかった場合に、自動的に設定される値を指定する制約。  
``` sql
カラム名 データ型 DEFAULT デフォルト値
```

2. **NOT NULL制約**  
→  指定したカラムにNULL値を許容しないようにする制約。  
``` sql
カラム名 データ型 NOT NULL
```

3. **UNIQUE制約**  
→  指定したカラムに重複する値を許容しないようにする制約。  
``` sql
カラム名 データ型 UNIQUE
```

4. **CHECK制約**  
→ 指定したカラムに保存される値が、指定された条件を満たしていることを保証する制約。  
``` sql
カラム名 データ型 CHECK (条件式)
```

では、これまで作ってきたUserテーブルに制約を追加してみましょう。


```python
# "User"テーブルを作成するSQLクエリを定義する
sample_query = """
CREATE TABLE IF NOT EXISTS User (  -- 存在しないときのみテーブルを作成
  UserId INTEGER, -- ユーザーID
  Name TEXT NOT NULL, -- ユーザー名。NULLを許容しない。
  Age INTEGER CHECK (Age >= 18), -- 年齢。18歳以上であることを保証する。
  Department TEXT DEFAULT 理工学部, -- 所属学科。未指定時は"理工学部"とする。
  Email TEXT UNIQUE -- メールアドレス。重複を許容しない。
);
"""

# SQLクエリを実行する
cursor.execute(sample_query)
```




    <sqlite3.Cursor at 0x7f21b0fff1c0>




```python
# sample1.dbに作成されたテーブルの構造を表示する
!sqlite3 sample1.db ".schema"
```

    CREATE TABLE User (  -- 存在しないときのみテーブルを作成
      UserId INTEGER, -- ユーザーID
      Name TEXT NOT NULL, -- ユーザー名。NULLを許容しない。
      Age INTEGER CHECK (Age >= 18), -- 年齢。18歳以上であることを保証する。
      Department TEXT DEFAULT 理工学部, -- 所属学科。未指定時は"理工学部"とする。
      Email TEXT UNIQUE -- メールアドレス。重複を許容しない。
    );
    

#### 主キー

テーブル内の各行を一意に識別するための列（カラム）のことを**主キー（Primary Key）**といいます。

主キーに設定された列は、重複が許されず、必ず何らかのデータが格納されます。

主キーの役割を担う列には、**主キー（PRIMARY KEY）制約**を付けます。
``` sql
カラム名 データ型 PRIMARY KEY
```

また、複数のカラムを組み合わせて1つの主キーとして指定する方法を  
**複合主キー（Composite Key）**といいます。

複数の列を組み合わせることで、各行を一意に識別したいときに使用します。


複合主キーの場合は、カラム名をカンマ区切りで指定して PRIMARY KEY 制約を付加します。  
CREATE TABLE文の最後に追加します。
``` sql
PRIMARY KEY(カラム名1, カラム名2, ...)
```

では、UserテーブルのUserIdカラムを主キーとしてみます。


```python
# "User"テーブルを削除
drop_columns = "DROP TABLE User;"

# SQLクエリを実行する
cursor.execute(drop_columns)

con.commit()
```


```python
# "User"テーブルを作成するSQLクエリを定義する
sample_query = """
CREATE TABLE IF NOT EXISTS User (  -- 存在しないときのみテーブルを作成
  UserId INTEGER PRIMARY KEY, -- ユーザーID。主キー。
  Name TEXT NOT NULL, -- ユーザー名。NULLを許容しない。
  Age INTEGER CHECK (Age >= 18), -- 年齢。18歳以上であることを保証する。
  Department TEXT DEFAULT 理工学部, -- 所属学科。未指定時は"理工学部"とする。
  Email TEXT UNIQUE -- メールアドレス。重複を許容しない。
);
"""

# SQLクエリを実行する
cursor.execute(sample_query)
```




    <sqlite3.Cursor at 0x7f21b0fff1c0>




```python
# sample1.dbに作成されたテーブルの構造を表示する
!sqlite3 sample1.db ".schema"
```

    CREATE TABLE User (  -- 存在しないときのみテーブルを作成
      UserId INTEGER PRIMARY KEY, -- ユーザーID。主キー。
      Name TEXT NOT NULL, -- ユーザー名。NULLを許容しない。
      Age INTEGER CHECK (Age >= 18), -- 年齢。18歳以上であることを保証する。
      Department TEXT DEFAULT 理工学部, -- 所属学科。未指定時は"理工学部"とする。
      Email TEXT UNIQUE -- メールアドレス。重複を許容しない。
    );
    

### データの追加

テーブルに新しいデータを追加したいときは、**INSERT文**を使います。  
基本形は以下の通りです。

``` sql
INSERT INTO テーブル名
　　　　　（列名1, 列名2, 列名3, …, 列名x）
　　VALUES（値1, 値2, 値3, …, 値x）
```

では、Userテーブルに学生の情報を追加してみましょう。


```python
add_query = """
INSERT INTO User 
           (UserId, Name, Age, Department, Email) 
    VALUES (2227000, 'Ichiro', 19, '応用化学生物学科', 'Ichiro@example.com');
"""

# SQLクエリを実行する
cursor.execute(add_query)

con.commit()
```

列名を指定しない場合は、  
テーブルの列の順序で値を指定することになります。


```python
add_query = """
INSERT INTO User 
    VALUES (2228000, 'Jiro', 20, '電子光工学科', 'Jiro@example.com');
"""

# SQLクエリを実行する
cursor.execute(add_query)

con.commit()
```

また、一度に複数の行を追加することもできます。  
以下のように、VALUESの括弧内に複数の値をカンマ区切りで指定します。


```python
add_query = """
INSERT INTO User 
    VALUES (2229010, 'Saburo', 18, '情報システム工学科', 'Saburo@example.com'), 
           (2229020, 'Siro', 19, '情報システム工学科', 'Siro@example.com'), 
           (2229030, 'Goro', 20, '情報システム工学科', 'Goro@example.com');
"""

# SQLクエリを実行する
cursor.execute(add_query)

con.commit()
```

このテーブルには制約を多く設けているので、追加の仕方によってはエラーが出ます。  
いろいろと試してみてください。

例1：Departmentカラムを指定しないと、**DEFAULT制約**により値が"理工学部"になる  
例2：Nameカラムを指定しないと、**NOT NULL制約**によりエラー  
例3：Emailカラムの値が重複していると、**UNIQUE制約**によりエラー  
例4：Ageカラムの値が18歳未満だと、**CHECK制約**によりエラー  

### データの取得

テーブルに格納されたデータを取得するには **SELECT文**を使用します。    
基本形は以下の通りです。

``` sql
SELECT 列名1, 列名2, 列名3, …, 列名x
　FROM テーブル名
```

また、すべての列を指定するときは、以下のように記述することが多いです。

``` sql
SELECT *
　FROM テーブル名
```

では、先ほどまでUserテーブルに追加してきた学生の情報を取得してみましょう。

`.headers on`を指定しているため、ヘッダーが表示されています。


```python
# Userテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM User"
```

    UserId|Name|Age|Department|Email
    2227000|Ichiro|19|応用化学生物学科|Ichiro@example.com
    2228000|Jiro|20|電子光工学科|Jiro@example.com
    2229010|Saburo|18|情報システム工学科|Saburo@example.com
    2229020|Siro|19|情報システム工学科|Siro@example.com
    2229030|Goro|20|情報システム工学科|Goro@example.com
    

また、**WHERE句**を用いることで、条件に合致するデータを取得することができます。

``` sql
SELECT *
　FROM テーブル名
　WHERE 条件式
```

今回は、情報システム工学科のデータのみを取り出してみます。


```python
# Userテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM User WHERE Department = '情報システム工学科'"
```

    UserId|Name|Age|Department|Email
    2229010|Saburo|18|情報システム工学科|Saburo@example.com
    2229020|Siro|19|情報システム工学科|Siro@example.com
    2229030|Goro|20|情報システム工学科|Goro@example.com
    

WHERE句については[こちら](https://www.javadrive.jp/sqlite/select/index3.html)のページなどを参考にしてみてください。

### データの更新

データベース内のテーブルの行の値を更新するには**UPDATE文**を使用します。    
基本形は以下の通りです。

``` sql
UPDATE テーブル名
　 SET 列名1 = 値1, 列名2 = 値2, …
　 WHERE 条件式  
```

WHERE句を省略すると、全ての行が更新されてしまう可能性があります。

ここでは、18歳のデータの学科は"理工学部"にデータを更新します。


```python
update_query = """
UPDATE User
  SET Department = '理工学部'
  WHERE Age = 18;
"""

# SQLクエリを実行する
cursor.execute(update_query)

con.commit()
```


```python
# Userテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM User"
```

    UserId|Name|Age|Department|Email
    2227000|Ichiro|19|応用化学生物学科|Ichiro@example.com
    2228000|Jiro|20|電子光工学科|Jiro@example.com
    2229010|Saburo|18|理工学部|Saburo@example.com
    2229020|Siro|19|情報システム工学科|Siro@example.com
    2229030|Goro|20|情報システム工学科|Goro@example.com
    

### データの削除

データベース内のテーブルから行を削除するには**DELETE文**を使用します。    
基本形は以下の通りです。

``` sql
DELETE
　 FROM テーブル名
　 WHERE 条件式  
```

ここでは、情報システム工学科のデータを削除します。


```python
delete_query = """
DELETE
  FROM User
  WHERE Department = '情報システム工学科';
"""

# SQLクエリを実行する
cursor.execute(delete_query)

con.commit()
```


```python
# Userテーブルのデータを取得する
!sqlite3 sample1.db ".headers on" "SELECT * FROM User"
```

    UserId|Name|Age|Department|Email
    2227000|Ichiro|19|応用化学生物学科|Ichiro@example.com
    2228000|Jiro|20|電子光工学科|Jiro@example.com
    2229010|Saburo|18|理工学部|Saburo@example.com
    

### まとめ

ここまで紹介してきた**SELECT文**、**INSERT文**、**UPDATE文**、**DELETE文**が、  
SQLiteの四大命令（SQLの基本的な操作命令）になります。

これらの四大命令を組み合わせることで、データの基本的な操作が可能になります。  
また、これらの命令をSQLクエリとして組み合わせることで、複雑な操作も可能になります。
