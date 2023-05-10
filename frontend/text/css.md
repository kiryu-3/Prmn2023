# CSS



```python
# 最初に実行してください
import IPython
from IPython.display import display, HTML
```

## CSSとは

**CSS**とは、「Cascading Style Sheets」の略で、文章の見た目を装飾するための言語です。

HTMLのみだと白い背景と黒い文字のWebサイトになってしまいます。  
CSSを適用させ、HPの外装、内装を定義します。

### CSSを適用させる方法

CSSを適用させる方法は、大きく分けて3つあります。


1つ目は、外部CSSファイルを使用する方法です。  

外部CSSファイルを作成し、HTML内で **`link`要素** を使用してファイルを読み込みます。  
この方法では、複数のHTMLファイルで同じCSSを使用することができます。

この方法はGoogleColabではなぜかできなかったので、コードの紹介だけにとどめます。  
（おそらくセキュリティ上の問題）


```python
%%writefile style.css
@charset "UTF-8"
/* 文字化け防止 必ず先頭に置く*/
/* これ以降のコードでは省略する */

p {
  background-color: #DDFFDD;
}
```
    


```python
htm = HTML(f'''\
<html>
  <head>
    <!-- style.cssを読み込ませる(GoogleColab上ではできない) -->
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
      <p>カメの平均寿命は30年ほどです</p>
  </body>
</html>
''')
display(htm)
```


<html>
  <head>
    <!-- style.cssを読み込ませる(GoogleColab上ではできない) -->
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
      <p>カメの平均寿命は30年ほどです</p>
  </body>
</html>

![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/6d1b0264-78bf-4c91-a0aa-2812de7faee2)




2つ目は、`style`要素を使用する方法です。  

HTMLファイル内で`style`要素を使用することで、CSSを直接適用することができます。    
この方法では、HTMLとCSSを同じファイル内に含めることができます。

では、CSSを適用させて、背景色を変えてみましょう。  
（HTML編でも少し登場しました）


```python
htm = HTML(f'''\
<html>
  <head>
    <style>
      p {{
        background-color: #DDFFDD;
      }}
    </style>
  </head>
  <body>
      <!-- pタグにstyle属性を適用
          背景色を薄い緑色にする -->
      <p>カメの平均寿命は30年ほどです</p>
  </body>
</html>
''')
display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/9d8d82ba-ca6e-4f99-9c9c-3102202768ef)



3つ目は、インラインスタイル属性を使用する方法です。  

HTML要素のスタイル属性に直接CSSを指定することで、インラインでCSSを適用することができます。    
この方法では、HTML要素ごとにスタイルを指定することができます。



HTML編で登場したやり方と同じですが、確認がてら実行してみましょう。


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


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/eb656ef1-60db-483a-ae58-b5d11180597f)



一番ベストな方法は、1番目の方法である、外部CSSファイルを使用する方法です。  
外部CSSファイルを使用することで、HTMLとCSSを分離でき、作業の効率が上がります。

本資料ではPythonと組み合わせることで、無理やりですが  
HTMLとCSSを分離しようと思います。


```python
%%writefile style.css

p {
  background-color: #DDFFDD;
}
```

    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
    <style>{css}</style>
  </head>
  <body>
      <!-- pタグにstyle属性を適用
          背景色を薄い緑色にする -->
      <p>カメの平均寿命は30年ほどです</p>
  </body>
</html>
''')
display(htm)

```



![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/9bbc3a6e-3b5c-42ea-8646-f798cbbcb8f8)




### CSSの基本構造

CSSは、以下の3つの部分を組み合わせて、スタイルを指定します。

