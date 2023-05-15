# 第1章


```python
# 最初に実行してください
!apt-get install -y nodejs
```

<details>
<summary>xxx</summary>

aaaaaaaaaaaaaaaaaaaaa
bbbbbbbbbbbbbbbbbbb
ccccccccccccccccccccc
</details>

## console.log関数

**`console.log`関数**を使うことで画面に文字を表示することができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
console.log("Hello World!");
console.log("Welcome to JavaScript!");
console.log(25);
EOF

# 一時ファイルを実行する
node temp.js
```

    Hello World!
    Welcome to JavaScript!
    25
    

`console.log`関数の途中で改行したいときは、**" \n "** を途中に挿入します。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
console.log("Hello World!\nWelcome to JavaScript!");
EOF

# 一時ファイルを実行する
node temp.js
```

    Hello World!
    Welcome to JavaScript!
    

**`process.stdout.write`** 関数を使用すると、改行を防止することができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
process.stdout.write("Hello World! ");
process.stdout.write("Welcome to JavaScript!, ");
process.stdout.write("25");
EOF

# 一時ファイルを実行する
node temp.js
```

    Hello World! Welcome to JavaScript!, 25

## 数値型

数値型(Number)には**整数(integers)**、**浮動小数点数(floating-point numbers)** の2つがあります。  

また、JavaScriptには**BigInt型**という、非常に大きな整数を表すためのデータ型もあります。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
console.log(25);
console.log(25.25);
EOF

# 一時ファイルを実行する
node temp.js
```

    25
    25.25
    

### 数値型の算術演算子
以下表のような四則演算をすることができます。 

|演算子|  例  |  概要  |
| ---- | ---- | ---- |
|  +  |  x+y  |  足し算  |
|  -  |  x-y  |  引き算  |
|  *  |  x*y  |  掛け算  |
|  **  |  x**y  | 階乗  |
|  /  |  x/y  |  割り算<br>(商は実数)  |
|  %  |  x%y  |  剰余算<br>(除算の余り)  |



```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
console.log(25 + 1); // 足し算
console.log(25 - 1); // 引き算

console.log(2 * 4); // 掛け算
console.log(2 ** 4); // 階乗

console.log(25 / 4); // 割り算（商は実数）
console.log(25 % 4); // 剰余算

console.log( 25 - 2*5 ); // 演算子の優先順位
console.log( (25-2) * 5 ); // 剰余算
EOF

# 一時ファイルを実行する
node temp.js
```

    26
    24
    8
    16
    6.25
    1
    15
    115
    

## 文字列型

JavaScriptの文字列は『**シングルクォーテーション**』か『**ダブルクォーテーション**』で囲みます。  
単数文字か複数文字かの区別はなく、どちらを使ってもよいです。  

囲むときは同じものをセットで使う必要があることに注意しましょう。  
『**ダブルクォーテーション**』を使うことが多いようです。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
console.log('Hello World!');
console.log("Hello World!");
EOF

# 一時ファイルを実行する
node temp.js
```

    Hello World!
    Hello World!
    

### 文字列型の算術演算子
以下表のような四則演算をすることができます。 

|演算子|  説明  |  例  |  結果  |  
| ---- | ---- | ---- | ---- |  
|  +  |  連結（文字列+文字列）  |  'w' + 'w'  | ww |  
|  .repeat  |  反復（文字列.repeat(数値)) |  'w'.repeat(3)  | www |  


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
console.log("Hello" + "World!");
console.log("Hello".repeat(3));
EOF

# 一時ファイルを実行する
node temp.js
```

    HelloWorld!
    HelloHelloHello
    

### 数値型と文字列型の注意

JavaScriptでは、数値型と文字列型を結合することができます。  
数値型と文字列型を結合する場合は、数値型が自動的に文字列型に変換されます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
console.log(25 + 4);  // 29を出力
console.log("25" + "4");  // "254"を出力
EOF

# 一時ファイルを実行する
node temp.js
```

    29
    254
    


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
console.log("25" + 4);  // "254"を出力
EOF

# 一時ファイルを実行する
node temp.js
```

    254
    

## 変数

**変数**は、データを格納するためにコンピュータ内部に準備する箱のようなものです。  


JavaScriptで変数を宣言する場合は、**`let`** もしくは **`const`** キーワードを使います。

