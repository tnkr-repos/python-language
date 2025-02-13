from time_demo import heavy_work

def test_benchmark(benchmark):
    benchmark(heavy_work)

# run pytest for this to run