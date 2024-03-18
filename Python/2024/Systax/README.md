# Python 基本文法編

- [Python文法まとめ（Colab版）](../../2024/Systax/PythonBasic.ipynb)
- [Python文法まとめ（Qiita版）](https://qiita.com/kiryu-3/items/888319c76fd82440f601)

## 初めに
『データサイエンス入門』の中でPythonの基本文法をあらかた学習しました。  
本資料では、授業では紹介されていないものの、とても重要な文法事項について学習します。  

<details><summary>クラス</summary>

- pyファイルを分けるなど、大規模な開発の際にはクラス分けはほぼ確実に行う。
- Pythonでゲームを作りたい場合、ネットに転がっているコードは大体クラス分けをしている。
- 具体的なクラス設計は授業で。本資料の目的は最低限コードを読めるようにすること。
    
</details>

<details><summary>テキストファイル処理</summary>

- 開発において、CSVファイルと同じくらい読み込む機会が多い（？）。
- 本資料を参考にすれば、簡単なしりとりシステムを作るための準備ができる。
    
</details>

<details><summary>JSONデータ処理</summary>

- APIを利用することで、開発の幅を大幅に広げることができる。
- JSONデータの処理は、大体ディレクトリと同じである
- API利用におけるハードルを下げること、そもそもAPIというものが存在することを知ることが、本資料の目的である。
    
</details>

この資料の演習を通してPythonプログラミングの力を向上させ、本プロジェクトの最終成果物を作る際の参考にしてください。

<hr>

なお、本資料は、これから学科配属後に履修する以下授業との接続を意識して作られました。
<details><summary>『アプリケーションプログラミング（Python）』（電子光工学科2年秋学期）</summary>
    
  - Pythonの基本文法の再確認
  - クラスやテキストファイル処理、例外処理など、『データサイエンス入門』で学習していない文法事項も学ぶ
  - その後GUIアプリ制作やアルゴリズムの学習へ
    
  </details>
<details><summary>『Javaプログラミング（Java）』（情報システム工学科2年秋学期）</summary>

  - Javaの基本文法の学習
  - クラス設計の方法（これは言語関係なく重要）
  - 最終的にLINEBotアプリ制作など
 
  </details>
<details><summary>『情報システム開発基礎演習（Python）』（情報システム工学科3年春学期）</summary>


  - AWSのサービスなどを呼び出し、JSONデータ処理
  - 授業で扱うpythonコードを読むために、基本的なクラスの知識の予習が課される（？）
  - とはいっても扱い方は辞書と同じである。ということを本演習を通して学んでおくと一歩リードできるような。

  </details>

<hr>

なお、今回の演習で問われるような問題は、就活の際などプログラミングテストとして出題されることがあります。
就活対策として（Pythonに限らず）演習を積みたい場合は[paizaラーニング](https://paiza.jp/works/mondai)というサービスがおすすめです。


## 第0章<Git環境構築>

Gitの環境構築パートです。
- 2023年に運用した資料は[こちら](https://scrapbox.io/Prmn2023/Git(Prmn2023))
- 2024年度版は、未完成。

## 第1章＜基本文法総復習＞

『データサイエンス入門』で学習したPythonの基本文法を改めて確認します。

- 一年秋学期『情報学』の高野先生パートで登場したピラミッド、フローチャートではなくコーディング問題
- 成績データからGPAを計算する問題
- コーディングテストの問題の代表格？FizzBuzz問題
  
<hr>

- 問題は[こちら](../../2024/Systax/question/PythonBasic_BasicSyntax_Question.ipynb)
- 解答は[こちら](../../2024/Systax/answer/PythonBasic_BasicSyntax_Answer.ipynb)（公開前）

## 第2章＜クラス基礎＞

「**オブジェクト指向**」への第一歩を踏み出すため、**クラス**の基礎について確認していきます。 

- 昆虫の動作を表すクラスを作成し、それぞれの動作に対応するメソッドを実装する問題
- 車と給油所を操作する問題（発展問題付き）
- 銀行の口座情報を管理し、ATMをシミュレートする問題（発展問題付き）
  
<hr>

- 問題は[こちら](../../2024/Systax/question/PythonBasic_BasicClasses_Question.ipynb)
- 解答は[こちら](../../2024/Systax/answer/PythonBasic_BasicClasses_Answer.ipynb)（公開前）

## 第3章＜クラス応用＞

クラスの学習において最大の壁ともいわれる**継承**について確認していきます。 

- 昆虫の動作を表すクラスを作成し、それぞれの動作に対応するメソッドを実装後、継承を利用して機能を拡張する問題
- 継承を利用してトラックを操作する問題
- オーバーライドを利用してトラックを操作する問題（発展問題付き）
  
<hr>

- 問題は[こちら](../../2024/Systax/question/PythonBasic_AdvancedClasses_Question.ipynb)
- 解答は[こちら](../../2024/Systax/answer/PythonBasic_AdvancedClasses_Answer.ipynb)（公開前）

## 第4章＜テキストファイル処理＞

テキストファイルの読み込みをPythonで行う練習です。  

- テキストファイルにある家計簿データを処理する問題
- テキストファイルにある成績データからGPAを計算する問題
- テキストファイルにある単語データから先頭文字ごとに単語数を計算して表示する問題
  
<hr>

- 問題は[こちら](../../2024/Systax/question/PythonBasic_TextFiles_Question.ipynb)
- 解答は[こちら](../../2024/Systax/answer/PythonBasic_TextFiles_Answer.ipynb)（公開前）


## 第5章＜API利用・JSON処理＞

APIなどを利用する際によく登場する、JSONデータの扱いについて学びます。  

- JSONファイルから国コードの情報を取得し、特定の形式で出力する問題
- REST Countries APIから地域、小地域、人口、首都の情報をJSON形式で取得し、特定の形式で出力する問題
- Worldwide Public Holidays APIから指定された国の今年の祝日情報をJSON形式で取得し、特定の形式で出力する問題
  
<hr>

- 問題は[こちら](../../2024/Systax/question/PythonBasic_JSONProcessing_Question.ipynb)
- 解答は[こちら](../../2024/Systax/answer/PythonBasic_JSONProcessing_Answer.ipynb)（公開前）

