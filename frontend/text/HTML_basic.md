# HTML



```python
# 最初に実行してください
import IPython
from IPython.display import display, HTML
```

## HTMLとは

**HTML**とは、「Hyper Text Markup Language」の略で、WEBページを作成するための言語です。  
HPの構造を定義します。


## CSSとは

**CSS**とは、「Cascading Style Sheets」の略で、文章の見た目を装飾するための言語です。

HTMLのみだと白い背景と黒い文字のWebサイトになってしまいます。  
CSSを適用させ、HPの外装、内装を定義します。

### タグ

HTMLは、**タグ**と呼ばれる記号で構成されます。  
タグにはいろいろな種類があり、タグによって役割が変わってきます。

![](https://imgur.com/w24XDEw.png)

**開始タグ**と**終了タグ**は基本的にセットで使われますが、場合によっては終了タグのないものもあります。  

まずは出力してみましょう。  
GoogleColab上なので分かりずらいかもしれません。


```python
htm = HTML('''\
<!-- Doctype宣言 HTMLのバージョン指定（ここではHTML5） -->
<!DOCTYPE html>
<!-- Webページの言語を指定 -->
<html lang="ja">
<!-- ページのタイトルや説明文、外部ファイルのリンクなどのページの情報を指定。
     ブラウザに表示されない -->
<head>
    <!-- タイトルの指定　ページタイトルやブラウザタブ -->
    <title>HTML①</title>
    <!-- 文字コードの指定 -->
    <meta charset="UTF-8">
    <!-- ページについての説明文
 　　　　検索エンジンでページタイトルとともに表示される-->
    <meta name="description" content="カメについていろいろ紹介します">
    
</head>
<body>
    # 見出しを表示する
    <h1>カメの生態</h1>
    # 段落を表示する
    <p>カメの平均寿命は30年ほどです</p>
</body>
</html>
''')
 
display(htm)
```


<!-- Doctype宣言 HTMLのバージョン指定（ここではHTML5） -->
<!DOCTYPE html>
<!-- Webページの言語を指定 -->
<html lang="ja">
<!-- ページのタイトルや説明文、外部ファイルのリンクなどのページの情報を指定。
     ブラウザに表示されない -->
<head>
    <!-- タイトルの指定　ページタイトルやブラウザタブ -->
    <title>HTML①</title>
    <!-- 文字コードの指定 -->
    <meta charset="UTF-8">
    <!-- ページについての説明文
 　　　　検索エンジンでページタイトルとともに表示される-->
    <meta name="description" content="カメについていろいろ紹介します">

</head>
<body>
    # 見出しを表示する
    <h1>カメの生態</h1>
    # 段落を表示する
    <p>カメの平均寿命は30年ほどです</p>
</body>
</html>



**`head`タグ**では、文章のタイトルや文章に関する設定などを記述します。  
**`body`タグ**では、HTMLの本文を記述します。

### 属性

タグの中には、色々な設定を入れることができます。  
この付加情報の種類のことを**属性**といいます。  

![](https://imgur.com/Ah7tk6r.png)

開始タグ名のあとに、スペースを空けてから書いていきます。



**`style`属性**を使うと、タグの中にCSSを書くことができるようになります。

CSSについては今後述べていきますが、ひとまず背景色を変化させてみましょう。

なお、これ以降のコードでは **`head`タグの中身は省略します**。


```python
htm = HTML('''\
<body>
    <!-- pタグにstyle属性を適用
         背景色を薄い緑色にする -->
    <p style="background-color: #DDFFDD">カメの平均寿命は30年ほどです</p>
</body>
''')
 
display(htm)
```


<body>
    <!-- pタグにstyle属性を適用
         背景色を薄い緑色にする -->
    <p style="background-color: #DDFFDD">カメの平均寿命は30年ほどです</p>
</body>



### divタグ

まだ何のタグも紹介していませんが、最初に紹介するのは**`div`**タグです。

`div`タグは、特に目的がないが、複数のタグをグループ化したいときに使います。  
`div`タグによって、ページの構造を定義することが多いです。


```python
htm = HTML('''\
<body>
<!-- この大枠のdivタグの下の要素の背景色は"薄い赤" -->
<div style="background-color: #FADBDA">
    <p>グループ1-1</p>
    <div>
        <!-- 内側のstyle属性が反映され、背景色を"薄い緑"に再設定する -->
        <p style="background-color: #DDFFDD">グループ2-1</p>
        <!-- 外側のstyle属性が反映され、背景色は"薄い赤"のまま -->
        <p>グループ2-2</p>
    </div>
</div>
</body>
''')
 
display(htm)
```


<body>
<!-- この大枠のdivタグの下の要素の背景色は"薄い赤" -->
<div style="background-color: #FADBDA">
    <p>グループ1-1</p>
    <div>
        <!-- 内側のstyle属性が反映され、背景色を"薄い緑"に再設定する -->
        <p style="background-color: #DDFFDD">グループ2-1</p>
        <!-- 外側のstyle属性が反映され、背景色は"薄い赤"のまま -->
        <p>グループ2-2</p>
    </div>
</div>
</body>



### spanタグ

次に紹介するのは**`span`タグ**です。

`span`タグは、CSSで文章の一部を装飾したいときに使います。  


`div`タグで囲んだ要素は、1つのブロックとみなされ、
前後に改行が入ります。  
このような要素を**ブロック要素**といいます。

反対に、`span`タグで囲んだ要素は、ブロックの中とみなされ、前後に改行が入りません。  
このような要素を**インライン要素**といいます。


```python
htm = HTML('''\
<body>
<p>
  <!-- このspanタグの下の要素の背景色は"薄い赤" -->
  <span style="background-color: #DDFFDD">緑色で表示される部分</span>
  <!-- このspanタグの下の要素の背景色は"薄い緑" -->
  <span style="background-color: #FADBDA">赤色で表示される部分</span>
</p>
<p>
  <!-- このspanタグの下の要素の背景色は"薄い青" -->
  <span style="background-color: #D3DEF1">青色で表示される部分</span>
  <!-- このspanタグの下の要素の背景色は"薄い黄 -->
  <span style="background-color: #fff3b8">黄色で表示される部分</span>
</p>
</body>
''')
 
display(htm)
```


<body>
<p>
  <!-- このspanタグの下の要素の背景色は"薄い赤" -->
  <span style="background-color: #DDFFDD">緑色で表示される部分</span>
  <!-- このspanタグの下の要素の背景色は"薄い緑" -->
  <span style="background-color: #FADBDA">赤色で表示される部分</span>
</p>
<p>
  <!-- このspanタグの下の要素の背景色は"薄い青" -->
  <span style="background-color: #D3DEF1">青色で表示される部分</span>
  <!-- このspanタグの下の要素の背景色は"薄い黄 -->
  <span style="background-color: #fff3b8">黄色で表示される部分</span>
</p>
</body>



`p`タグの中では、改行が行われていないことが分かります。

### 基本的なタグ

`div`タグ以外の、よく使われる基本的なタグについて紹介します。

|タグ|用途|説明 |  
| ---| ---| --- |
|h1-h6|見出しタグ|数字が大きくなるほど小さい見出しになる|
|p|段落を表示|囲まれた文章が段落になる|
|a|リンクを貼る|href属性でリンク先を指定。|
|img|画像を表示|src属性で画像を指定。alt属性で画像に代わって表示されるテキストを指定。|
|strong|太文字を表示|囲まれた文章が太文字になる|

ここでは、"OK Google"というボタンをクリックすると、  
Googleのトップページに行くという設定をしていきましょう。


```python
htm = HTML('''\
<body>
<div>
  <h2>OK Google</h2>
  <p style="background-color: #FADBDA"><strong>こちら</strong>のボタンを押してください</p>
</div>
<div>
  <a href="https://www.google.com/?hl=ja">
  <img src="https://imgur.com/pwOe016.png" alt="OK Google">
  </a>
</div>
</body>
''')
 
display(htm)
```


<body>
<div>
  <h2>OK Google</h2>
  <p style="background-color: #FADBDA"><strong>こちら</strong>のボタンを押してください</p>
</div>
<div>
  <a href="https://www.google.com/?hl=ja">
  <img src="https://imgur.com/pwOe016.png" alt="OK Google">
  </a>
</div>
</body>



`img`タグを`a`タグで囲むことで、リンクを作ることができました。  
画像を右クリックして新しいタブで開くと、Googleにジャンプできることが確認できます。


### リスト関係のタグ

リストを表現するためのタグについて触れていきます。

**`ul`タグ**は、順序のないリスト（unordered list）を表現するための要素です。

この要素内に**`li`タグ**（list item）を含めることで、リストを作成することができます。  
**`li`**タグは、各リストの項目を表します。

一方、**`ol`**タグは、順序のあるリスト（ordered list）を表現するための要素です。

この要素内に`li`タグを含めることで、リストを作成することができます。  
`li`タグは、各リストの項目を表します。

`ol`タグには、属性を指定することもあります。

〇`start`属性：リストの開始番号を指定する。デフォルトは1。  
　　　　　　　正の整数を指定して好きな番号から始めることができる。

〇`type`属性：リストの番号の形式を指定する。以下の4つの値を指定できる。


|タグ|説明 |  
| ---| ---|
|"1"|デフォルトの番号形式。アラビア数字で表示する。|
|"A"|アルファベットの大文字で表示する。|
|"a"|アルファベットの小文字で表示する。|
|"I"|ローマ数字の大文字で表示する。|
|"i"|ローマ数字の小文字で表示する。|

ではリストを表示してみましょう。


```python
htm = HTML('''\
<body>
<h2>日本においてなじみのあるカメの種類</h2>
<ul>
  <li>ミドリガメ</li>
  <li>ヤマトイシガメ</li>
  <li>クサガメ</li>
</ul>
<ol start="0">
  <li>ミドリガメ</li>
  <li>ヤマトイシガメ</li>
  <li>クサガメ</li>
</ol>
<ol type="a">
  <li>ミドリガメ</li>
  <li>ヤマトイシガメ</li>
  <li>クサガメ</li>
</ol>
</body>
''')
 
display(htm)
```


<body>
<h2>日本においてなじみのあるカメの種類</h2>
<ul>
  <li>ミドリガメ</li>
  <li>ヤマトイシガメ</li>
  <li>クサガメ</li>
</ul>
<ol start="0">
  <li>ミドリガメ</li>
  <li>ヤマトイシガメ</li>
  <li>クサガメ</li>
</ol>
<ol type="a">
  <li>ミドリガメ</li>
  <li>ヤマトイシガメ</li>
  <li>クサガメ</li>
</ol>
</body>



### 表関係のタグ

HTMLで表を作るためには、以下の4つのタグを使用します。

|タグ|説明 |  
| ---| ---|
|**`table`タグ**|表全体を囲むタグ。このタグの中に行を記述する。|
|**`tr`タグ**|表の行を表すタグ。このタグの中に列を記述する。|
|**`th`タグ**|表の見出しセルを表すタグ。通常、表の最上段に1行だけ配置される。|
|**`td`タグ**|表のデータセルを表すタグ。このタグの中にデータを記述する。|

ではリストを表示してみましょう。


```python
htm = HTML('''\
<body>
<h2>カメの種類とサイズと平均寿命</h2>
<table>
  <tr>
    <th>種類</th>
    <th>最大甲長</th>
    <th>平均体重</th>
    <th>平均寿命（野生）</th>
    <th>平均寿命（飼育下）</th>
  </tr>
  <tr>
    <td>ミドリガメ</td>
    <td>20cm程度</td>
    <td>1kg程度</td>
    <td>45年程度</td>
    <td>70年以上</td>
  </tr>
  <tr>
    <td>ヤマトイシガメ</td>
    <td>30cm程度</td>
    <td>3kg程度</td>
    <td>15年程度</td>
    <td>30年以上</td>
  </tr>
  <tr>
    <td>クサガメ</td>
    <td>40cm程度</td>
    <td>10kg程度</td>
    <td>35年程度</td>
    <td>50年以上</td>
  </tr>
</table>
</body>
''')
 
display(htm)
```


<body>
<h2>カメの種類とサイズと平均寿命</h2>
<table>
  <tr>
    <th>種類</th>
    <th>最大甲長</th>
    <th>平均体重</th>
    <th>平均寿命（野生）</th>
    <th>平均寿命（飼育下）</th>
  </tr>
  <tr>
    <td>ミドリガメ</td>
    <td>20cm程度</td>
    <td>1kg程度</td>
    <td>45年程度</td>
    <td>70年以上</td>
  </tr>
  <tr>
    <td>ヤマトイシガメ</td>
    <td>30cm程度</td>
    <td>3kg程度</td>
    <td>15年程度</td>
    <td>30年以上</td>
  </tr>
  <tr>
    <td>クサガメ</td>
    <td>40cm程度</td>
    <td>10kg程度</td>
    <td>35年程度</td>
    <td>50年以上</td>
  </tr>
</table>
</body>



他に覚えておくと便利なタグ・属性について以下に紹介します。

|タグ・属性|説明 |  
| ---| ---|
|**`caption`タグ**|表のタイトルを設定するタグ。tableタグの直下に記述する。|
|**`colspan`属性**|列を結合するための属性。`td`タグや`th`タグの中に記述し、結合する列数を指定する。|
|**`rowspan`属性**|行を結合するための属性。`td`タグや`th`タグの中に記述し、結合する行数を指定する。|
|**`thead`タグ**|表のヘッダを区切る。|
|**`tbody`タグ**|表のボディを区切る。|
|**`tfoot`タグ**|表のフッタを区切る。|


ではリストのレイアウトを変えてみましょう。


```python
htm = HTML('''\
<body>
  <table>
    <!-- 表のタイトルを指定 -->
    <caption>カメの種類とサイズと平均寿命</caption>
    <!-- 表のヘッダ部分を区切る -->
    <thead>
      <tr>
        <!-- 種類列の見出しセルを2つの行にまたがるようにする -->
        <th rowspan="2">種類</th>
        <!-- サイズ列と平均寿命列の見出しセルを2つの列にまたがるようにする -->
        <th colspan="2">サイズ</th>
        <th colspan="2">平均寿命</th>
      </tr>
      <tr>
        <th>最大甲長</th>
        <th>平均体重</th>
        <th>野生</th>
        <th>飼育下</th>
      </tr>
    </thead>
    <!-- 表のボディ部分を区切る -->
    <tbody>
      <tr>
        <td>ミドリガメ</td>
        <td>20cm程度</td>
        <td>1kg程度</td>
        <td>45年程度</td>
        <td>70年以上</td>
      </tr>
      <tr>
        <td>ヤマトイシガメ</td>
        <td>30cm程度</td>
        <td>3kg程度</td>
        <td>15年程度</td>
        <td>30年以上</td>
      </tr>
      <tr>
        <td>クサガメ</td>
        <td>40cm程度</td>
        <td>10kg程度</td>
        <td>35年程度</td>
        <td>50年以上</td>
      </tr>
    </tbody>
  </table>
</body>

''')
 
display(htm)
```


<body>
  <table>
    <!-- 表のタイトルを指定 -->
    <caption>カメの種類とサイズと平均寿命</caption>
    <!-- 表のヘッダ部分を区切る -->
    <thead>
      <tr>
        <!-- 種類列の見出しセルを2つの行にまたがるようにする -->
        <th rowspan="2">種類</th>
        <!-- サイズ列と平均寿命列の見出しセルを2つの列にまたがるようにする -->
        <th colspan="2">サイズ</th>
        <th colspan="2">平均寿命</th>
      </tr>
      <tr>
        <th>最大甲長</th>
        <th>平均体重</th>
        <th>野生</th>
        <th>飼育下</th>
      </tr>
    </thead>
    <!-- 表のボディ部分を区切る -->
    <tbody>
      <tr>
        <td>ミドリガメ</td>
        <td>20cm程度</td>
        <td>1kg程度</td>
        <td>45年程度</td>
        <td>70年以上</td>
      </tr>
      <tr>
        <td>ヤマトイシガメ</td>
        <td>30cm程度</td>
        <td>3kg程度</td>
        <td>15年程度</td>
        <td>30年以上</td>
      </tr>
      <tr>
        <td>クサガメ</td>
        <td>40cm程度</td>
        <td>10kg程度</td>
        <td>35年程度</td>
        <td>50年以上</td>
      </tr>
    </tbody>
  </table>
</body>




### フォーム関係のタグ

これからはWebサイトでもよく見かける**フォーム**を作成していきます。

**`form`タグ**は、Wenページ上でのフォームを定義するためのタグです。  
以下のような属性を持ちます。

|属性|説明 |  
| ---| ---|
|**`action`属性**|データの送信先ページを指定。|
|**`method`属性**|データの転送方法を指定。主に**GET**か**POST**を入力。|
|**`name`属性**|フォームの名前を指定。|

**GET**は、URLにパラメータとして付与して送信する方法です。  
**POST**は、フォームの内容をHTTPリクエストのボディに含めて送信する方法です。

フォームにおいては、通常はデータを送信するときに利用する**POST**を指定します。

#### inputタグ

ここからは、フォーム内で使う各パーツを設置するためのタグについて触れます。

**`input`タグ**はユーザーからの入力を受け取るためのタグです。  
**`type属性`**によって、入力欄の種類を指定できます。

##### 1行テキスト入力欄

1行のテキストには入力する内容が多々あります。  
`type`属性でその種類を変えることができます。

|属性値|説明 |  
| ---| ---|
|**text**|1行のテキスト（初期値）|
|**password**|パスワード|
|**search**|検索するときのテキスト|
|**email**|メールアドレス|
|**url**|WebサイトのURL|

また、**`placeholder`属性**を指定することで、  
入力欄にあらかじめテキストを用意することができます。

ユーザーが文字を入力しようとすると、`placeholder`の値は消えます。

ではフォームを作成してみましょう。


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    メールアドレス：<input type="email" name="email" placeholder="b2220000@">
    <br> <!-- 改行 -->
    学籍番号：<input type="text" name="number" placeholder="b2220000">
    <br> <!-- 改行 -->
    パスワード：<input type="password" name="password">
  </form>
</body>
''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    メールアドレス：<input type="email" name="email" placeholder="b2220000@">
    <br> <!-- 改行 -->
    学籍番号：<input type="text" name="number" placeholder="b2220000">
    <br> <!-- 改行 -->
    パスワード：<input type="password" name="password">
  </form>
</body>



CSSを適用していないので、見た目は綺麗であるとはいえません。

##### 送信ボタン

フォームに入力した内容を送信するパーツになります。  
`type`属性の値を**`submit`**と指定します。



以下のような属性を適用することができます。

|属性|説明 |  
| ---| ---|
|**name**|ボタンの名前|
|**value**|ボタンに表示するテキスト|

では追加してみましょう。


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    メールアドレス：<input type="email" name="email" placeholder="b2220000@">
    <br>
    学籍番号：<input type="text" name="number" placeholder="b2220000">
    <br>
    パスワード：<input type="password" name="password">
    <br>
    <input type="submit" value="ログイン">
  </form>
</body>
''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    メールアドレス：<input type="email" name="email" placeholder="b2220000@">
    <br>
    学籍番号：<input type="text" name="number" placeholder="b2220000">
    <br>
    パスワード：<input type="password" name="password">
    <br>
    <input type="submit" value="ログイン">
  </form>
</body>



`type`属性を**image**にすると、送信ボタンに画像を使うことができます。


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    メールアドレス：<input type="email" name="email" placeholder="b2220000@">
    <br>
    学籍番号：<input type="text" name="number" placeholder="b2220000">
    <br>
    パスワード：<input type="password" name="password">
    <br>
    <input type="image" src="https://imgur.com/cfpIWbe.png" alt="送信する">
  </form>
</body>
''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    メールアドレス：<input type="email" name="email" placeholder="b2220000@">
    <br>
    学籍番号：<input type="text" name="number" placeholder="b2220000">
    <br>
    パスワード：<input type="password" name="password">
    <br>
    <input type="image" src="https://imgur.com/cfpIWbe.png" alt="送信する">
  </form>
</body>



##### ラジオボタン

複数ある選択肢のうち、複数の選択肢の中から一つだけ選択できるようにしたいときは、  
`type`属性に**radio**を指定します。  

作成したラジオボタンには、同じ**`name`属性**を指定することで、  
グループ化することができます。

以下のような属性を適用することができます。

|属性|説明 |  
| ---| ---|
|**name**|ラジオボタンの名前|
|**value**|送信される選択肢の値|
|**checked**|初期選択|


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    ニックネーム：<input type="text" name="password">
    <br>
    性別：
    <input type="radio" name="gender" value="man">男
    <input type="radio" name="gender" value="woman">女
    <input type="radio" name="gender" value="others">その他
  </form>
</body>
''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    ニックネーム：<input type="text" name="password">
    <br>
    性別：
    <input type="radio" name="gender" value="man">男
    <input type="radio" name="gender" value="woman">女
    <input type="radio" name="gender" value="others">その他
  </form>
</body>



##### チェックボックス

複数ある選択肢のうち、複数の選択肢の中から複数選択できるようにしたいときは、  
`type`属性に**checkbox**を指定します。  

作成したチェックボックスには、同じ**`name`属性**を指定することで、  
グループ化することができます。

以下のような属性を適用することができます。

|属性|説明 |  
| ---| ---|
|**name**|チェックボックスの名前|
|**value**|送信される選択肢の値|
|**checked**|初期選択|


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    ニックネーム：<input type="text" name="password">
    <br>
    性別：
    <input type="radio" name="gender" value="man">男
    <input type="radio" name="gender" value="woman">女
    <input type="radio" name="gender" value="others">その他
    <br>
    飼ってみたいカメの種類：
    <input type="checkbox" name="turtle" value="ミドリガメ">ミドリガメ
    <input type="checkbox" name="turtle" value="ヤマトイシガメ">ヤマトイシガメ
    <input type="checkbox" name="turtle" value="クサガメ">クサガメ
    <input type="checkbox" name="turtle" value="その他">その他
    <input type="checkbox" name="turtle" value="飼ってみたくない">興味なし
  </form>
</body>
''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    ニックネーム：<input type="text" name="password">
    <br>
    性別：
    <input type="radio" name="gender" value="man">男
    <input type="radio" name="gender" value="woman">女
    <input type="radio" name="gender" value="others">その他
    <br>
    飼ってみたいカメの種類：
    <input type="checkbox" name="turtle" value="ミドリガメ">ミドリガメ
    <input type="checkbox" name="turtle" value="ヤマトイシガメ">ヤマトイシガメ
    <input type="checkbox" name="turtle" value="クサガメ">クサガメ
    <input type="checkbox" name="turtle" value="その他">その他
    <input type="checkbox" name="turtle" value="飼ってみたくない">興味なし
  </form>
</body>



##### ファイルの選択

ローカルのファイルをアップロードするためには、 
`type`属性に**file**を指定します。

クリックすることで、ファイルをサーバーにアップロードすることができます。

このとき、`form`タグの**`enctype`属性**で、  
**multipart/form-data**を指定する必要があります。


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post", enctype="multipart/form-data">
    <input type="file">
    <br>
    <br>
    <input type="submit" value="送信">
  </form>
</body>
''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post", enctype="multipart/form-data">
    <input type="file">
    <br>
    <br>
    <input type="submit" value="送信">
  </form>
</body>



#### selectタグ

**`select`**タグは、ドロップダウンリストを作成するためのタグです。  
**`option`**タグを指定して、リストの選択肢を定義します。

以下のような属性を適用することができます。

＜`select`タグ＞  

|属性|説明|  
| ---| ---|
|**name**|セレクトボックスの名前|
|**multiple**|複数選択可能にする|

＜`option`タグ＞  

|属性|説明 |  
| ---| ---|
|**value**|送信される選択肢の値|
|**selected**|初期選択|


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    ニックネーム：<input type="text" name="password">
    <br>
    性別：
    <input type="radio" name="gender" value="man">男
    <input type="radio" name="gender" value="woman">女
    <input type="radio" name="gender" value="others">その他
    <br>
    飼ってみたいカメの種類：
    <select name="turtle">
      <option value="ミドリガメ">ミドリガメ</option>
      <option value="ヤマトイシガメ">ヤマトイシガメ</option>
      <option value="クサガメ">クサガメ</option>
      <option value="その他">その他</option>
      <option value="興味なし" selected>興味なし</option>
    </select>
  </form>
</body>
''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    ニックネーム：<input type="text" name="password">
    <br>
    性別：
    <input type="radio" name="gender" value="man">男
    <input type="radio" name="gender" value="woman">女
    <input type="radio" name="gender" value="others">その他
    <br>
    飼ってみたいカメの種類：
    <select name="turtle">
      <option value="ミドリガメ">ミドリガメ</option>
      <option value="ヤマトイシガメ">ヤマトイシガメ</option>
      <option value="クサガメ">クサガメ</option>
      <option value="その他">その他</option>
      <option value="興味なし" selected>興味なし</option>
    </select>
  </form>
</body>



#### textareaタグ

**`textarea`**タグは、複数行のテキスト入力欄を作成するためのタグです。 

`textarea`タグで囲まれた部分が初期値として表示されます。  
入力しようとしたときに消えるように指定したいときは、`placeholder`属性で指定すべきです。

**`cols`属性**を指定すると、テキストエリアの横幅を指定することができます。    
**`rows`属性**を指定すると、テキストエリアの縦幅を指定することができます。 


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    ニックネーム：<input type="text" name="password">
    <br>
    性別：
    <input type="radio" name="gender" value="man">男
    <input type="radio" name="gender" value="woman">女
    <input type="radio" name="gender" value="others">その他
    <br>
    飼ってみたいカメの種類：
    <select name="turtle">
      <option value="ミドリガメ">ミドリガメ</option>
      <option value="ヤマトイシガメ">ヤマトイシガメ</option>
      <option value="クサガメ">クサガメ</option>
      <option value="その他">その他</option>
      <option value="興味なし" selected>興味なし</option>
    </select>
    <br>
    <br>
    <br>
    <textarea name="message" placeholder="メッセージを入力"
              cols="40" rows="4"></textarea>
  </form>
</body>
''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    ニックネーム：<input type="text" name="password">
    <br>
    性別：
    <input type="radio" name="gender" value="man">男
    <input type="radio" name="gender" value="woman">女
    <input type="radio" name="gender" value="others">その他
    <br>
    飼ってみたいカメの種類：
    <select name="turtle">
      <option value="ミドリガメ">ミドリガメ</option>
      <option value="ヤマトイシガメ">ヤマトイシガメ</option>
      <option value="クサガメ">クサガメ</option>
      <option value="その他">その他</option>
      <option value="興味なし" selected>興味なし</option>
    </select>
    <br>
    <br>
    <br>
    <textarea name="message" placeholder="メッセージを入力"
              cols="40" rows="4"></textarea>
  </form>
</body>



#### buttonタグ

**`button`**タグは、フォームを送信するのではなく、  
単なるボタンとして機能させたいときに使用します。

以下のような属性を適用することができます。

|属性|説明|  
| ---| ---|
|**`type`**|ボタンの種類を指定する。"submit"（送信ボタン）・"reset"（リセットボタン）・"button"（単なるボタン）|
|**`name`**|ボタンが押されたことを判別する|
|**`value`**|ボタンに表示されるテキストを指定する|


```python
htm = HTML('''\
<body>
  <button type="submit" name="submit" value="送信する">送信</button>
  <br>
  <br>
  <button type="reset" name="reset" value="リセットする">リセット</button>
  <br>
  <br>
  <button type="button" name="button" value="クリックする">クリック</button>
</body>
''')
 
display(htm)
```


<body>
  <button type="submit" name="submit" value="送信する">送信</button>
  <br>
  <br>
  <button type="reset" name="reset" value="リセットする">リセット</button>
  <br>
  <br>
  <button type="button" name="button" value="クリックする">クリック</button>
</body>



#### labelタグ

**`label`タグ**は、フォーム部品と対応するラベルを関連付けるために使用されます。

ラベルは、フォーム部品の説明や目的を提供し、  
ユーザーにフォーム部品の使用方法を理解しやすくするために使用されます。

まずは、各ラベルテキストを`label`タグで囲み、**`for`属性**を付けます。  
次に、各フォーム部品に**`id`属性**を付けます。

この**`for`属性**と**`id`属性**を同じものにすることで、  
フォームとパーツが関連付けられます。

これにより、ユーザーがラベルをクリックした場合、  
関連付けられたフォーム部品が選択されます。

また、ラベルはフォーム部品の意味を説明するために使用されています。

今まで書いてきたコードに、ラベルを追加してみましょう。


```python
htm = HTML('''\
<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    <label for="nickname">ニックネーム：</label>
    <input type="text" name="nickname" id="nickname">
    <br>
    <label>性別：</label>
    <input type="radio" name="gender" value="man" id="gender-man">
    <label for="gender-man">男</label>
    <input type="radio" name="gender" value="woman" id="gender-woman">
    <label for="gender-woman">女</label>
    <input type="radio" name="gender" value="others" id="gender-others">
    <label for="gender-others">その他</label>
    <br>
    <label for="turtle">飼ってみたいカメの種類：</label>
    <select name="turtle" id="turtle">
      <option value="ミドリガメ">ミドリガメ</option>
      <option value="ヤマトイシガメ">ヤマトイシガメ</option>
      <option value="クサガメ">クサガメ</option>
      <option value="その他">その他</option>
      <option value="興味なし" selected>興味なし</option>
    </select>
  </form>
</body>

''')
 
display(htm)
```


<body>
  <form action="https://www.google.com/?hl=ja" method="post">
    <label for="nickname">ニックネーム：</label>
    <input type="text" name="nickname" id="nickname">
    <br>
    <label>性別：</label>
    <input type="radio" name="gender" value="man" id="gender-man">
    <label for="gender-man">男</label>
    <input type="radio" name="gender" value="woman" id="gender-woman">
    <label for="gender-woman">女</label>
    <input type="radio" name="gender" value="others" id="gender-others">
    <label for="gender-others">その他</label>
    <br>
    <label for="turtle">飼ってみたいカメの種類：</label>
    <select name="turtle" id="turtle">
      <option value="ミドリガメ">ミドリガメ</option>
      <option value="ヤマトイシガメ">ヤマトイシガメ</option>
      <option value="クサガメ">クサガメ</option>
      <option value="その他">その他</option>
      <option value="興味なし" selected>興味なし</option>
    </select>
  </form>
</body>




「ニックネーム」「性別」などのラベルテキストをクリックすると、  
関連付けられたフォーム部品が選択されています。


#### グループ分け

ページ内の構造を明確にするために、以下のような区分けをするためのタグは重要です。



・**`header`タグ**   
→ ページ全体のヘッダー部分を示す。通常はサイト名やロゴ、ナビゲーションなどが含まれる。 

・**`main`タグ**  
→ ページのメインコンテンツを示す。主にユーザーが求める情報が含まれる。  

・**`footer`タグ**  
→ ページ全体のフッター部分を示す。著作権表示や連絡先、サイトマップなどが含まれる。

今まで書いてきたコードを、分かりやすく区分けしてみましょう。


```python
htm = HTML('''\
<body>
  <!-- ヘッダー部分を作る -->
  <header>
    <h1>アンケート</h1>
    <!-- ナビゲーションメニューを作る -->
    <nav>
      <ul>
        <li><a href="#">ホーム</a></li>
        <li><a href="#">お問い合わせ</a></li>
      </ul>
    </nav>
  </header>
  <!-- メイン部分を作る -->
  <main>
    <form action="https://www.google.com/?hl=ja" method="post">
      <div>
        <label for="nickname">ニックネーム：</label>
        <input type="text" id="nickname" name="nickname">
      </div>
      <div>
        <label>性別：</label>
        <input type="radio" name="gender" value="man" id="gender-man">
        <label for="gender-man">男性</label>
        <input type="radio" name="gender" value="woman" id="gender-woman">
        <label for="gender-woman">女性</label>
        <input type="radio" name="gender" value="other" id="gender-other">
        <label for="gender-other">その他</label>
      </div>
      <div>
        <label for="turtle">飼ってみたいカメの種類：</label>
        <select name="turtle" id="turtle">
          <option value="ミドリガメ">ミドリガメ</option>
          <option value="ヤマトイシガメ">ヤマトイシガメ</option>
          <option value="クサガメ">クサガメ</option>
          <option value="その他">その他</option>
          <option value="no-interest" selected>興味なし</option>
        </select>
      </div>
      <button type="submit">送信する</button>
    </form>
  </main>
  <!-- フッター部分を作る -->
  <footer>
    <p>&copy; 2023 カメ飼育研究会</p>
  </footer>
</body>

''')
 
display(htm)
```


<body>
  <!-- ヘッダー部分を作る -->
  <header>
    <h1>アンケート</h1>
    <!-- ナビゲーションメニューを作る -->
    <nav>
      <ul>
        <li><a href="#">ホーム</a></li>
        <li><a href="#">お問い合わせ</a></li>
      </ul>
    </nav>
  </header>
  <!-- メイン部分を作る -->
  <main>
    <form action="https://www.google.com/?hl=ja" method="post">
      <div>
        <label for="nickname">ニックネーム：</label>
        <input type="text" id="nickname" name="nickname">
      </div>
      <div>
        <label>性別：</label>
        <input type="radio" name="gender" value="man" id="gender-man">
        <label for="gender-man">男性</label>
        <input type="radio" name="gender" value="woman" id="gender-woman">
        <label for="gender-woman">女性</label>
        <input type="radio" name="gender" value="other" id="gender-other">
        <label for="gender-other">その他</label>
      </div>
      <div>
        <label for="turtle">飼ってみたいカメの種類：</label>
        <select name="turtle" id="turtle">
          <option value="ミドリガメ">ミドリガメ</option>
          <option value="ヤマトイシガメ">ヤマトイシガメ</option>
          <option value="クサガメ">クサガメ</option>
          <option value="その他">その他</option>
          <option value="no-interest" selected>興味なし</option>
        </select>
      </div>
      <button type="submit">送信する</button>
    </form>
  </main>
  <!-- フッター部分を作る -->
  <footer>
    <p>&copy; 2023 カメ飼育研究会</p>
  </footer>
</body>



