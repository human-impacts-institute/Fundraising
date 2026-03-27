# Grants Dashboard

<link rel="stylesheet" href="assets/style.css">
<script defer src="assets/refresh-config.js"></script>
<script defer src="assets/refresh.js"></script>
<script defer src="assets/dashboard.js"></script>

Strategic view of funding opportunities, split into two action queues: research and apply.

<!-- DASHBOARD:START -->
<section class="dashboard">
<div class="dashboard-meta">
<button class="refresh-button" type="button">Refresh</button>
<div class="refreshed">Last refreshed: 2026-03-26</div>
</div>
<div class="snapshot">
<div class="card"><div class="card-label">Total funders</div><div class="card-value">317</div></div>
<div class="card"><div class="card-label">Missing deadlines</div><div class="card-value">273</div></div>
<div class="card"><div class="card-label">Missing links</div><div class="card-value">14</div></div>
<div class="card"><div class="card-label">With deadlines</div><div class="card-value">44</div></div>
</div>

<div class="grant-add-section">
  <button class="grant-add-toggle" type="button" aria-expanded="false" aria-controls="grant-add-form">+ Add a grant funder</button>
  <form id="grant-add-form" class="grant-add-form" hidden aria-label="Add a grant funder">
    <div class="form-row">
      <label for="ga-org">Organization name <span class="form-required">*</span></label>
      <input id="ga-org" name="org" type="text" required placeholder="e.g. Ford Foundation" autocomplete="organization">
    </div>
    <div class="form-row">
      <label for="ga-info-url">Information website</label>
      <input id="ga-info-url" name="infoUrl" type="url" placeholder="https://...">
    </div>
    <div class="form-row">
      <label for="ga-app-deadline">Application deadline (MM/DD/YYYY)</label>
      <input id="ga-app-deadline" name="appDeadline" type="text" placeholder="03/31/2027" pattern="\d{1,2}/\d{1,2}/\d{4}">
    </div>
    <div class="form-row">
      <label for="ga-loi-deadline">LOI deadline (MM/DD/YYYY)</label>
      <input id="ga-loi-deadline" name="loiDeadline" type="text" placeholder="02/15/2027" pattern="\d{1,2}/\d{1,2}/\d{4}">
    </div>
    <div class="form-row">
      <label for="ga-priority">Priority</label>
      <select id="ga-priority" name="priority">
        <option value="">-- select --</option>
        <option value="HIGH">HIGH</option>
        <option value="MEDIUM">MEDIUM</option>
        <option value="LOW">LOW</option>
        <option value="Other">Other</option>
      </select>
    </div>
    <div class="form-row form-row--full">
      <label for="ga-notes">Notes</label>
      <textarea id="ga-notes" name="notes" rows="3" placeholder="Any relevant context..."></textarea>
    </div>
    <div class="form-actions">
      <button type="submit" class="form-submit">Add funder</button>
      <span class="form-status" aria-live="polite"></span>
    </div>
  </form>
</div>

