import unittest
from smnsr.patients import TADPOLEData
import pandas as pd
import os
import shutil

MODALITY_PATH = "../modalities/"
DUMP_PATH = "../output/"
TMP_PATH = "./tmp/"
TARGET = "ADAS13"
PTIDS = ["011_S_0002", "011_S_0003", "011_S_0003", "011_S_0003", "011_S_0003"]
D3_FILE = "D3.csv"
TEST_PTID = "test_ptid"


class TestTADPOLEWrapper(unittest.TestCase):

    _data = TADPOLEData()

    def test_save_modality(self):
        if not os.path.exists(self.TMP_PATH):
            os.mkdir(self.TMP_PATH)
        self.data.save_modality(self.TMP_PATH)
        self.assertTrue(os.path.exists(self.TMP_PATH))
        if os.path.exists(self.TMP_PATH):
            shutil.rmtree(self.TMP_PATH)

    def test_get_modalities(self):
        modalities = self.data.getModalities()
        self.assertIsNotNone(modalities)
        self.assertTrue(len(modalities) > 0)

    #
    def test_get_xy(self):
        ptids = self.data.get_ptids()
        for modality in self.data.getModalities():
            x, y = self.data.getXY(ptids, modality, TARGET)
            self.assertIsNotNone(x)
            self.assertIsNotNone(y)
            self.assertTrue(x.shape[0] > 0)
            self.assertTrue(y.shape[0] == x.shape[0])

    def test_ridto_ptid(self):
        assert False

    def test_get_ptids(self):
        ptids = self._data.get_modalities()
        self.assertIsNotNone(ptids)
        self.assertTrue(len(ptids) > 0)

    def __create_test_data(self):
        d3_data = pd.read_csv(MODALITY_PATH + D3_FILE)
        d3_data = d3_data.tail(1).copy()
        d3_data[TADPOLEData.PTID] = TEST_PTID
        d3_data[TADPOLEData.C_MONTH] = 0
        return d3_data

    def test_snapshot(self):
        original: pd.DataFrame = self._data._df.copy()
        self._data.snapshopt()
        self.assertTrue(self._data._snapshot_data.equals(original))

    def test_add_measurement(self):
        self._data.snapshopt()
        self._data.add_measurement(self.__create_test_data())
        self.assertTrue(TEST_PTID in self._data.get_ptids())
        self._data.restore()

    def test_restore(self):
        self._data.snapshopt()
        self._data.add_measurement(self.__create_test_data())
        self.assertTrue(TEST_PTID in self._data.get_ptids())
        self._data.restore()
        self.assertFalse(TEST_PTID in self._data.get_ptids())

    def test_distance_to_date(self):
        months = self._data.distance_to_date("011_S_0002", 0, "2015-09-08")
        self.assertEqual(10 * 12, months)
