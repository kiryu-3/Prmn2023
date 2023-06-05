# 線形代数基礎

```python
# 最初に実行してください
import numpy as np
```

kamakiriさんの[こちら](https://takun-physics.net/category/%e5%a4%a7%e5%ad%a6%e6%95%b0%e5%ad%a6/)の記事群を主に参考にしました。


  - [行列](#行列)
  - [行列にスカラーを掛ける](#行列にスカラーを掛ける)
  - [行列の和](#行列の和)
  - [行列の積](#行列の積)
  - [特殊な行列](#特殊な行列)
    - [零行列](#零行列)
    - [単位行列](#単位行列)
    - [対角行列](#対角行列)
    - [転置行列](#転置行列)
    - [対称行列](#対称行列)
    - [交代行列](#交代行列)
    - [零因子](#零因子)
  - [逆行列](#逆行列)
    - [行列式](#行列式)
      - [2次の正方行列](#2次の正方行列)
      - [3次の正方行列](#3次の正方行列)
      - [4次以上の正方行列](#4次以上の正方行列)
    - [逆行列の求め方](#逆行列の求め方)
      - [2次の逆行列](#2次の逆行列)
      - [3次以上の逆行列](#3次以上の逆行列)
  - [固有値と固有ベクトル](#固有値と固有ベクトル)
    - [固有値](#固有値)
    - [固有ベクトル](#固有ベクトル)
    - [固有値・固有ベクトルを学ぶモチベーション](#固有値固有ベクトルを学ぶモチベーション)

<div style="page-break-before:always"></div>

## 行列

**行列**：数を方形に並べたもの。横の並びが**行**で、縦の並びが**列**である。

例 $m$行 $n$ 列の行列($m×n$行列)  

$$  
A = \left(  
\begin{matrix} 
a _ {11} & ･･･ & a _ {1n} \\ 
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
a _ {m1} & ･･･ & a _ {mn} 
\end{matrix}  
\right)  
$$

- $m=n$となる行列を**正方行列**と呼ぶ。
- 構成するそれぞれの数値を**要素**と呼ぶ。

参考記事はkamakiriさんの[こちら](https://takun-physics.net/11917/)です。

<div style="page-break-before:always"></div>

## 行列にスカラーを掛ける

行列にもスカラーを掛けることができる。

例　行列 $A$ を $k$ 倍した行列

$$
kA = \left(
\begin{matrix} 
ka_{11} & ･･･ & ka_{1n} \\ 
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
ka_{m1} & ･･･ & ka_{mn} 
\end{matrix} 
\right)
$$

<div style="page-break-before:always"></div>

## 行列の和

以下のように行列 $A$ と $B$ を定義する。

例 $m×n$行列 $A$と $B$


$$
A = \left(
\begin{matrix} 
a_{11} & ･･･ & a_{1n} \\ 
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
a_{m1} & ･･･ & a_{mn} 
\end{matrix} 
\right)

B = \left(
\begin{matrix} 
b_{11} & ･･･ & b_{1n} \\ 
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
b_{m1} & ･･･ & b_{mn} 
\end{matrix} 
\right)
$$

$A$と $B$の和 $A+B$ と差 $A-B$ は、次のように計算できる。

例 和 $A+B$ と差 $A-B$

$$
A+B = \left(
\begin{matrix} 
a_{11}+b_{11} & ･･･ & a_{1n}+b_{1n} \\ 
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
a_{m1}+b_{m1} & ･･･ & a_{mn}+b_{mn} 
\end{matrix} 
\right)

A-B = \left(
\begin{matrix} 
a_{11}-b_{11} & ･･･ & a_{1n}-b_{1n} \\ 
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
a_{m1}-b_{m1} & ･･･ & a_{mn}-b_{mn} 
\end{matrix} 
\right)
$$

- $A$と $B$の行数あるいは列数が異なる場合は、行列の和と差の計算はできない。

例　

$$
A = \left(
\begin{matrix} 
1 &  3 \\ 
5 & 7 
\end{matrix} 
\right)
$　　　$
B = \left(
\begin{matrix} 
2 & 4 \\ 
6 & 8 
\end{matrix} 
\right)

A+B = \left(
\begin{matrix} 
1+2 & 3+4 \\ 
5+6 & 7+8 
\end{matrix} 
\right)
= \left(
\begin{matrix} 
3 & 7 \\ 
11 & 15 
\end{matrix} 
\right)
$$


```python
arrayA = [
    [1, 3],
    [5, 7]
]
arrayB = [
    [2, 4],
    [6, 8]
]
ndarrayA = np.array(arrayA)
ndarrayB = np.array(arrayB)
print(ndarrayA + ndarrayB)
```

    [[ 3  7]
     [11 15]]
    

参考記事はkamakiriさんの[こちら](https://takun-physics.net/11917/#rtoc-5)です。

<div style="page-break-before:always"></div>

## 行列の積

以下のように行列 $A$と $B$と $C$を定義する。

例 $m×n$行列 $A$と $p×q$行列 $Bと$m×q$行列 $C$

$$
A = \left(
\begin{matrix} 
a_{11} & a_{12} & ･･･ & a_{1n} \\ 
a_{21} & a_{22} & ･･･ & a_{2n} \\
･ & ･ & ･･･ & ･ \\
･ & ･ & ･･･ & ･ \\
a_{m1} & a_{m2} & ･･･ & a_{mn} 
\end{matrix} 
\right)

B = \left(
\begin{matrix} 
b_{11} & b_{12} & ･･･ & b_{1q} \\ 
b_{21} & b_{22} & ･･･ & b_{2q} \\
･ & ･ & ･･･ & ･ \\
･ & ･ & ･･･ & ･ \\
b_{p1} & a_{p2} & ･･･ & b_{pq} 
\end{matrix} 
\right)

C = \left(
\begin{matrix} 
c_{11} & c_{12} & ･･･ & c_{1q} \\ 
c_{21} & c_{22} & ･･･ & c_{2q} \\
･ & ･ & ･･･ & ･ \\
･ & ･ & ･･･ & ･ \\
c_{m1} & c_{m2} & ･･･ & c_{mq} 
\end{matrix} 
\right)
$$

$A$と $B$の積 $AB(=C)$は、 $n=p$の時に定義できる。

例 $A$と $B$の積 $AB$である $m×q$の行列 $C$

$$
C = AB = \left(
\begin{matrix} 
a_{11}b_{11}+a_{12}b_{21}+･･･+a_{1n}b_{p1} & ･･･ & a_{11}b_{1q}+a_{12}b_{2q}+･･･+a_{1q}b_{pq} \\ 
a_{21}b_{11}+a_{22}b_{21}+･･･+a_{2n}b_{p1} & ･･･ & a_{21}b_{1q}+a_{22}b_{2q}+･･･+a_{2q}b_{pq} \\
･ & ･･･ & ･ \\
･ & ･･･ & ･ \\
a_{m1}b_{11}+a_{22}b_{21}+･･･+a_{mn}b_{p1} & ･･･ & a_{m1}b_{1q}+a_{m2}b_{2q}+･･･+a_{mq}b_{pq} \\
\end{matrix} 
\right)
$$

$A$が$m×n$行列、$B$が$p×q$行列で$n=p$のとき、  
$A$の行ベクトルを$\vec{a_1}$,$\vec{a_2}$,…,$\vec{a_m}$、$B$の列ベクトルを$b_1$,$b_2$,…,$b_q$とすると、

$$
AB = \left(
\begin{matrix} 
\vec{a_1}b_1 & \vec{a_1}b_2 & ･･･ & \vec{a_1}b_q \\ 
\vec{a_2}b_1 & \vec{a_2}b_2 & ･･･ & \vec{a_2}b_q \\
･ & ･ & ･･･ & \vec{a_1}b_q \\
\vec{a_m}b_1 & \vec{a_m}b_2 & ･･･ & \vec{a_m}b_q
\end{matrix} 
\right)
$$

積 $AB$はこのようになり、 $m×q$ 行列になる。

例　

$$
A = \left(
\begin{matrix} 
1 &  3 \\ 
5 & 7 
\end{matrix} 
\right)

B = \left(
\begin{matrix} 
2 & 4 \\ 
6 & 8 
\end{matrix} 
\right)
$$  

$$
AB = \left(
\begin{matrix} 
1×2+3×6 & 1×4+3×8 \\ 
5×2+7×6 & 5×4+7×8
\end{matrix} 
\right)
= \left(
\begin{matrix} 
20 & 28 \\ 
52 & 76 
\end{matrix} 
\right)
 ≠ BA
$$


```python
arrayA = [
    [1, 3],
    [5, 7]
]
arrayB = [
    [2, 4],
    [6, 8]
]
ndarrayA = np.array(arrayA)
ndarrayB = np.array(arrayB)
print(np.dot(ndarrayA,ndarrayB))
```

    [[20 28]
     [52 76]]
    

- 特別に $AB = BA$ が成り立つ場合、 $A$ と $B$ は**交換可能**であるといいます。

参考記事はkamakiriさんの[こちら](https://takun-physics.net/11917/#rtoc-3)です。

## 特殊な行列

### 零行列

成分がすべて0である行列を**零行列**といいます。$O$で表します。

$
O = \left(
\begin{matrix} 
0 & 0 \\ 
0 & 0 \\ 
0 & 0 
\end{matrix} 
\right)
$　, $
O = \left(
\begin{matrix} 
0 & 0 & 0 \\ 
0 & 0 & 0 \\
0 & 0 & 0 
\end{matrix} 
\right)
$ 


```python
shape = (3,2)
np.zeros(shape)
```




    array([[0., 0.],
           [0., 0.],
           [0., 0.]])




```python
shape = (3,3)
np.zeros(shape)
```




    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])



### 単位行列

対角成分がすべて1で、それ以外の成分がすべて0である正方行列を**単位行列**といいます。  
$n$次単位行列を$E_n$で表します。

$
E_n = \left(
\begin{matrix} 
1 & 0 \\ 
0 & 1 
\end{matrix} 
\right)
$　,  $
E_n = \left(
\begin{matrix} 
1 & 0 & 0 \\ 
0 & 1 & 0 \\
0 & 0 & 1 
\end{matrix} 
\right)
$ 


```python
np.eye(2, dtype=int)
```




    array([[1, 0],
           [0, 1]])




```python
np.eye(3, dtype=int)
```




    array([[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]])



### 対角行列

対角成分以外の成分がすべて0の正方行列を**対角行列**といいます。  


$
A = \left(
\begin{matrix} 
3 & 0 & 0 \\ 
0 & 1 & 0 \\ 
0 & 0 & -1
\end{matrix} 
\right)　, 
 O = \left(
\begin{matrix} 
0 & 0 \\ 
0 & 0 
\end{matrix} 
\right)
$　,  $
E_n = \left(
\begin{matrix} 
1 & 0 & 0 \\ 
0 & 1 & 0 \\
0 & 0 & 1 
\end{matrix} 
\right)
$ 


```python
np.eye(2, dtype=int)
```




    array([[1, 0],
           [0, 1]])




```python
np.eye(3, dtype=int)
```




    array([[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]])



参考記事はkamakiriさんの[こちら](https://takun-physics.net/13700/#rtoc-2)です。

### 転置行列

$m×n$行列$A$の行と列を入れ替えた行列を**転置行列**といいます。

$
A = \left(
\begin{matrix} 
1 & 3 & 5 \\ 
6 & 4 & 2
\end{matrix} 
\right)
$　のとき、
$
A^{ \mathrm{ T } } = \left(
\begin{matrix} 
1 & 6 \\ 
3 & 4 \\ 
5 & 2
\end{matrix} 
\right)
$



```python
array = [
    [1, 3, 5],
    [6, 4, 2]
]
ndarray = np.array(array)
print(np.transpose(ndarray))
```

    [[1 6]
     [3 4]
     [5 2]]
    


```python
array = [
    [1, 3, 5],
    [6, 4, 2]
]
ndarray = np.array(array)
print(ndarray.T)
```

    [[1 6]
     [3 4]
     [5 2]]
    

参考記事はkamakiriさんの[こちら](https://takun-physics.net/12062/)です。

### 対称行列

$n$次正方行列$A$において、$A=A^{ \mathrm{ T } }$の行列を**対称行列**といいます。

$
A = \left(
\begin{matrix} 
1 & 4 & 5 \\
4 & 2 & 6 \\  
5 & 6 & 3
\end{matrix} 
\right)
$




```python
array = [
    [1, 4, 5],
    [4, 2, 6],
    [5, 6, 3]
]
ndarray = np.array(array)
print(np.transpose(ndarray))
```

    [[1 4 5]
     [4 2 6]
     [5 6 3]]
    


```python
array = [
    [1, 4, 5],
    [4, 2, 6],
    [5, 6, 3]
]
ndarray = np.array(array)
print(ndarray.T)
```

    [[1 4 5]
     [4 2 6]
     [5 6 3]]
    

### 交代行列

$n$次正方行列$A$において、$A^{ \mathrm{ T } }=-A$の行列を**交代行列**といいます。

このとき、対角成分はすべて0になります。

$
A = \left(
\begin{matrix} 
0 & 1 & 2 \\
-1 & 0 & 3 \\  
-2 & -3 & 0
\end{matrix} 
\right)
$




```python
array = [
    [0, 1, 2],
    [-1, 0, 3],
    [-2, -3, 0]
]

ndarray = np.array(array)
n = ndarray.shape[0]  # 行列のサイズを取得

alternating_matrix = np.zeros((n, n))  # 交代行列をゼロ行列で初期化

for i in range(n):
    for j in range(n):
        if i != j:
            alternating_matrix[i, j] = -ndarray[i, j]  # 対角線上以外の要素の符号を反転

print(alternating_matrix)
```

    [[ 0. -1. -2.]
     [ 1.  0. -3.]
     [ 2.  3.  0.]]
    

### 零因子

2つの行列$A$と$B$の積が零行列$O$であっても、$A=O$、$B=O$であるとは限りません。  特に、

$$AB=O　,　 A≠O　,　B≠O$$

である行列$A$、$B$を**零因子**と呼びます。

$
A = \left(
\begin{matrix} 
1 & -2 \\ 
-2 & 4
\end{matrix} 
\right)
$　,　$
B = \left(
\begin{matrix} 
2 & 2 \\ 
1 & 1 
\end{matrix} 
\right)
$  


```python
arrayA = [
    [1, -2],
    [-2, 4]
]
arrayB = [
    [2, 2],
    [1, 1]
]
ndarrayA = np.array(arrayA)
ndarrayB = np.array(arrayB)
print(np.dot(ndarrayA,ndarrayB))
```

    [[0 0]
     [0 0]]
    

## 逆行列

ある正方行列$A$にたいして、$XA=E_n$、または$AX=E_n$となる行列$X$のことを  
**逆行列**と呼び、$A^{-1}$と呼びます。

$A$が逆行列を持つとき、$A$を**正則**、または**正則行列**と呼びます。

### 行列式

ある正方行列$A$の**行列式**は、$det(A)$または$|A|$というように表記します。

$|A|≠0$となるとき、$A$は正則となり、逆行列$A^{-1}$が存在します。

参考記事はkamakiriさんの[こちら](https://takun-physics.net/12196/)です。

#### 2次の正方行列

$$
A=\begin{pmatrix}  a &b\\  c & d \end{pmatrix}\\
$$

2次の正方行列の行列式は簡単に求めることができます。

$$
\begin{align*}  |A|&=\begin{vmatrix}  a &b\\  c & d  \end{vmatrix}=ad-bc \end{align*}
$$


```python
array = [
    [2, -3],
    [-4, 5]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(round(det, 2))
```

    -2.0
    


```python
array = [
    [103, 98],
    [99, 102]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(round(det, 2))
```

    804.0
    

参考記事はkamakiriさんの[こちら](https://takun-physics.net/12154/#rtoc-2)です。

#### 3次の正方行列

$$
A=\begin{pmatrix}  a_{11} &a_{12} & a_{13} \\  a_{21} &a_{22} & a_{23} \\  a_{31} &a_{32} & a_{33} \end{pmatrix}\\
$$

3次の正方行列の行列式は比較的簡単に求めることができます。  
（**サラスの公式**）

$$
\begin{align*}  |A|&=\begin{vmatrix}  a_{11} &a_{12} & a_{13} \\  a_{21} &a_{22} & a_{23} \\  a_{31} &a_{32} & a_{33} \\  \end{vmatrix}\\ &=a_{11} a_{22} a_{33}+a_{12} a_{23}a_{31}+a_{13}a_{32}a_{21} -a_{13}a_{22} a_{31}-a_{11}a_{32} a_{23} -a_{13}a_{21}a_{33} \end{align*}
$$

図でイメージしたい方は[こちら](https://takun-physics.net/wp-content/uploads/2021/02/f8f98c031cd273de2ea270bac90c3902-1024x576.jpg)を参考にしてください。


```python
array = [
    [3, 4, 5],
    [0, 9, 6],
    [0, 8, 7]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(round(det, 2))
```

    45.0
    


```python
array = [
    [1, -2, 3],
    [-2, 3, 5],
    [3, -4, 1]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(round(det, 2))
```

    -14.0
    

参考記事はkamakiriさんの[こちら](https://takun-physics.net/12154/#rtoc-3)です。

#### 4次以上の正方行列

$$
A=\begin{pmatrix}  a_{11} &a_{12} & a_{13} \\  a_{21} &a_{22} & a_{23} \\  a_{31} &a_{32} & a_{33} \\  a_{41} &a_{42} & a_{43} \end{pmatrix}\\
$$

4次以上の正方行列の行列式はちょっと複雑になります。

**余因子展開**をして求めることが多いようです。


```python
array = [
    [1, 1, 3, 1],
    [1, 1, 1, 3],
    [3, 1, 1, 1],
    [1, 3, 1, 1]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(round(det, 2))
```

    48.0
    


```python
array = [
    [1, 1, 1, -1, 3],
    [-1, 1, 1, 1, 2],
    [1, -1, 1, 1, 2],
    [-1, -1, 1, 1, 2],
    [1, 1, -1, 1, 3]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(round(det, 2))
```

    -48.0
    

参考記事はkamakiriさんの[こちら](https://takun-physics.net/12258/)です。

### 逆行列の求め方

#### 2次の逆行列

$ A=\begin{pmatrix}  a &b\\  c & d \end{pmatrix}\\ $の逆行列$X=A^{-1}$は、以下で与えられます。

$$
X = \frac{1}{ad - bc}\begin{pmatrix}  d & -b\\  -c & a \end{pmatrix}\\
$$


```python
array = [
    [4, 5],
    [-3, -2]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(f"行列式の値：{round(det, 2)}")

try:
    inv = np.linalg.inv(ndarray)
    print(f"逆行列：\n{inv}")
except np.linalg.LinAlgError:
    print("計算できません")
```

    行列式の値：7.0
    逆行列：
    [[-0.28571429 -0.71428571]
     [ 0.42857143  0.57142857]]
    

#### 3次以上の逆行列

3次以上の逆行列は、2次のように簡単には求めることができません。

Pythonでは簡単に求めることができます。


```python
array = [
    [1, -1, 3],
    [2, -1, 5],
    [2, 1, 4]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(f"行列式の値：{round(det, 2)}")

try:
    inv = np.linalg.inv(ndarray)
    print(f"逆行列：\n{inv}")
except np.linalg.LinAlgError:
    print("計算できません")
```

    行列式の値：1.0
    逆行列：
    [[-9.  7. -2.]
     [ 2. -2.  1.]
     [ 4. -3.  1.]]
    


```python
array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

ndarray = np.array(array)
det = np.linalg.det(ndarray)
print(f"行列式の値：{round(det, 2)}")

try:
    inv = np.linalg.inv(ndarray)
    print(f"逆行列：\n{inv}")
except np.linalg.LinAlgError:
    print("計算できません")
```

    行列式の値：0.0
    計算できません
    

参考記事はkamakiriさんの[こちら](https://takun-physics.net/12554/)です。

## 固有値と固有ベクトル

$n$次正方行列$A$に対し、

$$
Ax = λx　(x≠0)
$$

を満たす$λ$（スカラー）と$n$次ベクトル$x$が存在するとき、  
$λ$を$A$の**固有値**、$x$を$A$の$λ$に関する**固有ベクトル**といいます。

参考記事はkamakiriさんの[こちら](https://takun-physics.net/13634/)です。  

記事内では固有値・固有ベクトルを学ぶモチベーションについても触れられています。

### 固有値

正方行列$A$が与えられたとき、

$$
g_{A}(t) = |tE - A| = A = \left(
\begin{matrix} 
t - a_{11} & - a_{12} & ･･･ & - a_{1n} \\ 
- a_{21} & t - a_{22} & ･･･ & - a_{2n} \\
･ & ･ & ･･･ & ･ \\
･ & ･ & ･･･ & ･ \\
- a_{m1} & - a_{m2} & ･･･ & t - a_{mn} 
\end{matrix} 
\right)　(x≠0)
$$

を**固有多項式**、$g_{A}(t)=0$ を**固有方程式**と呼びます。

＜固有値の求め方＞

$n$次正方行列$A$の**固有値**は、固有方程式$g_A(t)=0$の解として求められます。


```python
array = [
    [5, -1],
    [2, 2]
]

ndarray = np.array(array)
eig = np.linalg.eig(ndarray)
print(eig[0])
```

    [4. 3.]
    

$A = \begin{pmatrix}  5 & -1\\  2 & 2 \end{pmatrix}$の場合、固有値は$λ = 4, λ = 3$と2個あります。


```python
array = [
    [3, -1],
    [1, 5]
]

ndarray = np.array(array)
eig = np.linalg.eig(ndarray)
print(eig[0])
```

    [4. 4.]
    

$A = \begin{pmatrix}  3 & -1\\  1 & 5 \end{pmatrix}$の場合、固有値は$λ = 4$と1個しかありません。

このように、固有多項式が$(t - λ)^mh(t)$と書けるとき（固有値に重解が含まれるとき）、  
$λ$を**重複度**$m$の解と呼びます。

$A = \begin{pmatrix}  3 & -1\\  1 & 5 \end{pmatrix}$の場合、固有多項式は$(t - 4)^2$となり、重複度は$2$となります。

参考記事はkamakiriさんの[こちら](https://takun-physics.net/13634/#rtoc-3)です。

### 固有ベクトル

＜固有ベクトルの求め方＞

固有値$λ$に対応する**固有ベクトル**は、同次連立1次方程式

$$
(λE - A)=0
$$

の自明でない解として求められます。


```python
array = [
    [5, -1],
    [2, 2]
]

ndarray = np.array(array)
eig = np.linalg.eig(ndarray)
print(eig[1])
```

    [[0.70710678 0.4472136 ]
     [0.70710678 0.89442719]]
    

$A = \begin{pmatrix}  5 & -1\\  2 & 2 \end{pmatrix}$の場合、  

固有値が$λ = 4$ の場合は、$λE - A = \begin{pmatrix}  4-5 & -(-1)\\  -(2) & 4-2 \end{pmatrix} = \begin{pmatrix}  -1 & -1\\  -2 & 2 \end{pmatrix}$となるので、  
固有ベクトルは$\begin{pmatrix}  x_1\\  x_2 \end{pmatrix} = \begin{pmatrix}  1\\  1 \end{pmatrix}C$ となります。

固有値が$λ = 3$ の場合は、$λE - A = \begin{pmatrix}  3-5 & -(-1)\\  -(2) & 3-2 \end{pmatrix} = \begin{pmatrix}  -2 & -1\\  -2 & 1 \end{pmatrix}$となるので、  
固有ベクトルは$\begin{pmatrix}  x_1\\  x_2 \end{pmatrix} = \begin{pmatrix}  1\\  2 \end{pmatrix}C$ となります。

※$C$：任意の数

**※ numpyで求めた固有方程式は、ベクトルの長さが1になるように正規化されています。**


```python
array = [
    [3, -1],
    [1, 5]
]

ndarray = np.array(array)
eig = np.linalg.eig(ndarray)
print(eig[1])
```

    [[-0.70710678 -0.70710678]
     [ 0.70710678  0.70710678]]
    

$A = \begin{pmatrix}  3 & -1\\  1 & 5 \end{pmatrix}$の場合、  

固有値が$λ = 4$ の場合は、$λE - A = \begin{pmatrix}  4-3 & -(-1)\\  -(1) & 4-5 \end{pmatrix} = \begin{pmatrix}  1 & 1\\  -1 & -1 \end{pmatrix}$となるので、  
固有ベクトルは$\begin{pmatrix}  x_1\\  x_2 \end{pmatrix} = \begin{pmatrix}  -1\\  1 \end{pmatrix}C$ となります。


※$C$：任意の数

参考記事はkamakiriさんの[こちら](https://takun-physics.net/13634/#rtoc-4)です。

### 固有値・固有ベクトルを学ぶモチベーション

固有値と固有ベクトルを使うことで、**対角行列**を作ることができるようになります。



対角行列を作ることができるようになるメリットは以下の通りです。

- 計算量を削減することができる
- 行列のべき乗の計算が簡単になる

本資料では解説しないので、kamakiriさんの記事を参考にしてください。

- 対角行列の作り方：https://takun-physics.net/13700/
- 基底変換の方法：https://takun-physics.net/14064/

