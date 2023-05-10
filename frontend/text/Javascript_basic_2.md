# 第2章


```python
# 最初に実行してください
!apt-get install -y nodejs
```

## 制御構文


文の実行順をコントロールするプログラムの構成を**制御構造**といいます。 
 
  代表的な構造が**順次**（これまで学習してきたもの）・分岐・繰り返し（今回学習）です。  
この3つの制御構造を組み合わせることで、どんなに複雑なプログラムでも作成できることが理論上可能です。  
これを**構造化定理**といいます。

## 条件式
分岐する条件・繰り返しを続ける条件のことを**条件式**といいます。  
分岐や繰り返しを行いたいときに利用されます。  



### 比較演算子
条件式を立てるときは**比較演算子**と呼ばれる演算子を用います。  

|比較演算子|使い方|説明|
|:---:| :---: | :---: |
|==|a == b|aとbが同じである(a=b)|
|!=|a != b|aがbではない(a≠b)|
|<|a < b|aがbよりも小さい|
|>|a > b|aがbよりも大きい|
|<=|a <= b|aがb以下である(a≦b)|
|>=|a >= b|aがb以上である(a≧b)|

### Boolean型
比較演算子を用いた条件式は、  
条件が成立したら **"true"** 、しなければ **"false**" に置き換わります。

"true"と"false"は**真偽値**といい、データ型は**Boolean型**です。

プログラムで確認してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

console.log(4 == 4); // true
console.log(4 != 4); // false

console.log(4 < 4); // false
console.log(4 > 4); // false
console.log(4 <= 4); // true
console.log(4 >= 4); // true

console.log(4 == 4.0); // JavaScriptが勝手に型を調整するのでtrue
console.log(4 == "4.0"); // JavaScriptが勝手に型を調整して比較するのでtrue

EOF

# 一時ファイルを実行する
node temp.js
```

    true
    false
    false
    false
    true
    true
    true
    true
    

### 論理演算子

2つ以上の条件を組み合わせて、より複雑な条件式を使いたい場合は、  **論理演算子**を用います。

|論理演算子|説明|意味|
|:---:| :---: | :---: |
|&&|かつ|両方の条件が満たされたらTrue|
|\|\||または|どちらかの条件が満たされたらTrue|
|!|否定|条件が満たされなかったらTrue|

プログラムで確認してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const number = Math.floor(Math.random() * 16); // 0～15までの整数をランダムに取得
console.log(number);

console.log(number >= 0 && number <= 10); // 0以上10以下の値ならTrue
console.log(number <= 0 || number >= 10); // 0以下の値か10以上の値ならTrue
console.log(!(number == 10)); // numberが10ではなかったらTrue

EOF

# 一時ファイルを実行する
node temp.js
```

    0
    true
    true
    true
    

## if文 

 
条件に応じて処理を分岐させるために使用される**if文**は、  
ほとんどのプログラミング言語で似たような構文を持っています。

if文には、ifブロック、else ifブロック（省略可能）、elseブロックがあります。

JavaScriptでは、ブロックの範囲を波括弧（{}）で示します。

基本形は**if-else構文**です。  
条件式が成立したときとしなかったときで、処理を分けることができます。  


``` javascript
if (条件式) {
  // 条件式がtrueの場合に実行する文
} else {
  // 条件式がfalseの場合に実行する文
}
```

条件式が成立しなかった場合に何もしない場合は、elseブロックを省略することができます。  
これは**ifのみの構文**となります。

``` javascript
if (条件式) {
    // 条件式が真の場合に実行する文
}
```

条件式が成立しなかった時には別の条件式で判定したい場合は、  
ifブロックのあとにelifブロックを追加した**if-else if構文**を使用します。

``` javascript
if (条件式1) {
  // 条件式1が真の場合に実行する処理
} else if (条件式2) {
  // 条件式1が偽で条件式2が真の場合に実行する処理
} else {
  // 条件式1と条件式2が偽の場合に実行する処理
}
```

下のコードは、**if-else構文**を用いたプログラムの例です。  


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let number = Math.floor(Math.random() * 101); // 0～100までの整数をランダムに取得
console.log(`この科目の合計点は${number}点です`);
let result = number % 2;

// 偶数奇数判定をするプログラム
if (result == 0) {
  console.log(`${number} は偶数です`);
} else {
  console.log(`${number} は奇数です`);
}

