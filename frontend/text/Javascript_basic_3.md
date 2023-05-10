# 第3章


```python
# 最初に実行してください
!apt-get install -y nodejs
```

## オブジェクト

Javascriptでは、「数値」「文字列」「真偽値」などのあらゆる情報が  
**『オブジェクト』** として管理されています。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let name1 = "Chitose";
let name2 = "Hokudai";

console.log(19); // 整数
console.log(3.14);  // 浮動小数点数
console.log("Hello");
console.log(true);

EOF

# 一時ファイルを実行する
node temp.js
```

    19
    3.14
    Hello
    true
    

![python_3-1.png](https://bit.ly/3HhNMyC)

## メソッド


オブジェクトに何らかの操作を行うための関数のことを**メソッド**といいます。

オブジェクトの種類に応じて多くのメソッドがあります。

## 文字列型のメソッド

文字を変換するためのメソッドには、以下のようなものがあります。

|メソッド|説明|
|:---:| :---: |
|toLowerCase()|すべての文字を小文字に変換|
|toUpperCase()|すべての文字を大文字に変換|
|indexOf()|指定した文字列が最初に現れるインデックスを取得|
|includes()|指定した文字列が含まれるかどうかを判定|
|slice()|指定した位置から指定した位置までの部分文字列を取得|
|split()|指定した区切り文字で文字列を分割して、配列として取得|
|replace()|文字列の中の指定した文字列を別の文字列に置換|

プログラムで確認してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// 文字列オブジェクトを生成
let name = "Chitose Taro";

// 文字列を変換するメソッド
console.log(`${name.toLowerCase()} : lower`);
console.log(`${name.toUpperCase()} : upper`);

EOF

# 一時ファイルを実行する
node temp.js
```

    chitose taro : lower
    CHITOSE TARO : upper
    


```python
# 文字列オブジェクトを生成
str = "Hello World"

# countメソッド
print(f"{str.count('l')}")
```

    3
    


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// spllitを変換するメソッド
let str = "hello world";
console.log(`${str.split('l').length - 1}`);

EOF

# 一時ファイルを実行する
node temp.js
```

    3
    


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let str = "b1990040";

// replaceメソッド
console.log(str.replace('b1990', 'b2019'));

EOF

# 一時ファイルを実行する
node temp.js
```

    b2019040
    

