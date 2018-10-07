import numpy as np
import json

class PreprocessData():
    def __init__(self, value):
        self.value = value
        self.executeProcessing()

        return self.value

    def doFFT(self):
        if "data" not in self.value.keys():
            print("No data to do FFT on. Returning....")
            return
        rawSequenceString = self.value["data"]
	rawSequence = json.loads(rawSequenceString)
        fftSequence = np.fft.fft(rawSequence)

        self.value["data"] = fftSequence

    def executeProcessing(self):
        self.doFFT()
