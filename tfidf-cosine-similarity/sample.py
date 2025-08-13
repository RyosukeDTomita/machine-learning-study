from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import MeCab
import unidic_lite

def tokenize_ja(text):
    tagger = MeCab.Tagger(f'-r /dev/null -d {unidic_lite.DICDIR}')
    nodes = tagger.parseToNode(text)
    tokens = []
    while nodes:
        if nodes.feature.split(',')[0] in ['名詞', '動詞', '形容詞']:  # 主要な品詞のみを対象
            tokens.append(nodes.surface)
        nodes = nodes.next
    return tokens

# テンプレートと比較対象の文章
template_text = """
宇宙に始まりはあるが、終わりはない。　―――無限
星にもまた始まりはあるが、自らの力をもって滅び逝く。　―――有限
英知を持つ者こそ、最も愚かであること。歴史からも読み取れる。
海に生ける魚は、陸の世界を知らない。彼らが英知を持てば、それもまた滅び逝く。
人間が光の速さを超えるのは、魚たちが陸で生活を始めるよりも滑稽。
これは抗える者たちに対する、神からの最後通告とも言えよう。
"""
modified_text = """
宇宙に始まりはあるが、終わりはない。無限。
星にもまた始まりはあるが、自らの力をもって滅びゆく。有限。
英知を持つ者こそ最も愚かであるのは歴史からも読み取れる。
海に生ける魚は陸の世界を知らない。
彼らが英知を持てばそれもまた滅びゆく。
人間が光の速さを超えるのは、魚たちが陸で生活を始めるよりも滑稽。
これは、そんな神からの最後通告に抗った者たちによる――
執念のエピグラフ。
"""

# TF-IDFベクトル化
# NOTE: デフォルトでは、日本語のテキストを適切に分割していないため、MeCabを使用してトークン化しないと文章を一つの単語として扱うことになる。
vectorizer = TfidfVectorizer(tokenizer=tokenize_ja)
tfidf_matrix = vectorizer.fit_transform([template_text, modified_text])

# 語彙（単語）一覧の取得と表示
print("\n抽出された単語一覧:")
print(vectorizer.get_feature_names_out())
print("\nTF-IDF行列（各行が文書、各列が単語に対応）:")
print(tfidf_matrix.toarray())

# コサイン類似度計算
similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
print(f"類似度: {similarity:.4f}")

