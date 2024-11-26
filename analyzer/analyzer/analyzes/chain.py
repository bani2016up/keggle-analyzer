from typing import Any
import pandas as pd
from .abc_analyze import ABCAnalyze
from schemas import ResultModel, ErrorModel, SuccessModel
import time

class AnalyzesChain:


    def __init__(self, init_data: pd.DataFrame):
        self.data: pd.DataFrame = init_data
        self.analyses: list[ABCAnalyze] = []

        self._results: ResultModel = ResultModel(status="not_executed", error=None, results=[])
        self._is_complied = False

    @property
    def is_complied(self) -> bool:
        return self._is_complied

    @is_complied.setter
    def is_complied(self, value: Any):
        raise PermissionError("is_complied property is read-only")

    @property
    def results(self) -> ResultModel:
        return self._results

    @results.setter
    def results(self, value: Any):
        raise PermissionError("results property is read-only")

    def add_analysis(self, analysis: ABCAnalyze):
        self.analyses.append(analysis)

    def perform_analyses(self):
        step = 1
        for analysis in self.analyses:
            start = time.time()
            try:
                analysis.perform()
                step += 1
            except Exception as e:
                end = time.time()
                self._results.error = ErrorModel(msg=str(e), step=step, analyze_type=type(analysis).__name__, exec_time=end - start)
                self._results.status = "error"
                break
            end = time.time()
            self._results.results.append(SuccessModel(msg=f"Analysis {type(analysis).__name__} completed successfully.", exec_time=end - start))
