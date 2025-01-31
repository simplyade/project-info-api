Project Info API Documentation

Endpoints
*GET /project-info*
Returns project information in JSON format.

*Response*

| Field            | Type   | Description                             |
| :---------------- | :----- | :-------------------------------------- |
| project_description | string | A brief description of the project.  |
| api_documentation  | object | API documentation metadata.          |
| job_posting        | string | A link to the job posting.           |

*Example Response*

```
{
  "project_description": "This is a simple API that provides information about a project.",
  "api_documentation": {
    "endpoint_url": "https://api.example.com/project-info",
    "request_format": "None",
    "response_format": "JSON"
  },
  "job_posting": "https://hng.tech/hire/python-developers"
}