![](https://imgur.com/fAdOwMj.png)

〇**セレクタ**  
→スタイルを適用する要素を指定するための識別子。HTMLの要素名、クラス名、ID名、属性値などを指定する。

〇**プロパティ**  
→スタイルの種類を指定するためのキーワード。コロン「:」を続けて書く。

〇**値**  
→プロパティに指定する具体的なスタイルの値。最後にセミコロン「;」を最後に書く。

では、以下のコードを実行してみましょう。


```python
%%writefile style.css

/* divタグ内の要素の背景色を薄い灰色にする */
div {
  background-color: #F2F2F2;
}

/* spanタグ内の要素の背景色を薄い緑色にする */
span {
  background-color: #DDFFDD
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div>
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div>
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div>
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')
display(htm)
```

![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/fd2a6cbf-90d8-49e8-9ee6-d61f6211311e)







`div`タグで囲んだところの背景色が薄い灰色になっています。  
そして、`span`タグで囲んだところの背景色が薄い緑色になっています。



しかし、このままではコードの中のすべての`div`タグ内の要素が  
上書きしない限りは薄い灰色になってしまいます。

そこで、要素を識別する必要があります。

### クラスとID

**`class`属性**と **`id`属性** は、CSSでスタイルを指定する際に  
要素を識別するために使用されます。

#### class属性

**`class`属性**は、同じスタイルを複数の要素に適用したい場合に使用されます。  
複数の要素で同じclass属性の値を指定することで、同じスタイルが適用されます。

CSSのスタイル定義では、「.」(ドット)を使って`class`属性を指定します。



先ほどのコードのうち、「最大甲長」の背景色を薄い青色に、  
「野生での平均寿命」の背景色を薄い黄色に変更します。


```python
%%writefile style.css

div {
  background-color: #F2F2F2;
}

span {
  background-color: #DDFFDD
}

/* "kotyo"クラス内の要素の背景色を薄い青色にする */
.kotyo {
  background-color: #D3DEF1
}

/* "jumyo"クラス内の要素の背景色を薄い黄色にする */
.jumyo {
  background-color: #fff3b8
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <!-- "kotyo"クラスの要素の背景色は"薄い青" -->
      <!-- "jumyo"クラスの要素の背景色は"薄い黄" -->
      <div>
          <h3><span>ミドリガメ</span></h3>
          <p><strong class="kotyo">最大甲長</strong>は20cm程度です</p>
          <p><strong class="jumyo">野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div>
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong class="kotyo">最大甲長</strong>は30cm程度です</p>
          <p><strong class="jumyo">野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div>
          <h3><span>クサガメ</span></h3>
          <p><strong class="kotyo">最大甲長</strong>は40cm程度です</p>
          <p><strong class="jumyo">野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')
display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/f1944a7e-8637-4156-aaed-0bb089321d8c)




#### id属性

**`id`属性** は、一つの要素に対して一意にスタイルを指定したい場合に使用されます。  
同じ **`id`属性** の値を複数の要素で指定することはできません。

CSSのスタイル定義では、「#」(シャープ)を使って`id`属性を指定します。



先ほどのコードのうち、「最大甲長」の最大値の背景色と、  
「野生での平均寿命」の最大値の背景色を薄い赤色に変更します。


```python
%%writefile style.css

div {
  background-color: #F2F2F2;
}

span {
  background-color: #DDFFDD
}

.kotyo {
  background-color: #D3DEF1
}

.jumyo {
  background-color: #fff3b8
}

/* id"kotyo_max"の要素の背景色を薄い赤色にする */
#kotyo_max {
  background-color: #FADBDA
}

/* id"jumyo_max"の要素の背景色を薄い赤色にする */
#jumyo_max {
  background-color: #FADBDA
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <!-- id"kotyo_max"の要素の背景色は"薄い赤" -->
      <!-- id"jumyo_max"の要素の背景色は"薄い赤" -->
      <div>
          <h3><span>ミドリガメ</span></h3>
          <p><strong class="kotyo">最大甲長</strong>は20cm程度です</p>
          <p><strong class="jumyo">野生での平均寿命</strong>は<span id="jumyo_max">45年</span>程度です</p>
      </div>
      <div>
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong class="kotyo">最大甲長</strong>は30cm程度です</p>
          <p><strong class="jumyo">野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div>
          <h3><span>クサガメ</span></h3>
          <p><strong class="kotyo">最大甲長</strong>は<span id="kotyo_max">40cm</span>程度です</p>
          <p><strong class="jumyo">野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')
