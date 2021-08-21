import abc

class MachineLearningModel:
    @abc.abstractmethod
    def predict(self, input):
        raise NotImplementedError("Implement your sound!")


class CustomClassifier(MachineLearningModel):
    def predict(self, input):
        print("Cool ML stuff happening...")
