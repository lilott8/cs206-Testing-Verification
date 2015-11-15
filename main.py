from benchmarks.Benchmark import Benchmark
from prioritizations.Total import Total
from prioritizations.Random import Random
from prioritizations.Additional import Additional
import sys


def main():
    benchmarks = []
    # read all input and create benchmarks for us
    with open(sys.argv[1]) as f:
        for line in f:
            benchmarks.append(Benchmark(sys.argv[2], line))
            break
    # print or run all benchmarks from here
    for (x, benchmark) in enumerate(benchmarks):
        random = Random(benchmark.results)
        total = Total(benchmark.results)
        #print branch.results
        # random = Random(benchmark.results)
        break
        ###
        # print benchmark
        ###

if __name__ == "__main__":
    main()
