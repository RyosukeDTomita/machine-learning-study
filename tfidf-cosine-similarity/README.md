# TF-IDFとコサイン類似度を用いた日本語テキストの類似度計算

## HOW TO USE

```shell
uv run sample.py
```

---

## 概要

- Term frequency(単語頻度)とInverse document frequency(逆文書頻度)によってベクトル化を行っている。
- 内積の定義式を変形してcosを求めているだけ。文章から得られたベクトル同士のcosを求めることで、類似度を求めている。 --> ベクトルの方向が似ている=cosが1に近づく(-90<=0<=90)でcosの値は正

[参考](https://www.jstage.jst.go.jp/article/jkg/70/7/70_373/_pdfhttps://www.jstage.jst.go.jp/article/jkg/70/7/70_373/_pdf)

---

## 感想

- 単語がどれくらい頻出するのかしかみていない
  - 単語を置き換えた文があった場合には置き換える単語の類似性は見えない。
  - 語順が変わった際の差も出にくい。