文字列型のメソッドを使って他にもいろんな処理を行いたい際は、  
[こちら](https://www.javadrive.jp/javascript/string/)のサイトを参考にしてください。

## mutableとimmutable



変更可能なオブジェクトを **「mutable」**、  
変更不可能なオブジェクトを **「immutable」** といいます。

|データ型|mutable or immutable|
|:---:| :---: |
|number|immutable|
|string|immutable|
|boolean|immutable|
|null|immutable|
|object|mutable|
|array|mutable|
|Map|mutable|
|Set|mutable|

文字列型のオブジェクトは **immutable** なので、  
メソッドで生成された文字列オブジェクトは、新しいものとなります。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// 文字列オブジェクトを生成
let name1 = "Chitose Taro";
console.log(`置換前のname1 : ${name1}`);

// lowerメソッド
let name2 = name1.toLowerCase();

console.log(`置換後のname1 : ${name1}`);
console.log(`置換後のname2 : ${name2}`);

EOF

# 一時ファイルを実行する
node temp.js
```

    置換前のname1 : Chitose Taro
    置換後のname1 : Chitose Taro
    置換後のname2 : chitose taro
    

## コレクション


JavaScriptには、 **配列** (**Array**)、 **マップ** (**Map**)、**セット** (**Set**)の3つの主要なコレクションがあります。

これらは、関連するデータをグループにして、まとめて1つの変数として扱うことができます。

## 配列


**配列**は、複数の値を1列に並べて管理するためのコレクションです。  
配列の各要素には0から始まるインデックス番号が付けられます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let nothing = null; // nullの代入

// 変数nothingがnullかどうかで分岐
if (nothing === null) {
    console.log(`nothingは${nothing}です`);
} else {
    console.log(`nothingは${nothing}ではありません`);
}

EOF

# 一時ファイルを実行する
node temp.js
```

    nothingはnullです
    

上記のコードでは、nullを代入した変数nothingをif文で評価し、  
その結果に応じてメッセージを出力しています。

注意すべき点としては、Pythonと異なり、JavaScriptでは  
比較演算子として **"==="** を使用する必要があることです。

また、nullとundefinedは別物なので、  
間違ってundefinedを評価しないように注意してください。

### 配列の作成方法

Javascriptで配列を作成する方法はいくつかあります。

#### [ ]を使って配列を作成する

以下のようにして、空の配列を作成することができます。

``` javascript
let arrayName = []; //空の配列を作成する
```

ここで `arrayName` は配列の名前で、 [ ] の中に要素を入れます。

配列内の要素は、文字列、数値、真偽値、オブジェクト、配列など、  
JavaScriptで扱えるあらゆるデータ型を格納することができます。

#### [ ]を使って配列を初期化する

配列の中に要素を含めて、初期化された配列を作成することができます。  
要素は、カンマで区切って配列の中に記述することができます。

``` javascript
let arrayName = [item1, item2, item3]; //要素を持つ配列を作成する
```

#### `Array`コンストラクタを使って配列を作成する

この方法では、`Array()`コンストラクターを使って配列を作成します。

``` javascript
let arr = new Array(); // 空の配列を作成する

```

この方法は、引数として渡すことができる配列の長さを指定することができます。

たとえば、次のようにして、長さが3の配列を作成することができます。

``` javascript
const arr = new Array(3); // 長さが3の配列を作成する
```

### 配列の要素の参照

ではまず、3つの学科の配列を作ってまとめて表示してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const gakka = ["Ouka", "Denshi", "Josisu"];
console.log(gakka);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Ouka', 'Denshi', 'Josisu' ]
    

配列内の特定の要素を参照することもできます。

``` javascript
arrayName[添え字]
```

以下のコードは、配列の1番目の要素を表示するプログラムです。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const gakka = ["Ouka", "Denshi", "Josisu"];
console.log(gakka[1]);

EOF

# 一時ファイルを実行する
node temp.js
```

    Denshi
    

Javascriptでは、添え字として負の数を指定することができません。  
最後の要素にアクセスしたいときは、以下のようにしましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const gakka = ["Ouka", "Denshi", "Josisu"];
console.log(gakka[gakka.length - 1]);

EOF

# 一時ファイルを実行する
node temp.js
```

    Josisu
    

for文を組み合わせることで、簡単にすべての中身を表示するプログラムを書けます。 


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const gakka = ["Ouka", "Denshi", "Josisu"];
for (let p of gakka) {
  console.log(p);
}

EOF

# 一時ファイルを実行する
node temp.js
```

    Ouka
    Denshi
    Josisu
    

### 配列内の合計と要素数の取得

JavaScriptにも、リスト（配列）の合計を求めるための方法があります。  
それは、**`reduce()`メソッド** を使うことです。

`reduce()`メソッドは、リストの要素を1つずつ加算していき、最終的な合計値を返します。

各学科の人数の合計を求めてみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const ninzuu = [75, 99, 94];
const total = ninzuu.reduce((acc, curr) => acc + curr, 0);
console.log(`合計人数は${total}人です`);

EOF

# 一時ファイルを実行する
node temp.js
```

    合計人数は268人です
    

このコードでは、`ninzuu`という配列を定義し、`reduce()`メソッドを使って配列の合計を計算しています。

`reduce()`メソッドには、1つ目の引数として、加算結果を累積するための初期値として0を渡し、  
2つ目の引数として、リストの要素を加算する関数を定義しています。

この関数は、前の処理結果を示す`acc`と、次に加算する要素を示す`curr`を  
引数に取り、それらを加算した結果を返します。

Javascriptには、平均を求めるメソッドはありません。


しかし、配列の要素数で合計を割ることで平均値を求めることができます。   
**`length`プロパティ** を使います。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const ninzuu = [75, 99, 94];
const total = ninzuu.reduce((acc, curr) => acc + curr, 0);
const ave = total / ninzuu.length;
console.log(`平均人数は${ave}人です`);

EOF

# 一時ファイルを実行する
node temp.js
```

    平均人数は89.33333333333333人です
    

### 配列のメソッド 

 
作成したリストの要素を追加したり削除したりできます。  
[こちら](https://www.javadrive.jp/javascript/array/)のページには紹介していないメソッドもあります。

#### 要素のカウント

Pythonでいう**`count`メソッド** のようなものは、Javascriptにはありません。  

**`filter`メソッド** を使えば、似たようなことができます。




```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const university = ["Hokudai", "Hokudai", "Hokudai", "Hokudai", "Hokudai",
                    "Hokudai", "Chitose", "Chitose", "Chitose", "Muroran"];
const count = university.filter((x) => x === "Hokudai").length;
console.log(count);

EOF

# 一時ファイルを実行する
node temp.js
```

    6
    

このコードでは、`university`という配列を定義し、`filter()メソッド`を使って  
`hokudai`と等しい要素だけを取り出し、その数を取得しています。

`filter()`メソッドは、配列の要素を一つずつ処理し、コールバック関数で  
条件に合致するかどうかを判定して、新しい配列を作成します。

その後、`length`プロパティで、新しい配列の要素数を取得しています。

#### 要素の追加

作成した配列に要素を追加するには、**`push`メソッド** を使います。  
配列の末尾に値が追加されます。

以下のコードは、配列`university` に要素`Hakodate`を追加しているプログラムの例です。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ["Chitose", "Hokudai", "Muroran"];
console.log(university);
university.push("Hakodate");
console.log(university);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Muroran' ]
    [ 'Chitose', 'Hokudai', 'Muroran', 'Hakodate' ]
    

この`push`メソッドとfor文を応用すると、以下のようなリストの作成ができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// 空の配列を作成する
let s = [];

// for文とpush()で配列の中身を追加する
for (let i = 0; i < 5; i++) {
  s.push(i);
}

// 結果の確認
console.log(s);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 0, 1, 2, 3, 4 ]
    

#### 要素の削除

**`pop`メソッド** を使うと、配列の末尾の要素を削除することができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ["Chitose", "Hokudai", "Muroran"];
console.log(university);
university.pop();
console.log(university);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Muroran' ]
    [ 'Chitose', 'Hokudai' ]
    

`length`プロパティを0に設定することで、配列内の要素をすべて削除します。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ['Chitose', 'Hokudai', 'Hakodate', 'Muroran'];
console.log(university);
university.length = 0;
console.log(university);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Hakodate', 'Muroran' ]
    []
    

#### 指定位置への要素の追加と削除

**`splice`メソッド** では、配列の指定された位置に新しい要素を挿入したり、既存の要素を削除したりします。

第一引数は、挿入または削除を開始するインデックスです。  
第二引数は、削除する要素の数です。  
第三引数以降は、新しい要素です。

下記のコードでは、2番目の位置に"Hakodate"を挿入し、元の要素を後ろに移動させています。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ["Chitose", "Hokudai", "Muroran"];
console.log(university);
university.splice(2, 0, "Hakodate");
console.log(university);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Muroran' ]
    [ 'Chitose', 'Hokudai', 'Hakodate', 'Muroran' ]
    

下記のコードでは、2番目の要素を削除しています。  



```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ['Chitose', 'Hokudai', 'Hakodate', 'Muroran'];
console.log(university);
university.splice(2, 1);
console.log(university);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Hakodate', 'Muroran' ]
    [ 'Chitose', 'Hokudai', 'Muroran' ]
    

オブジェクトを指定して要素を削除することもできます。   
**`indexOf()`メソッド** を使用して"Hakodate"のインデックスを検索しています。

同じオブジェクトが2回出てくると、最初にヒットする方だけ削除されます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ['Chitose', 'Hokudai', 'Hakodate', 'Muroran'];
console.log(university);
university.splice(university.indexOf('Hakodate'), 1);
console.log(university);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Hakodate', 'Muroran' ]
    [ 'Chitose', 'Hokudai', 'Muroran' ]
    

#### 配列のソート（昇順・降順）


**`sort`メソッド** を使うと、配列の要素を昇順に並び替えることができます。    

`sort`メソッドの後に **`reverse`メソッド** をつけると、降順に並び替えることができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ['Chitose', 'Hokudai', 'Hakodate', 'Muroran'];
console.log(university);

let university1 = university.sort();  // 昇順（アルファベット順）に並び替え
console.log(university1);

let university2 = university.sort().reverse();  // 降順（アルファベット順）に並び替え
console.log(university2);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Hakodate', 'Muroran' ]
    [ 'Chitose', 'Hakodate', 'Hokudai', 'Muroran' ]
    [ 'Muroran', 'Hokudai', 'Hakodate', 'Chitose' ]
    

#### 配列の結合

**`concat`メソッド** をつかうと、配列を結合することができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let gakka_2022 = [75, 99, 94];
let gakka_2021 = [80, 83, 90];
let gakka = gakka_2022.concat(gakka_2021);
console.log(gakka);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 75, 99, 94, 80, 83, 90 ]
    

