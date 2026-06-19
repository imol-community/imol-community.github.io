# Adding Job Openings

To suggest a new job opening, please open a pull request and edit `src/pages/jobs.md`.

Jobs are grouped by section:

- `PhD`
- `Postdoc`
- `Internships`
- `Full-time`

Add each position as an `<article class="job-card">` below the relevant heading.

Use this format:

```html
<article class="job-card">
  <h4>Position title</h4>

  <dl class="job-details">
    <div>
      <dt>Institution</dt>
      <dd>Institution name</dd>
    </div>
    <div>
      <dt>Location</dt>
      <dd>City, country, remote possibility</dd>
    </div>
    <div>
      <dt>Duration</dt>
      <dd>Duration of the contract</dd>
    </div>
    <div>
      <dt>Start date</dt>
      <dd>Starting date</dd>
    </div>
    <div>
      <dt>Salary</dt>
      <dd>Salary or salary range, if public</dd>
    </div>
    <div>
      <dt>More info</dt>
      <dd>here</dd>
    </div>
  </dl>

  <!-- Please give an expiration date for this position in this comment: YYYY-MM-DD -->

  <p><b>Job description</b></p>
  <p>Full job description goes here.</p>

  <p><b>Full project description & application instructions:</b> here</p>
</article>
```