EOF

# 一時ファイルを実行する
node temp.js
```

    この科目の合計点は32点です
    32 は偶数です
    

下のコードは、**if-elif構文**を用い、  なおかつ論理演算子も用いたプログラムの例です。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let point = Math.floor(Math.random() * 101); // 0～100までの整数をランダムに取得
console.log(`この科目の合計点は${point}点です`);

if (point >= 0 && point < 60) { // 0点以上60点未満
  console.log("成績はEです");
} else if (point >= 60 && point < 70) { // 60点以上70点未満
  console.log("成績はDです");
} else if (point >= 70 && point < 80) { // 70点以上80点未満
  console.log("成績はBです");
} else if (point >= 80 && point < 90) { // 80点以上90点未満
  console.log("成績はAです");
} else if (point >= 90 && point <= 100) { // 90点以上100点以下
  console.log("成績はSです");
} else { // エラー処理
  console.log("点数を正しく入力してください");
}

EOF

# 一時ファイルを実行する
node temp.js
```

    この科目の合計点は72点です
    成績はBです
    

## switch文

JavaScriptには**switch文**があります。  
switch文は、複数の条件に対して処理を分岐させる場合に使用されます。

以下は、switch文の基本的な書き方です。

``` javascript
switch (式) {
  case 値1:
    // 値1に該当する処理
    break;
  case 値2:
    // 値2に該当する処理
    break;
  case 値3:
    // 値3に該当する処理
    break;
  default:
    // 上記のいずれにも該当しない場合の処理
    break;
}
```

switch文は、式の評価結果によって、値1、値2、値3のいずれかに該当する場合に、その処理を実行します。  
該当する値がない場合は、**default**の処理を実行します。

また、**break**文がない場合は、該当する処理の実行後に次の処理も実行されます。  
（この後詳しく解説します）

## whileループ  
回数の決まっていない繰り返しには、**whileループ**を使用することが多いです。  

``` javascript
while (条件式) {
  繰り返す処理
}
```

処理を実行する前に条件式を評価します。  
評価結果が**true**である間は、処理が繰り返し実行されます。

 下のコードは、第1回目～第3回目まで出力するプログラムの例です。  


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let i = 0;
while (i < 3) {
  console.log(`${i+1}回目です`);
  i++;
}
console.log("終了しました");

EOF

# 一時ファイルを実行する
node temp.js
```

    1回目です
    2回目です
    3回目です
    終了しました
    

変数`i`のように、繰り返すたびにその値が変化し、繰り返しの条件となる変数のことを  
**カウンタ変数**または**ループ変数**（**ループカウンタ**）といいます。  

変数`i`の値をwhileブロックの中で更新し忘れると、繰り返しが終了しません。  
このようないつまでも続く繰り返しのことを**無限ループ**と呼びます。

あえて無限ループを作るときは以下のようにしましょう。  


``` javascript
while (true) {
  // 無限ループの処理
}
```

## forループ   
コンピュータは、同じことを何回も繰り返すことができます。    
回数の決まっている繰り返しには、**forループ**を使用することが多いです。  

``` javascript
for (初期化処理; 繰り返し条件 ; 繰り返し時処理) {
  繰り返す処理;
}
```

#### 初期化処理




for文による繰り返しを始める前に、最初に一回だけ実行される文です。  
通常、何回目のループなのかを記録する変数の宣言や初期化を行います。

このような変数を**ループ変数**といいます。  
ループ変数は1文字の変数名（特に「**i**」）にすることが多いです。  
for文内での計算や表示などの処理に用いることができます。

#### 繰り返し条件



ループを継続するかしないかを判定する条件式です。  
評価結果が真である間は、処理が繰り返し実行されます。


#### 繰り返し時処理


ループの本体で実行される文です。  
通常は、ループ変数の値を更新する文を書きます。

### プログラム例

下のコードは、第0回目～第3回目まで出力するプログラムの例です。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

for (let i = 0; i < 4; i++) {
  console.log(`${i}回目です`);
}
console.log("終了しました");

EOF

# 一時ファイルを実行する
node temp.js
```

    0回目です
    1回目です
    2回目です
    3回目です
    終了しました
    

開始値と増減値は省略しています。  
**(終了値-1)**回までの反復処理が行われることが確認できました。  

