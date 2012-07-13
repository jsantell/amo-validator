import os
import sys

for root, dirs, files in os.walk(sys.argv[1]):
    for filename in files:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            root, filename)
        with open(path) as f:
            data = f.read()
            ct = float(len(data))

            results = [data.count(" ") / ct,
                       data.count("\t") / ct,
                       data.count("\n") / ct,
                       data.count("\r") / ct]
            results = map(lambda x: round(x, 4), results)
            results = map(str, results)
            print "data.addSample((", ", ".join(results), ", ), [%s])" % \
                       sys.argv[2]