display(htm)
```

![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/7171c8c6-8397-46cc-8f84-01329e283258)






### 文字や文章の装飾

#### 文字のフォント

**`font-family`** プロパティでは、文字のフォントを指定することができます。  


以下のような値を適用することができます。

〇フォント名  
→フォントの名前を記述する。  
　フォント名に日本語やスペースがある場合は、「'」か「"」で囲んで指定する。  

〇キーワード  
→ `serif`(明朝系)、`sans-serif`(ゴシック系)、`monospace`(等幅)、  
　 `cursive`(筆記体)、`fantasy`(装飾系)、`system-ui`(規定フォント) から指定する。

フォントの違いについて確認してみましょう。


```python
%%writefile style.css

/* ミドリガメの項目のフォントを明朝系にする */
#midori {
  font-family: serif;
}

/* ヤマトイシガメの項目のフォントを等幅にする */
#yamato {
  font-family: monospace;
}

/* クサガメの項目のフォントを筆記体にする */
#kusa {
  font-family: cursive;
}
```


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/4b60e12a-d6e4-495d-a775-2f584bd7c0a2)




#### 文字の大きさ

**`font-size`** プロパティでは、文字のサイズを指定することができます。  


以下のような値を適用することができます。

〇数値  
→ 数値に「px」「rem」「%」などの単位をつける。  

〇キーワード  
→ `xx-small`、`x-small`、`small`、`medium`、`large`、`x-large`、`xx-large` から指定する。

サイズの違いについて確認してみましょう。


```python
%%writefile style.css

/* ミドリガメの項目のサイズをsmallにする */
#midori {
  font-size: small;
}

/* ヤマトイシガメの項目のサイズをmediumにする */
#yamato {
  font-size: medium;
}

/* クサガメの項目のサイズをlargeにする */
#kusa {
  font-size: large;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```

![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/f009e54d-7174-4a29-a597-5357c839ebbf)




#### 文字の太さ

**`font-weight`** プロパティでは、文字の太さを指定することができます。  


以下のような値を適用することができます。

〇数値  
→ 1~1000までの任意の数値を指定する。  

〇キーワード  
→ `normal`(標準)、`bold`(太字)、`lighter`(一段階細く)、 `bolder`(一段階太く) から指定する。


太さの違いについて確認してみましょう。


```python
%%writefile style.css

/* ミドリガメの項目の太さはそのままにする */
#midori {
  font-weight: normal;
}

/* ヤマトイシガメの項目の太さをlighterにする */
#yamato {
  font-weight: lighter;
}

/* クサガメの項目の太さをbolderにする */
#kusa {
  font-weight: bolder;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p>最大甲長は20cm程度です</p>
          <p>野生での平均寿命は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p>最大甲長は30cm程度です</p>
          <p>野生での平均寿命は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p>最大甲長は40cm程度です</p>
          <p>野生での平均寿命は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/087c840f-d604-4a68-9569-bfe3d2da454b)




#### 文字列の水平方向の配置

**`text-align`** プロパティでは、文字列の水平方向の配置方法を指定することができます。  


以下のような値を適用することができます。 

〇キーワード  
→ `left`(左揃え)、`right`(右揃え)、`center`(中央揃え)、`justify`(両端揃え) から指定する。

配置の違いについて確認してみましょう。


```python
%%writefile style.css

/* ミドリガメの項目は左揃えにする */
#midori {
  text-align: left;
}

/* ヤマトイシガメの項目は中央揃えにする */
#yamato {
  text-align: center;
}

/* クサガメの項目は右揃えにする */
#kusa {
  text-align: right;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```

![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/fe736346-01fe-4e54-affa-b0d719df35fd)






#### 文字列の装飾

**`text-decoration`** プロパティでは、文字列の装飾方法を指定することができます。  


以下のような値を適用することができます。 

〇キーワード  
→ `underline`(下線)、`line-through`(打ち消し線)、`overline`(強調) から指定する。

文字列を装飾してみましょう。