下のコードは、第1回目～第3回目まで出力するプログラムの例です。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

for(let i = 1; i < 6; i += 2) {
  console.log(`${i}回目です`);
}
console.log("終了しました");

EOF

# 一時ファイルを実行する
node temp.js
```

    1回目です
    3回目です
    5回目です
    終了しました
    

1からスタートすることができました。   

下のコードは、第1回目～第5回目までの内奇数回を出力するプログラムの例です。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

for (let i = 1; i < 6; i += 2) {
  console.log(`${i}回目です`);
}
console.log("終了しました");

EOF

# 一時ファイルを実行する
node temp.js
```

    1回目です
    3回目です
    5回目です
    終了しました
    

for文を使って九九を表示してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// 縦方向のループ用
for (let num1 = 1; num1 < 10; num1++) {
  // 横方向のループ用
  for (let num2 = 1; num2 < 10; num2++) {
    // 改行なしで2ケタ表示
    process.stdout.write(`${num1 * num2 < 10 ? " " : ""}${num1 * num2} `);
  }
  // 1行分が終わったので改行を実施
  console.log()
}

EOF

# 一時ファイルを実行する
node temp.js
```

     1  2  3  4  5  6  7  8  9 
     2  4  6  8 10 12 14 16 18 
     3  6  9 12 15 18 21 24 27 
     4  8 12 16 20 24 28 32 36 
     5 10 15 20 25 30 35 40 45 
     6 12 18 24 30 36 42 48 54 
     7 14 21 28 35 42 49 56 63 
     8 16 24 32 40 48 56 64 72 
     9 18 27 36 45 54 63 72 81 
    

## 繰り返しの中断
処理によっては、繰り返しを最後まで行わずに途中で中断したいことがあります。  


**break文**はループそのものを中断し、ループの次に記述された処理へと進みます。 

以下のコードで確認しましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let i = 0;

while (true) {
  console.log(`${i+1}回目です`);
  i++;

  if (i == 3) {
    break;
  }
}

console.log("終了しました");

EOF

# 一時ファイルを実行する
node temp.js
```

    1回目です
    2回目です
    3回目です
    終了しました
    

一方の**continue文**は、ループの現在の回だけを中断してループの先頭へ戻り、次の回のループを継続します。  

**※多重ループの場合、break文、continue文は現在のループに対してのみ有効です。**


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

for (let i = 1; i <= 5; i++) {
  if (i % 2 === 0) {  // 変数iが偶数のときループをスキップ
    continue;
  }
  
  console.log(`第${i}回目`);
}

console.log("終了しました");

EOF

# 一時ファイルを実行する
node temp.js
```

    第1回目
    第3回目
    第5回目
    終了しました
    

下のコードは、break文とcontinue文と無限ループを用いて、  
成績処理を3回だけ行うプログラムの例です。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let count = 1; // 成績処理回数

while (true) {
  let point = Math.floor(Math.random() * (111 - (-10) + 1) + (-10)); // -10～110までの整数をランダムに取得
  console.log(`${count}回目`);
  console.log(`この科目の合計点は${point}点です`);

  if (point >= 0 && point < 60) { // 0点以上60点未満
    console.log("成績はEです\n");
  } else if (point >= 60 && point < 70) { // 60点以上70点未満
    console.log("成績はDです\n");
  } else if (point >= 70 && point < 80) { // 70点以上80点未満
    console.log("成績はBです\n");
  } else if (point >= 80 && point < 90) { // 80点以上90点未満
    console.log("成績はAです\n");
  } else if (point >= 90 && point <= 100) { // 90点以上100点以下
    console.log("成績はSです\n");
  } else { // エラー処理
    console.log("点数を正しく入力してください\n");
    continue; // 成績処理をしてないものとしてループの先頭へ
  }

  count += 1;
  if (count == 4) { // 3回の成績処理を終えたらループから抜ける
    break;
  }
}

console.log("終了しました");

EOF

# 一時ファイルを実行する
node temp.js
```

    1回目
    この科目の合計点は104点です
    点数を正しく入力してください
    
    1回目
    この科目の合計点は40点です
    成績はEです
    
    2回目
    この科目の合計点は95点です
    成績はSです
    
    3回目
    この科目の合計点は68点です
    成績はDです
    
    終了しました
    

## for文による参照