#### joinとsplit

**`join`メソッド** を使うと、文字列の配列を一つの文字列に連結できます。  
このとき、結合する際の区切り文字を指定できます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ['Chitose', 'Hokudai', 'Hakodate', 'Muroran'];

let text = university.join(" ");  // 空白で文字列を区切る
console.log(text);

text = university.join("\\");  // "\"で文字列を区切る
console.log(text);

EOF

# 一時ファイルを実行する
node temp.js
```

    Chitose Hokudai Hakodate Muroran
    Chitose\Hokudai\Hakodate\Muroran
    

文字列の **`split`メソッド** を使うと、文字列の区切り文字を指定できます。

引数に文字列を分割する際の区切り文字を指定します。  
省略した場合は**空白**で文字列を分割します。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let filename = "sample.py";
let splitFilename = filename.split(".");
console.log(splitFilename[0]); // "."の左側の文字列を出力
console.log(splitFilename[1]); // "."の右側の文字列を出力

EOF

# 一時ファイルを実行する
node temp.js
```

    sample
    py
    

上記のコードでは、`split()`メソッドを使用して、  
"."を区切り文字として文字列を分割しています。

分割された文字列は、配列の要素として変数`splitFilename`に代入されます。  
そして、配列のインデックスを指定して、"."の左側と右側の文字列を取得しています。

