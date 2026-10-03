from datetime import datetime


class PipelineMonitor:

    def __init__(self):
        self.runs = []

    def record_run(
        self,
        pipeline_name,
        run_id,
        status,
        duration_minutes,
        error=None
    ):

        run = {
            "pipeline": pipeline_name,
            "run_id": run_id,
            "status": status,
            "duration_minutes": duration_minutes,
            "error": error,
            "timestamp": datetime.now().isoformat()
        }

        self.runs.append(run)

    def success_rate(self):

        if not self.runs:
            return 0

        successful = sum(
            r["status"] == "SUCCESS"
            for r in self.runs
        )

        return successful / len(self.runs) * 100

    def failed_runs(self):

        return [
            r for r in self.runs
            if r["status"] == "FAILED"
        ]

    def print_report(self):

        print("\nPipeline Monitoring Report")
        print("=" * 40)

        print(
            f"Total Runs: {len(self.runs)}"
        )

        print(
            f"Success Rate: {self.success_rate():.2f}%"
        )

        print(
            f"Failed Runs: {len(self.failed_runs())}"
        )


monitor = PipelineMonitor()

monitor.record_run(
    pipeline_name="SalesDataPipeline",
    run_id="RUN001",
    status="SUCCESS",
    duration_minutes=4
)

monitor.record_run(
    pipeline_name="SalesDataPipeline",
    run_id="RUN002",
    status="FAILED",
    duration_minutes=2,
    error="Invalid amount value"
)

monitor.record_run(
    pipeline_name="SalesDataPipeline",
    run_id="RUN003",
    status="SUCCESS",
    duration_minutes=5
)

monitor.print_report()