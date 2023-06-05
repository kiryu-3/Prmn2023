<meta charset="utf-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Machine_Learning_0</title>

<!-- Load mathjax -->

<!-- MathJax configuration -->

<!-- End of mathjax configuration -->

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                線形代数基礎¶
                =======
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[2]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="c1">\# 最初に実行してください</span>
                        <span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                kamakiriさんの[こちら](https://takun-physics.net/category/%e5%a4%a7%e5%ad%a6%e6%95%b0%e5%ad%a6/)の記事群を主に参考にしました。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                行列¶
                ---
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                **行列**：数を方形に並べたもの。横の並びが**行**で、縦の並びが**列**である。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                例 $m$行$n$列の行列($m×n$行列)

                $
                A = \left(
                \begin{matrix} 
                a_{11} & ･･･ & a_{1n} \\ 
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                a_{m1} & ･･･ & a_{mn} 
                \end{matrix} 
                \right)
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                * $m=n$となる行列を**正方行列**と呼ぶ。
                * 構成するそれぞれの数値を**要素**と呼ぶ。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/11917/)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                行列にスカラーを掛ける¶
                ------------
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                行列にもスカラーを掛けることができる。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                例　行列$A$を$k$倍した行列

                $
                kA = \left(
                \begin{matrix} 
                ka_{11} & ･･･ & ka_{1n} \\ 
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                ka_{m1} & ･･･ & ka_{mn} 
                \end{matrix} 
                \right)
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                行列の和¶
                -----
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                以下のように行列$A$と$B$を定義する。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                例 $m×n$行列$A$と$B$

                $
                A = \left(
                \begin{matrix} 
                a_{11} & ･･･ & a_{1n} \\ 
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                a_{m1} & ･･･ & a_{mn} 
                \end{matrix} 
                \right)
                $　　　$
                B = \left(
                \begin{matrix} 
                b_{11} & ･･･ & b_{1n} \\ 
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                b_{m1} & ･･･ & b_{mn} 
                \end{matrix} 
                \right)
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $A$と$B$の和$A+B$と差$A-B$は、次のように計算できる。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                例 和$A+B$と差$A-B$

                $
                A+B = \left(
                \begin{matrix} 
                a_{11}+b_{11} & ･･･ & a_{1n}+b_{1n} \\ 
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                a_{m1}+b_{m1} & ･･･ & a_{mn}+b_{mn} 
                \end{matrix} 
                \right)
                $　　　$
                A-B = \left(
                \begin{matrix} 
                a_{11}-b_{11} & ･･･ & a_{1n}-b_{1n} \\ 
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                a_{m1}-b_{m1} & ･･･ & a_{mn}-b_{mn} 
                \end{matrix} 
                \right)
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                * $A$と$B$の行数あるいは列数が異なる場合は、行列の和と差の計算はできない。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                例　

                $
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
                $

                $
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
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[3]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">arrayA</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">arrayB</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">6</span><span class="p">,</span> <span class="mi">8</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">ndarrayA</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">arrayA</span><span class="p">)</span>
                        <span class="n">ndarrayB</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">arrayB</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">ndarrayA</span> <span class="o">+</span> <span class="n">ndarrayB</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[ 3  7]
                     [11 15]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/11917/#rtoc-5)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                行列の積¶
                -----
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                以下のように行列$A$と$B$と$C$を定義する。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                例 $m×n$行列Aと$p×q$行列Bと$m×q$行列$C$

                $
                A = \left(
                \begin{matrix} 
                a_{11} & a_{12} & ･･･ & a_{1n} \\ 
                a_{21} & a_{22} & ･･･ & a_{2n} \\
                ･ & ･ & ･･･ & ･ \\
                ･ & ･ & ･･･ & ･ \\
                a_{m1} & a_{m2} & ･･･ & a_{mn} 
                \end{matrix} 
                \right)
                $　　　$
                B = \left(
                \begin{matrix} 
                b_{11} & b_{12} & ･･･ & b_{1q} \\ 
                b_{21} & b_{22} & ･･･ & b_{2q} \\
                ･ & ･ & ･･･ & ･ \\
                ･ & ･ & ･･･ & ･ \\
                b_{p1} & a_{p2} & ･･･ & b_{pq} 
                \end{matrix} 
                \right)
                $　　　$
                C = \left(
                \begin{matrix} 
                c_{11} & c_{12} & ･･･ & c_{1q} \\ 
                c_{21} & c_{22} & ･･･ & c_{2q} \\
                ･ & ･ & ･･･ & ･ \\
                ･ & ･ & ･･･ & ･ \\
                c_{m1} & c_{m2} & ･･･ & c_{mq} 
                \end{matrix} 
                \right)
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $A$と$B$の積$AB(=C)$は、$n=p$の時に定義できる。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                例 $A$と$B$の積$AB$である$m×q$の行列$C$

                $
                C = AB = \left(
                \begin{matrix} 
                a_{11}b_{11}+a_{12}b_{21}+･･･+a_{1n}b_{p1} & ･･･ & a_{11}b_{1q}+a_{12}b_{2q}+･･･+a_{1q}b_{pq} \\ 
                a_{21}b_{11}+a_{22}b_{21}+･･･+a_{2n}b_{p1} & ･･･ & a_{21}b_{1q}+a_{22}b_{2q}+･･･+a_{2q}b_{pq} \\
                ･ & ･･･ & ･ \\
                ･ & ･･･ & ･ \\
                a_{m1}b_{11}+a_{22}b_{21}+･･･+a_{mn}b_{p1} & ･･･ & a_{m1}b_{1q}+a_{m2}b_{2q}+･･･+a_{mq}b_{pq} \\
                \end{matrix} 
                \right)
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $A$が$m×n$行列、$B$が$p×q$行列で$n=p$のとき、  
                $A$の行ベクトルを$\vec{a_1}$,$\vec{a_2}$,…,$\vec{a_m}$、$B$の列ベクトルを$b_1$,$b_2$,…,$b_q$とすると、

                $
                AB = \left(
                \begin{matrix} 
                \vec{a_1}b_1 & \vec{a_1}b_2 & ･･･ & \vec{a_1}b_q \\ 
                \vec{a_2}b_1 & \vec{a_2}b_2 & ･･･ & \vec{a_2}b_q \\
                ･ & ･ & ･･･ & \vec{a_1}b_q \\
                \vec{a_m}b_1 & \vec{a_m}b_2 & ･･･ & \vec{a_m}b_q
                \end{matrix} 
                \right)
                $

                積$AB$はこのようになり、$m×q$ 行列になる。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                例　

                $
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
                $

                $
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
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[4]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">arrayA</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">arrayB</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">6</span><span class="p">,</span> <span class="mi">8</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">ndarrayA</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">arrayA</span><span class="p">)</span>
                        <span class="n">ndarrayB</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">arrayB</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">dot</span><span class="p">(</span><span class="n">ndarrayA</span><span class="p">,</span><span class="n">ndarrayB</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[20 28]
                     [52 76]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                * 特別に$AB = BA$が成り立つ場合、$A$と$B$は**交換可能**であるといいます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/11917/#rtoc-3)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                特殊な行列¶
                ------
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 零行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                成分がすべて0である行列を**零行列**といいます。$O$で表します。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
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
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[5]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">shape</span> <span class="o">=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">2</span><span class="p">)</span>
                        <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">shape</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[5]:</div>

                <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
                    <pre>
                    array([[0., 0.],
                           [0., 0.],
                           [0., 0.]])
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[6]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">shape</span> <span class="o">=</span> <span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">3</span><span class="p">)</span>
                        <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">(</span><span class="n">shape</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[6]:</div>

                <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
                    <pre>
                    array([[0., 0., 0.],
                           [0., 0., 0.],
                           [0., 0., 0.]])
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 単位行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                対角成分がすべて1で、それ以外の成分がすべて0である正方行列を**単位行列**といいます。  
                $n$次単位行列を$E_n$で表します。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
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
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[7]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">np</span><span class="o">.</span><span class="n">eye</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[7]:</div>

                <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
                    <pre>
                    array([[1, 0],
                           [0, 1]])
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[8]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">np</span><span class="o">.</span><span class="n">eye</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[8]:</div>

                <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
                    <pre>
                    array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 対角行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                対角成分以外の成分がすべて0の正方行列を**対角行列**といいます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
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
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[9]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">np</span><span class="o">.</span><span class="n">eye</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[9]:</div>

                <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
                    <pre>
                    array([[1, 0],
                           [0, 1]])
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[10]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">np</span><span class="o">.</span><span class="n">eye</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt">Out[10]:</div>

                <div class="jp-RenderedText jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/plain">
                    <pre>
                    array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/13700/#rtoc-2)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 転置行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $m×n$行列$A$の行と列を入れ替えた行列を**転置行列**といいます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
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
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[11]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">6</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">transpose</span><span class="p">(</span><span class="n">ndarray</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[1 6]
                     [3 4]
                     [5 2]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[12]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">6</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">ndarray</span><span class="o">.</span><span class="n">T</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[1 6]
                     [3 4]
                     [5 2]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/12062/)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 対称行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $n$次正方行列$A$において、$A=A^{ \mathrm{ T } }$の行列を**対称行列**といいます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $
                A = \left(
                \begin{matrix} 
                1 & 4 & 5 \\
                4 & 2 & 6 \\  
                5 & 6 & 3
                \end{matrix} 
                \right)
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[13]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">transpose</span><span class="p">(</span><span class="n">ndarray</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[1 4 5]
                     [4 2 6]
                     [5 6 3]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[14]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">ndarray</span><span class="o">.</span><span class="n">T</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[1 4 5]
                     [4 2 6]
                     [5 6 3]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 交代行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $n$次正方行列$A$において、$A^{ \mathrm{ T } }=-A$の行列を**交代行列**といいます。

                このとき、対角成分はすべて0になります。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $
                A = \left(
                \begin{matrix} 
                0 & 1 & 2 \\
                -1 & 0 & 3 \\  
                -2 & -3 & 0
                \end{matrix} 
                \right)
                $
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[15]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span><span class="o">=</span><span class="p">[</span>
                            <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">],</span>
                            <span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="o">-</span><span class="mi">3</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">n</span> <span class="o">=</span> <span class="n">ndarray</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>  <span class="c1">\# 行列のサイズを取得</span>

                        <span class="n">alternating_matrix</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">zeros</span><span class="p">((</span><span class="n">n</span><span class="p">,</span> <span class="n">n</span><span class="p">))</span>  <span class="c1">\# 交代行列をゼロ行列で初期化</span>

                        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
                            <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">n</span><span class="p">):</span>
                                <span class="k">if</span> <span class="n">i</span> <span class="o">!=</span> <span class="n">j</span><span class="p">:</span>
                                    <span class="n">alternating_matrix</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="p">]</span> <span class="o">=</span> <span class="o">-</span><span class="n">ndarray</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="p">]</span>  <span class="c1">\# 対角線上以外の要素の符号を反転</span>

                        <span class="nb">print</span><span class="p">(</span><span class="n">alternating_matrix</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[ 0. -1. -2.]
                     [ 1.  0. -3.]
                     [ 2.  3.  0.]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 零因子¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                2つの行列$A$と$B$の積が零行列$O$であっても、$A=O$、$B=O$であるとは限りません。  特に、
                $$AB=O　,　 A≠O　,　B≠O$$

                である行列$A$、$B$を**零因子**と呼びます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
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
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[16]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">arrayA</span> <span class="o">=</span><span class="p">[</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">],</span>
                            <span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="mi">4</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">arrayB</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span>
                        <span class="p">]</span>
                        <span class="n">ndarrayA</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">arrayA</span><span class="p">)</span>
                        <span class="n">ndarrayB</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">arrayB</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">dot</span><span class="p">(</span><span class="n">ndarrayA</span><span class="p">,</span><span class="n">ndarrayB</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[0 0]
                     [0 0]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                逆行列¶
                ----
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ある正方行列$A$にたいして、$XA=E_n$、または$AX=E_n$となる行列$X$のことを  
                **逆行列**と呼び、$A^{-1}$と呼びます。

                $A$が逆行列を持つとき、$A$を**正則**、または**正則行列**と呼びます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 行列式¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ある正方行列$A$の**行列式**は、$det(A)$または$|A|$というように表記します。

                $|A|≠0$となるとき、$A$は正則となり、逆行列$A^{-1}$が存在します。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/12196/)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                #### 2次の正方行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">$$
            A=\begin{pmatrix}  a &b\\  c & d \end{pmatrix}\\
            $$</div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                2次の正方行列の行列式は簡単に求めることができます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">$$
            \begin{align*}  |A|&=\begin{vmatrix}  a &b\\  c & d  \end{vmatrix}=ad-bc \end{align*}
            $$</div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[22]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="o">-</span><span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="o">-</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    -2.0
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[24]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">103</span><span class="p">,</span> <span class="mi">98</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">99</span><span class="p">,</span> <span class="mi">102</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    804.0
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/12154/#rtoc-2)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                #### 3次の正方行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">$$
            A=\begin{pmatrix}  a_{11} &a_{12} & a_{13} \\  a_{21} &a_{22} & a_{23} \\  a_{31} &a_{32} & a_{33} \end{pmatrix}\\
            $$</div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                3次の正方行列の行列式は比較的簡単に求めることができます。  
                （**サラスの公式**）
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">$$
            \begin{align*}  |A|&=\begin{vmatrix}  a_{11} &a_{12} & a_{13} \\  a_{21} &a_{22} & a_{23} \\  a_{31} &a_{32} & a_{33} \\  \end{vmatrix}\\ &=a_{11} a_{22} a_{33}+a_{12} a_{23}a_{31}+a_{13}a_{32}a_{21} -a_{13}a_{22} a_{31}-a_{11}a_{32} a_{23} -a_{13}a_{21}a_{33} \end{align*}
            $$</div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                図でイメージしたい方は[こちら](https://takun-physics.net/wp-content/uploads/2021/02/f8f98c031cd273de2ea270bac90c3902-1024x576.jpg)を参考にしてください。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[25]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">9</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    45.0
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[23]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span><span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="o">-</span><span class="mi">4</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    -14.0
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/12154/#rtoc-3)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                #### 4次以上の正方行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">$$
            A=\begin{pmatrix}  a_{11} &a_{12} & a_{13} \\  a_{21} &a_{22} & a_{23} \\  a_{31} &a_{32} & a_{33} \\  a_{41} &a_{42} & a_{43} \end{pmatrix}\\
            $$</div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                4次以上の正方行列の行列式はちょっと複雑になります。

                **余因子展開**をして求めることが多いようです。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[26]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    48.0
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[27]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span>
                            <span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">))</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    -48.0
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/12258/)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 逆行列の求め方¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                #### 2次の逆行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $ A=\begin{pmatrix}  a &b\\  c & d \end{pmatrix}\\ $の逆行列$X=A^{-1}$は、以下で与えられます。
                $$
                X = \frac{1}{ad - bc}\begin{pmatrix}  d & -b\\  -c & a \end{pmatrix}\\
                $$
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[40]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
                            <span class="p">[</span><span class="o">-</span><span class="mi">3</span><span class="p">,</span> <span class="o">-</span><span class="mi">2</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"行列式の値：</span><span class="si">{</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

                        <span class="k">try</span><span class="p">:</span>
                            <span class="n">inv</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">inv</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"逆行列：</span><span class="se">\n</span><span class="si">{</span><span class="n">inv</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                        <span class="k">except</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">LinAlgError</span><span class="p">:</span>
                            <span class="nb">print</span><span class="p">(</span><span class="s2">"計算できません"</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    行列式の値：7.0
                    逆行列：
                    [[-0.28571429 -0.71428571]
                     [ 0.42857143  0.57142857]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                #### 3次以上の逆行列¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                3次以上の逆行列は、2次のように簡単には求めることができません。

                Pythonでは簡単に求めることができます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[41]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span><span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mi">4</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"行列式の値：</span><span class="si">{</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

                        <span class="k">try</span><span class="p">:</span>
                            <span class="n">inv</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">inv</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"逆行列：</span><span class="se">\n</span><span class="si">{</span><span class="n">inv</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                        <span class="k">except</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">LinAlgError</span><span class="p">:</span>
                            <span class="nb">print</span><span class="p">(</span><span class="s2">"計算できません"</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    行列式の値：1.0
                    逆行列：
                    [[-9.  7. -2.]
                     [ 2. -2.  1.]
                     [ 4. -3.  1.]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[42]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span> <span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">4</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="mi">6</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">7</span><span class="p">,</span> <span class="mi">8</span><span class="p">,</span> <span class="mi">9</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">det</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">det</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"行列式の値：</span><span class="si">{</span><span class="nb">round</span><span class="p">(</span><span class="n">det</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>

                        <span class="k">try</span><span class="p">:</span>
                            <span class="n">inv</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">inv</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                            <span class="nb">print</span><span class="p">(</span><span class="sa">f</span><span class="s2">"逆行列：</span><span class="se">\n</span><span class="si">{</span><span class="n">inv</span><span class="si">}</span><span class="s2">"</span><span class="p">)</span>
                        <span class="k">except</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">LinAlgError</span><span class="p">:</span>
                            <span class="nb">print</span><span class="p">(</span><span class="s2">"計算できません"</span><span class="p">)</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    行列式の値：0.0
                    計算できません
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/12554/)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                固有値と固有ベクトル¶
                -----------
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $n$次正方行列$A$に対し、
                $$
                Ax = λx　(x≠0)
                $$

                を満たす$λ$（スカラー）と$n$次ベクトル$x$が存在するとき、  
                $λ$を$A$の**固有値**、$x$を$A$の$λ$に関する**固有ベクトル**といいます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/13634/)です。

                記事内では固有値・固有ベクトルを学ぶモチベーションについても触れられています。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 固有値¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
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
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ＜固有値の求め方＞

                $n$次正方行列$A$の**固有値**は、固有方程式$g_A(t)=0$の解として求められます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[51]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span><span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">eig</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">eig</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">eig</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [4. 3.]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $A = \begin{pmatrix}  5 & -1\\  2 & 2 \end{pmatrix}$の場合、固有値は$λ = 4, λ = 3$と2個あります。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[52]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span><span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">eig</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">eig</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">eig</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [4. 4.]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $A = \begin{pmatrix}  3 & -1\\  1 & 5 \end{pmatrix}$の場合、固有値は$λ = 4$と1個しかありません。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                このように、固有多項式が$(t - λ)^mh(t)$と書けるとき（固有値に重解が含まれるとき）、  
                $λ$を**重複度**$m$の解と呼びます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $A = \begin{pmatrix}  3 & -1\\  1 & 5 \end{pmatrix}$の場合、固有多項式は$(t - 4)^2$となり、重複度は$2$となります。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/13634/#rtoc-3)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 固有ベクトル¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ＜固有ベクトルの求め方＞

                固有値$λ$に対応する**固有ベクトル**は、同次連立1次方程式
                $$
                (λE - A)=0
                $$

                の自明でない解として求められます。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[53]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span><span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">5</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">eig</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">eig</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">eig</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[0.70710678 0.4472136 ]
                     [0.70710678 0.89442719]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $A = \begin{pmatrix}  5 & -1\\  2 & 2 \end{pmatrix}$の場合、

                固有値が$λ = 4$ の場合は、$λE - A = \begin{pmatrix}  4-5 & -(-1)\\  -(2) & 4-2 \end{pmatrix} = \begin{pmatrix}  -1 & -1\\  -2 & 2 \end{pmatrix}$となるので、  
                固有ベクトルは$\begin{pmatrix}  x_1\\  x_2 \end{pmatrix} = \begin{pmatrix}  1\\  1 \end{pmatrix}C$ となります。

                固有値が$λ = 3$ の場合は、$λE - A = \begin{pmatrix}  3-5 & -(-1)\\  -(2) & 3-2 \end{pmatrix} = \begin{pmatrix}  -2 & -1\\  -2 & 1 \end{pmatrix}$となるので、  
                固有ベクトルは$\begin{pmatrix}  x_1\\  x_2 \end{pmatrix} = \begin{pmatrix}  1\\  2 \end{pmatrix}C$ となります。

                ※$C$：任意の数
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                **※ numpyで求めた固有方程式は、ベクトルの長さが1になるように正規化されています。**
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[54]:</div>

            <div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
                <div class="CodeMirror cm-s-jupyter">
                    <div class=" highlight hl-ipython3">
                        <pre>
                        <span></span><span class="n">array</span><span class="o">=</span> <span class="p">[</span>
                            <span class="p">[</span><span class="mi">3</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">],</span>
                            <span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">]</span>
                        <span class="p">]</span>

                        <span class="n">ndarray</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">array</span><span class="p">)</span>
                        <span class="n">eig</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">linalg</span><span class="o">.</span><span class="n">eig</span><span class="p">(</span><span class="n">ndarray</span><span class="p">)</span>
                        <span class="nb">print</span><span class="p">(</span><span class="n">eig</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
                        </pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="jp-Cell-outputWrapper">
        <div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser"></div>

        <div class="jp-OutputArea jp-Cell-outputArea">
            <div class="jp-OutputArea-child">
                <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>

                <div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
                    <pre>
                    [[-0.70710678 -0.70710678]
                     [ 0.70710678  0.70710678]]
                    </pre>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                $A = \begin{pmatrix}  3 & -1\\  1 & 5 \end{pmatrix}$の場合、

                固有値が$λ = 4$ の場合は、$λE - A = \begin{pmatrix}  4-3 & -(-1)\\  -(1) & 4-5 \end{pmatrix} = \begin{pmatrix}  1 & 1\\  -1 & -1 \end{pmatrix}$となるので、  
                固有ベクトルは$\begin{pmatrix}  x_1\\  x_2 \end{pmatrix} = \begin{pmatrix}  -1\\  1 \end{pmatrix}C$ となります。

                ※$C$：任意の数
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                参考記事はkamakiriさんの[こちら](https://takun-physics.net/13634/#rtoc-4)です。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                ### 固有値・固有ベクトルを学ぶモチベーション¶
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                固有値と固有ベクトルを使うことで、**対角行列**を作ることができるようになります。
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                対角行列を作ることができるようになるメリットは以下の通りです。

                * 計算量を削減することができる
                * 行列のべき乗の計算が簡単になる
            </div>
        </div>
    </div>
</div>

<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
    <div class="jp-Cell-inputWrapper">
        <div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser"></div>

        <div class="jp-InputArea jp-Cell-inputArea">
            <div class="jp-InputPrompt jp-InputArea-prompt"></div>

            <div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
                本資料では解説しないので、kamakiriさんの記事を参考にしてください。

                * 対角行列の作り方：https://takun-physics.net/13700/
                * 基底変換の方法：https://takun-physics.net/14064/
            </div>
        </div>
    </div>
</div>
