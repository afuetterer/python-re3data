import pytest
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser

from re3data._resources import Re3Data, Repository, RepositoryList, RepositoryName, RepositorySummary

CONTEXT = XmlContext()
PARSER = XmlParser(context=CONTEXT)


@pytest.fixture
def repository_list(repository_list_xml: str) -> RepositoryList:
    return PARSER.from_string(repository_list_xml, RepositoryList)


@pytest.fixture
def repository_summary(repository_list: RepositoryList) -> RepositorySummary:
    return repository_list.repository[0]


def test_repository_list(repository_list: RepositoryList) -> None:
    assert isinstance(repository_list, RepositoryList)
    repositories = repository_list.repository
    assert isinstance(repositories, list)
    assert len(repositories) == 3


def test_repository_summary(repository_summary: RepositorySummary) -> None:
    assert isinstance(repository_summary, RepositorySummary)
    assert repository_summary.id == "r3d100010371"
    assert repository_summary.doi == "https://doi.org/10.17616/R3P594"
    assert repository_summary.name == "ZACAT"
    assert repository_summary.href == "https://www.re3data.org/api/beta/repository/r3d100010371"


def test_repository_summary_mixin(repository_summary: RepositorySummary) -> None:
    repository_summary.link = None
    assert repository_summary.href is None


@pytest.fixture(scope="session")
def repository(repository_get_xml: str) -> Repository:
    return PARSER.from_string(repository_get_xml, Re3Data).repository[0]


def test_repository(repository: Repository, zenodo_id: str) -> None:
    assert repository.id == zenodo_id
    assert repository.re3data_org_identifier == zenodo_id
    assert isinstance(repository.repository_name, RepositoryName)
    assert repository.repository_name.value == "Zenodo"