**正規表現**を使うことで、複数条件で文字列を分割することができます。  
詳しくは[こちら](https://www.javadrive.jp/javascript/regexp/)の記事などが参考になります。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let filename = "PythonBasic_4.ipynb";
let splitFilename = filename.split(/[_\.]/);
console.log(splitFilename[0]); // "_"の左側の文字列を出力
console.log(splitFilename[1]); // "_"の右側の文字列を出力
console.log(splitFilename[2]); // "."の右側の文字列を出力

EOF

# 一時ファイルを実行する
node temp.js
```

    PythonBasic
    4
    ipynb
    

### 要素の変更

配列内の特定の要素の内容は変更できます。

``` javascript
配列[添え字] = 変更値
```

以下のコードは、配列の2番目の要素を変更するプログラムです。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ['Chitose', 'Hokudai', 'Hakodate', 'Muroran'];
university[2] = "Kitami";
console.log(university);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Kitami', 'Muroran' ]
    

`splice()`メソッドを使用しても、同じことができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let university = ['Chitose', 'Hokudai', 'Hakodate', 'Muroran'];
university.splice(2, 1, "Kitami");
console.log(university);

EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'Chitose', 'Hokudai', 'Kitami', 'Muroran' ]
    

### 配列の要素のスライス

配列で要素を指定する際、**スライス**という構文を用いることで、  
連続した範囲にある要素を参照することができます。

``` javascript
array.slice(start, end)
```

ここで、**`start`** はスライスの開始位置を指定する整数値であり、  
**`end`** はスライスの終了位置を指定する整数値です。

**`end`** で指定したインデックスはスライスには含まれないことに注意してください。

また、`start`と`end`は省略可能であり、  
省略された場合は、配列の先頭からの最初の要素から、配列の末尾までが選択されます。

`start`と`end`がどちらも省略された場合は、元の配列のコピーが返されます。



スライスした配列は、元の配列とは別の新しい配列として返されます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];

console.log(a.slice(1, 3));  // 添え字が1以上3未満の要素
console.log(a.slice(2));  // 添え字が2以上の全ての要素
console.log(a.slice(0, 3));  // 添え字が未満の全ての要素
console.log(a.slice());  // 全ての要素
console.log(a.filter((_, i) => i % 2 === 0));  // 2つ飛ばし

EOF

# 一時ファイルを実行する
node temp.js
```

Javascriptでは、増減値を指定することができません。

代わりに `filter()` メソッドを使用することで、  
指定したステップごとに要素を取り出すことができます。

### .includes()

listオブジェクトに対しても、**`.includes()`** メソッドを適用することができます。

|使い方|説明|
| :---: | :---: |
|b.includes(a)|aはbに含まれる|
|!b.includes(a)|aがbに含まれていない|


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let a = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100];

const university = ['Chitose', 'Hokudai', 'Hakodate', 'Muroran'];

// 文字列"Hokudai"が配列内に入っているかどうか
console.log(university.includes("Hokudai"));
// 文字列"Hokudai"が配列内に入っていないかどうか
console.log(!university.includes("Hokudai"));

// 文字列"Kitami"が配列内に入っているかどうか
console.log(university.includes("Kitami"));
// 文字列"Kitami"が配列内に入っていないかどうか
console.log(!university.includes("Kitami"));

EOF

# 一時ファイルを実行する
node temp.js
```

    true
    false
    false
    true
    

### 二次元配列

配列の中に配列を入れた構造は、**2次元配列**と呼ばれます。  
表の構造を持つデータ管理などに使われます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let number = [
  ["Ouka",80,75],   // 0行目
  ["Denshi",83,99], // 1行目
  ["Josisu",90,94]  // 2行目
];

console.log(number);  // リストnumber全体を参照
console.log(number[0]);  // リストnumberの0番目だけを参照
console.log(`${number[1][0]}の2022年の人数は${number[1][2]}人です`);  // リストnumberの1番目だけを参照

EOF

# 一時ファイルを実行する
node temp.js
```

    [ [ 'Ouka', 80, 75 ],
      [ 'Denshi', 83, 99 ],
      [ 'Josisu', 90, 94 ] ]
    [ 'Ouka', 80, 75 ]
    Denshiの2022年の人数は99人です
    
