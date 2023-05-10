# 第4章


```python
# 最初に実行してください
!apt-get install -y nodejs
```

## 関数
様々な処理が機能として１つにまとまっているものを**関数**といいます。

### 組み込み関数


Javascriptで最初から準備されている関数のことを、**組み込み関数**といいます。

組み込み関数には、以下のようなものがあります。

#### 文字列関数

文字列に関する処理を行うための関数です。

``` javascript
length: 文字列の長さを取得する関数です。
indexOf: 指定した文字列が最初に現れる位置を取得する関数です。
substring: 指定した範囲の文字列を取得する関数です。
replace: 指定した文字列を別の文字列に置換する関数です。
toUpperCase: 文字列を大文字に変換する関数です。
toLowerCase: 文字列を小文字に変換する関数です。
```

#### 配列関数

配列に関する処理を行うための関数です。  

``` javascript
push: 配列の末尾に要素を追加する関数です。
pop: 配列の末尾の要素を削除し、その要素を取得する関数です。
shift: 配列の先頭の要素を削除し、その要素を取得する関数です。
unshift: 配列の先頭に要素を追加する関数です。
slice: 配列の一部を取り出して新しい配列を作成する関数です。

#### 数値関数

数値に関する処理を行うための関数です。  
[こちら](https://www.javadrive.jp/javascript/math_class/)などのページにはより詳しい解説があります。

``` javascript
parseInt: 文字列を整数に変換する関数です。
parseFloat: 文字列を浮動小数点数に変換する関数です。
Math.abs: 絶対値を取得する関数です。
Math.round: 四捨五入した値を取得する関数です。
Math.floor: 小数点以下を切り捨てた値を取得する関数です。
```

また、最大値と最小値を求める関数もあります。

``` javascript
Math.min()：最小値を求める関数です。  
Math.max()：最大値を求める関数です。  
```

試しに、リストを作成して実行してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

const l = [1, 2, 3];

// 最大値を表示
console.log(Math.max(...l)); // 出力: 3

// 最小値を表示
console.log(Math.min(...l)); // 出力: 1

EOF

# 一時ファイルを実行する
node temp.js
```

    3
    1
    

リストを展開して関数に渡すために、「...演算子」を使用しています。

### 関数の定義


組み込み関数とは別に、関数は自分で作ることもできます。  

関数を自分で作れるようになると、プログラムを複数の部品に分けることができるようになります。  
1つのプログラムを複数の部品に分けることを**部品化**といいます。メリットは以下の通りです。  

- プログラム全体の見通しがよくなり、処理を把握しやすくなる
- 機能ごとに関数を記述するため、修正範囲を限定できる
- 何度も使う機能を関数にまとめることで、プログラミングの作業効率が上がる

一般的に、JavaScriptの関数の定義は以下のようになります。

``` javascript
// 関数の定義
function 関数名(){
    // 処理内容
}

```

関数名の右にある()の部分は、より複雑な関数を定義するときに使います。  
構文の2行目以降は、この関数が呼び出されたときに実行する処理を記述します。  


この部分を**関数ブロック**といいます。

シンプルな関数の場合は、次のような構文で呼び出すことができます。  

``` javascript
関数名();
```

では、呼び出されると`"Hello"`と表示する  
hello関数を作成してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

function hello() {
  console.log("Hello");
}

hello(); // 関数の呼び出し

EOF

# 一時ファイルを実行する
node temp.js
```

    Hello
    

関数内で準備された変数（**ローカル変数**）は、その関数の中でしか読み書きできません。  
このようなローカル変数の性質を**独立性**といいます。


```python
"""
実行するとエラーが出ます
"""
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

function hello() {
  let greet = "Hello";
  console.log(greet);
}

hello();
console.log(greet); // 変数greetは利用できない

EOF

