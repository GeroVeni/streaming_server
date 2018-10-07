import numpy as np
import json

class PreprocessData():
    def __init__(self, value):
        self.value = value
        self.executeProcessing()



    def doFFT(self):
        if "data" not in self.value.keys():
            print("No data to do FFT on. Returning....")
            noDataMessage = {"Message": "No data to do FFT on"}
            return noDataMessage
        rawSequenceString = self.value["data"]
        rawSequence = json.loads(rawSequenceString)
        fftSequence = np.fft.fft(rawSequence)

        self.value["data"] = fftSequence

    def executeProcessing(self):
        self.doFFT()

        # Return the value
        return self.value