```python
%%writefile style.css

/* ミドリガメの項目は赤い下線を引く */
#midori {
  text-decoration: underline red;
}

/* ヤマトイシガメの項目は青い打ち消し線を引く */
#yamato {
  text-decoration: line-through blue;
}

/* クサガメの項目は強調する（上線を引く） */
#kusa {
  text-decoration: overline;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```

![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/ab2d7442-99f8-40bc-acd8-ee38c3635784)





#### 行の高さ

**`line-height`** プロパティでは、行の高さ（行間）を指定することができます。  

おすすめの数値は **1.5~1.9** だそうです。


行の高さを変更してみましょう。


```python
%%writefile style.css

/* ミドリガメの項目は行の高さはそのまま */
#midori {
  line-height: normal;
  background-color: #DDFFDD;
}

/* ヤマトイシガメの項目は行の高さを"1.7"にする */
#yamato {
  line-height: 1.7;
  background-color: #D3DEF1;
}

/* クサガメの項目は行の高さを"2.5"にする */
#kusa {
  line-height: 2.5;
  background-color: #fff3b8;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/7f25a618-97b2-4fe3-8c1c-d0bb253205d0)




### 色を付ける

文字や背景の色を指定するには、**カラーコード** を使用する方法や、  
**RGB値** を使用する方法などがあります。  

RGB値を指定したときは、透明度を表す **Alpha値** を指定することができます。  
RGB各値は0から255まで、透明度は0から1までの間で記述します。

#### 文字に色を付ける

**`color`** プロパティでは、テキストの色を指定することができます。  



文字の色を変更してみましょう。


```python
%%writefile style.css

/* ミドリガメの項目はキーワードを使って文字色を赤色にする */
#midori {
  color: red;
}

/* ヤマトイシガメの項目はRGB値を使って文字色を緑色にする */
#yamato {
  color: rgb(0, 255, 0);
}

/* クサガメの項目はRGBA値を使って文字色を緑色にする */
/* 透明度はかなり高めに設定する */
#kusa {
  color: rgb(0, 0, 255, 0.2);
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/e6960402-a4e7-49a4-a744-765cbe6ac7cf)




#### 背景に色を付ける

**`background-color`** プロパティでは、背景の色を指定することができます。  
これまでも散々出てきました。



背景の色を変更してみましょう。  
ページ全体の背景に色を付けたいときは、`body`タグに対して指定します。


```python
%%writefile style.css

/* bodyタグ内の要素の背景色を薄い灰色にする */
body {
  background-color: #F2F2F2;
}

/* spanタグ内の要素の背景色を薄い緑色にする */
span {
  background-color: #DDFFDD
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/47202b34-312c-4991-ab34-34012fae0834)




### 背景に画像を設置する

背景に画像を設定する際に必要なプロパティは、  
以下に紹介する3つが主なものになります。

#### 背景画像を指定

**`background-image`** プロパティでは、背景画像を指定します。  

値には画像のファイルパスやURLを指定します。



とりあえず背景に画像を設置してみましょう。  
今回設置する画像はこちらです。

![](https://imgur.com/VctMf95.png)


```python
%%writefile style.css

