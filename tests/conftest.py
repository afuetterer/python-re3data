# SPDX-FileCopyrightText: 2024 Heinz-Alexander Fütterer
#
# SPDX-License-Identifier: MIT

from __future__ import annotations

from typing import TYPE_CHECKING

import httpx
import pytest

from re3data import AsyncClient, Client

if TYPE_CHECKING:
    from respx import MockRouter, Route


@pytest.fixture(scope="session")
def vcr_config() -> dict[str, str]:
    return {"cassette_library_dir": "tests/cassettes"}


@pytest.fixture(scope="session")
def client() -> Client:
    return Client()


@pytest.fixture(scope="session")
def async_client() -> AsyncClient:
    return AsyncClient()


@pytest.fixture(scope="session")
def zenodo_id() -> str:
    # Ref: https://www.re3data.org/repository/r3d100010468
    return "r3d100010468"


@pytest.fixture(scope="session")
def repository_list_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
        <list>
            <repository>
                <id>r3d100010371</id>
                <doi>https://doi.org/10.17616/R3P594</doi>
                <name>ZACAT</name>
                <link href="https://www.re3data.org/api/beta/repository/r3d100010371" rel="self"/>
            </repository>
            <repository>
                <id>r3d100010376</id>
                <doi>https://doi.org/10.17616/R31G7K</doi>
                <name>Land Processes Distributed Active Archive Center</name>
                <link href="https://www.re3data.org/api/beta/repository/r3d100010376" rel="self"/>
            </repository>
            <repository>
                <id>r3d100010829</id>
                <doi>https://doi.org/10.17616/R3TW4Q</doi>
                <name>India Water Portal</name>
                <link href="https://www.re3data.org/api/beta/repository/r3d100010829" rel="self"/>
            </repository>
        </list>
        """


@pytest.fixture()
def mock_repository_list_route(respx_mock: MockRouter, repository_list_xml: str) -> Route:
    return respx_mock.get("https://www.re3data.org/api/beta/repositories").mock(
        return_value=httpx.Response(httpx.codes.OK, text=repository_list_xml)
    )


REPOSITORY_GET_XML: str = """<?xml version="1.0" encoding="utf-8"?>
<!--re3data.org Schema for the Description of Research
Data Repositories. Version 2.2, December 2014. doi:10.2312/re3.006-->
<r3d:re3data xmlns:r3d="http://www.re3data.org/schema/2-2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.re3data.org/schema/2-2 http://schema.re3data.org/2-2/re3dataV2-2.xsd">
  <r3d:repository>
    <r3d:re3data.orgIdentifier>r3d100010468</r3d:re3data.orgIdentifier>
    <r3d:repositoryName language="eng">Zenodo</r3d:repositoryName>
    <r3d:repositoryURL>https://zenodo.org/</r3d:repositoryURL>
    <r3d:repositoryIdentifier>FAIRsharing_doi:10.25504/FAIRsharing.wy4egf</r3d:repositoryIdentifier>
    <r3d:repositoryIdentifier>RRID:SCR_004129</r3d:repositoryIdentifier>
    <r3d:repositoryIdentifier>RRID:nlx_158614</r3d:repositoryIdentifier>
    <r3d:description language="eng">ZENODO builds and operates a simple and innovative service that
      enables researchers, scientists, EU projects and institutions to share and showcase
      multidisciplinary research results (data and publications) that are not part of the existing
      institutional or subject-based repositories of the research communities.
      ZENODO enables researchers, scientists, EU projects and institutions to:
      easily share the long tail of small research results in a wide variety of formats including
      text, spreadsheets, audio, video, and images across all fields of science.
      display their research results and get credited by making the research results citable and
      integrate them into existing reporting lines to funding agencies like the European Commission.
      easily access and reuse shared research results.</r3d:description>
    <r3d:repositoryContact>https://zenodo.org/contact</r3d:repositoryContact>
    <r3d:repositoryContact>info@zenodo.org</r3d:repositoryContact>
    <r3d:type>other</r3d:type>
    <r3d:size updated="2023-04-26">2.916.709 results</r3d:size>
    <r3d:startDate>2013-05-08</r3d:startDate>
    <r3d:endDate></r3d:endDate>
    <r3d:repositoryLanguage>eng</r3d:repositoryLanguage>
    <r3d:subject subjectScheme="DFG">1 Humanities and Social Sciences</r3d:subject>
    <r3d:subject subjectScheme="DFG">2 Life Sciences</r3d:subject>
    <r3d:subject subjectScheme="DFG">3 Natural Sciences</r3d:subject>
    <r3d:subject subjectScheme="DFG">4 Engineering Sciences</r3d:subject>
    <r3d:missionStatementURL>https://about.zenodo.org/</r3d:missionStatementURL>
    <r3d:contentType contentTypeScheme="parse">Archived data</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Audiovisual data</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Images</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Networkbased data</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Plain text</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Raw data</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Scientific and statistical data formats</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Source code</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Standard office documents</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Structured graphics</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">Structured text</r3d:contentType>
    <r3d:contentType contentTypeScheme="parse">other</r3d:contentType>
    <r3d:providerType>dataProvider</r3d:providerType>
    <r3d:keyword>FAIR</r3d:keyword>
    <r3d:keyword>multidisciplinary</r3d:keyword>
    <r3d:institution>
      <r3d:institutionName language="eng">European Commission, Horizon 2020</r3d:institutionName>
      <r3d:institutionCountry>EEC</r3d:institutionCountry>
      <r3d:responsibilityType>funding</r3d:responsibilityType>
      <r3d:institutionType>non-profit</r3d:institutionType>
      <r3d:institutionURL>
        https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en
      </r3d:institutionURL>
      <r3d:responsibilityStartDate>2014</r3d:responsibilityStartDate>
      <r3d:responsibilityEndDate>2020</r3d:responsibilityEndDate>
      <r3d:institutionContact>https://research-and-innovation.ec.europa.eu/contact-us_en</r3d:institutionContact>
    </r3d:institution>
    <r3d:institution>
      <r3d:institutionName language="eng">European Commission, Research &amp; Innovation, Seventh Framework Programm - FP7</r3d:institutionName>
      <r3d:institutionAdditionalName language="eng">FP7</r3d:institutionAdditionalName>
      <r3d:institutionCountry>EEC</r3d:institutionCountry>
      <r3d:responsibilityType>funding</r3d:responsibilityType>
      <r3d:institutionType>non-profit</r3d:institutionType>
      <r3d:institutionURL>https://commission.europa.eu/research-and-innovation_en</r3d:institutionURL>
      <r3d:responsibilityStartDate></r3d:responsibilityStartDate>
      <r3d:responsibilityEndDate></r3d:responsibilityEndDate>
      <r3d:institutionContact>https://research-and-innovation.ec.europa.eu/contact-us_en</r3d:institutionContact>
    </r3d:institution>
    <r3d:institution>
      <r3d:institutionName language="eng">European Organization for Nuclear Research</r3d:institutionName>
      <r3d:institutionAdditionalName language="fra">CERN</r3d:institutionAdditionalName>
      <r3d:institutionAdditionalName language="fra">Centre Européen pour la Recherche Nucléaire</r3d:institutionAdditionalName>
      <r3d:institutionCountry>EEC</r3d:institutionCountry>
      <r3d:responsibilityType>funding</r3d:responsibilityType>
      <r3d:responsibilityType>general</r3d:responsibilityType>
      <r3d:responsibilityType>technical</r3d:responsibilityType>
      <r3d:institutionType>non-profit</r3d:institutionType>
      <r3d:institutionURL>https://home.cern/</r3d:institutionURL>
      <r3d:institutionIdentifier>ROR:01ggx4157</r3d:institutionIdentifier>
      <r3d:responsibilityStartDate></r3d:responsibilityStartDate>
      <r3d:responsibilityEndDate></r3d:responsibilityEndDate>
      <r3d:institutionContact>https://about.zenodo.org/contact/</r3d:institutionContact>
    </r3d:institution>
    <r3d:institution>
      <r3d:institutionName language="eng">OpenAIRE</r3d:institutionName>
      <r3d:institutionAdditionalName language="eng">Open Access Infrastructure for Research in Europa</r3d:institutionAdditionalName>
      <r3d:institutionCountry>EEC</r3d:institutionCountry>
      <r3d:responsibilityType>funding</r3d:responsibilityType>
      <r3d:responsibilityType>general</r3d:responsibilityType>
      <r3d:institutionType>non-profit</r3d:institutionType>
      <r3d:institutionURL>https://www.openaire.eu/</r3d:institutionURL>
      <r3d:institutionIdentifier>ROR:019kf3481</r3d:institutionIdentifier>
      <r3d:institutionIdentifier>RRID:SCR_013740</r3d:institutionIdentifier>
      <r3d:responsibilityStartDate></r3d:responsibilityStartDate>
      <r3d:responsibilityEndDate></r3d:responsibilityEndDate>
      <r3d:institutionContact>https://www.openaire.eu/contact-us</r3d:institutionContact>
    </r3d:institution>
    <r3d:policy>
      <r3d:policyName>Policies</r3d:policyName>
      <r3d:policyURL>https://about.zenodo.org/policies/</r3d:policyURL>
    </r3d:policy>
    <r3d:policy>
      <r3d:policyName>Terms of use</r3d:policyName>
      <r3d:policyURL>https://about.zenodo.org/terms/</r3d:policyURL>
    </r3d:policy>
    <r3d:databaseAccess>
      <r3d:databaseAccessType>open</r3d:databaseAccessType>
    </r3d:databaseAccess>
    <r3d:databaseLicense>
      <r3d:databaseLicenseName>CC0</r3d:databaseLicenseName>
      <r3d:databaseLicenseURL>https://creativecommons.org/publicdomain/zero/1.0/</r3d:databaseLicenseURL>
    </r3d:databaseLicense>
    <r3d:dataAccess>
      <r3d:dataAccessType>closed</r3d:dataAccessType>
    </r3d:dataAccess>
    <r3d:dataAccess>
      <r3d:dataAccessType>embargoed</r3d:dataAccessType>
    </r3d:dataAccess>
    <r3d:dataAccess>
      <r3d:dataAccessType>open</r3d:dataAccessType>
    </r3d:dataAccess>
    <r3d:dataAccess>
      <r3d:dataAccessType>restricted</r3d:dataAccessType>
      <r3d:dataAccessRestriction>registration</r3d:dataAccessRestriction>
    </r3d:dataAccess>
    <r3d:dataLicense>
      <r3d:dataLicenseName>CC</r3d:dataLicenseName>
      <r3d:dataLicenseURL>https://creativecommons.org/</r3d:dataLicenseURL>
    </r3d:dataLicense>
    <r3d:dataLicense>
      <r3d:dataLicenseName>CC0</r3d:dataLicenseName>
      <r3d:dataLicenseURL>https://creativecommons.org/publicdomain/zero/1.0/</r3d:dataLicenseURL>
    </r3d:dataLicense>
    <r3d:dataLicense>
      <r3d:dataLicenseName>other</r3d:dataLicenseName>
      <r3d:dataLicenseURL>https://about.zenodo.org/policies/</r3d:dataLicenseURL>
    </r3d:dataLicense>
    <r3d:dataUpload>
      <r3d:dataUploadType>restricted</r3d:dataUploadType>
      <r3d:dataUploadRestriction>registration</r3d:dataUploadRestriction>
    </r3d:dataUpload>
    <r3d:dataUploadLicense>
      <r3d:dataUploadLicenseName>Policies</r3d:dataUploadLicenseName>
      <r3d:dataUploadLicenseURL>https://about.zenodo.org/policies/</r3d:dataUploadLicenseURL>
    </r3d:dataUploadLicense>
    <r3d:software>
      <r3d:softwareName>other</r3d:softwareName>
    </r3d:software>
    <r3d:versioning>yes</r3d:versioning>
    <r3d:api apiType="OAI-PMH">https://zenodo.org/oai2d</r3d:api>
    <r3d:api apiType="REST">https://developers.zenodo.org/</r3d:api>
    <r3d:pidSystem>DOI</r3d:pidSystem>
    <r3d:citationGuidelineURL>https://about.zenodo.org/</r3d:citationGuidelineURL>
    <r3d:aidSystem>ORCID</r3d:aidSystem>
    <r3d:enhancedPublication>yes</r3d:enhancedPublication>
    <r3d:qualityManagement>no</r3d:qualityManagement>
    <r3d:metadataStandard>
      <r3d:metadataStandardName metadataStandardScheme="DCC">DataCite Metadata Schema</r3d:metadataStandardName>
      <r3d:metadataStandardURL>
        http://www.dcc.ac.uk/resources/metadata-standards/datacite-metadata-schema</r3d:metadataStandardURL>
    </r3d:metadataStandard>
    <r3d:metadataStandard>
      <r3d:metadataStandardName metadataStandardScheme="DCC">Dublin Core</r3d:metadataStandardName>
      <r3d:metadataStandardURL>http://www.dcc.ac.uk/resources/metadata-standards/dublin-core</r3d:metadataStandardURL>
    </r3d:metadataStandard>
    <r3d:remarks>Zenodo is covered by Thomson Reuters Data Citation Index. Zenodo uses Altmetric metrics and provides
      impact information in the form of software citations (15.01.2019). Zenodo uses invenio repository software.
      OpenAIRE Orphan Record Repository got a make-over and was re-branded as ZENODO. Zenodo uses Invenio repository
      software. ZENODO was launched within the OpenAIREplus project as part of a European-wide research infrastructure.
      Easy upload and semi-automatic metadata completion by communication with existing online services such as
      DropBox for upload, Mendeley/ORCID/CrossRef/OpenAIRE for upload and pre-filling metadata.
    </r3d:remarks>
    <r3d:entryDate>2013-06-13</r3d:entryDate>
    <r3d:lastUpdate>2023-04-26</r3d:lastUpdate>
  </r3d:repository>
</r3d:re3data>
"""


@pytest.fixture(scope="session")
def repository_get_xml() -> str:
    return REPOSITORY_GET_XML


@pytest.fixture()
def mock_repository_get_route(respx_mock: MockRouter) -> Route:
    return respx_mock.get("https://www.re3data.org/api/beta/repository/r3d100010468").mock(
        return_value=httpx.Response(httpx.codes.OK, text=REPOSITORY_GET_XML)
    )


@pytest.fixture()
def mock_server_error(respx_mock: MockRouter) -> Route:
    return respx_mock.get("https://www.re3data.org/api/beta/repositories").mock(
        return_value=httpx.Response(httpx.codes.INTERNAL_SERVER_ERROR)
    )