**`let`** は再代入可能な変数、**`const`** は再代入不可能な定数として宣言します。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
let name = "Chitose";  // nameという変数に、文字列の"Chitose"を代入
let number = "b1998040";  // numberという変数に、文字列の"b1998040"を代入
let age = 25;  // ageという変数に、整数の"25"を代入 

console.log(name);
console.log(number);
console.log(age);
EOF

# 一時ファイルを実行する
node temp.js
```

    Chitose
    b1998040
    25
    

変数のキーワードについては[JavaDriveの記事](https://www.javadrive.jp/javascript/var/)や[3PySciの記事](https://3pysci.com/javascript-3/)が参考になります。

### 自己代入
変数に入っている数値を利用して計算を行い、再度その変数に書き戻す演算を**自己代入**といいます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js
let age = 25;

// 元の変数に対して4を加算する
age = age + 4;
console.log(age);
EOF

# 一時ファイルを実行する
node temp.js
```

    29
    

自己代入には省略形があります。  
以下の表を参考にしてください。

|代入演算子|  記述例  |  意味  | 
| ---- | ---- | ---- |    
| +=  |  a +=  b  |  a = a + b  |   
|  -=  |  a -=  b  |  a = a - b  | 
|  *=  |  a *=  b  |  a = a * b  | 
|  /=  |  a /=  b  | a = a / b  |
|  %=  |  a %=  b  |  a = a % b  | 
|  **=  |  a **=  b  | a = a ** b  |


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let age = 25;
age += 4;
console.log(age);  // 足し算

age = 25;
age -= 4;
console.log(age);  // 引き算

age = 2;
age *= 4;
console.log(age);  // 掛け算

age = 2;
age **= 4;
console.log(age);  // 階乗

age = 25;
age /= 4;
console.log(age);  // 割り算（商は実数）

age = 25;
age %= 4;
console.log(age);  // 剰余算


EOF

# 一時ファイルを実行する
node temp.js
```

    29
    21
    8
    16
    6.25
    1
    

## データ型


プログラムで扱うことのできるデータの種類を**データ型**といいます。 




JavaScriptにおけるデータ型は以下表のようなものがあります。

|種類|  型  |  例  | 
| ---- | ---- | ---- |    
| 文字列  |  string  |  "Taro" , "b2220000"  |   
|  整数  |  number  |  -12 , 19  | 
|  浮動小数点数  |  number  |  -0.5 , 19.0  | 
|  真偽値  |  boolean  | True , False  |

Pythonとは異なり、JavaScriptには明示的に型を指定する必要がありません。  
JavaScriptでは、変数に代入された値に基づいて、その変数の型が自動的に決まります。

**Pythonでは、変数代入した値によってそのデータ型が決まります。**

Pythonの柔軟性がよく分かるでしょう。

### typeof演算子


**typeof演算子**を使うと、変数にどのような型の値が格納されているかを調べることができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let name = "Chitose";
let number = "b1998040";
let age = 25;

console.log(typeof name);
console.log(typeof number);
console.log(typeof age);


EOF

# 一時ファイルを実行する
node temp.js
```

    string
    string
    number
    

### 型変換


データ型を別のものに変換する際には、**型変換**を行います。


JavaScriptでは、以下のように変換する先の型を表す関数を使用します。

|種類|  変換先の型名 | 
| ---- | ---- |   
| 文字列  |  String()  |   
|  整数  |  parseInt()  |
|  浮動小数点数  |  parseFloat()  |
|  真偽値  |  Boolean()  |


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let age = "25";
console.log(typeof age); // 最初は文字列型です

age = parseInt(age);
console.log(typeof age); // 型変換して整数型になりました

EOF

# 一時ファイルを実行する
node temp.js
```

    string
    number
    

数値と文字列の間で演算が行われる場合は、 数値型に揃えられてから演算が行われます。  

このように自動的に型変換が行われる仕組みを**暗黙の型変換**といいます。  
ただし、真偽値と文字列の間では暗黙の型変換は行われません。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let age = 25;
console.log(typeof age);

let plus = 0.5;
console.log(typeof plus);

age += plus; // ageが浮動小数点に揃えられて演算
console.log(typeof age);

EOF

# 一時ファイルを実行する
node temp.js
```

    number
    number
    number
    

## テンプレート文字列


JavaScriptでは、テンプレート文字列を使用することで、  
文字列の中に値を埋め込むことができます。