/* 背景画像を設定する */
body {
  background-image: url(https://imgur.com/VctMf95.png);
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/d4b9cbd6-351e-4bac-a992-525430198e58)




#### 背景画像の繰り返しを設定

**`background-repeat`** プロパティでは、背景画像の繰り返し方を指定します。  




以下のような値を適用することができます。 

〇キーワード  
→ `repeat`(縦・横ともに繰り返す)、`no-repeat`(繰り返さない)、  
　`repeat-x`(横方向に繰り返す) 、`repeat-y`（縦方向に繰り返す）から指定する。

では先ほどの画像の繰り返しを設定してみましょう。  
デフォルトでは`repeat`が設定されていました。


```python
%%writefile style.css

/* 画像を縦方向に繰り返す */
body {
  background-image: url(https://imgur.com/VctMf95.png);
  background-repeat: repeat-y;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/cfd2580d-b878-4264-8d25-e6a60e89f8cc)





```python
%%writefile style.css

/* 画像を横方向に繰り返す */
body {
  background-image: url(https://imgur.com/VctMf95.png);
  background-repeat: repeat-x;
}
```

    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/d06fd61a-258d-4db5-aa1f-20be07014390)




#### 背景画像のサイズを設定

**`background-size`** プロパティでは、背景画像のサイズを指定します。  




以下のような値を適用することができます。

〇数値  
→ 数値に「px」「rem」「%」などの単位をつける。  

〇キーワード  
→ `auto（元サイズ）`、`cover`、`contain`から指定する。

`cover`を指定すると、表示領域に画像が完全に収まるように大きさが調整されます。  
画像の縦横比は維持されます。

表示してみましょう。


```python
%%writefile style.css

/* 背景画像を設定する */
body {
  background-image: url(https://imgur.com/VctMf95.png);
  background-repeat: no-repeat;
  background-size: cover;
}
```

    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/fe056c2c-9d9f-4402-80b9-f819b5c8fb5b)




表示領域に余白が発生しないように、画像が拡大しました。

`contain`を指定すると、表示領域の幅または高さに画像の幅または高さが  
一致するように大きさが調整されます。画像の縦横比は維持されます。

表示してみましょう。


```python
%%writefile style.css

/* 背景画像を設定する */
body {
  background-image: url(https://imgur.com/VctMf95.png);
  background-repeat: no-repeat;
  background-size: contain;
}
```

    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div id="midori">
          <h3><span>ミドリガメ</span></h3>
          <p><strong>最大甲長</strong>は20cm程度です</p>
          <p><strong>野生での平均寿命</strong>は45年程度です</p>
      </div>
      <div id="yamato">
          <h3><span>ヤマトイシガメ</span></h3>
          <p><strong>最大甲長</strong>は30cm程度です</p>
          <p><strong>野生での平均寿命</strong>は15年程度です</p>
      </div>
      <div id="kusa">
          <h3><span>クサガメ</span></h3>
          <p><strong>最大甲長</strong>は40cm程度です</p>
          <p><strong>野生での平均寿命</strong>は35年程度です</p>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/5e02e352-f1a6-4eae-b648-194d5fec7e48)




表示領域の高さと一致するように、画像の高さを拡大して合わせました。

### 幅と高さを指定

テキストや画像、背景色や枠線のサイズなど、レイアウトの各要素のサイズを指定するときは、  
 **`width`** プロパティや **`height`** プロパティを使用します。

`width`プロパティで要素の横幅を、`height`プロパティで要素の縦幅を指定します。  
単位は数値に「px」「rem」「%」などをつけたものです。

では、ドイツの国旗を表現してみましょう。


```python
%%writefile style.css

/* 幅300px、高さ200pxの領域を設定 */
.flag {
  width: 300px;
  height: 200px;
}

/* 一番上の黒い水平帯を設定 */
.black {
  background-color: black;
  width: 100%;
  height: 33.33%;
}

/* 真ん中の赤い水平帯を設定 */
.red {
  background-color: red;
  width: 100%;
  height: 33.33%;
}

/* 一番下の金の水平帯を設定 */
.gold {
  background-color: gold;
  width: 100%;
  height: 33.33%;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div class="flag">
          <div class="black"></div>
          <div class="red"></div>
          <div class="gold"></div>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/e05845e2-bf08-4a36-8f1f-6ca85acd774f)




### 余白を指定

余白に関するプロパティには以下のようなものがあります。

〇 **margin**  
→ 要素の外側の余白を指定する。  
〇 **padding**    
→ 要素の内側の余白を指定する。  
〇 **border**    
→ 要素の境界線を指定する。

![](https://imgur.com/5j3y5Kk.png)


#### margin

**`margin`プロパティ** を指定すると、上下左右の外側の余白を個別に指定できます。

|指定方法|説明|  
| ---| ---|
|**`margin-top`**|上側の余白を指定|
|**`margin-right`**|右側の余白を指定|
|**`margin-bottom`**|下側の余白を指定|
|**`margin-left`**|左側の余白を指定|

また、半角スペースで区切ることで、  
上から時計回りに上右下左の余白を指定することができます。

|指定方法|説明|  
| ---| ---|
|margin: 四辺すべて;|margin: 10px;|
|margin: 上下 左右;|margin: 10px 20px;|
|margin: 上 左右 下;|margin: 10px 20px 30px;|
|margin: 上 右 下 左;|margin: 10px 20px 30px 40px;|

数値に「px」「rem」「%」などをつけたもので外側の余白を指定します。  
**`auto`** を指定すると、自動設定される値が設定されます。


```python
%%writefile style.css

/* 幅300px、高さ250pxの領域を設定 */
.box {
  width: 300px;
  height: 250px;
  background-color: #F2F2F2;
}

/* 3つの要素の高さはそれぞれ親要素の20% */
/* 3つの要素の幅はそれぞれ親要素の80% */
#midori {
  height: 50px;
  background-color: #DDFFDD;
  margin: 0% 10% 50px 10%;
}

/* ヤマトイシガメの項目は行の高さを"1.7"にする */
#yamato {
  height: 50px;
  background-color: #D3DEF1;
  margin: 0% 10% 50px 10%; 
}

/* クサガメの項目は行の高さを"2.5"にする */
#kusa {
  height: 50px;
  background-color: #fff3b8;
  margin: 0% 10% 0% 10%;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div class="box">
          <div id="midori">ミドリガメ</div>
          <div id="yamato">ヤマトイシガメ</div>
          <div id="kusa">クサガメ</div>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/c5e968f9-c4b1-478c-8e69-361a64616a37)




#### padding

**`padding`プロパティ** を指定すると、上下左右の内側の余白を個別に指定できます。

|指定方法|説明|  
| ---| ---|
|**`padding-top`**|上側の余白を指定|
|**`padding-right`**|右側の余白を指定|
|**`padding-bottom`**|下側の余白を指定|
|**`padding-left`**|左側の余白を指定|


```python
%%writefile style.css

/* 幅300px、高さ250pxの領域を設定 */
.box {
  width: 300px;
  height: 250px;
  background-color: #F2F2F2;
}

#midori {
  height: 50px;
  background-color: #DDFFDD;
  margin: 0% 10% 50px 10%;
}

/* 要素の内側の左方向に親要素の幅の10%(30px)の余白 */
#yamato {
  height: 50px;
  background-color: #D3DEF1;
  margin: 0% 10% 50px 10%; 
  padding-left: 10%;
}

/* 要素の内側の上方向に50pxの余白 */
#kusa {
  height: 50px;
  background-color: #fff3b8;
  margin: 0% 10% 0% 10%;
  padding-top: 50px;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div class="box">
          <div id="midori">ミドリガメ</div>
          <div id="yamato">ヤマトイシガメ</div>
          <div id="kusa">クサガメ</div>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/73c1640a-c2fa-4c1a-90bc-f5372098f825)




#### 補足

前回は「クサガメ」の項目は、要素の内側の上方向に50pxの余白を設定しました。

このような上下の余白を、paddingやmarginの **%指定** で行おうとすると、少し値がおかしくなります。  
以下のコードを実行してください。


```python
%%writefile style.css

/* 幅300px、高さ250pxの領域を設定 */
.box {
  width: 300px;
  height: 250px;
  background-color: #F2F2F2;
}

#midori {
  height: 50px;
  background-color: #DDFFDD;
  margin: 0% 10% 50px 10%;
}

/* 要素の内側の左方向に親要素の幅の10%(30px)の余白 */
#yamato {
  height: 50px;
  background-color: #D3DEF1;
  margin: 0% 10% 50px 10%; 
  padding-left: 10%;
}

/* 誤り：要素の内側の上方向に親要素の"高さ"の20%(50px)の余白 */
/* 正解：要素の内側の上方向に親要素の"幅"の20%(60px)の余白 */
#kusa {
  height: 50px;
  background-color: #fff3b8;
  margin: 0% 10% 0% 10%;
  padding-top: 20%;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div class="box">
          <div id="midori">ミドリガメ</div>
          <div id="yamato">ヤマトイシガメ</div>
          <div id="kusa">クサガメ</div>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/312b2e67-4107-4a77-aa67-8a49fe2dba6e)



微妙な違いですが、`padding-top`は親要素の"高さ"の20%である50pxではなく、  
親要素の"幅"の20pxである60pxになります。

paddingやmarginを指定したときにおこる現象だそうです。    
`width`の値を変更して実行すると、余白の違いが生まれると思います。  
[こちら](https://diwao.com/2017/06/padding_margin_per.html)のページなどを参考にしてください。

### 線を引く

要素に境界線を追加するときは、以下のプロパティを使用します。

#### 境界線の幅を指定

**`border-width`** プロパティでは、境界線の幅を指定します。  




以下のような値を適用することができます。

〇数値  
→ 数値に「px」「rem」「%」などの単位をつける。  

〇キーワード  
→ `thin`(細い線)、`medium`(普通の太さ)、`thick`(太い線) から指定する。

では線の太さを変えてみましょう。  
この後解説しますが、線のスタイルは"実線"としています。


```python
%%writefile style.css


/* 境界線の太さは普通の太さ */
#midori {
  border-width: medium;
  border-style: solid;
}

/* 境界線の太さは太い線 */
#yamato {
  border-width: thick;
  border-style: solid;
}

