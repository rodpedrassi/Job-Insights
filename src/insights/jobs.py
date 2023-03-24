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
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError


if __name__ == "__main__":
    jobs = read("data/jobs.csv")
    job_types = get_unique_job_types("data/jobs.csv")
    print(job_types)