<h2 class="queue-title">Review / Research Priority Queue</h2>
<div class="table-wrap">
<table class="dashboard-table">
<thead><tr><th class="col-rank">Rank</th><th>Organization</th><th>Priority</th><th>Next deadline</th><th class="col-programs">Programs</th><th>Links</th><th>Notes</th></tr></thead>
<tbody>
<tr class="priority-high"><td class="col-rank">1</td><td class="col-org">H&amp;M</td><td class="col-priority">HIGH</td><td class="col-deadline"></td><td class="col-programs">7</td><td class="col-links"><a href="https://hmfoundation.com/" target="_blank" rel="noopener">info</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-high"><td class="col-rank">2</td><td class="col-org">Charles Hayden Foundation</td><td class="col-priority">HIGH</td><td class="col-deadline"></td><td class="col-programs">7</td><td class="col-links"><a href="https://charleshaydenfoundation.org/current-grants/" target="_blank" rel="noopener">info</a> <a href="https://us.grantrequest.com/Login.aspx?ReturnUrl=%2fapplication.aspx%3fSA%3dSNA%26FID%3d35002%26sid%3d2345&amp;SA=SNA&amp;FID=35002&amp;sid=2345" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-med"><td class="col-rank">3</td><td class="col-org">IOBY (crowd funding)</td><td class="col-priority">MEDIUM</td><td class="col-deadline"></td><td class="col-programs">7</td><td class="col-links"><a href="https://ioby.org/resources/closing/" target="_blank" rel="noopener">info</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-unknown"><td class="col-rank">4</td><td class="col-org">NYC Venture Philanthropy Fund</td><td class="col-priority">NO</td><td class="col-deadline"></td><td class="col-programs">8</td><td class="col-links"><a href="https://philanthropynewyork.org/redhen/org/113" target="_blank" rel="noopener">info</a> <a href="https://philanthropynewyork.org/search?keys=grants" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-unknown"><td class="col-rank">5</td><td class="col-org">Wege Foundation</td><td class="col-priority">NO</td><td class="col-deadline"></td><td class="col-programs">7</td><td class="col-links"><a href="https://wegefoundation.com/grants/" target="_blank" rel="noopener">info</a> <a href="https://wegefoundation.com/wp-content/uploads/2022/12/Sample-Online-Application-Form-2022-12-16.pdf" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-high"><td class="col-rank">6</td><td class="col-org">Lily Auchinloss Foundation</td><td class="col-priority">HIGH</td><td class="col-deadline">2026-04-15</td><td class="col-programs">7</td><td class="col-links"><a href="https://lilynyc.org/cycles-deadlines/" target="_blank" rel="noopener">info</a> <a href="https://lilynyc.org/types-of-grants/" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Environmental/Preservation Grant opens march 15 and might be a good opportunity for HII (Robine 01/22/26)</td></tr>
<tr class="priority-low"><td class="col-rank">7</td><td class="col-org">Constellation Energy Group Foundation</td><td class="col-priority">LOW</td><td class="col-deadline"></td><td class="col-programs">6</td><td class="col-links"><a href="https://www.constellationenergy.com/our-esg-principles/community/community-champions.html" target="_blank" rel="noopener">info</a> <a href="https://www.cybergrants.com/pls/cybergrants/ao_login.login?x_gm_id=9474&amp;x_proposal_type_id=78824" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-low"><td class="col-rank">8</td><td class="col-org">Environmental Media Fund</td><td class="col-priority">LOW</td><td class="col-deadline"></td><td class="col-programs">6</td><td class="col-links"><a href="https://www.environmentalmediafund.org/Home.aspx" target="_blank" rel="noopener">info</a> <a href="https://www.environmentalmediafund.org/Page.aspx?PageID=33" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-high"><td class="col-rank">9</td><td class="col-org">Andrew W. Mellon Foundation</td><td class="col-priority">HIGH</td><td class="col-deadline"></td><td class="col-programs">4</td><td class="col-links"><a href="https://www.mellon.org/" target="_blank" rel="noopener">info</a> <a href="https://www.mellon.org/resources" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span> They are currently taking applications on a rolling basis for &quot;Funding Inquiries for Mellon’s Humanities in Place Pro...</td></tr>
<tr class="priority-high"><td class="col-rank">10</td><td class="col-org">The Chanel Foundation</td><td class="col-priority">HIGH, 2025 TO DO</td><td class="col-deadline"></td><td class="col-programs">1</td><td class="col-links"><a href="https://www.fondationchanel.org/en/" target="_blank" rel="noopener">info</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span> No clear open/upcoming opportunities; may be worth relationship outreach (gender + climate angle) but not actionable ...</td></tr>
<tr class="priority-low"><td class="col-rank">11</td><td class="col-org">Jet Blue</td><td class="col-priority">LOW</td><td class="col-deadline"></td><td class="col-programs">6</td><td class="col-links"><a href="https://jetbluefoundation.org/" target="_blank" rel="noopener">info</a> <a href="https://jetbluefoundation.org/programs" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-med"><td class="col-rank">12</td><td class="col-org">Dr. Robert C. and Tina Sohn Foundation</td><td class="col-priority">MEDIUM</td><td class="col-deadline"></td><td class="col-programs">7</td><td class="col-links"><a href="http://www.sohnfoundation.org/Grant_guidelines1.htm" target="_blank" rel="noopener">info</a> <a href="http://www.sohnfoundation.org/Grant_application.htm" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-high"><td class="col-rank">13</td><td class="col-org">Fordham University Flourishing In Community Grants</td><td class="col-priority">HIGH</td><td class="col-deadline"></td><td class="col-programs">3</td><td class="col-links"><a href="https://www.fordham.edu/about/living-the-mission/thriving-communities/application/" target="_blank" rel="noopener">info</a> <a href="https://drive.google.com/drive/folders/1ByN-uR7arBN7SFVpnBxTwVcohnH31BVT" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-high"><td class="col-rank">14</td><td class="col-org">Gordon &amp; Betty Moore Foundation</td><td class="col-priority">HIGH</td><td class="col-deadline"></td><td class="col-programs">3</td><td class="col-links"><a href="https://www.moore.org/" target="_blank" rel="noopener">info</a> <a href="https://www.moore.org/grants" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span> The latest grants they have posted on their website are form november 2025 and are grants from other organisations su...</td></tr>
<tr class="priority-unknown"><td class="col-rank">15</td><td class="col-org">North Face Explore Fund</td><td class="col-priority">NO</td><td class="col-deadline"></td><td class="col-programs">4</td><td class="col-links"><a href="https://www.thenorthface.com/en-us/about-us/outdoor-exploration/about-the-explore-fund" target="_blank" rel="noopener">info</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-unknown"><td class="col-rank">16</td><td class="col-org">Rauschenberg Foundation</td><td class="col-priority">NO</td><td class="col-deadline"></td><td class="col-programs">4</td><td class="col-links"><a href="https://www.rauschenbergfoundation.org/programs/grants" target="_blank" rel="noopener">info</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-unknown"><td class="col-rank">17</td><td class="col-org">Shelley &amp; Donald Rubin Foundation</td><td class="col-priority">NO</td><td class="col-deadline"></td><td class="col-programs">4</td><td class="col-links"><a href="https://www.sdrubin.org/our-board-and-staff-1" target="_blank" rel="noopener">info</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-low"><td class="col-rank">18</td><td class="col-org">Simmons Family Foundation</td><td class="col-priority">LOW</td><td class="col-deadline"></td><td class="col-programs">5</td><td class="col-links"><a href="http://simmonsfoundation.org" target="_blank" rel="noopener">info</a> <a href="http://simmonsfoundation.org/id4.html" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-low"><td class="col-rank">19</td><td class="col-org">US State Department</td><td class="col-priority">LOW</td><td class="col-deadline"></td><td class="col-programs">5</td><td class="col-links"><a href="https://www.state.gov/grants-process-overview/" target="_blank" rel="noopener">info</a> <a href="https://www.grants.gov/applicants/grant-applications/how-to-apply-for-grants" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-unknown"><td class="col-rank">20</td><td class="col-org">National Endowment for the Arts</td><td class="col-priority">NO</td><td class="col-deadline"></td><td class="col-programs">5</td><td class="col-links"><a href="https://www.arts.gov/grants" target="_blank" rel="noopener">info</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-high"><td class="col-rank">21</td><td class="col-org">Pratt Industries</td><td class="col-priority">HIGH</td><td class="col-deadline"></td><td class="col-programs">1</td><td class="col-links"><a href="https://www.prattindustries.com/latest-news/category/philanthropy/" target="_blank" rel="noopener">info</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-low"><td class="col-rank">22</td><td class="col-org">Earthwatch Institute</td><td class="col-priority">LOW</td><td class="col-deadline"></td><td class="col-programs">4</td><td class="col-links"><a href="http://earthwatch.org/" target="_blank" rel="noopener">info</a> <a href="https://earthwatch.org/partnerships/grants-and-foundations" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-low"><td class="col-rank">23</td><td class="col-org">Pinkerton Foundation</td><td class="col-priority">LOW, LOI</td><td class="col-deadline"></td><td class="col-programs">6</td><td class="col-links"><a href="http://www.thepinkertonfoundation.org/grant-guidelines" target="_blank" rel="noopener">info</a> <a href="https://pinkerton.fluxx.io/user_sessions/new" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-med"><td class="col-rank">24</td><td class="col-org">William and Flora Hewlett Foundation</td><td class="col-priority">MEDIUM</td><td class="col-deadline"></td><td class="col-programs">6</td><td class="col-links"><a href="https://hewlett.org/programs/environment/" target="_blank" rel="noopener">info</a> <a href="https://hewlett.smapply.io" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-unknown"><td class="col-rank">25</td><td class="col-org">NY Community Trust</td><td class="col-priority">2026 TO DO</td><td class="col-deadline"></td><td class="col-programs">7</td><td class="col-links"><a href="https://thenytrust.org/grant-funding/environment-nyc/" target="_blank" rel="noopener">info</a> <a href="https://grantseeker.thenytrust.org/" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span> Rolling admissions Typically do not fund environmental education programs</td></tr>
<tr class="priority-high"><td class="col-rank">26</td><td class="col-org">Climate Emergency Fund</td><td class="col-priority">HIGH</td><td class="col-deadline"></td><td class="col-programs">2</td><td class="col-links"><a href="https://www.climateemergencyfund.org/apply" target="_blank" rel="noopener">info</a> <a href="https://webportalapp.com/sp/login/cef_application" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span> They don&#x27;t fund organizations that don&#x27;t utilize disruptive protest or art instillations which may rule us out.</td></tr>
<tr class="priority-high"><td class="col-rank">27</td><td class="col-org">Rockefeller Brothers Fund</td><td class="col-priority">HIGH</td><td class="col-deadline"></td><td class="col-programs">2</td><td class="col-links"><a href="https://www.rbf.org/grants/for-grant-seekers" target="_blank" rel="noopener">info</a> <a href="https://rbf.givingdata.com/portal/campaign/programapp?panelMode=signIn" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span> arts/culture window closed for 2025; possible to reapply in 2026 but unsolicited success rate very low.</td></tr>
<tr class="priority-unknown"><td class="col-rank">28</td><td class="col-org">Kresge Foundation</td><td class="col-priority">NO</td><td class="col-deadline"></td><td class="col-programs">7</td><td class="col-links"><a href="https://kresge.org/grants-social-investments/current-funding-opportunities/" target="_blank" rel="noopener">info</a> <a href="https://kresge.org/grants-social-investments/how-to-apply/" target="_blank" rel="noopener">apply</a></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span></td></tr>
<tr class="priority-unknown"><td class="col-rank">29</td><td class="col-org">Alaska Venture Fund</td><td class="col-priority"></td><td class="col-deadline"></td><td class="col-programs">0</td><td class="col-links"></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span> <span class="badge badge-warn">missing links</span></td></tr>
<tr class="priority-unknown"><td class="col-rank">30</td><td class="col-org">Biodiversity Funders Group</td><td class="col-priority"></td><td class="col-deadline"></td><td class="col-programs">0</td><td class="col-links"></td><td class="col-notes"><span class="badge badge-warn">missing deadline</span> <span class="badge badge-warn">missing links</span></td></tr>
</tbody></table></div>
<h2 class="queue-title">Apply Next Queue (deadline-driven)</h2>
<div class="table-wrap">
<table class="dashboard-table">
<thead><tr><th class="col-rank">Rank</th><th>Organization</th><th>Priority</th><th class="col-deadline">LOI</th><th class="col-deadline">Apply by</th><th class="col-days">Days left</th><th class="col-programs">Programs</th><th>Links</th><th>Notes</th></tr></thead>
<tbody>
<tr class="priority-high"><td class="col-rank">1</td><td class="col-org">Lily Auchinloss Foundation</td><td class="col-priority">HIGH</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Apr 15, 2026</td><td class="col-days" data-deadline="2026-04-15"></td><td class="col-programs">7</td><td class="col-links"><a href="https://lilynyc.org/cycles-deadlines/" target="_blank" rel="noopener">info</a> <a href="https://lilynyc.org/types-of-grants/" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Environmental/Preservation Grant opens march 15 and might be a good opportunity for HII (Robine 01/22/26)</td></tr>
<tr class="priority-med"><td class="col-rank">2</td><td class="col-org">NYSP2I (The New York State Pollution Prevention Institute)</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Apr 18, 2026</td><td class="col-days" data-deadline="2026-04-18"></td><td class="col-programs">7</td><td class="col-links"><a href="https://www.rit.edu/affiliate/nysp2i/funding" target="_blank" rel="noopener">info</a></td><td class="col-notes"></td></tr>
<tr class="priority-med"><td class="col-rank">3</td><td class="col-org">Brooklyn ORG / Brooklyn Community Foundation</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">May 15, 2026</td><td class="col-days" data-deadline="2026-05-15"></td><td class="col-programs">7</td><td class="col-links"><a href="https://brooklyn.org/" target="_blank" rel="noopener">info</a> <a href="https://brooklyn.org/how-to-apply-for-bko-funding/" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-low"><td class="col-rank">4</td><td class="col-org">Dreyfus Foundation</td><td class="col-priority">LOW</td><td class="col-deadline">Jul 15, 2026</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-days" data-deadline="2026-07-15"></td><td class="col-programs">8</td><td class="col-links"><a href="http://www.mvdreyfusfoundation.org/#!application-guidelines" target="_blank" rel="noopener">info</a> <a href="https://webportalapp.com/sp/login/max_and_victoria_dreyfus_foundation_grant" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-unknown"><td class="col-rank">5</td><td class="col-org">Vilcek Foundation</td><td class="col-priority"></td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Apr 30, 2026</td><td class="col-days" data-deadline="2026-04-30"></td><td class="col-programs">5</td><td class="col-links"><a href="https://vilcek.org/grants/" target="_blank" rel="noopener">info</a> <a href="https://portal.vilcek.org/grantportal/s/login/?ec=302&amp;startURL=%2Fgrantportal%2Fs%2F%3F_gl%3D1*epgerc*_gcl_au*MTMwODY3NzE0Ni4xNzM3NzM0ODk3*_ga*MTY4Mjg0NTYzNy4xNzM3NzM0ODk3*_ga_PMRH1P23GE*MTczNzczNDg5Ny4xLjEuMTczNzczNTQyMC4wLjAuMA..*_ga_2V5DYM0WCN*MTczNzczNDg5Ny4xLjEuMTczNzczNTQyMC41OS4wLjE0Mzg2MzM5NA.." target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-unknown"><td class="col-rank">6</td><td class="col-org">Florence Muller Fdn</td><td class="col-priority">NO</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">May 1, 2026</td><td class="col-days" data-deadline="2026-05-01"></td><td class="col-programs">5</td><td class="col-links"><a href="https://www.fmmullerfdn.org/" target="_blank" rel="noopener">info</a> <a href="https://www.fmmullerfdn.org/grant-guidelines" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Must be within 6 NY counties (not applicable to NYC)</td></tr>
<tr class="priority-med"><td class="col-rank">7</td><td class="col-org">Creative Capital</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Apr 2, 2026</td><td class="col-days" data-deadline="2026-04-02"></td><td class="col-programs">3</td><td class="col-links"><a href="https://creative-capital.org/creative-capital-award/award-application/" target="_blank" rel="noopener">info</a> <a href="https://apply.creative-capital.org/#button" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Fund specific new creative works not ongoing exhibitions or programs</td></tr>
<tr class="priority-med"><td class="col-rank">8</td><td class="col-org">RTX Corporation</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Jul 31, 2026</td><td class="col-days" data-deadline="2026-07-31"></td><td class="col-programs">6</td><td class="col-links"><a href="https://www.utcfoundation.org/who-we-are.html" target="_blank" rel="noopener">info</a> <a href="https://www.utcfoundation.org/contact-us.html" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Must be sponsored by an RTX employee to apply</td></tr>
<tr class="priority-med"><td class="col-rank">9</td><td class="col-org">Barker Welfare Foundation</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Aug 1, 2026</td><td class="col-days" data-deadline="2026-08-01"></td><td class="col-programs">6</td><td class="col-links"><a href="https://www.barkerwelfare.org/" target="_blank" rel="noopener">info</a> <a href="https://www.barkerwelfare.org/funding-inquiry/" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-high"><td class="col-rank">10</td><td class="col-org">NBC Universal Impact Grants</td><td class="col-priority">HIGH, 2025 TO DO</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Apr 15, 2026</td><td class="col-days" data-deadline="2026-04-15"></td><td class="col-programs">1</td><td class="col-links"><a href="https://www.localimpactgrants.com/" target="_blank" rel="noopener">info</a></td><td class="col-notes">The applying organization’s total expenses must be between $100,000 and $1,000,000; revenue must be greater than $100...</td></tr>
<tr class="priority-med"><td class="col-rank">11</td><td class="col-org">Tiffany &amp; Co. Foundation</td><td class="col-priority">MEDIUM</td><td class="col-deadline">May 1, 2026</td><td class="col-deadline">Aug 1, 2026</td><td class="col-days" data-deadline="2026-05-01"></td><td class="col-programs">3</td><td class="col-links"><a href="https://www.tiffanyandcofoundation.org" target="_blank" rel="noopener">info</a> <a href="https://www.tiffanyandcofoundation.org/how-to-apply.html" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-med"><td class="col-rank">12</td><td class="col-org">Sappi- Ideas That Matter</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Jul 15, 2026</td><td class="col-days" data-deadline="2026-07-15"></td><td class="col-programs">4</td><td class="col-links"><a href="https://www.sappi.com/sappi-ideas-that-matter" target="_blank" rel="noopener">info</a></td><td class="col-notes"></td></tr>
<tr class="priority-med"><td class="col-rank">13</td><td class="col-org">11th Hour Racing</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Mar 31, 2026</td><td class="col-days" data-deadline="2026-03-31"></td><td class="col-programs">1</td><td class="col-links"><a href="https://11thhourracing.org/grant-giving/" target="_blank" rel="noopener">info</a> <a href="https://11thhourracing.org/apply-for-a-grant/" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Mainly focused on ocean conservation efforts</td></tr>
<tr class="priority-med"><td class="col-rank">14</td><td class="col-org">Robert Lehman Foundation -</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Apr 1, 2026</td><td class="col-days" data-deadline="2026-04-01"></td><td class="col-programs">1</td><td class="col-links"><a href="https://www.robertlehmanfoundation.org/" target="_blank" rel="noopener">info</a> <a href="https://www.robertlehmanfoundation.org/guidelines.php" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-med"><td class="col-rank">15</td><td class="col-org">Samuel H. Kress Foundation</td><td class="col-priority">MEDIUM, Invitation Only</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Apr 1, 2026</td><td class="col-days" data-deadline="2026-04-01"></td><td class="col-programs">1</td><td class="col-links"><a href="https://www.kressfoundation.org/Programs/Grants/History-of-Art" target="_blank" rel="noopener">info</a> <a href="https://www.kressfoundation.org/Programs/Grants/Conservation" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-unknown"><td class="col-rank">16</td><td class="col-org">NYS Department of Environmental Conservation Environmental Justice - Green Jobs for Youth</td><td class="col-priority">2026 TO DO</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Jan 28, 2026</td><td class="col-days" data-deadline="2026-01-28"></td><td class="col-programs">7</td><td class="col-links"><a href="https://dec.ny.gov/environmental-protection/environmental-justice/grant-programs" target="_blank" rel="noopener">info</a> <a href="https://esupplier.sfs.ny.gov/psc/fscm/SUPPLIER/ERP/c/NUI_FRAMEWORK.PT_LANDINGPAGE.GBL?&amp;.&amp;" target="_blank" rel="noopener">apply</a></td><td class="col-notes">previous notes say no DEC grants currently fit HII (as of Jan/June 2025); deprioritize unless eligibility changes.</td></tr>
<tr class="priority-unknown"><td class="col-rank">17</td><td class="col-org">Prince Albert of Monaco II Foundation (HII Europe)</td><td class="col-priority">2026 TO DO</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Mar 31, 2026</td><td class="col-days" data-deadline="2026-03-31"></td><td class="col-programs">1</td><td class="col-links"><a href="https://www.fpa2.org/en/submit-a-project" target="_blank" rel="noopener">info</a> <a href="https://www.fpa2.org/en/submit-a-project" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Applied in 2025; strong climate fit and should be actively followed up.</td></tr>
<tr class="priority-unknown"><td class="col-rank">18</td><td class="col-org">NYSERDA (Dept of Labor) - Climate Justice Fellow</td><td class="col-priority">2026 TO DO</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Jun 30, 2026</td><td class="col-days" data-deadline="2026-06-30"></td><td class="col-programs">3</td><td class="col-links"><a href="https://www.nyserda.ny.gov/All-Programs/Climate-Justice-Fellowship" target="_blank" rel="noopener">info</a> <a href="https://portal.nyserda.ny.gov/CORE_Solicitation_Detail_Page?SolicitationId=a0rt000001Mh9IN&amp;_gl=1*1gejtjc*_gcl_au*ODAyMzgwODYyLjE3MzgwMTkwMDY.*_ga*MjAwNTY0NzUwNi4xNzM4MDE4Njk0*_ga_DRYJB34TXH*MTczODAxOTAwNi4xLjEuMTczODAxOTE1MS42MC4wLjA." target="_blank" rel="noopener">apply</a></td><td class="col-notes">Rolling admissions on first come first served Up to $40k per fellow Fellow must be NYS resident and from a disadvanta...</td></tr>
<tr class="priority-med"><td class="col-rank">19</td><td class="col-org">Trust for Mutual Understanding</td><td class="col-priority">MEDIUM</td><td class="col-deadline">May 6, 2026</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-days" data-deadline="2026-05-06"></td><td class="col-programs">1</td><td class="col-links"><a href="https://www.tmuny.org" target="_blank" rel="noopener">info</a> <a href="https://tmuny.fluxx.io/user_sessions/new" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Do not fund youth initatives; must partner with an org in one of these countries: lbania, Armenia, Azerbaijan, Bosnia...</td></tr>
<tr class="priority-unknown"><td class="col-rank">20</td><td class="col-org">Foundation for Sustainability and Innovation</td><td class="col-priority">NO</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Apr 15, 2026</td><td class="col-days" data-deadline="2026-04-15"></td><td class="col-programs">0</td><td class="col-links"><a href="http://fsifoundation.com/grants/" target="_blank" rel="noopener">info</a></td><td class="col-notes"></td></tr>
<tr class="priority-med"><td class="col-rank">21</td><td class="col-org">Ben &amp; Jerry&#x27;s Foundation</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Feb 25, 2026</td><td class="col-days" data-deadline="2026-02-25"></td><td class="col-programs">5</td><td class="col-links"><a href="https://benandjerrysfoundation.org/" target="_blank" rel="noopener">info</a></td><td class="col-notes"></td></tr>
<tr class="priority-low"><td class="col-rank">22</td><td class="col-org">Awesome Foundation</td><td class="col-priority">LOW</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Mar 27, 2026</td><td class="col-days" data-deadline="2026-03-27"></td><td class="col-programs">0</td><td class="col-links"><a href="https://www.awesomefoundation.org/en/about_us" target="_blank" rel="noopener">info</a> <a href="https://www.awesomefoundation.org/en/submissions/new" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-low"><td class="col-rank">23</td><td class="col-org">City Council Funding (Participatory Budgeting Brooklyn Districts) - Infrastructure</td><td class="col-priority">LOW</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Feb 18, 2026</td><td class="col-days" data-deadline="2026-02-18"></td><td class="col-programs">5</td><td class="col-links"><a href="https://council.nyc.gov/budget/discretionary-funding-policies-and-procedures/" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-med"><td class="col-rank">24</td><td class="col-org">New York City Environmental Fund at Hudson River Foundation</td><td class="col-priority">MEDIUM</td><td class="col-deadline">Feb 13, 2026</td><td class="col-deadline">Mar 30, 2026</td><td class="col-days" data-deadline="2026-02-13"></td><td class="col-programs">4</td><td class="col-links"><a href="http://www.hudsonriver.org/nycef/" target="_blank" rel="noopener">info</a> <a href="https://www.hudsonriver.org/grants" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-med"><td class="col-rank">25</td><td class="col-org">Dominion</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Feb 20, 2026</td><td class="col-days" data-deadline="2026-02-20"></td><td class="col-programs">4</td><td class="col-links"><a href="https://www.dominionenergy.com/our-company/customers-and-community/charitable-foundation" target="_blank" rel="noopener">info</a> <a href="https://www.instrumentl.com/grants/dominion-energy-foundation-grants" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-unknown"><td class="col-rank">26</td><td class="col-org">Con Edison</td><td class="col-priority">2026 TO DO</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Jun 30, 2026</td><td class="col-days" data-deadline="2026-06-30"></td><td class="col-programs">1</td><td class="col-links"><a href="https://www.coned.com/en/community-affairs/strategic-partnerships/apply-for-a-grant" target="_blank" rel="noopener">info</a> <a href="https://www.coned.com/en/community-affairs/strategic-partnerships/apply-for-a-grant" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Concept Paper must be submitted before April 30th and submissions that qualify will be invited to submit an application</td></tr>
<tr class="priority-unknown"><td class="col-rank">27</td><td class="col-org">JMG Foundation</td><td class="col-priority">NO</td><td class="col-deadline">Mar 1, 2026</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-days" data-deadline="2026-03-01"></td><td class="col-programs">4</td><td class="col-links"><a href="https://jmgoldmanfoundation.org/about-us/" target="_blank" rel="noopener">info</a> <a href="https://jmgoldmanfoundation.org/grant-information/" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-unknown"><td class="col-rank">28</td><td class="col-org">George Gund Foundation</td><td class="col-priority">NO</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Mar 15, 2026</td><td class="col-days" data-deadline="2026-03-15"></td><td class="col-programs">4</td><td class="col-links"><a href="https://gundfoundation.org/grantmaking/what-we-believe/" target="_blank" rel="noopener">info</a> <a href="https://gundfoundation.org/grantmaking/apply-for-a-grant/" target="_blank" rel="noopener">apply</a></td><td class="col-notes"></td></tr>
<tr class="priority-unknown"><td class="col-rank">29</td><td class="col-org">Invoking the Pause (ITP)</td><td class="col-priority">NO</td><td class="col-deadline">Mar 15, 2026</td><td class="col-deadline">May 1, 2026</td><td class="col-days" data-deadline="2026-03-15"></td><td class="col-programs">4</td><td class="col-links"><a href="https://invokingthepause.org/home.html" target="_blank" rel="noopener">info</a> <a href="https://invokingthepause.org/climatechallengecohort.html" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Funds: accomodation, transport, stipends, childcare, facilitation for a team workshop</td></tr>
<tr class="priority-med"><td class="col-rank">30</td><td class="col-org">NYS DEC Grants- Hudson River Estuary</td><td class="col-priority">MEDIUM</td><td class="col-deadline"><span class="no-deadline">—</span></td><td class="col-deadline">Aug 7, 2026</td><td class="col-days" data-deadline="2026-08-07"></td><td class="col-programs">1</td><td class="col-links"><a href="https://dec.ny.gov/nature/waterbodies/oceans-estuaries/hudson-river-estuary-program/grants-funding-opportunities#:~:text=Since%201999%2C%20DEC&#x27;s%20Hudson%20River,of%20habitat%20and%20natural%20resources." target="_blank" rel="noopener">info</a> <a href="https://grantsmanagement.ny.gov/" target="_blank" rel="noopener">apply</a></td><td class="col-notes">Must be pre-qualified in SFS before app deadline</td></tr>
</tbody></table></div>
</section>
<!-- DASHBOARD:END -->