/* 境界線の太さは細い線 */
#kusa {
  border-width: thin;
  border-style: solid;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div class="box">
          <div id="midori">ミドリガメ</div>
          <br>
          <br>
          <div id="yamato">ヤマトイシガメ</div>
          <br>
          <br>
          <div id="kusa">クサガメ</div>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/9a5053a5-a989-42ab-90bb-2a0e8789f78d)




#### 境界線の種類を指定

**`border-style`プロパティ** を指定すると、境界線の種類を指定できます。

|指定方法|説明|  
| ---| ---|
|**`none`**|線を非表示|
|**`solid`**|1本の実線|
|**`double`**|2本の実線|
|**`dashed`**|破線|
|**`dotted`**|点線|

では線の種類を変えてみましょう。 


```python
%%writefile style.css


/* 境界線の種類は2本の実線 */
#midori {
  border-width: medium;
  border-style: double;
}

/* 境界線の種類は点線 */
#yamato {
  border-width: thick;
  border-style: dotted;
}

/* 境界線の種類は破線 */
#kusa {
  border-width: thin;
  border-style: dashed;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div class="box">
          <div id="midori">ミドリガメ</div>
          <br>
          <br>
          <div id="yamato">ヤマトイシガメ</div>
          <br>
          <br>
          <div id="kusa">クサガメ</div>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/6f44c6e1-c5b8-43ba-9a9c-9ef42f8f314b)



#### 境界線の色を指定

**`border-color`プロパティ** を指定すると、境界線の色を指定できます。

境界線の色を指定するには、 **カラーコード** を使用する方法や、  
 **RGB値** を使用する方法などがあります。  

RGB値を指定したときは、透明度を表す **Alpha値** を指定することができます。  
RGB各値は0から255まで、透明度は0から1までの間で記述します。


```python
%%writefile style.css


