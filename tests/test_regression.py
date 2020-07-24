from unittest import TestCase
from smnsr.models import SMNSR
from smnsr.patients import AugmentedTADPOLEData, TADPOLEData
import pandas as pd
import pandas as pd
import numpy as np


class TestSNSR(TestCase):

    TS_FILE = "merged_0.p"
    MODALITY = "cognitive1"
    DUMP_PATH = "../output/"
    MODALITY_PATH = "../modalities/"
    TARGET = "ADAS13"
    tadpole_data = TADPOLEData(modality_k=2)
    data = AugmentedTADPOLEData(
        tadpole_data, DUMP_PATH + TS_FILE, tadpole_data.get_ptids()
    )
    FORECAST_STEP_SIZE = 6
    FORECAST_DISTANCE = 120
    D1_D2_FILE = "TADPOLE_D1_D2.csv"

    def __forecast_test(self, x, forecast_start="2018-01-01"):
        model = SMNSR(
            self.data, training_cv_folds=2, mode="bypass_knnsr", forecast=True
        )
        model.fit(self.data.get_ptids())
        y_hat = model.predict(
            x.tail(10),
            self.TARGET,
            forecast_start=forecast_start,
            forecast_end="2022-12-01",
        )

        self.assertIsNotNone(y_hat)
        self.assertTrue(y_hat.shape[0] > 0)

    def test_forecast(self, baseline="last"):
        x = self.data.get_ptids()[0:100]
        n_patients = len(x)
        n_predicted_points = int(self.FORECAST_DISTANCE / self.FORECAST_STEP_SIZE)
        model = SMNSR(
            self.data,
            training_cv_folds=2,
            mode="bypass_knnsr",
            forecast=True,
            baseline=baseline,
        )
        model.fit(self.data.get_ptids())
        y_hat = model.predict(x, self.TARGET)

        self.assertIsNotNone(y_hat)
        self.assertTrue(y_hat.shape[0] > 0)

        self.assertTrue(y_hat.shape[0] == n_patients * n_predicted_points)

    def test_forecast_on_df(self):
        x: pd.DataFrame = pd.read_csv(
            self.MODALITY_PATH + self.D1_D2_FILE, low_memory=False
        )
        x = x.groupby(TADPOLEData.PTID).tail(1)
        self.__forecast_test(x)

    def test_forecast_on_df_to_date(self):
        x: pd.DataFrame = pd.read_csv(
            self.MODALITY_PATH + self.D1_D2_FILE, low_memory=False
        )
        x = x.groupby(TADPOLEData.PTID).tail(10)
        x = self.tadpole_data.df_raw
        self.__forecast_test(x, forecast_start="2020-12-01")

    def test_forecast_on_df_3(self):

        x: pd.DataFrame = pd.read_csv(self.MODALITY_PATH + self.D3, low_memory=False)
        x[TADPOLEData.PTID] = self.data.data.rids_to_ptids(x[TADPOLEData.RID])
        x = x.iloc[0:100, :]
        self.__forecast_test(x)
