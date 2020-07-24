import unittest
from smnsr.patients import TADPOLEData
from smnsr.patients import create_features
import psutil
import ray


class TestTimeseriesCreation(unittest.TestCase):

    data = TADPOLEData()
    MODALITIES = ["cognitive2"]

    def test_create_features(self):
        ray.init(num_cpus=psutil.cpu_count(logical=False), ignore_reinit_error=True)
        ptids = self.data.get_ptids()
        timeseries_features, knn_models = create_features(
            self.data, ptids, [], modalities=self.MODALITIES
        )
        self.assertIsNotNone(timeseries_features)
        self.assertTrue(set(timeseries_features.keys()), set(self.MODALITIES))