/* 境界線の色を指定 */
#midori {
  border-width: medium;
  border-style: double;
  border-color: tomato;
}

/* 境界線の色を上右下左それぞれで指定 */
#yamato {
  border-width: thick;
  border-style: dotted;
  border-color: tan blue tomato black;
}

/* borderプロパティで一括指定（順番は自由） */
#kusa {
  border: thin dashed blue;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <div class="box">
          <div id="midori">ミドリガメ</div>
          <br>
          <br>
          <div id="yamato">ヤマトイシガメ</div>
          <br>
          <br>
          <div id="kusa">クサガメ</div>
      </div>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/e31d98a4-b812-4ae9-a8a0-13b40a0aa534)



### リストを修飾

リストを修飾するときは、以下のプロパティを使用します。

まずは就職前のhtmlについて確認しましょう。


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


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/c4236ccf-4e16-4700-a112-731c8f806b95)




#### リストマーカーの種類を指定

**`list-style-type`プロパティ** を指定すると、リストマーカーの種類を指定できます。

|指定方法|説明|  
| ---| ---|
|**`none`**|リストマーカーを非表示|
|**`disc`**|黒丸|
|**`circle`**|白丸|
|**`square`**|四角|
|**`decimal`**|数字|
|**`lower-alpha`**|小文字アルファベット|
|**`upper-alpha`**|大文字アルファベット|

