from text_analyzer.analyze import analyze_file

report = analyze_file("data/sample.txt", top_n=10)
print(report)