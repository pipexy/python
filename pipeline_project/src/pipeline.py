import grpc
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class PipelineStep:
    service_url: str
    output_format: str

class Pipeline:
    def __init__(self):
        self.input_url: Optional[str] = None
        self.output_url: Optional[str] = None
        self.steps: List[PipelineStep] = []

    def input(self, url: str) -> 'Pipeline':
        self.input_url = url
        return self

    def data(self, service_url: str, output_format: str) -> 'Pipeline':
        self.steps.append(PipelineStep(service_url, output_format))
        return self

    def output(self, url: str) -> 'Pipeline':
        self.output_url = url
        return self

class PipelineExecutor:
    def __init__(self, pipeline: Pipeline):
        self.pipeline = pipeline

    def execute(self):
        try:
            # Process input
            data = self._read_input()

            # Execute pipeline steps
            for step in self.pipeline.steps:
                data = self._execute_step(step, data)

            # Write output
            self._write_output(data)

        except Exception as e:
            raise RuntimeError(f"Pipeline execution failed: {str(e)}")

    def _read_input(self):
        # TODO: Implement input reading based on URL type
        pass

    def _execute_step(self, step: PipelineStep, data):
        # TODO: Implement step execution using gRPC
        pass

    def _write_output(self, data):
        # TODO: Implement output writing based on URL type
        pass