文字列や配列（次回学習）などのデータの集まりは、  
forループを使って簡単に参照することができます。



以下のコードは、文字列"b2223456" を順に1文字ずつ変数numberに格納し、  
1文字ずつ出力するプログラムです。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// numberという変数に、"b1990040"という文字列を入れる
let number = "b1990040";

// for文で文字列を1文字ずつ出力する
for(let i=0; i<number.length; i++){
console.log(number[i]);
}

EOF

# 一時ファイルを実行する
node temp.js
```

    b
    1
    9
    9
    0
    0
    4
    0
    

今後「配列」などを学習した際に活躍します。

# 第2章補足


## 文字列同士の比較

Javascriptにおける数字と文字列の比較では、少しだけ違いがあります。  
C言語よりは大分簡単に扱うことができます。  

|比較演算子|使い方|説明|
|:---:| :---: | :---: |
|==|a==b|aとbが同じである(a=b)|
|!=|a!=b|aがbではない(a≠b)|
|<|a<b|aがbより辞書的に前|
|>|a>b|aがbより辞書的に後|
|<=|a<=b|aがbより辞書的に前または同じ|
|>=|a>=b|aがbより辞書的に後または同じ|


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let name1 = "Chitose";
let name2 = "Hokudai";

console.log(name1 == name2); // "Chitose"と"Hokudai"は同じではないのでfalse
console.log(name1 != name2); // "Chitose"と"Hokudai"は同じではないのでtrue

console.log(name1 < name2); // "Chitose"は"Hokudai"より辞書的に前なのでtrue
console.log(name1 > name2); // "Chitose"は"Hokudai"より辞書的に後ではないなのでfalse
console.log(name1 <= name2); // "Chitose"は"Hokudai"より辞書的に前なのでtrue
console.log(name1 >= name2); // "Chitose"は"Hokudai"より辞書的に後ではないなのでfalse

EOF

# 一時ファイルを実行する
node temp.js
```

    false
    true
    true
    false
    true
    false
    

## .includes()


JavaScriptには、文字列や配列に特定の要素が含まれるかどうかを判定するための  
**`.includes()`**メソッドが用意されています。

`.includes()`メソッドは、引数に指定した要素が  
対象の文字列や配列に含まれる場合に true を、含まれていない場合には false を返します。

|使い方|説明|
| :---: | :---: |
|b.includes(a)|aはbに含まれる|
|!b.includes(a)|aがbに含まれていない|


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let a = "b1990040";
let b = "b199";

console.log(a.includes(b)); // "b199"が"b1990040"に含まれるのでtrue
console.log(!a.includes(b)); // "b199"が"b199040"に含まれるのでfalse

EOF

# 一時ファイルを実行する
node temp.js
```

    true
    false
    

## 三項演算子


JavaScriptにおける**三項演算子**は、条件式を評価して真偽値を返し、  
真であれば第1引数を、偽であれば第2引数を返す演算子です。

一般的な書き方は以下の通りです。

``` javascript
// 一般的なfor文
if (条件式) {
  // 条件式がtrueの場合に実行する文
} else {
  // 条件式がfalseの場合に実行する文
}
```

``` javascript
// 三項演算子
条件式 ? 式1 : 式2

```

さきほどの関数のif文の箇所を1行で記述しましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const number = Math.floor(Math.random() * 101); // 0~100の整数をランダムに取得
console.log(`この科目の合計点は${number}点です`);
const result = number % 2;

// 偶数奇数判定をするプログラム
result == 0 ? console.log(`${number} は偶数です`) : console.log(`${number} は奇数です`);

EOF

# 一時ファイルを実行する
node temp.js
```

    この科目の合計点は94点です
    94 は偶数です
    

三項演算子はif文を簡潔に書くために使われることが多いです。  
結構癖が強めです。

## null

何も存在しないことを表すオブジェクトは、Pythonでは "None" と呼ばれますが、  
JavaScriptには対応するものがあります。

それは、 "**null**" という特別な値です。

JavaScriptでは、"**undefined**" という値も存在しますが、  
PythonのNoneとは少し異なります。  

undefinedは、値が設定されていないことを表し、  
nullは、存在しないことを明示的に表します。

例えば、変数が何らかの値を持たない場合や、オブジェクトのプロパティが存在しない場合に、    
nullを使用することができます。