テンプレート文字列は、バッククォート「```」で囲まれた文字列です。  
埋め込みたい値を「**${}**」で囲んで書きます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const name = "Chitose";
const age = 25;

console.log(`${name}さんの年齢は ${age}歳 です`);

EOF

# 一時ファイルを実行する
node temp.js
```

    Chitoseさんの年齢は 25歳 です
    

また、テンプレート文字列内では、式を記述することもできます。  

例えば、以下のように記述することで、変数`age`に4を足した値をテンプレート文字列に埋め込んで  
コンソールに出力することができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const name = "Chitose";
const age = 25;

console.log(`${name}さんの年齢は ${age}歳 です`);
console.log(`4年後は ${age+4}歳 です`);

EOF

# 一時ファイルを実行する
node temp.js
```

    Chitoseさんの年齢は 25歳 です
    4年後は 29歳 です
    

テンプレート文字列については、[こちら](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Template_literals)のページも参考になります。

## 入力を受け取る


Google Colab上でのJavaScriptの実行環境は、プロンプトを表示することができないため、  
ユーザーからの入力を受け取ることができません。

`prompt`関数は、ラウザ上で実行されるJavaScriptの関数です、

実行環境によっては使えるので、ぜひ試してみてください。

``` py
%%bash

# 一時ファイルにコードを書き込む
# 今回はエラー吐きます
cat <<'EOF' > temp.js

const name = "Chitose";
const age = prompt("年齢を入力してください");  // メッセージを指定して入力を促す

console.log(`${name}さんの年齢は ${age}歳 です`);
console.log(`4年後は ${Number(age)+4}歳 です`);  // ageは文字列型なので、Number関数で数値型に変換します

EOF

# 一時ファイルを実行する
node temp.js
```

## 乱数




**乱数**とは、ランダムで何が出るか分からない数字のことです。  
確率・統計的な処理や、数値シミュレーションには欠かせません。  

JavaScriptで乱数を扱う場合、Mathオブジェクトを使用します。  
以下にまとめたものを示します。

||書き方|意味|  
|:---:|:---|:---| 
|1|Math.random()|0以上1未満のランダムな数を返す|  
|2|Math.floor(Math.random() * (最大値 - 最小値 + 1)) + 最小値 |最小値以上最大値以下のランダムな整数を返す|  
|3|Math.random() * (最大値 - 最小値) + 最小値|最小値以上最大値未満のランダムな数を返す|  
|4|データ[Math.floor(Math.random() * データ.length)]|データの中でランダムに一つだけ要素を返す|
|5|データ.sort(() => Math.random() - 0.5)[0]|データの中からランダムに一つだけ要素を返す|  

### Math.random()
  

**0.0以上、1.0未満**のランダムな実数を返します。  


### Math.floor(Math.random() * (最大値 - 最小値 + 1)) + 最小値


**最小値 ≦ N ≦ 最大値**となるランダムな整数Nを返します。  
以下のコードは、0~20の中から整数値をランダムに選んでいます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

console.log(Math.floor(Math.random() * (21 - 0 + 1)) + 0);

EOF

# 一時ファイルを実行する
node temp.js
```

    2
    

### Math.random() * (最大値 - 最小値) + 最小値


**最小値 ≦ N ≦ 最大値**となるランダムな実数Nを返します。  
以下のコードは、0~20の中から実数値をランダムに選んでいます。  


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

console.log(Math.random() * (20 - 0) + 0);

EOF

# 一時ファイルを実行する
node temp.js
```

    8.453544298121756
    

### データ[Math.floor(Math.random() * データ.length)]


**文字列**など（他に**文字列**、**Map**、**Set**）のデータからランダムに要素を1つ選んで返します。  
以下のコードは、文字列の中からランダムな文字を表示するプログラムです。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

var string = "ABCD";
console.log(string[Math.floor(Math.random() * string.length)]);

EOF

# 一時ファイルを実行する
node temp.js
```

    C
    

### データ.sort(() => Math.random() - 0.5)[0]


配列の要素をランダムにシャッフルし、先頭の要素を返します。

以下のコードは、クラスの番号4つが含まれている配列を用意し、4つの要素をシャッフルした配列`class`を表示するプログラムです。


```python
import random
ABC_list = ['A', 'B', 'C', 'D']
random.shuffle(ABC_list)
print(ABC_list)
```

    ['D', 'B', 'C', 'A']
    


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let classes = ['A', 'B', 'C', 'D'];
let shuffledClasses = classes.sort(() => Math.random() - 0.5);

console.log(shuffledClasses);


