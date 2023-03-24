from typing import Union, List, Dict

from src.insights.jobs import (
    read,
)

# from jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    salaries = [
        int(job["max_salary"]) for job in jobs if job["max_salary"].isdigit()
    ]
    return max(salaries)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    salaries = [
        int(job["min_salary"]) for job in jobs if job["min_salary"].isdigit()
    ]
    return min(salaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salary = int(salary)
        # Quando tem erro de tipos 1 / '2'
    except TypeError:
        raise ValueError
        # Erro ao acessar uma chave que não existe (caso job venha sem as keys)
    except KeyError:
        raise ValueError
    else:
        if min_salary > max_salary:
            raise ValueError
        return min_salary <= salary <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    filtered_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_list.append(job)
        except ValueError:
            continue
    return filtered_list


if __name__ == "__main__":
    jobs = read("data/jobs.csv")
    maxSalary = get_max_salary("data/jobs.csv")
    minSalary = get_min_salary("data/jobs.csv")
    filtered_jobs = filter_by_salary_range(jobs, 5000)
    a = [1, 2, 3, 4]
    print(filtered_jobs)
