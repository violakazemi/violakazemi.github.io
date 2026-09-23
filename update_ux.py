import re

html_template = """<!DOCTYPE HTML>
<html lang="en">
<head>
    <title>UX/UI Redesign Concept - Viola Kazemi</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="stylesheet" href="assets/css/main.css" />
    <link rel="icon" type="image/png" href="images/logo.png" />
    
    <style>
        details {
            background-color: var(--color-bg-card);
            border: 1px solid var(--color-border);
            border-radius: var(--radius-sm);
            padding: var(--space-2) var(--space-3);
            margin-bottom: var(--space-3);
            transition: box-shadow 0.2s ease;
        }
        details:hover { box-shadow: var(--shadow-sm); }
        summary {
            font-weight: 600;
            cursor: pointer;
            list-style: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        summary::-webkit-details-marker { display: none; }
        summary::after { content: '+'; font-size: 1.2rem; color: var(--color-text-secondary); }
        details[open] summary::after { content: '\u2212'; }
        details p { margin-top: var(--space-2); margin-bottom: 0; font-size: var(--fs-small); color: var(--color-text-secondary); max-width: 100%; }
        
        .grid-2 {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: var(--space-4);
            margin-bottom: var(--space-3);
        }
        @media screen and (max-width: 768px) {
            .grid-2 { grid-template-columns: 1fr; }
        }
    </style>
</head>
<body>

    <header class="global-header">
        <a href="/" class="logo">Viola Kazemi <span style="color: var(--color-text-secondary); font-weight: 400;">/ UX/UI Redesign Concept</span></a>
        <nav>
            <a href="/" class="button button-secondary">Home</a>
        </nav>
    </header>

    <section class="section" style="padding-top: 120px; padding-bottom: var(--space-5);">
        <div class="container">
            <div style="width: 100%; margin-bottom: var(--space-5);">
                <span class="badge">UX/UI Redesign</span>
                <h1 style="margin-top: var(--space-2);">UX/UI Redesign Concept</h1>
                <p class="subtitle" style="font-size: 1.25rem; max-width: 800px;">A comprehensive approach to modernizing a legacy interface by balancing aesthetic elevation with functional accessibility.</p>
            </div>
        </div>
    </section>

    <section class="section" style="padding-top: 0;">
        <div class="container">
            <div style="max-width: 800px; margin: 0 auto;">

<h2 style="margin-bottom: var(--space-3);">Updated Project Direction</h2>
<p>The uploaded screenshots provide the first visual audit of the existing insurance Android app.</p>
<p>Do not describe the hamburger menu as definitively &ldquo;bad&rdquo; yet. Treat the screenshots as evidence of potential navigation and hierarchy issues that need validation.</p>
<p>The central design question is:</p>
<blockquote style="border-left: 4px solid var(--color-border); padding-left: var(--space-3); margin-left: 0; color: var(--color-text-secondary); font-style: italic; margin-bottom: var(--space-4);">
    <p>Is the current hamburger-menu navigation model still appropriate for an insurance app, or does it hide important tasks and mix too many unrelated destinations together?</p>
</blockquote>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h1 style="margin-bottom: var(--space-3);">Initial Visual Audit</h1>

<h2 style="margin-top: var(--space-4);">Observation 1: Mixed-Purpose Navigation Menu</h2>
<p>The hamburger menu combines several types of destinations in one long list:</p>
<ul>
    <li>Insurance tasks</li>
    <li>Claims</li>
    <li>Coverage</li>
    <li>Policies</li>
    <li>Billing</li>
    <li>Documents</li>
    <li>Support</li>
    <li>Benefits or promotional content</li>
    <li>Profile</li>
    <li>Settings</li>
    <li>Feedback</li>
    <li>Legal information</li>
    <li>Logout</li>
</ul>
<h3>Design Question</h3>
<p>Should these destinations be separated into clearer groups based on user goals, frequency, importance, or task type?</p>
<h3>Evidence</h3>
<div style="width: 100%; border-radius: var(--radius-md); overflow: hidden; background-color: var(--color-bg-card); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); margin: var(--space-3) 0;">
    <div style="width: 100%; padding-bottom: 56.25%; background-color: rgba(0,0,0,0.03); position: relative;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--color-text-secondary); font-weight: 600;">[Insert screenshot of open hamburger menu]</div>
    </div>
</div>
<h3>Status</h3>
<p>Observed in screenshot. User impact requires validation.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h2 style="margin-top: var(--space-4);">Observation 2: Limited Information Hierarchy</h2>
<p>The menu appears to present many destinations with similar row treatment.</p>
<p>Some items use icons while other items appear as text-only rows. There are limited visible section labels or strong groupings.</p>
<h3>Design Question</h3>
<p>Can users quickly understand:</p>
<ul>
    <li>Which items are primary?</li>
    <li>Which items are secondary?</li>
    <li>Which items relate to account management?</li>
    <li>Which items are informational or legal?</li>
    <li>Which items are urgent or task-oriented?</li>
</ul>
<h3>Evidence</h3>
<div style="width: 100%; border-radius: var(--radius-md); overflow: hidden; background-color: var(--color-bg-card); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); margin: var(--space-3) 0;">
    <div style="width: 100%; padding-bottom: 56.25%; background-color: rgba(0,0,0,0.03); position: relative;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--color-text-secondary); font-weight: 600;">[Insert annotated hamburger menu screenshot]</div>
    </div>
</div>
<h3>Status</h3>
<p>Observed in screenshot. Severity and user impact require validation.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h2 style="margin-top: var(--space-4);">Observation 3: Logout Has High Visual Priority</h2>
<p>Logout appears near the top of the navigation menu, before many core insurance tasks.</p>
<h3>Design Question</h3>
<p>Should logout be visually separated from primary product navigation and placed within an account-management area?</p>
<h3>Potential Risk</h3>
<p>The current placement may give an account-exit action similar or greater prominence than important insurance tasks.</p>
<h3>Evidence</h3>
<div style="width: 100%; border-radius: var(--radius-md); overflow: hidden; background-color: var(--color-bg-card); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); margin: var(--space-3) 0;">
    <div style="width: 100%; padding-bottom: 56.25%; background-color: rgba(0,0,0,0.03); position: relative;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--color-text-secondary); font-weight: 600;">[Insert cropped screenshot showing logout placement]</div>
    </div>
</div>
<h3>Status</h3>
<p>Observed in screenshot. Accidental selection and user confusion require testing.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h2 style="margin-top: var(--space-4);">Observation 4: Multiple Navigation Patterns</h2>
<p>Different screens appear to use different navigation treatments:</p>
<ul>
    <li>Hamburger icon</li>
    <li>Back arrow</li>
    <li>Different header layouts</li>
    <li>Different title placement</li>
    <li>Different combinations of actions</li>
    <li>Different green header treatments</li>
</ul>
<h3>Design Question</h3>
<p>Does the app communicate a consistent navigation model across:</p>
<ul>
    <li>Global navigation</li>
    <li>Local navigation</li>
    <li>Back navigation</li>
    <li>Account navigation</li>
    <li>Home navigation?</li>
</ul>
<h3>Evidence</h3>
<div style="width: 100%; border-radius: var(--radius-md); overflow: hidden; background-color: var(--color-bg-card); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); margin: var(--space-3) 0;">
    <div style="width: 100%; padding-bottom: 56.25%; background-color: rgba(0,0,0,0.03); position: relative;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--color-text-secondary); font-weight: 600;">[Insert settings, billing, error, and trips screenshots]</div>
    </div>
</div>
<h3>Status</h3>
<p>Observed across screenshots. Requires a navigation-pattern audit.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h2 style="margin-top: var(--space-4);">Observation 5: Competing Green Treatments</h2>
<p>Green appears across:</p>
<ul>
    <li>Headers</li>
    <li>Status areas</li>
    <li>Buttons</li>
    <li>Navigation</li>
    <li>Icons</li>
    <li>Action controls</li>
    <li>Selected states</li>
</ul>
<h3>Design Question</h3>
<p>Are color roles clearly defined, or are navigation, actions, status, and brand elements competing for attention?</p>
<h3>Evidence</h3>
<div style="width: 100%; border-radius: var(--radius-md); overflow: hidden; background-color: var(--color-bg-card); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); margin: var(--space-3) 0;">
    <div style="width: 100%; padding-bottom: 56.25%; background-color: rgba(0,0,0,0.03); position: relative;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--color-text-secondary); font-weight: 600;">[Insert color annotation board]</div>
    </div>
</div>
<h3>Status</h3>
<p>Visual observation. Requires color-role and accessibility review.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h2 style="margin-top: var(--space-4);">Observation 6: Home Actions and Menu Destinations May Overlap</h2>
<p>The home screen contains prominent actions such as starting a claim and viewing coverage. Related destinations also appear in the hamburger menu.</p>
<h3>Design Question</h3>
<p>Which tasks should be:</p>
<ol>
    <li>Promoted on the home screen?</li>
    <li>Available through persistent navigation?</li>
    <li>Located inside a secondary menu?</li>
    <li>Available contextually within a policy or claim?</li>
</ol>
<h3>Evidence</h3>
<div style="width: 100%; border-radius: var(--radius-md); overflow: hidden; background-color: var(--color-bg-card); border: 1px solid var(--color-border); box-shadow: var(--shadow-sm); margin: var(--space-3) 0;">
    <div style="width: 100%; padding-bottom: 56.25%; background-color: rgba(0,0,0,0.03); position: relative;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: var(--color-text-secondary); font-weight: 600;">[Insert home screen and hamburger menu side by side]</div>
    </div>
</div>
<h3>Status</h3>
<p>Potential information-architecture issue. Requires task-priority research.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h1 style="margin-bottom: var(--space-3);">Updated Problem Space</h1>
<p>The current product appears to have a navigation structure that may combine:</p>
<ul>
    <li>Global navigation</li>
    <li>Insurance task navigation</li>
    <li>Account management</li>
    <li>Settings</li>
    <li>Support</li>
    <li>Legal and informational content</li>
</ul>
<p>The project should investigate whether this structure makes it difficult for customers to understand:</p>
<ul>
    <li>Where they are</li>
    <li>Where to begin</li>
    <li>Which destinations matter most</li>
    <li>Where to find a specific insurance task</li>
    <li>How to distinguish account actions from insurance actions</li>
</ul>
<p>Do not finalize the problem statement until the screenshots, task audit, and research have been reviewed.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h1 style="margin-bottom: var(--space-3);">Updated Research Questions</h1>

<h2 style="margin-top: var(--space-4);">Navigation Discoverability</h2>
<ul>
    <li>Do users notice the hamburger icon?</li>
    <li>Do users understand what it contains?</li>
    <li>Can users predict where a task will be located?</li>
    <li>Do users expect important insurance tasks to be visible without opening a menu?</li>
</ul>

<h2 style="margin-top: var(--space-4);">Menu Comprehension</h2>
<ul>
    <li>Do users understand the grouping of menu items?</li>
    <li>Are insurance tasks distinguishable from account and legal items?</li>
    <li>Do users recognize the difference between &ldquo;Start a Claim&rdquo; and &ldquo;Track My Claim&rdquo;?</li>
    <li>Do users understand where &ldquo;My Profile,&rdquo; Settings,&rdquo; and &ldquo;Logout&rdquo; belong?</li>
</ul>

<h2 style="margin-top: var(--space-4);">Task Priority</h2>
<ul>
    <li>Which tasks are most important?</li>
    <li>Which tasks are frequent?</li>
    <li>Which tasks are urgent?</li>
    <li>Which tasks are rarely used?</li>
    <li>Which tasks need persistent access?</li>
</ul>

<h2 style="margin-top: var(--space-4);">Navigation Model</h2>
<p>Compare:</p>
<ol>
    <li>Improved hamburger menu</li>
    <li>Bottom navigation</li>
    <li>Hybrid navigation</li>
    <li>Task-based home navigation</li>
    <li>A role or policy-based navigation model, if relevant</li>
</ol>
<p>Do not select bottom navigation only because hamburger menus are considered outdated.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h1 style="margin-bottom: var(--space-3);">Required Navigation Audit</h1>
<p>Create a table with the following columns:</p>
<div style="overflow-x: auto; margin-bottom: var(--space-4);">
<table style="width: 100%; border-collapse: collapse; font-size: var(--fs-small);">
    <thead>
        <tr style="border-bottom: 2px solid var(--color-border);">
            <th style="padding: 8px; text-align: left;">Destination</th>
            <th style="padding: 8px; text-align: left;">Current location</th>
            <th style="padding: 8px; text-align: left;">User goal</th>
            <th style="padding: 8px; text-align: left;">Frequency</th>
            <th style="padding: 8px; text-align: left;">Urgency</th>
            <th style="padding: 8px; text-align: left;">Importance</th>
            <th style="padding: 8px; text-align: left;">Current visibility</th>
            <th style="padding: 8px; text-align: left;">Proposed location</th>
            <th style="padding: 8px; text-align: left;">Evidence</th>
        </tr>
    </thead>
    <tbody>
        <!-- Add empty rows as needed, or populate based on the list below -->
    </tbody>
</table>
</div>
<p>Include at minimum:</p>
<ul>
    <li>Homepage</li>
    <li>Start a Claim</li>
    <li>Track My Claim</li>
    <li>View My Coverage</li>
    <li>Manage Policies</li>
    <li>View My Billing</li>
    <li>Proof of Insurance</li>
    <li>Documents</li>
    <li>Contact Us</li>
    <li>My Profile</li>
    <li>Settings</li>
    <li>Logout</li>
    <li>Privacy, Security & Legal</li>
    <li>Feedback</li>
    <li>Benefits or promotional destinations</li>
</ul>
<p>Use [Unknown] where frequency, urgency, or importance has not been researched.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h1 style="margin-bottom: var(--space-3);">Screenshot Annotation Plan</h1>
<p>Create annotated versions of the screenshots showing:</p>

<h2 style="margin-top: var(--space-4);">Hamburger Menu</h2>
<p>Annotate:</p>
<ul>
    <li>Total number of destinations</li>
    <li>Primary task items</li>
    <li>Account-related items</li>
    <li>Legal/informational items</li>
    <li>Logout placement</li>
    <li>Icon usage</li>
    <li>Missing section headings</li>
    <li>Divider patterns</li>
    <li>Menu width</li>
    <li>Background overlay</li>
    <li>Relationship to the underlying page</li>
</ul>

<h2 style="margin-top: var(--space-4);">Home Screen</h2>
<p>Annotate:</p>
<ul>
    <li>Primary actions</li>
    <li>Quick-action controls</li>
    <li>Policy or coverage cards</li>
    <li>Repeated destinations</li>
    <li>Information hierarchy</li>
    <li>What is visible without opening navigation</li>
</ul>

<h2 style="margin-top: var(--space-4);">Settings Screen</h2>
<p>Annotate:</p>
<ul>
    <li>Header/navigation treatment</li>
    <li>Settings grouping</li>
    <li>Row height</li>
    <li>Icon and label consistency</li>
    <li>Separation between settings categories</li>
</ul>

<h2 style="margin-top: var(--space-4);">Billing Screen</h2>
<p>Annotate:</p>
<ul>
    <li>Header treatment</li>
    <li>Back or hamburger behavior</li>
    <li>Billing information hierarchy</li>
    <li>Expandable sections</li>
    <li>Relationship between global and local navigation</li>
</ul>

<h2 style="margin-top: var(--space-4);">Error Screen</h2>
<p>Annotate:</p>
<ul>
    <li>Back navigation</li>
    <li>Recovery action</li>
    <li>Header behavior</li>
    <li>Whether the user has a clear way to return to a useful destination</li>
</ul>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h1 style="margin-bottom: var(--space-3);">Case Study Narrative</h1>
<p>Use this narrative structure:</p>

<h2 style="margin-top: var(--space-4);">1. Trigger</h2>
<p>I noticed that the insurance app&rsquo;s navigation made several different types of destinations compete within one hamburger menu.</p>

<h2 style="margin-top: var(--space-4);">2. Initial Hypothesis</h2>
<p>The current navigation may be hiding important insurance tasks and may not clearly separate product actions from account, support, and legal content.</p>

<h2 style="margin-top: var(--space-4);">3. Investigation</h2>
<p>I audited the existing screens, mapped the destinations, reviewed task priority, and compared alternative navigation models.</p>

<h2 style="margin-top: var(--space-4);">4. Decision</h2>
<p>I selected a navigation direction based on discoverability, task priority, accessibility, scalability, and implementation complexity.</p>

<h2 style="margin-top: var(--space-4);">5. Prototype</h2>
<p>I created a prototype to compare the selected direction against the existing navigation model.</p>

<h2 style="margin-top: var(--space-4);">6. Validation</h2>
<p>I tested whether users could find important insurance tasks and understand the new navigation structure.</p>

<h2 style="margin-top: var(--space-4);">7. Reflection</h2>
<p>I learned that replacing a hamburger menu is not automatically the right solution. The stronger design decision comes from understanding which tasks deserve visibility and how the information architecture supports them.</p>

<hr style="border: 0; border-top: 1px solid var(--color-border); margin: var(--space-5) 0;">

<h1 style="margin-bottom: var(--space-3);">Important Writing Rules</h1>
<p>Use language such as:</p>
<ul>
    <li>&ldquo;The screenshots suggest&hellip;&rdquo;</li>
    <li>&ldquo;The initial audit revealed&hellip;&rdquo;</li>
    <li>&ldquo;This raised a question&hellip;&rdquo;</li>
    <li>&ldquo;This became a hypothesis to validate&hellip;&rdquo;</li>
    <li>&ldquo;The evidence indicated&hellip;&rdquo;</li>
    <li>&ldquo;The prototype was designed to test&hellip;&rdquo;</li>
</ul>
<p>Avoid unsupported statements such as:</p>
<ul>
    <li>&ldquo;Users were confused,&rdquo; unless tested</li>
    <li>&ldquo;Everyone hates hamburger menus&rdquo;</li>
    <li>&ldquo;The menu caused users to fail&rdquo;</li>
    <li>&ldquo;Bottom navigation is objectively better&rdquo;</li>
    <li>&ldquo;The redesign improved conversion&rdquo;</li>
    <li>&ldquo;Users completed tasks faster,&rdquo; unless measured</li>
    <li>&ldquo;The company shipped this redesign&rdquo;</li>
</ul>
<p>Refer to the product only as:</p>
<ul>
    <li>&ldquo;an insurance company&rsquo;s Android app&rdquo;</li>
    <li>&ldquo;an insurance mobile app&rdquo;</li>
    <li>&ldquo;the existing insurance app&rdquo;</li>
    <li>&ldquo;the current product&rdquo;</li>
</ul>
<p>Do not use the original company name anywhere in the case study.</p>

            </div>
        </div>
    </section>

    <!-- Bottom Navigation -->
    <section id="bottom-nav" style="background: none !important; box-shadow: none !important; border: none !important; margin-top: var(--space-5) !important; margin-bottom: var(--space-6) !important;">
        <div class="inner container" style="display: flex !important; justify-content: space-between !important; align-items: center !important; gap: var(--space-2) !important;">
            <a href="#" id="btn-prev-project" class="button button-secondary">&larr; Previous Concept</a>
            <a href="#" id="btn-next-project" class="button button-secondary">Next Concept &rarr;</a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div>
                    <h3>Case Studies</h3>
                    <ul>
                        <li><a href="museum">Museum Educator Dashboard</a></li>
                        <li><a href="golaab">Golaab Jewelry: Keepsake Builder</a></li>
                    </ul>
                </div>
                
                <div>
                    <h3>Design Lab</h3>
                    <ul>
                        <li><a href="tomaan">Tomaan: Fraud Verification</a></li>
                        <li><a href="promptlab-carbon">IBM watsonx: Prompt Compare</a></li>
                        <li><a href="smart-substitutions">Agentic Grocery Substitutions</a></li>
                        <li><a href="transparent-jar">The Transparent Jar</a></li>
                    </ul>
                </div>
                <div>
                    <h3>Connect</h3>
                    <ul>
                        <li><a href="mailto:viola.kazemi@gmail.com">Email</a></li>
                        <li><a href="https://www.linkedin.com/in/viola-kazemi/" target="_blank">LinkedIn</a></li>
                        <li><a href="ViolaKazemi.pdf">Download Resume</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-copyright" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px;">
                <p style="margin: 0;">&copy; 2026 Viola Kazemi. All rights reserved.</p>
                <a href="sudoku.html" class="button button-secondary" style="padding: 5px 15px; font-size: 0.9em;">Play a Game 🎮</a>
            </div>
        </div>
    </footer>

    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/js/main.js"></script>

</body>
</html>
"""

with open("ux-ui-redesign.html", "w") as f:
    f.write(html_template)