## How scoring works

The dashboard generates **two different scores**, each designed to answer a different fundraising question.

---

### 1. Review Priority Score

**Question:** *Which funders need research, cleanup, or follow-up first?*

This score helps identify records that are **important but incomplete, outdated, or unclear**.

A higher Review Priority Score means a funder should be reviewed sooner.

The score increases when:

* The funder is marked **High or Medium priority**
* The funder supports **multiple HII programs**
* Information has **not been updated recently**
* **Deadlines are missing or unclear**
* **Websites or application links are missing**
* Key fields like *What They Fund* or *Geography* are empty

This queue is best used for:

* Research days
* Data cleanup
* Strategic planning
* Delegating follow-ups to staff or interns

---

### 2. Application Priority Score

**Question:** *Which grants should we apply to next?*

This score is only calculated for funders that have **at least one known deadline**.

A higher Application Priority Score means the funder is a stronger near-term opportunity.

The score increases when:

* A deadline is **soon**
* The funder supports **multiple HII programs**
* The relationship is **warm or active**
* The funder is marked as a **higher priority**

The score is reduced when:

* The process is **invitation-only**
* The application is described as **complex or high-burden**
* The deadline has already passed

This queue is best used for:

* Weekly application planning
* Grant calendar reviews
* Deciding what *not* to apply to yet

---

### Why two scores?

Fundraising work happens in **two modes**:

1. **Research & preparation**
2. **Application & execution**

Separating these scores prevents urgent deadlines from hiding important strategic work — and prevents incomplete records from cluttering application planning.

---

### How to use the dashboard

* Start with **Apply Next** when planning submissions
* Use **Update Queue** to assign research and cleanup tasks
* Re-run the script after updating the Google Sheet to refresh priorities

The dashboard is designed to be **iterative** — scores improve as your data improves.
