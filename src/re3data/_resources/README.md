# Resource Generation

The dataclasses in `_resources` were primarily generated using
[xsdata](https://xsdata.readthedocs.io/en/v24.5/codegen/intro/).

## `RepositoryList` and `RepositorySummary` (/repositories)

To generate the list resources, we used the following commands:

```console
python -m pip install ".[cli]" "xsdata[cli]"
re3data repository list --return-type=xml > repository_list.xml
xsdata generate --config=src/re3data/_resources/.repository_list.xml repository_list.xml
```

The `ListType` was renamed to `RepositoryList`, and the `Repository` resource from the `/repository/{id}` endpoint was
renamed to `RepositorySummary` to avoid name collisions. The `RepositorySummary` includes only 4 fields, compared to the
original 20+ fields.

To make it more convenient to access the link's href attribute, a mixin class was added to the `RepositorySummary`.

Here's an example:

```pycon
>>> repository_summary = re3data.repositories.list()[0]
>>> repository_summary.link.href
'https://www.re3data.org/api/beta/repository/r3d100010468'
>>> repository_summary.href # for convenience
'https://www.re3data.org/api/beta/repository/r3d100010468'
```

## `Re3data` and `Repository` (/repository/{id})

To generate these resources, we used:

```console
xsdata generate --config=src/re3data/_resources/.repository.xml http://schema.re3data.org/2-2/re3dataV2-2.xsd
```

The original XSD file had a lot of nesting, which would have been translated to multiple layers of nested classes.
Instead, the dataclasses were unnested and renamed accordingly.

To make it more convenient to access the identifier attribute, a mixin class was added to the `Repository`.

Here's an example:

```pycon
>>> repository = re3data.repositories.get("r3d100010468")
>>> repository.re3data_org_identifier
'r3d100010468'
>>> repository.id # for convenience
'r3d100010468'
```

### Changes from Original XML Schema

This section highlights the differences between the original XML Schema and the data returned from the API. While the
schema provides a clear structure, the actual data may not always conform to it.

For instance, the size element in the schema has an attribute called `updated` with a type of `dateFormat`, but this is
not consistently reflected in the API responses.

```xsd
<xs:element name="size" msdata:Prefix="r3d" minOccurs="0" maxOccurs="1">
  <xs:annotation>
    <xs:documentation>
      The number of items contained in the research data repository.
    </xs:documentation>
  </xs:annotation>
  <xs:complexType>
    <xs:simpleContent>
      <xs:extension base="xs:string">
        <xs:attribute name="updated" msdata:Prefix="r3d" type="dateFormat" use="required" form="unqualified">
          <xs:annotation>
            <xs:documentation>
              The date of the last update of the research data repository size.
            </xs:documentation>
          </xs:annotation>
        </xs:attribute>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
</xs:element>
```

For instance, a repository with an "updated" value of `""` led to `ConverterWarnings`, indicating that the data did not
fully adhere to the schema's expectations.

```xml
<size updated="" />
```

```console
ConverterWarning: Failed to convert value `` to one of (<class 'xsdata.models.datatype.XmlDate'>, <class 'xsdata.models.datatype.XmlPeriod'>)
```

To resolve this issue, we manually added support for accepting `str` types, allowing the API responses to be processed
correctly.

```python
class Size:
    ...
    updated: None | XmlPeriod | XmlDate | str  # str added manually
    ...
```

Similarly, adjustments were made to various date-related elements in the XML responses (`start_date`, `end_date`,
`responsibility_start_date`, `responsibility_end_date`), ensuring a smoother conversion process and minimizing potential
errors.

Additionally, the `softwareNames` type in the schema was defined as having the value `DataVerse`, but the API returned
`Dataverse` instead - note the difference: the schema's capitalization ("V") versus the API's lowercase ("v"). To ensure
consistency, we manually corrected the spelling to match the expected format.

```xsd
<xs:simpleType name="softwareNames">
  <xs:restriction base="xs:string">
    <xs:enumeration value="CKAN"/>
    <xs:enumeration value="DataVerse"/>
    ...
  </xs:restriction>
</xs:simpleType>
```

```python
class SoftwareNames(Enum):
    ...
    DATA_VERSE = "Dataverse"  # lowercase v
    ...
```
