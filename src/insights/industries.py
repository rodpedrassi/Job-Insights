from typing import List, Dict
from src.insights.jobs import (
    read,
)

# from jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    all_industries = set()
    for job in jobs:
        if job["industry"] != "":
            all_industries.add(job["industry"])
    return list(all_industries)


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError


if __name__ == "__main__":
    job_industries = get_unique_industries("data/jobs.csv")
    print(job_industries)