# 一時ファイルを実行する
node temp.js
```

#### 関数と引数


呼び出し元から関数へデータを渡す仕組みを**引数**といいます。   
呼び出し側で渡すデータを**実引数**、そのデータを受け取る変数を**仮引数**といいます。  
引数には、数値や文字列のなどのオブジェクトを引き渡すことができます。    





``` javascript
// 関数の定義
function 関数名(引数1, 引数2, ...){
    // 処理内容
}

```

関数名に続くカッコの中に書いた変数名は、関数が呼び出された際に  
データを引数で受け取り、関数内で扱っていくものです。

引数がある関数の場合は、次のような構文で呼び出すことができます。  

``` javascript
関数名(引数1, 引数2, ...);
```

関数名の後ろのカッコ内でデータを渡しています。

偶数奇数判定をするhantei関数を作成してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

function hantei(num) {  // 仮引数numで実引数numberの値を受け取る
  if (num % 2 === 0) {
    console.log(`${num}は偶数です`);
  } else {
    console.log(`${num}は奇数です`);
  }
}

let number = 2;
hantei(number);  // 実引数numberをhantei関数に渡す

number = 3;
hantei(number);  // 実引数numberをhantei関数に渡す

EOF

# 一時ファイルを実行する
node temp.js
```

    2は偶数です
    3は奇数です
    

複数の引数を渡すことも可能です。  

税込み価格を表示するtax_price関数を作成してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

function tax_price(name, price, tax) {  // 仮引数name,price,taxで実引数の値を受け取る
  console.log(`${name}の税抜き価格は${price}円です`);
  console.log(`${name}の税込み価格は${price * (1+(tax*0.01))}円です\n`);
}

tax_price("牛丼並盛", 408, 10);  // 店の中で食べるときは消費税率10%
tax_price("牛丼並盛", 408, 8);   // 持ち帰って食べるときは消費税率8%

EOF

# 一時ファイルを実行する
node temp.js
```

    牛丼並盛の税抜き価格は408円です
    牛丼並盛の税込み価格は448.8円です
    
    牛丼並盛の税抜き価格は408円です
    牛丼並盛の税込み価格は440.64000000000004円です
    
    

#### 関数と戻り値


関数から呼び出し元へデータを渡す仕組みを**戻り値**といいます。  
関数で何らかの処理を行った結果を他の関数でも利用することができるようになります。 
 
戻り値には、数値や文字列のなどのオブジェクトを引き渡すことができます。



``` javascript
// 関数の定義
function 関数名(引数1, 引数2, ...){
    // 処理内容
    return 戻り値;
}

```

関数定義の最終行には**return文**を書きます。  
関数内の処理を終了し、呼び出し元にデータを渡すことが出来ます。  

引数と戻り値がある関数の場合は、次のような構文で呼び出すことができます。  

``` javascript
戻り値を受け取る変数名 = 関数名(引数1, 引数2, ...);
```

`関数名(引数1,引数2,…)`の部分は、関数の実行後に戻り値に置き換わります。  
結果として、変数に戻り値が代入されることになります。

hantei関数内で偶数か奇数を判断し、その戻り値を出力しましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

function hantei(num) {  // 仮引数numで実引数numberの値を受け取る
  if (num % 2 === 0) {
    return "偶数";
  } else {
    return "奇数";
  }
}

let number = 2;
let judge = hantei(number);  // 実引数numberをhantei関数に渡す
console.log(`${number}は${judge}です`);

number = 3;
judge = hantei(number);  // 実引数numberをhantei関数に渡す
console.log(`${number}は${judge}です`);

EOF

# 一時ファイルを実行する
node temp.js
```

    2は偶数です
    3は奇数です
    

乱数を戻り値に指定するとサイコロ関数が出来上がります。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// サイコロを関数で表現する

function saikoro() {
return Math.floor(Math.random() * 6) + 1; // 1～6の乱数
}

for (let i = 0; i < 3; i++) {
console.log(saikoro());
}

EOF

