import math


class CountVectorizer:
    def __init__(self):
        self.vocabulary = {}
        self.matrix = []

    def fit_transform(self, corpus: list) -> list:
        """
        Расчет матрицы на основе корпусных данных
        corpus – переменная с фразой

        Две части:
        1. Отбор всех уникальных слов по их порядку
        2. Подсчет использования каждого из слов в строке
        """
        for string in corpus:
            for word in string.split(" "):
                word = word.lower()
                if word not in self.vocabulary:
                    self.vocabulary[word] = 0

        for string in corpus:
            current_vocabulary = {key: 0 for key in self.vocabulary}
            for word in string.split(" "):
                word = word.lower()
                current_vocabulary[word] += 1
            self.matrix.append(list(current_vocabulary.values()))
        return self.matrix

    def get_feature_names(self) -> list:
        """
        Вывод всех слов, рассматриваемых в предложениях
        """
        return list(self.vocabulary.keys())


class TfidfTransformer:
    def __init__(self):
        self.tfidf = []

    def tf_transform(self, matrix: list) -> list:
        """
        Расчет матрицы tf
        Вывод: значения изначальной матрицы, деленные на число слов в строке
        """
        tf = []
        for row in matrix:
            tf_row = []
            for element in row:
                tf_row.append(round(element / sum(row), 3))
            tf.append(tf_row)
        return tf

    def idf_transform(self, matrix: list, feature_names: list) -> list:
        """
        Расчет матрицы idf на основе следующих данных:
        feature_names – названия всех слов в наборе данных,
                        результат get_feature_names в классе CountVectorizer

        Вывод: преобразованные значения изначальной матрицы
        """
        idf = []
        for idx_element in range(len(feature_names)):
            count_element = 0
            for idx_row in range(len(matrix)):
                if matrix[idx_row][idx_element] > 0:
                    count_element += 1
            current_idf = math.log((len(matrix) + 1) / (count_element + 1)) + 1
            idf.append(round(current_idf, 3))
        return idf

    def fit_transform(self, matrix: list, feature_names: list) -> list:
        """
        Расчет матрицы tfidf на основе следующих данных:
        tf;
        idf

        Вывод: перемноженные друг на друга матрицы
        (жалко, нельзя использовать numpy...)
        """
        tf = self.tf_transform(matrix)
        idf = self.idf_transform(matrix, feature_names)
        for idx_row in range(len(tf)):
            tfidf_row = []
            for idx_column in range(len(idf)):
                tfidf_row.append(round(tf[idx_row][idx_column] * idf[idx_column], 3))
            self.tfidf.append(tfidf_row)
        return self.tfidf


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self._transformer = TfidfTransformer()

    def fit_transform(self, corpus: list) -> list:
        matrix = super().fit_transform(corpus)
        vocabulary = super().get_feature_names()
        return self._transformer.fit_transform(matrix, vocabulary)


if __name__ == '__main__':
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste"
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)
