from text_analyzer.analyze import tokenize, build_report


def test_tokenize_removes_punctuation_and_lowercases():
    text = "Python, PYTHON! Java?"
    tokens = tokenize(text)
    assert tokens == ["python", "python", "java"]


def test_build_report_basic_stats():
    tokens = ["python", "python", "java"]
    report = build_report(tokens, top_n=1)

    assert report["total_words"] == 3
    assert report["unique_words"] == 2
    assert report["top_words"] == [("python", 2)]