# 一時ファイルを実行する
node temp.js
```

    5
    6
    4
    

戻り値は複数指定することができません。  
しかし、配列にしてしまえば複数のデータを扱うことができます。

税込み価格を表示するtax_price関数を作成してみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

function taxPrice(price) {
  const keigen = price * (1 + 8 * 0.01);  // 持ち帰って食べるときは消費税率8%
  const notKeigen = price * (1 + 10 * 0.01);  // 店の中で食べるときは消費税率10%
  return [keigen, notKeigen];  // 戻り値は一つの配列
}

const name = "牛丼";
const price = 408;
const [keigen, notKeigen] = taxPrice(price);  // 戻り値の配列を分割代入
console.log(`${name}の税抜き価格は${price}円です`);
console.log(`持ち帰って食べるときの価格は${keigen}円です`);
console.log(`店の中で食べるときの価格は${notKeigen}円です`);

EOF

# 一時ファイルを実行する
node temp.js
```

    牛丼の税抜き価格は408円です
    持ち帰って食べるときの価格は440.64000000000004円です
    店の中で食べるときの価格は448.8円です
    

### アロー関数

JavaScriptにおける**アロー関数**は、通常の関数定義の代替手段として使われる関数式のことです。

アロー関数は、コードを簡潔にすることができるため、ES6以降では広く使われるようになっています。  
ただし、引数の数や処理の複雑さに応じて、通常の関数定義の方が可読性が高くなる場合もあります。

一般的には以下のような構文を持ちます。

``` javascript
const 関数名 = (引数1, 引数2, ...) => {
  // 関数の処理
  return 戻り値;
};
```

または、引数が一つの場合は引数の括弧を省略することもできます。

``` javascript
const 関数名 = 引数 => {
  // 関数の処理
  return 戻り値;
};
```

さらに、処理が1つの式で完結する場合はreturn文と中括弧を省略することもできます。

``` javascript
const 関数名 = 引数 => 式;
```

では、アロー関数を使って、先ほどまで登場してきた関数を書き換えてみましょう。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// 呼び出されると"Hello"と表示する hello関数
const hello = () => {
  console.log("Hello");
}

hello(); // 関数の呼び出し

EOF

# 一時ファイルを実行する
node temp.js
```

    Hello
    


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// 偶数奇数判定をするhantei関数
const hantei = (num) => {  // 仮引数numで実引数numberの値を受け取る
  if (num % 2 === 0) {
    console.log(`${num}は偶数です`);
  } else {
    console.log(`${num}は奇数です`);
  }
}

let number = 2;
hantei(number);  // 実引数numberをhantei関数に渡す

number = 3;
hantei(number);  // 実引数numberをhantei関数に渡す

EOF

# 一時ファイルを実行する
node temp.js
```

    2は偶数です
    3は奇数です
    


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

// サイコロ関数
const saikoro = () => Math.floor(Math.random() * 6) + 1;

for (let i = 0; i < 3; i++) {
  console.log(saikoro());
}

EOF

# 一時ファイルを実行する
node temp.js
```

    4
    6
    3
    

### グローバル変数

JavaScriptにおいて、関数の外側で定義された変数を**グローバル変数**と呼びます。  
グローバル変数は、どの関数からでもアクセスすることができます。

※同名のローカル変数がある場合は、ローカル変数が優先して利用されます。


```bash
%%bash

# 一時ファイルにコードを書き込む
cat <<'EOF' > temp.js

let greet = "Hello";

function hello() {
  console.log(greet);
}

hello();

EOF

# 一時ファイルを実行する
node temp.js
```

    Hello
    

関数の**独立性**を考えると、hello関数の中身では変数が何も定義されていないので、  
変数`greet`は使えないように思えます。 

しかしエラーは出ません。それは変数`greet`がグローバル変数であるからです。

ただし、グローバル変数はどこからでも変更できるため、誤って上書きしてしまう可能性があります。  
そのため、グローバル変数を使用する際は、注意が必要です。

関数内でのみ使用する変数は、関数内で定義し、  
グローバル変数をできるだけ避けるようにしましょう。
