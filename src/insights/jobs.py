from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as csvfile:
        jobs = list(csv.DictReader(csvfile))
        return jobs


def get_unique_job_types(path: str) -> List[str]:
    jobs = read(path)
    all_jobs_types = set()
    for job in jobs:
        all_jobs_types.add(job["job_type"])
    return list(all_jobs_types)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobs_by_type = [job for job in jobs if job["job_type"] == job_type]
    return jobs_by_type


if __name__ == "__main__":
    jobs = read("data/jobs.csv")
    job_types = get_unique_job_types("data/jobs.csv")
    jobs_by_type = filter_by_job_type(jobs, "FULL_TIME")
    print(jobs_by_type)
