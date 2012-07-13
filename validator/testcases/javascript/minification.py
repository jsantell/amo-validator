import pickle

from pybrain.datasets import SupervisedDataSet

data = SupervisedDataSet(4, 1)
data.addSample(( 0.0935, 0.0341, 0.0322, 0.0308 , ), [0])
data.addSample(( 0.0691, 0.0269, 0.0331, 0.0 , ), [0])
data.addSample(( 0.1122, 0.0379, 0.0309, 0.0275 , ), [0])
data.addSample(( 0.2212, 0.0006, 0.0253, 0.021 , ), [0])
data.addSample(( 0.2618, 0.0127, 0.0274, 0.0052 , ), [0])
data.addSample(( 0.0809, 0.0376, 0.0294, 0.025 , ), [0])
data.addSample(( 0.0131, 0.0011, 0.0014, 0.0 , ), [0])
data.addSample(( 0.1832, 0.0214, 0.0283, 0.0118 , ), [0])
data.addSample(( 0.0493, 0.1161, 0.0372, 0.0369 , ), [0])
data.addSample(( 0.0727, 0.1126, 0.0327, 0.0311 , ), [0])
data.addSample(( 0.1979, 0.0, 0.0287, 0.0198 , ), [0])
data.addSample(( 0.0798, 0.0003, 0.0005, 0.0003 , ), [0])
data.addSample(( 0.0792, 0.0838, 0.026, 0.0247 , ), [0])
data.addSample(( 0.0676, 0.0619, 0.0272, 0.0245 , ), [0])
data.addSample(( 0.0675, 0.0803, 0.0334, 0.0323 , ), [0])
data.addSample(( 0.2361, 0.0094, 0.0301, 0.0292 , ), [0])
data.addSample(( 0.1286, 0.0, 0.0286, 0.0236 , ), [0])
data.addSample(( 0.2691, 0.0007, 0.0213, 0.0202 , ), [0])
data.addSample(( 0.1051, 0.0001, 0.0274, 0.0257 , ), [0])
data.addSample(( 0.07, 0.0429, 0.0221, 0.0214 , ), [0])
data.addSample(( 0.0657, 0.0441, 0.0216, 0.0211 , ), [0])
data.addSample(( 0.0364, 0.0571, 0.0249, 0.023 , ), [0])
data.addSample(( 0.0592, 0.0948, 0.0451, 0.0438 , ), [0])
data.addSample(( 0.1582, 0.0118, 0.0312, 0.0287 , ), [0])
data.addSample(( 0.1365, 0.0, 0.0252, 0.0188 , ), [0])
data.addSample(( 0.058, 0.0275, 0.023, 0.018 , ), [0])
data.addSample(( 0.146, 0.0666, 0.0359, 0.0028 , ), [0])
data.addSample(( 0.0867, 0.0766, 0.0397, 0.0389 , ), [0])
data.addSample(( 0.0845, 0.0303, 0.0348, 0.0235 , ), [0])
data.addSample(( 0.0549, 0.0839, 0.0305, 0.0297 , ), [0])
data.addSample(( 0.0621, 0.0819, 0.0337, 0.0044 , ), [0])
data.addSample(( 0.0723, 0.0, 0.0335, 0.0295 , ), [0])
data.addSample(( 0.0529, 0.087, 0.0326, 0.0015 , ), [0])
data.addSample(( 0.0228, 0.0589, 0.0276, 0.0234 , ), [0])
data.addSample(( 0.0289, 0.0541, 0.0272, 0.0267 , ), [0])
data.addSample(( 0.063, 0.049, 0.0208, 0.0197 , ), [0])
data.addSample(( 0.0886, 0.0773, 0.04, 0.0392 , ), [0])
data.addSample(( 0.0463, 0.094, 0.0305, 0.0293 , ), [0])
data.addSample(( 0.0691, 0.0146, 0.0277, 0.0247 , ), [0])
data.addSample(( 0.0157, 0.002, 0.0013, 0.0011 , ), [0])
data.addSample(( 0.0495, 0.0553, 0.0343, 0.0337 , ), [0])
data.addSample(( 0.0797, 0.0309, 0.0296, 0.0 , ), [0])

data.addSample(( 0.0142, 0.0, 0.0023, 0.0 , ), [1])
data.addSample(( 0.0044, 0.0002, 0.0002, 0.0 , ), [1])
data.addSample(( 0.0076, 0.0, 0.0001, 0.0 , ), [1])
data.addSample(( 0.0257, 0.0, 0.0025, 0.0 , ), [1])
data.addSample(( 0.0044, 0.0002, 0.0, 0.0 , ), [1])
data.addSample(( 0.0046, 0.0002, 0.0, 0.0 , ), [1])
data.addSample(( 0.0044, 0.0002, 0.0, 0.0 , ), [1])
data.addSample(( 0.0143, 0.0, 0.0001, 0.0 , ), [1])
data.addSample(( 0.0044, 0.0002, 0.0, 0.0 , ), [1])
data.addSample(( 0.0159, 0.0001, 0.0001, 0.0 , ), [1])
data.addSample(( 0.0169, 0.0, 0.0055, 0.0 , ), [1])
data.addSample(( 0.0044, 0.0002, 0.0, 0.0 , ), [1])
data.addSample(( 0.013, 0.0, 0.0, 0.0 , ), [1])
data.addSample(( 0.0044, 0.0002, 0.0, 0.0 , ), [1])


try:
    with open("minification_network.brain") as f:
        net = pickle.load(f)
except IOError:
    from pybrain.tools.shortcuts import buildNetwork
    net = buildNetwork(4, 16, 1, bias=True)

    from pybrain.supervised.trainers import BackpropTrainer
    trainer = BackpropTrainer(net, learningrate=0.01, momentum=0.99)
    trainer.trainOnDataset(data, 1000)
    trainer.testOnData()

    with open("minification_network.brain", "w") as f:
        pickle.dump(net, f)


def is_minified(script):
    length = len(script)
    data = (script.count(" ") / length,
            script.count("\t") / length,
            script.count("\n") / length,
            script.count("\r") / length, )
    return net.activate(data)