ではリストマーカーの種類を変えてみましょう。 


```python
%%writefile style.css
/* リストマーカーの種類は白丸 */
.normal {
  list-style-type: circle;
}

/* リストマーカーの種類は四角 */
.square {
  list-style-type: square;
}

/* リストマーカーの種類は小文字アルファベット */
.alpha {
  list-style-type: lower-alpha;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <h2>日本においてなじみのあるカメの種類</h2>
      <ul class="normal">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ul>
      <ol class="square">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ol>
      <ol class="alpha">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ol>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/a6e65cb7-9f7f-4376-a956-a6a8d885258f)




#### リストマーカーの位置を指定

**`list-style-position`プロパティ** を指定すると、リストマーカーの位置を指定できます。

|指定方法|説明|  
| ---| ---|
|**outside**|ボックスの外側に表示|
|**inside**|ボックスの内側に表示|

ではリストマーカーの位置を変えてみましょう。   
背景色もつけて分かりやすくします。


```python
%%writefile style.css
/* それぞれの要素の<li>タグに背景色をつける

/* ここは設定いじらない */
.normal {
  list-style-type: circle;
}

.normal li {
  background-color: #DDFFDD;
}

/* ボックスの外側に表示 */
.square {
  list-style-type: square;
  list-style-position: outside;
}

.square li {
  background-color: #D3DEF1;
}

/* ボックスの内側に表示 */
.alpha {
  list-style-type: lower-alpha;
  list-style-position: inside;
}

.alpha li {
  background-color: #fff3b8;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <h2>日本においてなじみのあるカメの種類</h2>
      <ul class="normal">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ul>
      <ol class="square">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ol>
      <ol class="alpha">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ol>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/8c8d5fe4-60ef-4501-badc-f8bbf1c73887)




#### リストマーカーの画像を指定

**`list-style-image`プロパティ** を指定すると、リストマーカーの画像を指定できます。

余り複雑な画像にするとコンテンツの邪魔になるので、注意が必要です。

ではリストマーカーの画像を変えてみましょう。   
使用する画像は背景画像でも使った以下の画像です。

![](https://imgur.com/RTGMDr6.png)


```python
%%writefile style.css
/* それぞれの要素の<li>タグに背景色をつける

/* ここは設定いじらない */
.normal {
  list-style-type: circle;
  list-style-image: url(https://imgur.com/RTGMDr6.png);
}

.normal li {
  background-color: #DDFFDD;
}

/* ボックスの外側に表示 */
.square {
  list-style-type: square;
  list-style-position: outside;
}

.square li {
  background-color: #D3DEF1;
}

/* ボックスの内側に表示 */
.alpha {
  list-style-type: lower-alpha;
  list-style-position: inside;
}

.alpha li {
  background-color: #fff3b8;
}
```
    


```python
with open('/content/style.css', 'r') as f:
  css = f.read()

htm = HTML(f'''\
<html>
  <head>
      <style>{css}</style>
  </head>
  <body>
      <h2>日本においてなじみのあるカメの種類</h2>
      <ul class="normal">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ul>
      <ol class="square">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ol>
      <ol class="alpha">
          <li>ミドリガメ</li>
          <li>ヤマトイシガメ</li>
          <li>クサガメ</li>
      </ol>
  </body>
</html>
''')

display(htm)
```


![image](https://github.com/kiryu-3/Prmn2023/assets/84606676/693de928-d92b-4740-8421-c3be2c413826)