EOF

# 一時ファイルを実行する
node temp.js
```

    [ 'B', 'A', 'C', 'D' ]
    

# 第1章補足

## コメント

「//」 記号を利用すると、コメントを入力することができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// コメント

EOF

# 一時ファイルを実行する
node temp.js
```

複数コメントを入力したいときは、範囲を選択して  
"Ctrlキー+「/」キー" を押すと一気にコメント化できます。

## 全角スペース
全角スペースは空白とはみなされません。

## エスケープシーケンス

「"」や「'」などの特殊な文字列を入力するためには、  
**エスケープシーケンス**と呼ばれる特殊な文字列を使う必要があります。

以下表のような特殊文字を扱うことができます。

|表記|  意味  |
| ---- | ---- |
|  \n  |  改行  |
|  \t  |  Tabキー  |
|  \\"  |  ダブルクォーテーション  | 
|  \\'  |  シングルクォーテーション  |
|  \\  |  \マーク  | 



```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

console.log("\"はダブルクォーテーションと読みます");
console.log("\'はシングルクォーテーションと読みます");
console.log("\\は日本語では円記号ですが、海外ではバックスラッシュと呼びます");

EOF

# 一時ファイルを実行する
node temp.js
```

    "はダブルクォーテーションと読みます
    'はシングルクォーテーションと読みます
    \は日本語では円記号ですが、海外ではバックスラッシュと呼びます
    

## インクリメント・デクリメント演算子


JavaScriptにはインクリメント・デクリメント演算子があります。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let count = 1;

count++; // インクリメント
count++; // インクリメント
count++; // インクリメント
console.log(count); // 4

count--; // デクリメント
console.log(count); // 3

EOF

# 一時ファイルを実行する
node temp.js
```

    4
    3
    

ただし、自己代入演算子を使っても同じ結果を得ることができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let count = 1;

count += 1; // インクリメント
count += 1; // インクリメント
count += 1; // インクリメント
console.log(count); // 4

count -= 1; // デクリメント
console.log(count); // 3


EOF

# 一時ファイルを実行する
node temp.js
```

    4
    3
    

詳しい話は[こちら](https://www.javadrive.jp/javascript/ope/index6.html)のページが参考になります。

## lengthプロパティ

JavaScriptには、文字列の長さを取得するための **`length`** プロパティ があります。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let count = 1;

// "これは文字です"を変数sに代入
let s = 'これは文字です';

// 文字列変数sの長さを出力
console.log(s.length);

EOF

# 一時ファイルを実行する
node temp.js
```

    7
    

## 文字列とインデックス

文字列の場合、**添え字**（**インデックス**）を指定することで、特定の文字を取得できます。  
添え字は**1ではなく0からスタートします**。 

以下のコードでは、文字列の1文字目を取得しています。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// "b2223456"を変数numberに代入
let number = "b1998040";

// numberから「b」だけ取得する
console.log(number[0]);

EOF

# 一時ファイルを実行する
node temp.js
```

    b
    

負の数を指定すると、末尾からの順番で指定することもできます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// "b2223456"を変数numberに代入
let number = "b1998040";

// numberから最後の文字「0」を取得する
console.log(number[number.length - 1]);

EOF

# 一時ファイルを実行する
node temp.js
```

    0
    

以下のコードでは、複数の文字をまとめて取得しています。  
このとき、**スライス**という構文を用います。

※`A`は**開始値**。`A:`と`B`を指定しなかった場合は添え字が`A`以上のすべての要素を参照する  
※`B`は**終了値**。`:B`と`A`を指定しなかった場合は添え字が`B`未満のすべての要素を参照する  
※`C`は**増減値**。`A:B`と`C`を指定しなかった場合は増減値は「+1」となる  
※`:`とだけ指定すると、すべての要素を参照する


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// "b2223456"を変数numberに代入
let number = "b1998040";

// numberから「b199」を取得する
console.log(number.slice(0, 4));

// 以下のように省略可能
console.log(number.slice(0, 4));

//添字4以降を取得
console.log(number.slice(4));

EOF

# 一時ファイルを実行する
node temp.js
```

    b199
    b199
    8040
    

増減値を負の数にすると、逆順にして取り出すことができます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// "b2223456"を変数numberに代入
let number = "b1998040";

// 逆順にして取り出す
console.log(number.split("").reverse().join(""));

EOF

# 一時ファイルを実行する
node temp.js
```

    0408991b
    
