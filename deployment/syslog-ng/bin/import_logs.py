





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">



  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-d7b19415c108234b91acac0d0c02091c860993c13687a757ee345cc1ecd3a9d1.css" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-d8af8b7dd51ee94d7ab4f44b513e681da376a0e759768cc5e8888151ec02ab9c.css" media="all" rel="stylesheet" />
  
  
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/site-537c466d44a69d38c4bd60c2fd2955373ef96d051bd97b2ad30ed039acc97bff.css" media="all" rel="stylesheet" />
  

  <meta name="viewport" content="width=device-width">
  
  <title>piwik-log-analytics/import_logs.py at master · piwik/piwik-log-analytics · GitHub</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars2.githubusercontent.com/u/698038?v=3&amp;s=400" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="piwik/piwik-log-analytics" property="og:title" /><meta content="https://github.com/piwik/piwik-log-analytics" property="og:url" /><meta content="piwik-log-analytics - Import any kind of server logs in Piwik for powerful log analytics. Universal log file parsing and reporting." property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  
  <meta name="pjax-timeout" content="1000">
  
  <meta name="request-id" content="E88C:657B:23CDE62:35027C5:59035435" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

  <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
<meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="E88C:657B:23CDE62:35027C5:59035435" name="octolytics-dimension-request_id" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged Out">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="ZGY1MmE2ZDk5YjNjNzQzNWZhM2Y1ZWVmMTlhZTMyNDNiYTQzMmRiNzM2MmEzM2U0YTYwNjc5MzM1MDdiN2NiZnx7InJlbW90ZV9hZGRyZXNzIjoiODEuMi45My4yOSIsInJlcXVlc3RfaWQiOiJFODhDOjY1N0I6MjNDREU2MjozNTAyN0M1OjU5MDM1NDM1IiwidGltZXN0YW1wIjoxNDkzMzkwMzkwLCJob3N0IjoiZ2l0aHViLmNvbSJ9">


  <meta name="html-safe-nonce" content="f4138d8981ad651ac50de8876382dcd742c6d42e">

  <meta http-equiv="x-pjax-version" content="58d922146c874a4175fc26176a233f9b">
  

    
  <meta name="description" content="piwik-log-analytics - Import any kind of server logs in Piwik for powerful log analytics. Universal log file parsing and reporting.">
  <meta name="go-import" content="github.com/piwik/piwik-log-analytics git https://github.com/piwik/piwik-log-analytics.git">

  <meta content="698038" name="octolytics-dimension-user_id" /><meta content="piwik" name="octolytics-dimension-user_login" /><meta content="31684749" name="octolytics-dimension-repository_id" /><meta content="piwik/piwik-log-analytics" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="31684749" name="octolytics-dimension-repository_network_root_id" /><meta content="piwik/piwik-log-analytics" name="octolytics-dimension-repository_network_root_nwo" />
        <link href="https://github.com/piwik/piwik-log-analytics/commits/master.atom" rel="alternate" title="Recent Commits to piwik-log-analytics:master" type="application/atom+xml">


    <link rel="canonical" href="https://github.com/piwik/piwik-log-analytics/blob/master/import_logs.py" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  </head>

  <body class="logged-out env-production page-blob">
    


  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



          <header class="site-header js-details-container Details" role="banner">
  <div class="container-responsive">
    <a class="header-logo-invertocat" href="https://github.com/" aria-label="Homepage" data-ga-click="(Logged out) Header, go to homepage, icon:logo-wordmark">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
    </a>

    <button class="btn-link float-right site-header-toggle js-details-target" type="button" aria-label="Toggle navigation">
      <svg aria-hidden="true" class="octicon octicon-three-bars" height="24" version="1.1" viewBox="0 0 12 16" width="18"><path fill-rule="evenodd" d="M11.41 9H.59C0 9 0 8.59 0 8c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zm0-4H.59C0 5 0 4.59 0 4c0-.59 0-1 .59-1H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1h.01zM.59 11H11.4c.59 0 .59.41.59 1 0 .59 0 1-.59 1H.59C0 13 0 12.59 0 12c0-.59 0-1 .59-1z"/></svg>
    </button>

    <div class="site-header-menu">
      <nav class="site-header-nav">
        <a href="/features" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:features" data-selected-links="/features /features">
          Features
</a>        <a href="/business" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:business" data-selected-links="/business /business/security /business/customers /business">
          Business
</a>        <a href="/explore" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship /showcases /explore">
          Explore
</a>        <a href="/pricing" class="js-selected-navigation-item nav-item" data-ga-click="Header, click, Nav menu - item:pricing" data-selected-links="/pricing /pricing/developer /pricing/team /pricing/business-hosted /pricing/business-enterprise /pricing">
          Pricing
</a>      </nav>

      <div class="site-header-actions">
          <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/piwik/piwik-log-analytics/search" class="js-site-search-form" data-scoped-search-url="/piwik/piwik-log-analytics/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/piwik/piwik-log-analytics/blob/master/import_logs.py" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>


          <a class="text-bold site-header-link" href="/login?return_to=%2Fpiwik%2Fpiwik-log-analytics%2Fblob%2Fmaster%2Fimport_logs.py" data-ga-click="(Logged out) Header, clicked Sign in, text:sign-in">Sign in</a>
            <span class="text-gray">or</span>
            <a class="text-bold site-header-link" href="/join?source=header-repo" data-ga-click="(Logged out) Header, clicked Sign up, text:sign-up">Sign up</a>
      </div>
    </div>
  </div>
</header>


  </div>

  <div id="start-of-content" class="accessibility-aid"></div>

    <div id="js-flash-container">
</div>



  <div role="main">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode">
    <div id="js-repo-pjax-container" data-pjax-container>
        



  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav">
    <div class="container repohead-details-container">


      <ul class="pagehead-actions">
  <li>
      <a href="/login?return_to=%2Fpiwik%2Fpiwik-log-analytics"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to watch a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
    Watch
  </a>
  <a class="social-count" href="/piwik/piwik-log-analytics/watchers"
     aria-label="19 users are watching this repository">
    19
  </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fpiwik%2Fpiwik-log-analytics"
    class="btn btn-sm btn-with-count tooltipped tooltipped-n"
    aria-label="You must be signed in to star a repository" rel="nofollow">
    <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
    Star
  </a>

    <a class="social-count js-social-count" href="/piwik/piwik-log-analytics/stargazers"
      aria-label="68 users starred this repository">
      68
    </a>

  </li>

  <li>
      <a href="/login?return_to=%2Fpiwik%2Fpiwik-log-analytics"
        class="btn btn-sm btn-with-count tooltipped tooltipped-n"
        aria-label="You must be signed in to fork a repository" rel="nofollow">
        <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
        Fork
      </a>

    <a href="/piwik/piwik-log-analytics/network" class="social-count"
       aria-label="44 users forked this repository">
      44
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/piwik" class="url fn" rel="author">piwik</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/piwik/piwik-log-analytics" data-pjax="#js-repo-pjax-container">piwik-log-analytics</a></strong>

</h1>

    </div>
    <div class="container">
      
<nav class="reponav js-repo-nav js-sidenav-container-pjax"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/piwik/piwik-log-analytics" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /piwik/piwik-log-analytics" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/piwik/piwik-log-analytics/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /piwik/piwik-log-analytics/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">43</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/piwik/piwik-log-analytics/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /piwik/piwik-log-analytics/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">4</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/piwik/piwik-log-analytics/projects" class="js-selected-navigation-item reponav-item" data-selected-links="repo_projects new_repo_project repo_project /piwik/piwik-log-analytics/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>


  <a href="/piwik/piwik-log-analytics/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="pulse /piwik/piwik-log-analytics/pulse">
    <svg aria-hidden="true" class="octicon octicon-pulse" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M11.5 8L8.8 5.4 6.6 8.5 5.5 1.6 2.38 8H0v2h3.6l.9-1.8.9 5.4L9 8.5l1.6 1.5H14V8z"/></svg>
    Pulse
</a>
  <a href="/piwik/piwik-log-analytics/graphs" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors /piwik/piwik-log-analytics/graphs">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Graphs
</a>

</nav>

    </div>
  </div>

<div class="container new-discussion-timeline experiment-repo-nav">
  <div class="repository-content">

    
          

<a href="/piwik/piwik-log-analytics/blob/f724b5d2ae0de60cd4fec2f0eb340481eda3d213/import_logs.py" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:052e8cac121c457a891fda40aa9eb55c -->

<div class="file-navigation js-zeroclipboard-container">
  
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/piwik/piwik-log-analytics/blob/142_illegal_seek/import_logs.py"
               data-name="142_illegal_seek"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                142_illegal_seek
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/piwik/piwik-log-analytics/blob/date-format-option/import_logs.py"
               data-name="date-format-option"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                date-format-option
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/piwik/piwik-log-analytics/blob/generation_time_milli/import_logs.py"
               data-name="generation_time_milli"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                generation_time_milli
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/piwik/piwik-log-analytics/blob/master/import_logs.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/piwik/piwik-log-analytics/blob/mattab-patch-1/import_logs.py"
               data-name="mattab-patch-1"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                mattab-patch-1
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

  <div class="BtnGroup float-right">
    <a href="/piwik/piwik-log-analytics/find/master"
          class="js-pjax-capture-input btn btn-sm BtnGroup-item"
          data-pjax
          data-hotkey="t">
      Find file
    </a>
    <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
  </div>
  <div class="breadcrumb js-zeroclipboard-target">
    <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/piwik/piwik-log-analytics"><span>piwik-log-analytics</span></a></span></span><span class="separator">/</span><strong class="final-path">import_logs.py</strong>
  </div>
</div>



  <div class="commit-tease">
      <span class="float-right">
        <a class="commit-tease-sha" href="/piwik/piwik-log-analytics/commit/55a410cf6fcd4249a0b6f820c6b88d56ee7cdf2d" data-pjax>
          55a410c
        </a>
        <relative-time datetime="2017-02-13T02:11:22Z">Feb 13, 2017</relative-time>
      </span>
      <div>
        <img alt="@mattab" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/466765?v=3&amp;s=40" width="20" />
        <a href="/mattab" class="user-mention" rel="contributor">mattab</a>
          <a href="/piwik/piwik-log-analytics/commit/55a410cf6fcd4249a0b6f820c6b88d56ee7cdf2d" class="message" data-pjax="true" title="user agents must be lowercase">user agents must be lowercase</a>
      </div>

    <div class="commit-tease-contributors">
      <button type="button" class="btn-link muted-link contributors-toggle" data-facebox="#blob_contributors_box">
        <strong>37</strong>
         contributors
      </button>
          <a class="avatar-link tooltipped tooltipped-s" aria-label="mattab" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=mattab"><img alt="@mattab" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/466765?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="diosmosis" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=diosmosis"><img alt="@diosmosis" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/125140?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="cbonte" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=cbonte"><img alt="@cbonte" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/433384?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="cbay" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=cbay"><img alt="@cbay" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/725049?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="tsteur" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=tsteur"><img alt="@tsteur" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/273120?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="BeezyT" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=BeezyT"><img alt="@BeezyT" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/150845?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="gregorg" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=gregorg"><img alt="@gregorg" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/541602?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="sgiehl" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=sgiehl"><img alt="@sgiehl" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/1579355?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="marcenuc" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=marcenuc"><img alt="@marcenuc" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/5284?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="ledahulevogyre" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=ledahulevogyre"><img alt="@ledahulevogyre" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/408253?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="craue" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=craue"><img alt="@craue" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/800119?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="postalservice14" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=postalservice14"><img alt="@postalservice14" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/46067?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="tzi" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=tzi"><img alt="@tzi" class="avatar" height="20" src="https://avatars3.githubusercontent.com/u/415891?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="sgjava" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=sgjava"><img alt="@sgjava" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/3740007?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="RMastop" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=RMastop"><img alt="@RMastop" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/7987117?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="Framartin" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=Framartin"><img alt="@Framartin" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/1850174?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="Kdecherf" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=Kdecherf"><img alt="@Kdecherf" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/226063?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="wronan" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=wronan"><img alt="@wronan" class="avatar" height="20" src="https://avatars2.githubusercontent.com/u/11873141?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="gregoire-astruc" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=gregoire-astruc"><img alt="@gregoire-astruc" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/494291?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="goetzk" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=goetzk"><img alt="@goetzk" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/8732490?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="halfdan" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=halfdan"><img alt="@halfdan" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/176576?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="andrejb" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=andrejb"><img alt="@andrejb" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/79672?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="da2x" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=da2x"><img alt="@da2x" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/1102886?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="cdgraff" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=cdgraff"><img alt="@cdgraff" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/1087447?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="bgrzyscc" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=bgrzyscc"><img alt="@bgrzyscc" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/5320037?v=3&amp;s=40" width="20" /> </a>
    <a class="avatar-link tooltipped tooltipped-s" aria-label="antoninblanc" href="/piwik/piwik-log-analytics/commits/master/import_logs.py?author=antoninblanc"><img alt="@antoninblanc" class="avatar" height="20" src="https://avatars0.githubusercontent.com/u/1034227?v=3&amp;s=40" width="20" /> </a>

    <button type="button" data-facebox="#blob_contributors_box" class="btn-link others-text">and others</button>

    </div>

    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header" data-facebox-id="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list" data-facebox-id="facebox-description">
          <li class="facebox-user-list-item">
            <img alt="@mattab" height="24" src="https://avatars2.githubusercontent.com/u/466765?v=3&amp;s=48" width="24" />
            <a href="/mattab">mattab</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@diosmosis" height="24" src="https://avatars1.githubusercontent.com/u/125140?v=3&amp;s=48" width="24" />
            <a href="/diosmosis">diosmosis</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@cbonte" height="24" src="https://avatars3.githubusercontent.com/u/433384?v=3&amp;s=48" width="24" />
            <a href="/cbonte">cbonte</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@cbay" height="24" src="https://avatars2.githubusercontent.com/u/725049?v=3&amp;s=48" width="24" />
            <a href="/cbay">cbay</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@tsteur" height="24" src="https://avatars3.githubusercontent.com/u/273120?v=3&amp;s=48" width="24" />
            <a href="/tsteur">tsteur</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@BeezyT" height="24" src="https://avatars3.githubusercontent.com/u/150845?v=3&amp;s=48" width="24" />
            <a href="/BeezyT">BeezyT</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@gregorg" height="24" src="https://avatars2.githubusercontent.com/u/541602?v=3&amp;s=48" width="24" />
            <a href="/gregorg">gregorg</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@sgiehl" height="24" src="https://avatars1.githubusercontent.com/u/1579355?v=3&amp;s=48" width="24" />
            <a href="/sgiehl">sgiehl</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@marcenuc" height="24" src="https://avatars2.githubusercontent.com/u/5284?v=3&amp;s=48" width="24" />
            <a href="/marcenuc">marcenuc</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@ledahulevogyre" height="24" src="https://avatars2.githubusercontent.com/u/408253?v=3&amp;s=48" width="24" />
            <a href="/ledahulevogyre">ledahulevogyre</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@craue" height="24" src="https://avatars0.githubusercontent.com/u/800119?v=3&amp;s=48" width="24" />
            <a href="/craue">craue</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@postalservice14" height="24" src="https://avatars0.githubusercontent.com/u/46067?v=3&amp;s=48" width="24" />
            <a href="/postalservice14">postalservice14</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@tzi" height="24" src="https://avatars1.githubusercontent.com/u/415891?v=3&amp;s=48" width="24" />
            <a href="/tzi">tzi</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@sgjava" height="24" src="https://avatars3.githubusercontent.com/u/3740007?v=3&amp;s=48" width="24" />
            <a href="/sgjava">sgjava</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@RMastop" height="24" src="https://avatars3.githubusercontent.com/u/7987117?v=3&amp;s=48" width="24" />
            <a href="/RMastop">RMastop</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@Framartin" height="24" src="https://avatars0.githubusercontent.com/u/1850174?v=3&amp;s=48" width="24" />
            <a href="/Framartin">Framartin</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@Kdecherf" height="24" src="https://avatars3.githubusercontent.com/u/226063?v=3&amp;s=48" width="24" />
            <a href="/Kdecherf">Kdecherf</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@wronan" height="24" src="https://avatars0.githubusercontent.com/u/11873141?v=3&amp;s=48" width="24" />
            <a href="/wronan">wronan</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@gregoire-astruc" height="24" src="https://avatars3.githubusercontent.com/u/494291?v=3&amp;s=48" width="24" />
            <a href="/gregoire-astruc">gregoire-astruc</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@goetzk" height="24" src="https://avatars2.githubusercontent.com/u/8732490?v=3&amp;s=48" width="24" />
            <a href="/goetzk">goetzk</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@halfdan" height="24" src="https://avatars3.githubusercontent.com/u/176576?v=3&amp;s=48" width="24" />
            <a href="/halfdan">halfdan</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@andrejb" height="24" src="https://avatars2.githubusercontent.com/u/79672?v=3&amp;s=48" width="24" />
            <a href="/andrejb">andrejb</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@da2x" height="24" src="https://avatars3.githubusercontent.com/u/1102886?v=3&amp;s=48" width="24" />
            <a href="/da2x">da2x</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@cdgraff" height="24" src="https://avatars2.githubusercontent.com/u/1087447?v=3&amp;s=48" width="24" />
            <a href="/cdgraff">cdgraff</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@bgrzyscc" height="24" src="https://avatars3.githubusercontent.com/u/5320037?v=3&amp;s=48" width="24" />
            <a href="/bgrzyscc">bgrzyscc</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@antoninblanc" height="24" src="https://avatars2.githubusercontent.com/u/1034227?v=3&amp;s=48" width="24" />
            <a href="/antoninblanc">antoninblanc</a>
          </li>
          <li class="facebox-user-list-item">
            <img alt="@lesensei" height="24" src="https://avatars2.githubusercontent.com/u/1148387?v=3&amp;s=48" width="24" />
            <a href="/lesensei">lesensei</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/piwik/piwik-log-analytics/raw/master/import_logs.py" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/piwik/piwik-log-analytics/blame/master/import_logs.py" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/piwik/piwik-log-analytics/commits/master/import_logs.py" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>


        <button type="button" class="btn-octicon disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
        </button>
        <button type="button" class="btn-octicon btn-octicon-danger disabled tooltipped tooltipped-nw"
          aria-label="You must be signed in to make or propose changes">
          <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
        </button>
  </div>

  <div class="file-info">
      <span class="file-mode" title="File mode">executable file</span>
      <span class="file-info-divider"></span>
      2391 lines (2026 sloc)
      <span class="file-info-divider"></span>
    92.1 KB
  </div>
</div>

  

  <div itemprop="text" class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>!/usr/bin/python</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> vim: et sw=4 ts=4:</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Piwik - free/libre analytics platform</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> @link http://piwik.org</span></td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> @license http://www.gnu.org/licenses/gpl-3.0.html GPL v3 or later</span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> @version $Id$</span></td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> For more info see: http://piwik.org/log-analytics/ and http://piwik.org/docs/log-analytics-tool-how-to/</span></td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> Requires Python 2.6 or 2.7</span></td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span></span></td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> base64</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> bz2</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> ConfigParser</td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> datetime</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> fnmatch</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> gzip</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> hashlib</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> httplib</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> inspect</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> itertools</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> logging</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> optparse</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> os.path</td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> Queue</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> re</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> sys</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> threading</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> time</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> urllib</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> urllib2</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> urlparse</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> subprocess</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> functools</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> traceback</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> socket</td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> textwrap</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line"><span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">import</span> json</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line"><span class="pl-k">except</span> <span class="pl-c1">ImportError</span>:</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">import</span> simplejson <span class="pl-k">as</span> json</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">ImportError</span>:</td>
      </tr>
      <tr>
        <td id="L50" class="blob-num js-line-number" data-line-number="50"></td>
        <td id="LC50" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> sys.version_info <span class="pl-k">&lt;</span> (<span class="pl-c1">2</span>, <span class="pl-c1">6</span>):</td>
      </tr>
      <tr>
        <td id="L51" class="blob-num js-line-number" data-line-number="51"></td>
        <td id="LC51" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> <span class="pl-k">&gt;&gt;</span> sys.stderr, <span class="pl-s"><span class="pl-pds">&#39;</span>simplejson (http://pypi.python.org/pypi/simplejson/) is required.<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L52" class="blob-num js-line-number" data-line-number="52"></td>
        <td id="LC52" class="blob-code blob-code-inner js-file-line">            sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L53" class="blob-num js-line-number" data-line-number="53"></td>
        <td id="LC53" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L54" class="blob-num js-line-number" data-line-number="54"></td>
        <td id="LC54" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L55" class="blob-num js-line-number" data-line-number="55"></td>
        <td id="LC55" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L56" class="blob-num js-line-number" data-line-number="56"></td>
        <td id="LC56" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L57" class="blob-num js-line-number" data-line-number="57"></td>
        <td id="LC57" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span># Constants.</span></td>
      </tr>
      <tr>
        <td id="L58" class="blob-num js-line-number" data-line-number="58"></td>
        <td id="LC58" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L59" class="blob-num js-line-number" data-line-number="59"></td>
        <td id="LC59" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L60" class="blob-num js-line-number" data-line-number="60"></td>
        <td id="LC60" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">STATIC_EXTENSIONS</span> <span class="pl-k">=</span> <span class="pl-c1">set</span>((</td>
      </tr>
      <tr>
        <td id="L61" class="blob-num js-line-number" data-line-number="61"></td>
        <td id="LC61" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>gif jpg jpeg png bmp ico svg svgz ttf otf eot woff woff2 class swf css js xml robots.txt webp<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L62" class="blob-num js-line-number" data-line-number="62"></td>
        <td id="LC62" class="blob-code blob-code-inner js-file-line">).split())</td>
      </tr>
      <tr>
        <td id="L63" class="blob-num js-line-number" data-line-number="63"></td>
        <td id="LC63" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L64" class="blob-num js-line-number" data-line-number="64"></td>
        <td id="LC64" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">DOWNLOAD_EXTENSIONS</span> <span class="pl-k">=</span> <span class="pl-c1">set</span>((</td>
      </tr>
      <tr>
        <td id="L65" class="blob-num js-line-number" data-line-number="65"></td>
        <td id="LC65" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>7z aac arc arj asf asx avi bin csv deb dmg doc docx exe flac flv gz gzip hqx <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L66" class="blob-num js-line-number" data-line-number="66"></td>
        <td id="LC66" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>ibooks jar json mpg mp2 mp3 mp4 mpeg mov movie msi msp odb odf odg odp <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L67" class="blob-num js-line-number" data-line-number="67"></td>
        <td id="LC67" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>ods odt ogg ogv pdf phps ppt pptx qt qtm ra ram rar rpm rtf sea sit tar tbz <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L68" class="blob-num js-line-number" data-line-number="68"></td>
        <td id="LC68" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>bz2 tbz tgz torrent txt wav webm wma wmv wpd xls xlsx xml xsd z zip <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L69" class="blob-num js-line-number" data-line-number="69"></td>
        <td id="LC69" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>azw3 epub mobi apk<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L70" class="blob-num js-line-number" data-line-number="70"></td>
        <td id="LC70" class="blob-code blob-code-inner js-file-line">).split())</td>
      </tr>
      <tr>
        <td id="L71" class="blob-num js-line-number" data-line-number="71"></td>
        <td id="LC71" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L72" class="blob-num js-line-number" data-line-number="72"></td>
        <td id="LC72" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> A good source is: http://phpbb-bots.blogspot.com/</span></td>
      </tr>
      <tr>
        <td id="L73" class="blob-num js-line-number" data-line-number="73"></td>
        <td id="LC73" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span> user agents must be lowercase</span></td>
      </tr>
      <tr>
        <td id="L74" class="blob-num js-line-number" data-line-number="74"></td>
        <td id="LC74" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">EXCLUDED_USER_AGENTS</span> <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L75" class="blob-num js-line-number" data-line-number="75"></td>
        <td id="LC75" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>adsbot-google<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L76" class="blob-num js-line-number" data-line-number="76"></td>
        <td id="LC76" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>ask jeeves<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L77" class="blob-num js-line-number" data-line-number="77"></td>
        <td id="LC77" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>baidubot<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L78" class="blob-num js-line-number" data-line-number="78"></td>
        <td id="LC78" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>bot-<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L79" class="blob-num js-line-number" data-line-number="79"></td>
        <td id="LC79" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>bot/<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L80" class="blob-num js-line-number" data-line-number="80"></td>
        <td id="LC80" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>ccooter/<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L81" class="blob-num js-line-number" data-line-number="81"></td>
        <td id="LC81" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>crawl<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L82" class="blob-num js-line-number" data-line-number="82"></td>
        <td id="LC82" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>curl<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L83" class="blob-num js-line-number" data-line-number="83"></td>
        <td id="LC83" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>echoping<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L84" class="blob-num js-line-number" data-line-number="84"></td>
        <td id="LC84" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>exabot<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L85" class="blob-num js-line-number" data-line-number="85"></td>
        <td id="LC85" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>feed<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L86" class="blob-num js-line-number" data-line-number="86"></td>
        <td id="LC86" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>googlebot<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L87" class="blob-num js-line-number" data-line-number="87"></td>
        <td id="LC87" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>ia_archiver<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L88" class="blob-num js-line-number" data-line-number="88"></td>
        <td id="LC88" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>java/<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L89" class="blob-num js-line-number" data-line-number="89"></td>
        <td id="LC89" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>libwww<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L90" class="blob-num js-line-number" data-line-number="90"></td>
        <td id="LC90" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>mediapartners-google<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L91" class="blob-num js-line-number" data-line-number="91"></td>
        <td id="LC91" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>msnbot<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L92" class="blob-num js-line-number" data-line-number="92"></td>
        <td id="LC92" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>netcraftsurvey<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L93" class="blob-num js-line-number" data-line-number="93"></td>
        <td id="LC93" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>panopta<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L94" class="blob-num js-line-number" data-line-number="94"></td>
        <td id="LC94" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>pingdom.com_bot_<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L95" class="blob-num js-line-number" data-line-number="95"></td>
        <td id="LC95" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>robot<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L96" class="blob-num js-line-number" data-line-number="96"></td>
        <td id="LC96" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>spider<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L97" class="blob-num js-line-number" data-line-number="97"></td>
        <td id="LC97" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>surveybot<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L98" class="blob-num js-line-number" data-line-number="98"></td>
        <td id="LC98" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>twiceler<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L99" class="blob-num js-line-number" data-line-number="99"></td>
        <td id="LC99" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>voilabot<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L100" class="blob-num js-line-number" data-line-number="100"></td>
        <td id="LC100" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>yahoo<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L101" class="blob-num js-line-number" data-line-number="101"></td>
        <td id="LC101" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>yandex<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L102" class="blob-num js-line-number" data-line-number="102"></td>
        <td id="LC102" class="blob-code blob-code-inner js-file-line">)</td>
      </tr>
      <tr>
        <td id="L103" class="blob-num js-line-number" data-line-number="103"></td>
        <td id="LC103" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L104" class="blob-num js-line-number" data-line-number="104"></td>
        <td id="LC104" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PIWIK_DEFAULT_MAX_ATTEMPTS</span> <span class="pl-k">=</span> <span class="pl-c1">3</span></td>
      </tr>
      <tr>
        <td id="L105" class="blob-num js-line-number" data-line-number="105"></td>
        <td id="LC105" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PIWIK_DEFAULT_DELAY_AFTER_FAILURE</span> <span class="pl-k">=</span> <span class="pl-c1">10</span></td>
      </tr>
      <tr>
        <td id="L106" class="blob-num js-line-number" data-line-number="106"></td>
        <td id="LC106" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">DEFAULT_SOCKET_TIMEOUT</span> <span class="pl-k">=</span> <span class="pl-c1">300</span></td>
      </tr>
      <tr>
        <td id="L107" class="blob-num js-line-number" data-line-number="107"></td>
        <td id="LC107" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L108" class="blob-num js-line-number" data-line-number="108"></td>
        <td id="LC108" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">PIWIK_EXPECTED_IMAGE</span> <span class="pl-k">=</span> base64.b64decode(</td>
      </tr>
      <tr>
        <td id="L109" class="blob-num js-line-number" data-line-number="109"></td>
        <td id="LC109" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>R0lGODlhAQABAIAAAAAAAAAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw==<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L110" class="blob-num js-line-number" data-line-number="110"></td>
        <td id="LC110" class="blob-code blob-code-inner js-file-line">)</td>
      </tr>
      <tr>
        <td id="L111" class="blob-num js-line-number" data-line-number="111"></td>
        <td id="LC111" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L112" class="blob-num js-line-number" data-line-number="112"></td>
        <td id="LC112" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L113" class="blob-num js-line-number" data-line-number="113"></td>
        <td id="LC113" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span># Formats.</span></td>
      </tr>
      <tr>
        <td id="L114" class="blob-num js-line-number" data-line-number="114"></td>
        <td id="LC114" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L115" class="blob-num js-line-number" data-line-number="115"></td>
        <td id="LC115" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L116" class="blob-num js-line-number" data-line-number="116"></td>
        <td id="LC116" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">BaseFormatException</span>(<span class="pl-c1">Exception</span>): <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L117" class="blob-num js-line-number" data-line-number="117"></td>
        <td id="LC117" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L118" class="blob-num js-line-number" data-line-number="118"></td>
        <td id="LC118" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">BaseFormat</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L119" class="blob-num js-line-number" data-line-number="119"></td>
        <td id="LC119" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">name</span>):</td>
      </tr>
      <tr>
        <td id="L120" class="blob-num js-line-number" data-line-number="120"></td>
        <td id="LC120" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.name <span class="pl-k">=</span> name</td>
      </tr>
      <tr>
        <td id="L121" class="blob-num js-line-number" data-line-number="121"></td>
        <td id="LC121" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.regex <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L122" class="blob-num js-line-number" data-line-number="122"></td>
        <td id="LC122" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.date_format <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%d</span>/%b/%Y:%H:%M:%S<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L123" class="blob-num js-line-number" data-line-number="123"></td>
        <td id="LC123" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L124" class="blob-num js-line-number" data-line-number="124"></td>
        <td id="LC124" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_format</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">file</span>):</td>
      </tr>
      <tr>
        <td id="L125" class="blob-num js-line-number" data-line-number="125"></td>
        <td id="LC125" class="blob-code blob-code-inner js-file-line">        line <span class="pl-k">=</span> <span class="pl-v">file</span>.readline()</td>
      </tr>
      <tr>
        <td id="L126" class="blob-num js-line-number" data-line-number="126"></td>
        <td id="LC126" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L127" class="blob-num js-line-number" data-line-number="127"></td>
        <td id="LC127" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">file</span>.seek(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L128" class="blob-num js-line-number" data-line-number="128"></td>
        <td id="LC128" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">IOError</span>:</td>
      </tr>
      <tr>
        <td id="L129" class="blob-num js-line-number" data-line-number="129"></td>
        <td id="LC129" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L130" class="blob-num js-line-number" data-line-number="130"></td>
        <td id="LC130" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L131" class="blob-num js-line-number" data-line-number="131"></td>
        <td id="LC131" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>.check_format_line(line)</td>
      </tr>
      <tr>
        <td id="L132" class="blob-num js-line-number" data-line-number="132"></td>
        <td id="LC132" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L133" class="blob-num js-line-number" data-line-number="133"></td>
        <td id="LC133" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_format_line</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">line</span>):</td>
      </tr>
      <tr>
        <td id="L134" class="blob-num js-line-number" data-line-number="134"></td>
        <td id="LC134" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L135" class="blob-num js-line-number" data-line-number="135"></td>
        <td id="LC135" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L136" class="blob-num js-line-number" data-line-number="136"></td>
        <td id="LC136" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">JsonFormat</span>(<span class="pl-e">BaseFormat</span>):</td>
      </tr>
      <tr>
        <td id="L137" class="blob-num js-line-number" data-line-number="137"></td>
        <td id="LC137" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">name</span>):</td>
      </tr>
      <tr>
        <td id="L138" class="blob-num js-line-number" data-line-number="138"></td>
        <td id="LC138" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">super</span>(JsonFormat, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>(name)</td>
      </tr>
      <tr>
        <td id="L139" class="blob-num js-line-number" data-line-number="139"></td>
        <td id="LC139" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.json <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L140" class="blob-num js-line-number" data-line-number="140"></td>
        <td id="LC140" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.date_format <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>%Y-%m-<span class="pl-c1">%d</span>T%H:%M:%S<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L141" class="blob-num js-line-number" data-line-number="141"></td>
        <td id="LC141" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L142" class="blob-num js-line-number" data-line-number="142"></td>
        <td id="LC142" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_format_line</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">line</span>):</td>
      </tr>
      <tr>
        <td id="L143" class="blob-num js-line-number" data-line-number="143"></td>
        <td id="LC143" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L144" class="blob-num js-line-number" data-line-number="144"></td>
        <td id="LC144" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.json <span class="pl-k">=</span> json.loads(line)</td>
      </tr>
      <tr>
        <td id="L145" class="blob-num js-line-number" data-line-number="145"></td>
        <td id="LC145" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L146" class="blob-num js-line-number" data-line-number="146"></td>
        <td id="LC146" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L147" class="blob-num js-line-number" data-line-number="147"></td>
        <td id="LC147" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L148" class="blob-num js-line-number" data-line-number="148"></td>
        <td id="LC148" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L149" class="blob-num js-line-number" data-line-number="149"></td>
        <td id="LC149" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">match</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">line</span>):</td>
      </tr>
      <tr>
        <td id="L150" class="blob-num js-line-number" data-line-number="150"></td>
        <td id="LC150" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L151" class="blob-num js-line-number" data-line-number="151"></td>
        <td id="LC151" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> nginx outputs malformed JSON w/ hex escapes when confronted w/ non-UTF input. we have to</span></td>
      </tr>
      <tr>
        <td id="L152" class="blob-num js-line-number" data-line-number="152"></td>
        <td id="LC152" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> workaround this by converting hex escapes in strings to unicode escapes. the conversion is naive,</span></td>
      </tr>
      <tr>
        <td id="L153" class="blob-num js-line-number" data-line-number="153"></td>
        <td id="LC153" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> so it does not take into account the string&#39;s actual encoding (which we don&#39;t have access to).</span></td>
      </tr>
      <tr>
        <td id="L154" class="blob-num js-line-number" data-line-number="154"></td>
        <td id="LC154" class="blob-code blob-code-inner js-file-line">            line <span class="pl-k">=</span> line.replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span>x<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\\</span>u00<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L155" class="blob-num js-line-number" data-line-number="155"></td>
        <td id="LC155" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L156" class="blob-num js-line-number" data-line-number="156"></td>
        <td id="LC156" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.json <span class="pl-k">=</span> json.loads(line)</td>
      </tr>
      <tr>
        <td id="L157" class="blob-num js-line-number" data-line-number="157"></td>
        <td id="LC157" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">self</span></td>
      </tr>
      <tr>
        <td id="L158" class="blob-num js-line-number" data-line-number="158"></td>
        <td id="LC158" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L159" class="blob-num js-line-number" data-line-number="159"></td>
        <td id="LC159" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.json <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L160" class="blob-num js-line-number" data-line-number="160"></td>
        <td id="LC160" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L161" class="blob-num js-line-number" data-line-number="161"></td>
        <td id="LC161" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L162" class="blob-num js-line-number" data-line-number="162"></td>
        <td id="LC162" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">key</span>):</td>
      </tr>
      <tr>
        <td id="L163" class="blob-num js-line-number" data-line-number="163"></td>
        <td id="LC163" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Some ugly patchs ...</span></td>
      </tr>
      <tr>
        <td id="L164" class="blob-num js-line-number" data-line-number="164"></td>
        <td id="LC164" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> key <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>generation_time_milli<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L165" class="blob-num js-line-number" data-line-number="165"></td>
        <td id="LC165" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.json[key] <span class="pl-k">=</span>  <span class="pl-c1">int</span>(<span class="pl-c1">float</span>(<span class="pl-c1">self</span>.json[key]) <span class="pl-k">*</span> <span class="pl-c1">1000</span>)</td>
      </tr>
      <tr>
        <td id="L166" class="blob-num js-line-number" data-line-number="166"></td>
        <td id="LC166" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Patch date format ISO 8601</span></td>
      </tr>
      <tr>
        <td id="L167" class="blob-num js-line-number" data-line-number="167"></td>
        <td id="LC167" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> key <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L168" class="blob-num js-line-number" data-line-number="168"></td>
        <td id="LC168" class="blob-code blob-code-inner js-file-line">            tz <span class="pl-k">=</span> <span class="pl-c1">self</span>.json[key][<span class="pl-c1">19</span>:]</td>
      </tr>
      <tr>
        <td id="L169" class="blob-num js-line-number" data-line-number="169"></td>
        <td id="LC169" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.json[<span class="pl-s"><span class="pl-pds">&#39;</span>timezone<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> tz.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>:<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L170" class="blob-num js-line-number" data-line-number="170"></td>
        <td id="LC170" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.json[key] <span class="pl-k">=</span> <span class="pl-c1">self</span>.json[key][:<span class="pl-c1">19</span>]</td>
      </tr>
      <tr>
        <td id="L171" class="blob-num js-line-number" data-line-number="171"></td>
        <td id="LC171" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L172" class="blob-num js-line-number" data-line-number="172"></td>
        <td id="LC172" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L173" class="blob-num js-line-number" data-line-number="173"></td>
        <td id="LC173" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">self</span>.json[key]</td>
      </tr>
      <tr>
        <td id="L174" class="blob-num js-line-number" data-line-number="174"></td>
        <td id="LC174" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L175" class="blob-num js-line-number" data-line-number="175"></td>
        <td id="LC175" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> BaseFormatException()</td>
      </tr>
      <tr>
        <td id="L176" class="blob-num js-line-number" data-line-number="176"></td>
        <td id="LC176" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L177" class="blob-num js-line-number" data-line-number="177"></td>
        <td id="LC177" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_all</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>,):</td>
      </tr>
      <tr>
        <td id="L178" class="blob-num js-line-number" data-line-number="178"></td>
        <td id="LC178" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>.json</td>
      </tr>
      <tr>
        <td id="L179" class="blob-num js-line-number" data-line-number="179"></td>
        <td id="LC179" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L180" class="blob-num js-line-number" data-line-number="180"></td>
        <td id="LC180" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">remove_ignored_groups</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">groups</span>):</td>
      </tr>
      <tr>
        <td id="L181" class="blob-num js-line-number" data-line-number="181"></td>
        <td id="LC181" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> group <span class="pl-k">in</span> groups:</td>
      </tr>
      <tr>
        <td id="L182" class="blob-num js-line-number" data-line-number="182"></td>
        <td id="LC182" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">del</span> <span class="pl-c1">self</span>.json[group]</td>
      </tr>
      <tr>
        <td id="L183" class="blob-num js-line-number" data-line-number="183"></td>
        <td id="LC183" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L184" class="blob-num js-line-number" data-line-number="184"></td>
        <td id="LC184" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">RegexFormat</span>(<span class="pl-e">BaseFormat</span>):</td>
      </tr>
      <tr>
        <td id="L185" class="blob-num js-line-number" data-line-number="185"></td>
        <td id="LC185" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L186" class="blob-num js-line-number" data-line-number="186"></td>
        <td id="LC186" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">name</span>, <span class="pl-smi">regex</span>, <span class="pl-smi">date_format</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L187" class="blob-num js-line-number" data-line-number="187"></td>
        <td id="LC187" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">super</span>(RegexFormat, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>(name)</td>
      </tr>
      <tr>
        <td id="L188" class="blob-num js-line-number" data-line-number="188"></td>
        <td id="LC188" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> regex <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L189" class="blob-num js-line-number" data-line-number="189"></td>
        <td id="LC189" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.regex <span class="pl-k">=</span> re.compile(regex)</td>
      </tr>
      <tr>
        <td id="L190" class="blob-num js-line-number" data-line-number="190"></td>
        <td id="LC190" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> date_format <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L191" class="blob-num js-line-number" data-line-number="191"></td>
        <td id="LC191" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.date_format <span class="pl-k">=</span> date_format</td>
      </tr>
      <tr>
        <td id="L192" class="blob-num js-line-number" data-line-number="192"></td>
        <td id="LC192" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.matched <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L193" class="blob-num js-line-number" data-line-number="193"></td>
        <td id="LC193" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L194" class="blob-num js-line-number" data-line-number="194"></td>
        <td id="LC194" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_format_line</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">line</span>):</td>
      </tr>
      <tr>
        <td id="L195" class="blob-num js-line-number" data-line-number="195"></td>
        <td id="LC195" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>.match(line)</td>
      </tr>
      <tr>
        <td id="L196" class="blob-num js-line-number" data-line-number="196"></td>
        <td id="LC196" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L197" class="blob-num js-line-number" data-line-number="197"></td>
        <td id="LC197" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">match</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>,<span class="pl-smi">line</span>):</td>
      </tr>
      <tr>
        <td id="L198" class="blob-num js-line-number" data-line-number="198"></td>
        <td id="LC198" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>.regex:</td>
      </tr>
      <tr>
        <td id="L199" class="blob-num js-line-number" data-line-number="199"></td>
        <td id="LC199" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L200" class="blob-num js-line-number" data-line-number="200"></td>
        <td id="LC200" class="blob-code blob-code-inner js-file-line">        match_result <span class="pl-k">=</span> <span class="pl-c1">self</span>.regex.match(line)</td>
      </tr>
      <tr>
        <td id="L201" class="blob-num js-line-number" data-line-number="201"></td>
        <td id="LC201" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> match_result:</td>
      </tr>
      <tr>
        <td id="L202" class="blob-num js-line-number" data-line-number="202"></td>
        <td id="LC202" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.matched <span class="pl-k">=</span> match_result.groupdict()</td>
      </tr>
      <tr>
        <td id="L203" class="blob-num js-line-number" data-line-number="203"></td>
        <td id="LC203" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L204" class="blob-num js-line-number" data-line-number="204"></td>
        <td id="LC204" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.matched <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L205" class="blob-num js-line-number" data-line-number="205"></td>
        <td id="LC205" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> match_result</td>
      </tr>
      <tr>
        <td id="L206" class="blob-num js-line-number" data-line-number="206"></td>
        <td id="LC206" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L207" class="blob-num js-line-number" data-line-number="207"></td>
        <td id="LC207" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">key</span>):</td>
      </tr>
      <tr>
        <td id="L208" class="blob-num js-line-number" data-line-number="208"></td>
        <td id="LC208" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L209" class="blob-num js-line-number" data-line-number="209"></td>
        <td id="LC209" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">self</span>.matched[key]</td>
      </tr>
      <tr>
        <td id="L210" class="blob-num js-line-number" data-line-number="210"></td>
        <td id="LC210" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L211" class="blob-num js-line-number" data-line-number="211"></td>
        <td id="LC211" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> BaseFormatException(<span class="pl-s"><span class="pl-pds">&quot;</span>Cannot find group &#39;<span class="pl-c1">%s</span>&#39;.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> key)</td>
      </tr>
      <tr>
        <td id="L212" class="blob-num js-line-number" data-line-number="212"></td>
        <td id="LC212" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L213" class="blob-num js-line-number" data-line-number="213"></td>
        <td id="LC213" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_all</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>,):</td>
      </tr>
      <tr>
        <td id="L214" class="blob-num js-line-number" data-line-number="214"></td>
        <td id="LC214" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>.matched</td>
      </tr>
      <tr>
        <td id="L215" class="blob-num js-line-number" data-line-number="215"></td>
        <td id="LC215" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L216" class="blob-num js-line-number" data-line-number="216"></td>
        <td id="LC216" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">remove_ignored_groups</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">groups</span>):</td>
      </tr>
      <tr>
        <td id="L217" class="blob-num js-line-number" data-line-number="217"></td>
        <td id="LC217" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> group <span class="pl-k">in</span> groups:</td>
      </tr>
      <tr>
        <td id="L218" class="blob-num js-line-number" data-line-number="218"></td>
        <td id="LC218" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">del</span> <span class="pl-c1">self</span>.matched[group]</td>
      </tr>
      <tr>
        <td id="L219" class="blob-num js-line-number" data-line-number="219"></td>
        <td id="LC219" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L220" class="blob-num js-line-number" data-line-number="220"></td>
        <td id="LC220" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">W3cExtendedFormat</span>(<span class="pl-e">RegexFormat</span>):</td>
      </tr>
      <tr>
        <td id="L221" class="blob-num js-line-number" data-line-number="221"></td>
        <td id="LC221" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L222" class="blob-num js-line-number" data-line-number="222"></td>
        <td id="LC222" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">FIELDS_LINE_PREFIX</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>#Fields: <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L223" class="blob-num js-line-number" data-line-number="223"></td>
        <td id="LC223" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L224" class="blob-num js-line-number" data-line-number="224"></td>
        <td id="LC224" class="blob-code blob-code-inner js-file-line">    fields <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L225" class="blob-num js-line-number" data-line-number="225"></td>
        <td id="LC225" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;date&gt;\d+[-\d+]+<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L226" class="blob-num js-line-number" data-line-number="226"></td>
        <td id="LC226" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>time<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>[\d+:]+)[.\d]*?<span class="pl-pds">&#39;</span></span>, <span class="pl-c"><span class="pl-c">#</span> <span class="pl-k">TODO</span> should not assume date &amp; time will be together not sure how to fix ATM.</span></td>
      </tr>
      <tr>
        <td id="L227" class="blob-num js-line-number" data-line-number="227"></td>
        <td id="LC227" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>cs-uri-stem<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;path&gt;/\S*)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L228" class="blob-num js-line-number" data-line-number="228"></td>
        <td id="LC228" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>cs-uri-query<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;query_string&gt;\S*)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L229" class="blob-num js-line-number" data-line-number="229"></td>
        <td id="LC229" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>c-ip<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>&quot;?(?P&lt;ip&gt;[\w*.:-]*)&quot;?<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L230" class="blob-num js-line-number" data-line-number="230"></td>
        <td id="LC230" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>cs(User-Agent)<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;user_agent&gt;&quot;.*?&quot;|\S*)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L231" class="blob-num js-line-number" data-line-number="231"></td>
        <td id="LC231" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>cs(Referer)<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;referrer&gt;\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L232" class="blob-num js-line-number" data-line-number="232"></td>
        <td id="LC232" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>sc-status<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;status&gt;\d+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L233" class="blob-num js-line-number" data-line-number="233"></td>
        <td id="LC233" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>sc-bytes<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;length&gt;\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L234" class="blob-num js-line-number" data-line-number="234"></td>
        <td id="LC234" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>cs-host<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;host&gt;\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L235" class="blob-num js-line-number" data-line-number="235"></td>
        <td id="LC235" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>cs-username<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;userid&gt;\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L236" class="blob-num js-line-number" data-line-number="236"></td>
        <td id="LC236" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>time-taken<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;generation_time_secs&gt;[.\d]+)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L237" class="blob-num js-line-number" data-line-number="237"></td>
        <td id="LC237" class="blob-code blob-code-inner js-file-line">    }</td>
      </tr>
      <tr>
        <td id="L238" class="blob-num js-line-number" data-line-number="238"></td>
        <td id="LC238" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L239" class="blob-num js-line-number" data-line-number="239"></td>
        <td id="LC239" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L240" class="blob-num js-line-number" data-line-number="240"></td>
        <td id="LC240" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">super</span>(W3cExtendedFormat, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>(<span class="pl-s"><span class="pl-pds">&#39;</span>w3c_extended<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">None</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>%Y-%m-<span class="pl-c1">%d</span> %H:%M:%S<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L241" class="blob-num js-line-number" data-line-number="241"></td>
        <td id="LC241" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L242" class="blob-num js-line-number" data-line-number="242"></td>
        <td id="LC242" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_format</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">file</span>):</td>
      </tr>
      <tr>
        <td id="L243" class="blob-num js-line-number" data-line-number="243"></td>
        <td id="LC243" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.create_regex(<span class="pl-v">file</span>)</td>
      </tr>
      <tr>
        <td id="L244" class="blob-num js-line-number" data-line-number="244"></td>
        <td id="LC244" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L245" class="blob-num js-line-number" data-line-number="245"></td>
        <td id="LC245" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if we couldn&#39;t create a regex, this file does not follow the W3C extended log file format</span></td>
      </tr>
      <tr>
        <td id="L246" class="blob-num js-line-number" data-line-number="246"></td>
        <td id="LC246" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>.regex:</td>
      </tr>
      <tr>
        <td id="L247" class="blob-num js-line-number" data-line-number="247"></td>
        <td id="LC247" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L248" class="blob-num js-line-number" data-line-number="248"></td>
        <td id="LC248" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">file</span>.seek(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L249" class="blob-num js-line-number" data-line-number="249"></td>
        <td id="LC249" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">IOError</span>:</td>
      </tr>
      <tr>
        <td id="L250" class="blob-num js-line-number" data-line-number="250"></td>
        <td id="LC250" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L251" class="blob-num js-line-number" data-line-number="251"></td>
        <td id="LC251" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L252" class="blob-num js-line-number" data-line-number="252"></td>
        <td id="LC252" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L253" class="blob-num js-line-number" data-line-number="253"></td>
        <td id="LC253" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L254" class="blob-num js-line-number" data-line-number="254"></td>
        <td id="LC254" class="blob-code blob-code-inner js-file-line">        first_line <span class="pl-k">=</span> <span class="pl-v">file</span>.readline()</td>
      </tr>
      <tr>
        <td id="L255" class="blob-num js-line-number" data-line-number="255"></td>
        <td id="LC255" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L256" class="blob-num js-line-number" data-line-number="256"></td>
        <td id="LC256" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L257" class="blob-num js-line-number" data-line-number="257"></td>
        <td id="LC257" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">file</span>.seek(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L258" class="blob-num js-line-number" data-line-number="258"></td>
        <td id="LC258" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">IOError</span>:</td>
      </tr>
      <tr>
        <td id="L259" class="blob-num js-line-number" data-line-number="259"></td>
        <td id="LC259" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L260" class="blob-num js-line-number" data-line-number="260"></td>
        <td id="LC260" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L261" class="blob-num js-line-number" data-line-number="261"></td>
        <td id="LC261" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">self</span>.check_format_line(first_line)</td>
      </tr>
      <tr>
        <td id="L262" class="blob-num js-line-number" data-line-number="262"></td>
        <td id="LC262" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L263" class="blob-num js-line-number" data-line-number="263"></td>
        <td id="LC263" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">create_regex</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">file</span>):</td>
      </tr>
      <tr>
        <td id="L264" class="blob-num js-line-number" data-line-number="264"></td>
        <td id="LC264" class="blob-code blob-code-inner js-file-line">        fields_line <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L265" class="blob-num js-line-number" data-line-number="265"></td>
        <td id="LC265" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.w3c_fields:</td>
      </tr>
      <tr>
        <td id="L266" class="blob-num js-line-number" data-line-number="266"></td>
        <td id="LC266" class="blob-code blob-code-inner js-file-line">            fields_line <span class="pl-k">=</span> config.options.w3c_fields</td>
      </tr>
      <tr>
        <td id="L267" class="blob-num js-line-number" data-line-number="267"></td>
        <td id="LC267" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L268" class="blob-num js-line-number" data-line-number="268"></td>
        <td id="LC268" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> collect all header lines up until the Fields: line</span></td>
      </tr>
      <tr>
        <td id="L269" class="blob-num js-line-number" data-line-number="269"></td>
        <td id="LC269" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if we&#39;re reading from stdin, we can&#39;t seek, so don&#39;t read any more than the Fields line</span></td>
      </tr>
      <tr>
        <td id="L270" class="blob-num js-line-number" data-line-number="270"></td>
        <td id="LC270" class="blob-code blob-code-inner js-file-line">        header_lines <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L271" class="blob-num js-line-number" data-line-number="271"></td>
        <td id="LC271" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> fields_line <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L272" class="blob-num js-line-number" data-line-number="272"></td>
        <td id="LC272" class="blob-code blob-code-inner js-file-line">            line <span class="pl-k">=</span> <span class="pl-v">file</span>.readline().strip()</td>
      </tr>
      <tr>
        <td id="L273" class="blob-num js-line-number" data-line-number="273"></td>
        <td id="LC273" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L274" class="blob-num js-line-number" data-line-number="274"></td>
        <td id="LC274" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> line:</td>
      </tr>
      <tr>
        <td id="L275" class="blob-num js-line-number" data-line-number="275"></td>
        <td id="LC275" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L276" class="blob-num js-line-number" data-line-number="276"></td>
        <td id="LC276" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L277" class="blob-num js-line-number" data-line-number="277"></td>
        <td id="LC277" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> line.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>#<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L278" class="blob-num js-line-number" data-line-number="278"></td>
        <td id="LC278" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L279" class="blob-num js-line-number" data-line-number="279"></td>
        <td id="LC279" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L280" class="blob-num js-line-number" data-line-number="280"></td>
        <td id="LC280" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> line.startswith(W3cExtendedFormat.<span class="pl-c1">FIELDS_LINE_PREFIX</span>):</td>
      </tr>
      <tr>
        <td id="L281" class="blob-num js-line-number" data-line-number="281"></td>
        <td id="LC281" class="blob-code blob-code-inner js-file-line">                fields_line <span class="pl-k">=</span> line</td>
      </tr>
      <tr>
        <td id="L282" class="blob-num js-line-number" data-line-number="282"></td>
        <td id="LC282" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L283" class="blob-num js-line-number" data-line-number="283"></td>
        <td id="LC283" class="blob-code blob-code-inner js-file-line">                header_lines.append(line)</td>
      </tr>
      <tr>
        <td id="L284" class="blob-num js-line-number" data-line-number="284"></td>
        <td id="LC284" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L285" class="blob-num js-line-number" data-line-number="285"></td>
        <td id="LC285" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> fields_line:</td>
      </tr>
      <tr>
        <td id="L286" class="blob-num js-line-number" data-line-number="286"></td>
        <td id="LC286" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L287" class="blob-num js-line-number" data-line-number="287"></td>
        <td id="LC287" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L288" class="blob-num js-line-number" data-line-number="288"></td>
        <td id="LC288" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> store the header lines for a later check for IIS</span></td>
      </tr>
      <tr>
        <td id="L289" class="blob-num js-line-number" data-line-number="289"></td>
        <td id="LC289" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.header_lines <span class="pl-k">=</span> header_lines</td>
      </tr>
      <tr>
        <td id="L290" class="blob-num js-line-number" data-line-number="290"></td>
        <td id="LC290" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L291" class="blob-num js-line-number" data-line-number="291"></td>
        <td id="LC291" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Parse the &#39;Fields: &#39; line to create the regex to use</span></td>
      </tr>
      <tr>
        <td id="L292" class="blob-num js-line-number" data-line-number="292"></td>
        <td id="LC292" class="blob-code blob-code-inner js-file-line">        full_regex <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L293" class="blob-num js-line-number" data-line-number="293"></td>
        <td id="LC293" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L294" class="blob-num js-line-number" data-line-number="294"></td>
        <td id="LC294" class="blob-code blob-code-inner js-file-line">        expected_fields <span class="pl-k">=</span> <span class="pl-c1">type</span>(<span class="pl-c1">self</span>).fields.copy() <span class="pl-c"><span class="pl-c">#</span> turn custom field mapping into field =&gt; regex mapping</span></td>
      </tr>
      <tr>
        <td id="L295" class="blob-num js-line-number" data-line-number="295"></td>
        <td id="LC295" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L296" class="blob-num js-line-number" data-line-number="296"></td>
        <td id="LC296" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if the --w3c-time-taken-millisecs option is used, make sure the time-taken field is interpreted as milliseconds</span></td>
      </tr>
      <tr>
        <td id="L297" class="blob-num js-line-number" data-line-number="297"></td>
        <td id="LC297" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.w3c_time_taken_in_millisecs:</td>
      </tr>
      <tr>
        <td id="L298" class="blob-num js-line-number" data-line-number="298"></td>
        <td id="LC298" class="blob-code blob-code-inner js-file-line">            expected_fields[<span class="pl-s"><span class="pl-pds">&#39;</span>time-taken<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;generation_time_milli&gt;[\d.]+)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L299" class="blob-num js-line-number" data-line-number="299"></td>
        <td id="LC299" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L300" class="blob-num js-line-number" data-line-number="300"></td>
        <td id="LC300" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> mapped_field_name, field_name <span class="pl-k">in</span> config.options.custom_w3c_fields.iteritems():</td>
      </tr>
      <tr>
        <td id="L301" class="blob-num js-line-number" data-line-number="301"></td>
        <td id="LC301" class="blob-code blob-code-inner js-file-line">            expected_fields[mapped_field_name] <span class="pl-k">=</span> expected_fields[field_name]</td>
      </tr>
      <tr>
        <td id="L302" class="blob-num js-line-number" data-line-number="302"></td>
        <td id="LC302" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">del</span> expected_fields[field_name]</td>
      </tr>
      <tr>
        <td id="L303" class="blob-num js-line-number" data-line-number="303"></td>
        <td id="LC303" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L304" class="blob-num js-line-number" data-line-number="304"></td>
        <td id="LC304" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> add custom field regexes supplied through --w3c-field-regex option</span></td>
      </tr>
      <tr>
        <td id="L305" class="blob-num js-line-number" data-line-number="305"></td>
        <td id="LC305" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> field_name, field_regex <span class="pl-k">in</span> config.options.w3c_field_regexes.iteritems():</td>
      </tr>
      <tr>
        <td id="L306" class="blob-num js-line-number" data-line-number="306"></td>
        <td id="LC306" class="blob-code blob-code-inner js-file-line">            expected_fields[field_name] <span class="pl-k">=</span> field_regex</td>
      </tr>
      <tr>
        <td id="L307" class="blob-num js-line-number" data-line-number="307"></td>
        <td id="LC307" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L308" class="blob-num js-line-number" data-line-number="308"></td>
        <td id="LC308" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Skip the &#39;Fields: &#39; prefix.</span></td>
      </tr>
      <tr>
        <td id="L309" class="blob-num js-line-number" data-line-number="309"></td>
        <td id="LC309" class="blob-code blob-code-inner js-file-line">        fields_line <span class="pl-k">=</span> fields_line[<span class="pl-c1">9</span>:].strip()</td>
      </tr>
      <tr>
        <td id="L310" class="blob-num js-line-number" data-line-number="310"></td>
        <td id="LC310" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> field <span class="pl-k">in</span> re.split(<span class="pl-s"><span class="pl-pds">&#39;</span>\s+<span class="pl-pds">&#39;</span></span>, fields_line):</td>
      </tr>
      <tr>
        <td id="L311" class="blob-num js-line-number" data-line-number="311"></td>
        <td id="LC311" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L312" class="blob-num js-line-number" data-line-number="312"></td>
        <td id="LC312" class="blob-code blob-code-inner js-file-line">                regex <span class="pl-k">=</span> expected_fields[field]</td>
      </tr>
      <tr>
        <td id="L313" class="blob-num js-line-number" data-line-number="313"></td>
        <td id="LC313" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L314" class="blob-num js-line-number" data-line-number="314"></td>
        <td id="LC314" class="blob-code blob-code-inner js-file-line">                regex <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>(?:&quot;.*?&quot;|\S+)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L315" class="blob-num js-line-number" data-line-number="315"></td>
        <td id="LC315" class="blob-code blob-code-inner js-file-line">            full_regex.append(regex)</td>
      </tr>
      <tr>
        <td id="L316" class="blob-num js-line-number" data-line-number="316"></td>
        <td id="LC316" class="blob-code blob-code-inner js-file-line">        full_regex <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>\s+<span class="pl-pds">&#39;</span></span>.join(full_regex)</td>
      </tr>
      <tr>
        <td id="L317" class="blob-num js-line-number" data-line-number="317"></td>
        <td id="LC317" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L318" class="blob-num js-line-number" data-line-number="318"></td>
        <td id="LC318" class="blob-code blob-code-inner js-file-line">        logging.debug(<span class="pl-s"><span class="pl-pds">&quot;</span>Based on &#39;Fields:&#39; line, computed regex to be <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span>, full_regex)</td>
      </tr>
      <tr>
        <td id="L319" class="blob-num js-line-number" data-line-number="319"></td>
        <td id="LC319" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L320" class="blob-num js-line-number" data-line-number="320"></td>
        <td id="LC320" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.regex <span class="pl-k">=</span> re.compile(full_regex)</td>
      </tr>
      <tr>
        <td id="L321" class="blob-num js-line-number" data-line-number="321"></td>
        <td id="LC321" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L322" class="blob-num js-line-number" data-line-number="322"></td>
        <td id="LC322" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_for_iis_option</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L323" class="blob-num js-line-number" data-line-number="323"></td>
        <td id="LC323" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> config.options.w3c_time_taken_in_millisecs <span class="pl-k">and</span> <span class="pl-c1">self</span>._is_time_taken_milli() <span class="pl-k">and</span> <span class="pl-c1">self</span>._is_iis():</td>
      </tr>
      <tr>
        <td id="L324" class="blob-num js-line-number" data-line-number="324"></td>
        <td id="LC324" class="blob-code blob-code-inner js-file-line">            logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>WARNING: IIS log file being parsed without --w3c-time-taken-milli option. IIS<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L325" class="blob-num js-line-number" data-line-number="325"></td>
        <td id="LC325" class="blob-code blob-code-inner js-file-line">                         <span class="pl-s"><span class="pl-pds">&quot;</span> stores millisecond values in the time-taken field. If your logfile does this, the aforementioned<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L326" class="blob-num js-line-number" data-line-number="326"></td>
        <td id="LC326" class="blob-code blob-code-inner js-file-line">                         <span class="pl-s"><span class="pl-pds">&quot;</span> option must be used in order to get accurate generation times.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L327" class="blob-num js-line-number" data-line-number="327"></td>
        <td id="LC327" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L328" class="blob-num js-line-number" data-line-number="328"></td>
        <td id="LC328" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_is_iis</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L329" class="blob-num js-line-number" data-line-number="329"></td>
        <td id="LC329" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">len</span>([line <span class="pl-k">for</span> line <span class="pl-k">in</span> <span class="pl-c1">self</span>.header_lines <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>internet information services<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> line.lower() <span class="pl-k">or</span> <span class="pl-s"><span class="pl-pds">&#39;</span>iis<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> line.lower()]) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L330" class="blob-num js-line-number" data-line-number="330"></td>
        <td id="LC330" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L331" class="blob-num js-line-number" data-line-number="331"></td>
        <td id="LC331" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_is_time_taken_milli</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L332" class="blob-num js-line-number" data-line-number="332"></td>
        <td id="LC332" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>generation_time_milli<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.regex.pattern</td>
      </tr>
      <tr>
        <td id="L333" class="blob-num js-line-number" data-line-number="333"></td>
        <td id="LC333" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L334" class="blob-num js-line-number" data-line-number="334"></td>
        <td id="LC334" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">IisFormat</span>(<span class="pl-e">W3cExtendedFormat</span>):</td>
      </tr>
      <tr>
        <td id="L335" class="blob-num js-line-number" data-line-number="335"></td>
        <td id="LC335" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L336" class="blob-num js-line-number" data-line-number="336"></td>
        <td id="LC336" class="blob-code blob-code-inner js-file-line">    fields <span class="pl-k">=</span> W3cExtendedFormat.fields.copy()</td>
      </tr>
      <tr>
        <td id="L337" class="blob-num js-line-number" data-line-number="337"></td>
        <td id="LC337" class="blob-code blob-code-inner js-file-line">    fields.update({</td>
      </tr>
      <tr>
        <td id="L338" class="blob-num js-line-number" data-line-number="338"></td>
        <td id="LC338" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>time-taken<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;generation_time_milli&gt;[.\d]+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L339" class="blob-num js-line-number" data-line-number="339"></td>
        <td id="LC339" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>sc-win32-status<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;__win32_status&gt;\S+)<span class="pl-pds">&#39;</span></span> <span class="pl-c"><span class="pl-c">#</span> this group is useless for log importing, but capturing it</span></td>
      </tr>
      <tr>
        <td id="L340" class="blob-num js-line-number" data-line-number="340"></td>
        <td id="LC340" class="blob-code blob-code-inner js-file-line">                                                     <span class="pl-c"><span class="pl-c">#</span> will ensure we always select IIS for the format instead of</span></td>
      </tr>
      <tr>
        <td id="L341" class="blob-num js-line-number" data-line-number="341"></td>
        <td id="LC341" class="blob-code blob-code-inner js-file-line">                                                     <span class="pl-c"><span class="pl-c">#</span> W3C logs when detecting the format. This way there will be</span></td>
      </tr>
      <tr>
        <td id="L342" class="blob-num js-line-number" data-line-number="342"></td>
        <td id="LC342" class="blob-code blob-code-inner js-file-line">                                                     <span class="pl-c"><span class="pl-c">#</span> less accidental importing of IIS logs w/o --w3c-time-taken-milli.</span></td>
      </tr>
      <tr>
        <td id="L343" class="blob-num js-line-number" data-line-number="343"></td>
        <td id="LC343" class="blob-code blob-code-inner js-file-line">    })</td>
      </tr>
      <tr>
        <td id="L344" class="blob-num js-line-number" data-line-number="344"></td>
        <td id="LC344" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L345" class="blob-num js-line-number" data-line-number="345"></td>
        <td id="LC345" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L346" class="blob-num js-line-number" data-line-number="346"></td>
        <td id="LC346" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">super</span>(IisFormat, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>()</td>
      </tr>
      <tr>
        <td id="L347" class="blob-num js-line-number" data-line-number="347"></td>
        <td id="LC347" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L348" class="blob-num js-line-number" data-line-number="348"></td>
        <td id="LC348" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>iis<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L349" class="blob-num js-line-number" data-line-number="349"></td>
        <td id="LC349" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L350" class="blob-num js-line-number" data-line-number="350"></td>
        <td id="LC350" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">ShoutcastFormat</span>(<span class="pl-e">W3cExtendedFormat</span>):</td>
      </tr>
      <tr>
        <td id="L351" class="blob-num js-line-number" data-line-number="351"></td>
        <td id="LC351" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L352" class="blob-num js-line-number" data-line-number="352"></td>
        <td id="LC352" class="blob-code blob-code-inner js-file-line">    fields <span class="pl-k">=</span> W3cExtendedFormat.fields.copy()</td>
      </tr>
      <tr>
        <td id="L353" class="blob-num js-line-number" data-line-number="353"></td>
        <td id="LC353" class="blob-code blob-code-inner js-file-line">    fields.update({</td>
      </tr>
      <tr>
        <td id="L354" class="blob-num js-line-number" data-line-number="354"></td>
        <td id="LC354" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>c-status<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;status&gt;\d+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L355" class="blob-num js-line-number" data-line-number="355"></td>
        <td id="LC355" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>x-duration<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;generation_time_secs&gt;[.\d]+)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L356" class="blob-num js-line-number" data-line-number="356"></td>
        <td id="LC356" class="blob-code blob-code-inner js-file-line">    })</td>
      </tr>
      <tr>
        <td id="L357" class="blob-num js-line-number" data-line-number="357"></td>
        <td id="LC357" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L358" class="blob-num js-line-number" data-line-number="358"></td>
        <td id="LC358" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L359" class="blob-num js-line-number" data-line-number="359"></td>
        <td id="LC359" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">super</span>(ShoutcastFormat, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>()</td>
      </tr>
      <tr>
        <td id="L360" class="blob-num js-line-number" data-line-number="360"></td>
        <td id="LC360" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L361" class="blob-num js-line-number" data-line-number="361"></td>
        <td id="LC361" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>shoutcast<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L362" class="blob-num js-line-number" data-line-number="362"></td>
        <td id="LC362" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L363" class="blob-num js-line-number" data-line-number="363"></td>
        <td id="LC363" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">key</span>):</td>
      </tr>
      <tr>
        <td id="L364" class="blob-num js-line-number" data-line-number="364"></td>
        <td id="LC364" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> key <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>user_agent<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L365" class="blob-num js-line-number" data-line-number="365"></td>
        <td id="LC365" class="blob-code blob-code-inner js-file-line">            user_agent <span class="pl-k">=</span> <span class="pl-c1">super</span>(ShoutcastFormat, <span class="pl-c1">self</span>).get(key)</td>
      </tr>
      <tr>
        <td id="L366" class="blob-num js-line-number" data-line-number="366"></td>
        <td id="LC366" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> urllib2.unquote(user_agent)</td>
      </tr>
      <tr>
        <td id="L367" class="blob-num js-line-number" data-line-number="367"></td>
        <td id="LC367" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L368" class="blob-num js-line-number" data-line-number="368"></td>
        <td id="LC368" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">super</span>(ShoutcastFormat, <span class="pl-c1">self</span>).get(key)</td>
      </tr>
      <tr>
        <td id="L369" class="blob-num js-line-number" data-line-number="369"></td>
        <td id="LC369" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L370" class="blob-num js-line-number" data-line-number="370"></td>
        <td id="LC370" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">AmazonCloudFrontFormat</span>(<span class="pl-e">W3cExtendedFormat</span>):</td>
      </tr>
      <tr>
        <td id="L371" class="blob-num js-line-number" data-line-number="371"></td>
        <td id="LC371" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L372" class="blob-num js-line-number" data-line-number="372"></td>
        <td id="LC372" class="blob-code blob-code-inner js-file-line">    fields <span class="pl-k">=</span> W3cExtendedFormat.fields.copy()</td>
      </tr>
      <tr>
        <td id="L373" class="blob-num js-line-number" data-line-number="373"></td>
        <td id="LC373" class="blob-code blob-code-inner js-file-line">    fields.update({</td>
      </tr>
      <tr>
        <td id="L374" class="blob-num js-line-number" data-line-number="374"></td>
        <td id="LC374" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>x-event<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;event_action&gt;\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L375" class="blob-num js-line-number" data-line-number="375"></td>
        <td id="LC375" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>x-sname<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;event_name&gt;\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L376" class="blob-num js-line-number" data-line-number="376"></td>
        <td id="LC376" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>cs-uri-stem<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?:rtmp:/)?(?P&lt;path&gt;/\S*)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L377" class="blob-num js-line-number" data-line-number="377"></td>
        <td id="LC377" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>c-user-agent<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;user_agent&gt;&quot;.*?&quot;|\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L378" class="blob-num js-line-number" data-line-number="378"></td>
        <td id="LC378" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L379" class="blob-num js-line-number" data-line-number="379"></td>
        <td id="LC379" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> following are present to match cloudfront instead of W3C when we know it&#39;s cloudfront</span></td>
      </tr>
      <tr>
        <td id="L380" class="blob-num js-line-number" data-line-number="380"></td>
        <td id="LC380" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>x-edge-location<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;x_edge_location&gt;&quot;.*?&quot;|\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L381" class="blob-num js-line-number" data-line-number="381"></td>
        <td id="LC381" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>x-edge-result-type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;x_edge_result_type&gt;&quot;.*?&quot;|\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L382" class="blob-num js-line-number" data-line-number="382"></td>
        <td id="LC382" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>x-edge-request-id<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;x_edge_request_id&gt;&quot;.*?&quot;|\S+)<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L383" class="blob-num js-line-number" data-line-number="383"></td>
        <td id="LC383" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&#39;</span>x-host-header<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;x_host_header&gt;&quot;.*?&quot;|\S+)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L384" class="blob-num js-line-number" data-line-number="384"></td>
        <td id="LC384" class="blob-code blob-code-inner js-file-line">    })</td>
      </tr>
      <tr>
        <td id="L385" class="blob-num js-line-number" data-line-number="385"></td>
        <td id="LC385" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L386" class="blob-num js-line-number" data-line-number="386"></td>
        <td id="LC386" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L387" class="blob-num js-line-number" data-line-number="387"></td>
        <td id="LC387" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">super</span>(AmazonCloudFrontFormat, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>()</td>
      </tr>
      <tr>
        <td id="L388" class="blob-num js-line-number" data-line-number="388"></td>
        <td id="LC388" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L389" class="blob-num js-line-number" data-line-number="389"></td>
        <td id="LC389" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.name <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>amazon_cloudfront<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L390" class="blob-num js-line-number" data-line-number="390"></td>
        <td id="LC390" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L391" class="blob-num js-line-number" data-line-number="391"></td>
        <td id="LC391" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">key</span>):</td>
      </tr>
      <tr>
        <td id="L392" class="blob-num js-line-number" data-line-number="392"></td>
        <td id="LC392" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> key <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>event_category<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-s"><span class="pl-pds">&#39;</span>event_category<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.matched:</td>
      </tr>
      <tr>
        <td id="L393" class="blob-num js-line-number" data-line-number="393"></td>
        <td id="LC393" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>cloudfront_rtmp<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L394" class="blob-num js-line-number" data-line-number="394"></td>
        <td id="LC394" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> key <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.matched:</td>
      </tr>
      <tr>
        <td id="L395" class="blob-num js-line-number" data-line-number="395"></td>
        <td id="LC395" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>200<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L396" class="blob-num js-line-number" data-line-number="396"></td>
        <td id="LC396" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> key <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>user_agent<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L397" class="blob-num js-line-number" data-line-number="397"></td>
        <td id="LC397" class="blob-code blob-code-inner js-file-line">            user_agent <span class="pl-k">=</span> <span class="pl-c1">super</span>(AmazonCloudFrontFormat, <span class="pl-c1">self</span>).get(key)</td>
      </tr>
      <tr>
        <td id="L398" class="blob-num js-line-number" data-line-number="398"></td>
        <td id="LC398" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> urllib2.unquote(user_agent)</td>
      </tr>
      <tr>
        <td id="L399" class="blob-num js-line-number" data-line-number="399"></td>
        <td id="LC399" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L400" class="blob-num js-line-number" data-line-number="400"></td>
        <td id="LC400" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">super</span>(AmazonCloudFrontFormat, <span class="pl-c1">self</span>).get(key)</td>
      </tr>
      <tr>
        <td id="L401" class="blob-num js-line-number" data-line-number="401"></td>
        <td id="LC401" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L402" class="blob-num js-line-number" data-line-number="402"></td>
        <td id="LC402" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">_HOST_PREFIX</span> <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;host&gt;[\w\-\.]*)(?::\d+)?\s+<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L403" class="blob-num js-line-number" data-line-number="403"></td>
        <td id="LC403" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">_COMMON_LOG_FORMAT</span> <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L404" class="blob-num js-line-number" data-line-number="404"></td>
        <td id="LC404" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;ip&gt;\S+)\s+\S+\s+(?P&lt;userid&gt;\S+)\s+\[(?P&lt;date&gt;.*?)\s+(?P&lt;timezone&gt;.*?)\]\s+<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L405" class="blob-num js-line-number" data-line-number="405"></td>
        <td id="LC405" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>&quot;\S+\s+(?P&lt;path&gt;.*?)\s+\S+&quot;\s+(?P&lt;status&gt;\S+)\s+(?P&lt;length&gt;\S+)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L406" class="blob-num js-line-number" data-line-number="406"></td>
        <td id="LC406" class="blob-code blob-code-inner js-file-line">)</td>
      </tr>
      <tr>
        <td id="L407" class="blob-num js-line-number" data-line-number="407"></td>
        <td id="LC407" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">_NCSA_EXTENDED_LOG_FORMAT</span> <span class="pl-k">=</span> (<span class="pl-c1">_COMMON_LOG_FORMAT</span> <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L408" class="blob-num js-line-number" data-line-number="408"></td>
        <td id="LC408" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>\s+&quot;(?P&lt;referrer&gt;.*?)&quot;\s+&quot;(?P&lt;user_agent&gt;.*?)&quot;<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L409" class="blob-num js-line-number" data-line-number="409"></td>
        <td id="LC409" class="blob-code blob-code-inner js-file-line">)</td>
      </tr>
      <tr>
        <td id="L410" class="blob-num js-line-number" data-line-number="410"></td>
        <td id="LC410" class="blob-code blob-code-inner js-file-line">_S3_LOG_FORMAT <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L411" class="blob-num js-line-number" data-line-number="411"></td>
        <td id="LC411" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>\S+\s+(?P&lt;host&gt;\S+)\s+\[(?P&lt;date&gt;.*?)\s+(?P&lt;timezone&gt;.*?)\]\s+(?P&lt;ip&gt;\S+)\s+<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L412" class="blob-num js-line-number" data-line-number="412"></td>
        <td id="LC412" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>\S+\s+\S+\s+\S+\s+\S+\s+&quot;\S+\s+(?P&lt;path&gt;.*?)\s+\S+&quot;\s+(?P&lt;status&gt;\S+)\s+\S+\s+(?P&lt;length&gt;\S+)\s+<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L413" class="blob-num js-line-number" data-line-number="413"></td>
        <td id="LC413" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>\S+\s+\S+\s+\S+\s+&quot;(?P&lt;referrer&gt;.*?)&quot;\s+&quot;(?P&lt;user_agent&gt;.*?)&quot;<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L414" class="blob-num js-line-number" data-line-number="414"></td>
        <td id="LC414" class="blob-code blob-code-inner js-file-line">)</td>
      </tr>
      <tr>
        <td id="L415" class="blob-num js-line-number" data-line-number="415"></td>
        <td id="LC415" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">_ICECAST2_LOG_FORMAT</span> <span class="pl-k">=</span> ( <span class="pl-c1">_NCSA_EXTENDED_LOG_FORMAT</span> <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L416" class="blob-num js-line-number" data-line-number="416"></td>
        <td id="LC416" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>\s+(?P&lt;session_time&gt;\S+)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L417" class="blob-num js-line-number" data-line-number="417"></td>
        <td id="LC417" class="blob-code blob-code-inner js-file-line">)</td>
      </tr>
      <tr>
        <td id="L418" class="blob-num js-line-number" data-line-number="418"></td>
        <td id="LC418" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">_ELB_LOG_FORMAT</span> <span class="pl-k">=</span> (</td>
      </tr>
      <tr>
        <td id="L419" class="blob-num js-line-number" data-line-number="419"></td>
        <td id="LC419" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;date&gt;[0-9-]+T[0-9:]+)\.\S+\s+\S+\s+(?P&lt;ip&gt;\S+):\d+\s+\S+:\d+\s+\S+\s+(?P&lt;generation_time_secs&gt;\S+)\s+\S+\s+<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L420" class="blob-num js-line-number" data-line-number="420"></td>
        <td id="LC420" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;status&gt;\S+)\s+\S+\s+\S+\s+(?P&lt;length&gt;\S+)\s+<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L421" class="blob-num js-line-number" data-line-number="421"></td>
        <td id="LC421" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>&quot;\S+\s+\w+:\/\/(?P&lt;host&gt;[\w\-\.]*):\d+(?P&lt;path&gt;\/\S*)\s+[^&quot;]+&quot;\s+&quot;(?P&lt;user_agent&gt;[^&quot;]+)&quot;\s+\S+\s+\S+<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L422" class="blob-num js-line-number" data-line-number="422"></td>
        <td id="LC422" class="blob-code blob-code-inner js-file-line">)</td>
      </tr>
      <tr>
        <td id="L423" class="blob-num js-line-number" data-line-number="423"></td>
        <td id="LC423" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L424" class="blob-num js-line-number" data-line-number="424"></td>
        <td id="LC424" class="blob-code blob-code-inner js-file-line"><span class="pl-c1">FORMATS</span> <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L425" class="blob-num js-line-number" data-line-number="425"></td>
        <td id="LC425" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>common<span class="pl-pds">&#39;</span></span>: RegexFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>common<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">_COMMON_LOG_FORMAT</span>),</td>
      </tr>
      <tr>
        <td id="L426" class="blob-num js-line-number" data-line-number="426"></td>
        <td id="LC426" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>common_vhost<span class="pl-pds">&#39;</span></span>: RegexFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>common_vhost<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">_HOST_PREFIX</span> <span class="pl-k">+</span> <span class="pl-c1">_COMMON_LOG_FORMAT</span>),</td>
      </tr>
      <tr>
        <td id="L427" class="blob-num js-line-number" data-line-number="427"></td>
        <td id="LC427" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>ncsa_extended<span class="pl-pds">&#39;</span></span>: RegexFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>ncsa_extended<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">_NCSA_EXTENDED_LOG_FORMAT</span>),</td>
      </tr>
      <tr>
        <td id="L428" class="blob-num js-line-number" data-line-number="428"></td>
        <td id="LC428" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>common_complete<span class="pl-pds">&#39;</span></span>: RegexFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>common_complete<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">_HOST_PREFIX</span> <span class="pl-k">+</span> <span class="pl-c1">_NCSA_EXTENDED_LOG_FORMAT</span>),</td>
      </tr>
      <tr>
        <td id="L429" class="blob-num js-line-number" data-line-number="429"></td>
        <td id="LC429" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>w3c_extended<span class="pl-pds">&#39;</span></span>: W3cExtendedFormat(),</td>
      </tr>
      <tr>
        <td id="L430" class="blob-num js-line-number" data-line-number="430"></td>
        <td id="LC430" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>amazon_cloudfront<span class="pl-pds">&#39;</span></span>: AmazonCloudFrontFormat(),</td>
      </tr>
      <tr>
        <td id="L431" class="blob-num js-line-number" data-line-number="431"></td>
        <td id="LC431" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>iis<span class="pl-pds">&#39;</span></span>: IisFormat(),</td>
      </tr>
      <tr>
        <td id="L432" class="blob-num js-line-number" data-line-number="432"></td>
        <td id="LC432" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>shoutcast<span class="pl-pds">&#39;</span></span>: ShoutcastFormat(),</td>
      </tr>
      <tr>
        <td id="L433" class="blob-num js-line-number" data-line-number="433"></td>
        <td id="LC433" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>s3<span class="pl-pds">&#39;</span></span>: RegexFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>s3<span class="pl-pds">&#39;</span></span>, _S3_LOG_FORMAT),</td>
      </tr>
      <tr>
        <td id="L434" class="blob-num js-line-number" data-line-number="434"></td>
        <td id="LC434" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>icecast2<span class="pl-pds">&#39;</span></span>: RegexFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>icecast2<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">_ICECAST2_LOG_FORMAT</span>),</td>
      </tr>
      <tr>
        <td id="L435" class="blob-num js-line-number" data-line-number="435"></td>
        <td id="LC435" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>elb<span class="pl-pds">&#39;</span></span>: RegexFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>elb<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">_ELB_LOG_FORMAT</span>, <span class="pl-s"><span class="pl-pds">&#39;</span>%Y-%m-<span class="pl-c1">%d</span>T%H:%M:%S<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L436" class="blob-num js-line-number" data-line-number="436"></td>
        <td id="LC436" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>nginx_json<span class="pl-pds">&#39;</span></span>: JsonFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>nginx_json<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L437" class="blob-num js-line-number" data-line-number="437"></td>
        <td id="LC437" class="blob-code blob-code-inner js-file-line">}</td>
      </tr>
      <tr>
        <td id="L438" class="blob-num js-line-number" data-line-number="438"></td>
        <td id="LC438" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L439" class="blob-num js-line-number" data-line-number="439"></td>
        <td id="LC439" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L440" class="blob-num js-line-number" data-line-number="440"></td>
        <td id="LC440" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span># Code.</span></td>
      </tr>
      <tr>
        <td id="L441" class="blob-num js-line-number" data-line-number="441"></td>
        <td id="LC441" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L442" class="blob-num js-line-number" data-line-number="442"></td>
        <td id="LC442" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L443" class="blob-num js-line-number" data-line-number="443"></td>
        <td id="LC443" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Configuration</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L444" class="blob-num js-line-number" data-line-number="444"></td>
        <td id="LC444" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L445" class="blob-num js-line-number" data-line-number="445"></td>
        <td id="LC445" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Stores all the configuration options by reading sys.argv and parsing,</span></td>
      </tr>
      <tr>
        <td id="L446" class="blob-num js-line-number" data-line-number="446"></td>
        <td id="LC446" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    if needed, the config.inc.php.</span></td>
      </tr>
      <tr>
        <td id="L447" class="blob-num js-line-number" data-line-number="447"></td>
        <td id="LC447" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L448" class="blob-num js-line-number" data-line-number="448"></td>
        <td id="LC448" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    It has 2 attributes: options and filenames.</span></td>
      </tr>
      <tr>
        <td id="L449" class="blob-num js-line-number" data-line-number="449"></td>
        <td id="LC449" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L450" class="blob-num js-line-number" data-line-number="450"></td>
        <td id="LC450" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L451" class="blob-num js-line-number" data-line-number="451"></td>
        <td id="LC451" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">class</span> <span class="pl-en">Error</span>(<span class="pl-c1">Exception</span>):</td>
      </tr>
      <tr>
        <td id="L452" class="blob-num js-line-number" data-line-number="452"></td>
        <td id="LC452" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L453" class="blob-num js-line-number" data-line-number="453"></td>
        <td id="LC453" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L454" class="blob-num js-line-number" data-line-number="454"></td>
        <td id="LC454" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_create_parser</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L455" class="blob-num js-line-number" data-line-number="455"></td>
        <td id="LC455" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L456" class="blob-num js-line-number" data-line-number="456"></td>
        <td id="LC456" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Initialize and return the OptionParser instance.</span></td>
      </tr>
      <tr>
        <td id="L457" class="blob-num js-line-number" data-line-number="457"></td>
        <td id="LC457" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L458" class="blob-num js-line-number" data-line-number="458"></td>
        <td id="LC458" class="blob-code blob-code-inner js-file-line">        option_parser <span class="pl-k">=</span> optparse.OptionParser(</td>
      </tr>
      <tr>
        <td id="L459" class="blob-num js-line-number" data-line-number="459"></td>
        <td id="LC459" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">usage</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>Usage: %prog [options] log_file [ log_file [...] ]<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L460" class="blob-num js-line-number" data-line-number="460"></td>
        <td id="LC460" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">description</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Import HTTP access logs to Piwik. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L461" class="blob-num js-line-number" data-line-number="461"></td>
        <td id="LC461" class="blob-code blob-code-inner js-file-line">                         <span class="pl-s"><span class="pl-pds">&quot;</span>log_file is the path to a server access log file (uncompressed, .gz, .bz2, or specify - to read from stdin). <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L462" class="blob-num js-line-number" data-line-number="462"></td>
        <td id="LC462" class="blob-code blob-code-inner js-file-line">                         <span class="pl-s"><span class="pl-pds">&quot;</span> By default, the script will try to produce clean reports and will exclude bots, static files, discard http error and redirects, etc. This is customizable, see below.<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L463" class="blob-num js-line-number" data-line-number="463"></td>
        <td id="LC463" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">epilog</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>About Piwik Server Log Analytics: http://piwik.org/log-analytics/ <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L464" class="blob-num js-line-number" data-line-number="464"></td>
        <td id="LC464" class="blob-code blob-code-inner js-file-line">                   <span class="pl-s"><span class="pl-pds">&quot;</span>              Found a bug? Please create a ticket in http://dev.piwik.org/ <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L465" class="blob-num js-line-number" data-line-number="465"></td>
        <td id="LC465" class="blob-code blob-code-inner js-file-line">                   <span class="pl-s"><span class="pl-pds">&quot;</span>              Please send your suggestions or successful user story to hello@piwik.org <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L466" class="blob-num js-line-number" data-line-number="466"></td>
        <td id="LC466" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L467" class="blob-num js-line-number" data-line-number="467"></td>
        <td id="LC467" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L468" class="blob-num js-line-number" data-line-number="468"></td>
        <td id="LC468" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Basic auth user</span></td>
      </tr>
      <tr>
        <td id="L469" class="blob-num js-line-number" data-line-number="469"></td>
        <td id="LC469" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L470" class="blob-num js-line-number" data-line-number="470"></td>
        <td id="LC470" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--auth-user<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>auth_user<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L471" class="blob-num js-line-number" data-line-number="471"></td>
        <td id="LC471" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Basic auth user<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L472" class="blob-num js-line-number" data-line-number="472"></td>
        <td id="LC472" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L473" class="blob-num js-line-number" data-line-number="473"></td>
        <td id="LC473" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Basic auth password</span></td>
      </tr>
      <tr>
        <td id="L474" class="blob-num js-line-number" data-line-number="474"></td>
        <td id="LC474" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L475" class="blob-num js-line-number" data-line-number="475"></td>
        <td id="LC475" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--auth-password<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>auth_password<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L476" class="blob-num js-line-number" data-line-number="476"></td>
        <td id="LC476" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Basic auth password<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L477" class="blob-num js-line-number" data-line-number="477"></td>
        <td id="LC477" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L478" class="blob-num js-line-number" data-line-number="478"></td>
        <td id="LC478" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L479" class="blob-num js-line-number" data-line-number="479"></td>
        <td id="LC479" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--debug<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>-d<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>debug<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>count<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L480" class="blob-num js-line-number" data-line-number="480"></td>
        <td id="LC480" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Enable debug output (specify multiple times for more verbose)<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L481" class="blob-num js-line-number" data-line-number="481"></td>
        <td id="LC481" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L482" class="blob-num js-line-number" data-line-number="482"></td>
        <td id="LC482" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L483" class="blob-num js-line-number" data-line-number="483"></td>
        <td id="LC483" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--debug-tracker<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>debug_tracker<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L484" class="blob-num js-line-number" data-line-number="484"></td>
        <td id="LC484" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Appends &amp;debug=1 to tracker requests and prints out the result so the tracker can be debugged. If <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L485" class="blob-num js-line-number" data-line-number="485"></td>
        <td id="LC485" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>using the log importer results in errors with the tracker or improperly recorded visits, this option can <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L486" class="blob-num js-line-number" data-line-number="486"></td>
        <td id="LC486" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>be used to find out what the tracker is doing wrong. To see debug tracker output, you must also set the <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L487" class="blob-num js-line-number" data-line-number="487"></td>
        <td id="LC487" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>[Tracker] debug_on_demand INI config to 1 in your Piwik&#39;s config.ini.php file.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L488" class="blob-num js-line-number" data-line-number="488"></td>
        <td id="LC488" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L489" class="blob-num js-line-number" data-line-number="489"></td>
        <td id="LC489" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L490" class="blob-num js-line-number" data-line-number="490"></td>
        <td id="LC490" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--debug-request-limit<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>debug_request_limit<span class="pl-pds">&#39;</span></span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L491" class="blob-num js-line-number" data-line-number="491"></td>
        <td id="LC491" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Debug option that will exit after N requests are parsed. Can be used w/ --debug-tracker to limit the <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L492" class="blob-num js-line-number" data-line-number="492"></td>
        <td id="LC492" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>output of a large log file.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L493" class="blob-num js-line-number" data-line-number="493"></td>
        <td id="LC493" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L494" class="blob-num js-line-number" data-line-number="494"></td>
        <td id="LC494" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L495" class="blob-num js-line-number" data-line-number="495"></td>
        <td id="LC495" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--url<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>piwik_url<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L496" class="blob-num js-line-number" data-line-number="496"></td>
        <td id="LC496" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>REQUIRED Your Piwik server URL, eg. http://example.com/piwik/ or http://analytics.example.net<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L497" class="blob-num js-line-number" data-line-number="497"></td>
        <td id="LC497" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L498" class="blob-num js-line-number" data-line-number="498"></td>
        <td id="LC498" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L499" class="blob-num js-line-number" data-line-number="499"></td>
        <td id="LC499" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--api-url<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>piwik_api_url<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L500" class="blob-num js-line-number" data-line-number="500"></td>
        <td id="LC500" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>This URL will be used to send API requests (use it if your tracker URL differs from UI/API url), <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L501" class="blob-num js-line-number" data-line-number="501"></td>
        <td id="LC501" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>eg. http://other-example.com/piwik/ or http://analytics-api.example.net<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L502" class="blob-num js-line-number" data-line-number="502"></td>
        <td id="LC502" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L503" class="blob-num js-line-number" data-line-number="503"></td>
        <td id="LC503" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L504" class="blob-num js-line-number" data-line-number="504"></td>
        <td id="LC504" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--dry-run<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dry_run<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L505" class="blob-num js-line-number" data-line-number="505"></td>
        <td id="LC505" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L506" class="blob-num js-line-number" data-line-number="506"></td>
        <td id="LC506" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Perform a trial run with no tracking data being inserted into Piwik<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L507" class="blob-num js-line-number" data-line-number="507"></td>
        <td id="LC507" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L508" class="blob-num js-line-number" data-line-number="508"></td>
        <td id="LC508" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L509" class="blob-num js-line-number" data-line-number="509"></td>
        <td id="LC509" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--show-progress<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>show_progress<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L510" class="blob-num js-line-number" data-line-number="510"></td>
        <td id="LC510" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span>os.isatty(sys.stdout.fileno()),</td>
      </tr>
      <tr>
        <td id="L511" class="blob-num js-line-number" data-line-number="511"></td>
        <td id="LC511" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Print a progress report X seconds (default: 1, use --show-progress-delay to override)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L512" class="blob-num js-line-number" data-line-number="512"></td>
        <td id="LC512" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L513" class="blob-num js-line-number" data-line-number="513"></td>
        <td id="LC513" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L514" class="blob-num js-line-number" data-line-number="514"></td>
        <td id="LC514" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--show-progress-delay<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>show_progress_delay<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L515" class="blob-num js-line-number" data-line-number="515"></td>
        <td id="LC515" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">1</span>,</td>
      </tr>
      <tr>
        <td id="L516" class="blob-num js-line-number" data-line-number="516"></td>
        <td id="LC516" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Change the default progress delay<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L517" class="blob-num js-line-number" data-line-number="517"></td>
        <td id="LC517" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L518" class="blob-num js-line-number" data-line-number="518"></td>
        <td id="LC518" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L519" class="blob-num js-line-number" data-line-number="519"></td>
        <td id="LC519" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--add-sites-new-hosts<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>add_sites_new_hosts<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L520" class="blob-num js-line-number" data-line-number="520"></td>
        <td id="LC520" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L521" class="blob-num js-line-number" data-line-number="521"></td>
        <td id="LC521" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>When a hostname is found in the log file, but not matched to any website <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L522" class="blob-num js-line-number" data-line-number="522"></td>
        <td id="LC522" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>in Piwik, automatically create a new website in Piwik with this hostname to <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L523" class="blob-num js-line-number" data-line-number="523"></td>
        <td id="LC523" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>import the logs<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L524" class="blob-num js-line-number" data-line-number="524"></td>
        <td id="LC524" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L525" class="blob-num js-line-number" data-line-number="525"></td>
        <td id="LC525" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L526" class="blob-num js-line-number" data-line-number="526"></td>
        <td id="LC526" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--idsite<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>site_id<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L527" class="blob-num js-line-number" data-line-number="527"></td>
        <td id="LC527" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span> (<span class="pl-s"><span class="pl-pds">&quot;</span>When specified, <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L528" class="blob-num js-line-number" data-line-number="528"></td>
        <td id="LC528" class="blob-code blob-code-inner js-file-line">                   <span class="pl-s"><span class="pl-pds">&quot;</span>data in the specified log files will be tracked for this Piwik site ID.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L529" class="blob-num js-line-number" data-line-number="529"></td>
        <td id="LC529" class="blob-code blob-code-inner js-file-line">                   <span class="pl-s"><span class="pl-pds">&quot;</span> The script will not auto-detect the website based on the log line hostname (new websites will not be automatically created).<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L530" class="blob-num js-line-number" data-line-number="530"></td>
        <td id="LC530" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L531" class="blob-num js-line-number" data-line-number="531"></td>
        <td id="LC531" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L532" class="blob-num js-line-number" data-line-number="532"></td>
        <td id="LC532" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--idsite-fallback<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>site_id_fallback<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L533" class="blob-num js-line-number" data-line-number="533"></td>
        <td id="LC533" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Default Piwik site ID to use if the hostname doesn&#39;t match any <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L534" class="blob-num js-line-number" data-line-number="534"></td>
        <td id="LC534" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>known Website&#39;s URL. New websites will not be automatically created. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L535" class="blob-num js-line-number" data-line-number="535"></td>
        <td id="LC535" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>                         Used only if --add-sites-new-hosts or --idsite are not set<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L536" class="blob-num js-line-number" data-line-number="536"></td>
        <td id="LC536" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L537" class="blob-num js-line-number" data-line-number="537"></td>
        <td id="LC537" class="blob-code blob-code-inner js-file-line">        default_config <span class="pl-k">=</span> os.path.abspath(</td>
      </tr>
      <tr>
        <td id="L538" class="blob-num js-line-number" data-line-number="538"></td>
        <td id="LC538" class="blob-code blob-code-inner js-file-line">            os.path.join(os.path.dirname(<span class="pl-c1">__file__</span>),</td>
      </tr>
      <tr>
        <td id="L539" class="blob-num js-line-number" data-line-number="539"></td>
        <td id="LC539" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>../../config/config.ini.php<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L540" class="blob-num js-line-number" data-line-number="540"></td>
        <td id="LC540" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L541" class="blob-num js-line-number" data-line-number="541"></td>
        <td id="LC541" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L542" class="blob-num js-line-number" data-line-number="542"></td>
        <td id="LC542" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--config<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>config_file<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span>default_config,</td>
      </tr>
      <tr>
        <td id="L543" class="blob-num js-line-number" data-line-number="543"></td>
        <td id="LC543" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span>(</td>
      </tr>
      <tr>
        <td id="L544" class="blob-num js-line-number" data-line-number="544"></td>
        <td id="LC544" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>This is only used when --login and --password is not used. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L545" class="blob-num js-line-number" data-line-number="545"></td>
        <td id="LC545" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>Piwik will read the configuration file (default: <span class="pl-c1">%d</span>efault) to <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L546" class="blob-num js-line-number" data-line-number="546"></td>
        <td id="LC546" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>fetch the Super User token_auth from the config file. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L547" class="blob-num js-line-number" data-line-number="547"></td>
        <td id="LC547" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L548" class="blob-num js-line-number" data-line-number="548"></td>
        <td id="LC548" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L549" class="blob-num js-line-number" data-line-number="549"></td>
        <td id="LC549" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L550" class="blob-num js-line-number" data-line-number="550"></td>
        <td id="LC550" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--login<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>login<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L551" class="blob-num js-line-number" data-line-number="551"></td>
        <td id="LC551" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>You can manually specify the Piwik Super User login<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L552" class="blob-num js-line-number" data-line-number="552"></td>
        <td id="LC552" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L553" class="blob-num js-line-number" data-line-number="553"></td>
        <td id="LC553" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L554" class="blob-num js-line-number" data-line-number="554"></td>
        <td id="LC554" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--password<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>password<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L555" class="blob-num js-line-number" data-line-number="555"></td>
        <td id="LC555" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>You can manually specify the Piwik Super User password<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L556" class="blob-num js-line-number" data-line-number="556"></td>
        <td id="LC556" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L557" class="blob-num js-line-number" data-line-number="557"></td>
        <td id="LC557" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L558" class="blob-num js-line-number" data-line-number="558"></td>
        <td id="LC558" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--token-auth<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>piwik_token_auth<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L559" class="blob-num js-line-number" data-line-number="559"></td>
        <td id="LC559" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Piwik user token_auth, the token_auth is found in Piwik &gt; Settings &gt; API. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L560" class="blob-num js-line-number" data-line-number="560"></td>
        <td id="LC560" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>You must use a token_auth that has at least &#39;admin&#39; or &#39;super user&#39; permission. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L561" class="blob-num js-line-number" data-line-number="561"></td>
        <td id="LC561" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>If you use a token_auth for a non admin user, your users&#39; IP addresses will not be tracked properly. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L562" class="blob-num js-line-number" data-line-number="562"></td>
        <td id="LC562" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L563" class="blob-num js-line-number" data-line-number="563"></td>
        <td id="LC563" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L564" class="blob-num js-line-number" data-line-number="564"></td>
        <td id="LC564" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L565" class="blob-num js-line-number" data-line-number="565"></td>
        <td id="LC565" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--hostname<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>hostnames<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>append<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span>[],</td>
      </tr>
      <tr>
        <td id="L566" class="blob-num js-line-number" data-line-number="566"></td>
        <td id="LC566" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Accepted hostname (requests with other hostnames will be excluded). <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L567" class="blob-num js-line-number" data-line-number="567"></td>
        <td id="LC567" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>Can be specified multiple times<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L568" class="blob-num js-line-number" data-line-number="568"></td>
        <td id="LC568" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L569" class="blob-num js-line-number" data-line-number="569"></td>
        <td id="LC569" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L570" class="blob-num js-line-number" data-line-number="570"></td>
        <td id="LC570" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--exclude-path<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>excluded_paths<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>append<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span>[],</td>
      </tr>
      <tr>
        <td id="L571" class="blob-num js-line-number" data-line-number="571"></td>
        <td id="LC571" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Any URL path matching this exclude-path will not be imported in Piwik. Can be specified multiple times<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L572" class="blob-num js-line-number" data-line-number="572"></td>
        <td id="LC572" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L573" class="blob-num js-line-number" data-line-number="573"></td>
        <td id="LC573" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L574" class="blob-num js-line-number" data-line-number="574"></td>
        <td id="LC574" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--exclude-path-from<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>exclude_path_from<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L575" class="blob-num js-line-number" data-line-number="575"></td>
        <td id="LC575" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Each line from this file is a path to exclude (see: --exclude-path)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L576" class="blob-num js-line-number" data-line-number="576"></td>
        <td id="LC576" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L577" class="blob-num js-line-number" data-line-number="577"></td>
        <td id="LC577" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L578" class="blob-num js-line-number" data-line-number="578"></td>
        <td id="LC578" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--include-path<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>included_paths<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>append<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span>[],</td>
      </tr>
      <tr>
        <td id="L579" class="blob-num js-line-number" data-line-number="579"></td>
        <td id="LC579" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Paths to include. Can be specified multiple times. If not specified, all paths are included.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L580" class="blob-num js-line-number" data-line-number="580"></td>
        <td id="LC580" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L581" class="blob-num js-line-number" data-line-number="581"></td>
        <td id="LC581" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L582" class="blob-num js-line-number" data-line-number="582"></td>
        <td id="LC582" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--include-path-from<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>include_path_from<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L583" class="blob-num js-line-number" data-line-number="583"></td>
        <td id="LC583" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Each line from this file is a path to include<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L584" class="blob-num js-line-number" data-line-number="584"></td>
        <td id="LC584" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L585" class="blob-num js-line-number" data-line-number="585"></td>
        <td id="LC585" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L586" class="blob-num js-line-number" data-line-number="586"></td>
        <td id="LC586" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--useragent-exclude<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>excluded_useragents<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L587" class="blob-num js-line-number" data-line-number="587"></td>
        <td id="LC587" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>append<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span>[],</td>
      </tr>
      <tr>
        <td id="L588" class="blob-num js-line-number" data-line-number="588"></td>
        <td id="LC588" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>User agents to exclude (in addition to the standard excluded <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L589" class="blob-num js-line-number" data-line-number="589"></td>
        <td id="LC589" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>user agents). Can be specified multiple times<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L590" class="blob-num js-line-number" data-line-number="590"></td>
        <td id="LC590" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L591" class="blob-num js-line-number" data-line-number="591"></td>
        <td id="LC591" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L592" class="blob-num js-line-number" data-line-number="592"></td>
        <td id="LC592" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--enable-static<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>enable_static<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L593" class="blob-num js-line-number" data-line-number="593"></td>
        <td id="LC593" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L594" class="blob-num js-line-number" data-line-number="594"></td>
        <td id="LC594" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Track static files (images, css, js, ico, ttf, etc.)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L595" class="blob-num js-line-number" data-line-number="595"></td>
        <td id="LC595" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L596" class="blob-num js-line-number" data-line-number="596"></td>
        <td id="LC596" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L597" class="blob-num js-line-number" data-line-number="597"></td>
        <td id="LC597" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--enable-bots<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>enable_bots<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L598" class="blob-num js-line-number" data-line-number="598"></td>
        <td id="LC598" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L599" class="blob-num js-line-number" data-line-number="599"></td>
        <td id="LC599" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Track bots. All bot visits will have a Custom Variable set with name=&#39;Bot&#39; and value=&#39;$Bot_user_agent_here$&#39;<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L600" class="blob-num js-line-number" data-line-number="600"></td>
        <td id="LC600" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L601" class="blob-num js-line-number" data-line-number="601"></td>
        <td id="LC601" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L602" class="blob-num js-line-number" data-line-number="602"></td>
        <td id="LC602" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--enable-http-errors<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>enable_http_errors<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L603" class="blob-num js-line-number" data-line-number="603"></td>
        <td id="LC603" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L604" class="blob-num js-line-number" data-line-number="604"></td>
        <td id="LC604" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Track HTTP errors (status code 4xx or 5xx)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L605" class="blob-num js-line-number" data-line-number="605"></td>
        <td id="LC605" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L606" class="blob-num js-line-number" data-line-number="606"></td>
        <td id="LC606" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L607" class="blob-num js-line-number" data-line-number="607"></td>
        <td id="LC607" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--enable-http-redirects<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>enable_http_redirects<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L608" class="blob-num js-line-number" data-line-number="608"></td>
        <td id="LC608" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L609" class="blob-num js-line-number" data-line-number="609"></td>
        <td id="LC609" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Track HTTP redirects (status code 3xx except 304)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L610" class="blob-num js-line-number" data-line-number="610"></td>
        <td id="LC610" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L611" class="blob-num js-line-number" data-line-number="611"></td>
        <td id="LC611" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L612" class="blob-num js-line-number" data-line-number="612"></td>
        <td id="LC612" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--enable-reverse-dns<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>reverse_dns<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L613" class="blob-num js-line-number" data-line-number="613"></td>
        <td id="LC613" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L614" class="blob-num js-line-number" data-line-number="614"></td>
        <td id="LC614" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Enable reverse DNS, used to generate the &#39;Providers&#39; report in Piwik. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L615" class="blob-num js-line-number" data-line-number="615"></td>
        <td id="LC615" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>Disabled by default, as it impacts performance<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L616" class="blob-num js-line-number" data-line-number="616"></td>
        <td id="LC616" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L617" class="blob-num js-line-number" data-line-number="617"></td>
        <td id="LC617" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L618" class="blob-num js-line-number" data-line-number="618"></td>
        <td id="LC618" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--strip-query-string<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>strip_query_string<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L619" class="blob-num js-line-number" data-line-number="619"></td>
        <td id="LC619" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L620" class="blob-num js-line-number" data-line-number="620"></td>
        <td id="LC620" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Strip the query string from the URL<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L621" class="blob-num js-line-number" data-line-number="621"></td>
        <td id="LC621" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L622" class="blob-num js-line-number" data-line-number="622"></td>
        <td id="LC622" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L623" class="blob-num js-line-number" data-line-number="623"></td>
        <td id="LC623" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--query-string-delimiter<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>query_string_delimiter<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>?<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L624" class="blob-num js-line-number" data-line-number="624"></td>
        <td id="LC624" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>The query string delimiter (default: <span class="pl-c1">%d</span>efault)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L625" class="blob-num js-line-number" data-line-number="625"></td>
        <td id="LC625" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L626" class="blob-num js-line-number" data-line-number="626"></td>
        <td id="LC626" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L627" class="blob-num js-line-number" data-line-number="627"></td>
        <td id="LC627" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--log-format-name<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>log_format_name<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L628" class="blob-num js-line-number" data-line-number="628"></td>
        <td id="LC628" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span>(<span class="pl-s"><span class="pl-pds">&quot;</span>Access log format to detect (supported are: <span class="pl-c1">%s</span>). <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L629" class="blob-num js-line-number" data-line-number="629"></td>
        <td id="LC629" class="blob-code blob-code-inner js-file-line">                  <span class="pl-s"><span class="pl-pds">&quot;</span>When not specified, the log format will be autodetected by trying all supported log formats.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L630" class="blob-num js-line-number" data-line-number="630"></td>
        <td id="LC630" class="blob-code blob-code-inner js-file-line">                  <span class="pl-k">%</span> <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">sorted</span>(<span class="pl-c1">FORMATS</span>.iterkeys())))</td>
      </tr>
      <tr>
        <td id="L631" class="blob-num js-line-number" data-line-number="631"></td>
        <td id="LC631" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L632" class="blob-num js-line-number" data-line-number="632"></td>
        <td id="LC632" class="blob-code blob-code-inner js-file-line">        available_regex_groups <span class="pl-k">=</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>path<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>query_string<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>ip<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>user_agent<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>referrer<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L633" class="blob-num js-line-number" data-line-number="633"></td>
        <td id="LC633" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-s"><span class="pl-pds">&#39;</span>length<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>host<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>userid<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>generation_time_milli<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>event_action<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L634" class="blob-num js-line-number" data-line-number="634"></td>
        <td id="LC634" class="blob-code blob-code-inner js-file-line">                                  <span class="pl-s"><span class="pl-pds">&#39;</span>event_name<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>timezone<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>session_time<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L635" class="blob-num js-line-number" data-line-number="635"></td>
        <td id="LC635" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L636" class="blob-num js-line-number" data-line-number="636"></td>
        <td id="LC636" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--log-format-regex<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>log_format_regex<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L637" class="blob-num js-line-number" data-line-number="637"></td>
        <td id="LC637" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Regular expression used to parse log entries. Regexes must contain named groups for different log fields. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L638" class="blob-num js-line-number" data-line-number="638"></td>
        <td id="LC638" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>Recognized fields include: <span class="pl-c1">%s</span>. For an example of a supported Regex, see the source code of this file. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L639" class="blob-num js-line-number" data-line-number="639"></td>
        <td id="LC639" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>Overrides --log-format-name.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(available_regex_groups))</td>
      </tr>
      <tr>
        <td id="L640" class="blob-num js-line-number" data-line-number="640"></td>
        <td id="LC640" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L641" class="blob-num js-line-number" data-line-number="641"></td>
        <td id="LC641" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L642" class="blob-num js-line-number" data-line-number="642"></td>
        <td id="LC642" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--log-date-format<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>log_date_format<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L643" class="blob-num js-line-number" data-line-number="643"></td>
        <td id="LC643" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Format string used to parse dates. You can specify any format that can also be specified to <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L644" class="blob-num js-line-number" data-line-number="644"></td>
        <td id="LC644" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>the strptime python function.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L645" class="blob-num js-line-number" data-line-number="645"></td>
        <td id="LC645" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L646" class="blob-num js-line-number" data-line-number="646"></td>
        <td id="LC646" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L647" class="blob-num js-line-number" data-line-number="647"></td>
        <td id="LC647" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--log-hostname<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>log_hostname<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L648" class="blob-num js-line-number" data-line-number="648"></td>
        <td id="LC648" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Force this hostname for a log format that doesn&#39;t include it. All hits <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L649" class="blob-num js-line-number" data-line-number="649"></td>
        <td id="LC649" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>will seem to come to this host<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L650" class="blob-num js-line-number" data-line-number="650"></td>
        <td id="LC650" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L651" class="blob-num js-line-number" data-line-number="651"></td>
        <td id="LC651" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L652" class="blob-num js-line-number" data-line-number="652"></td>
        <td id="LC652" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--skip<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>skip<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">0</span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L653" class="blob-num js-line-number" data-line-number="653"></td>
        <td id="LC653" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Skip the n first lines to start parsing/importing data at a given line for the specified log file<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L654" class="blob-num js-line-number" data-line-number="654"></td>
        <td id="LC654" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L655" class="blob-num js-line-number" data-line-number="655"></td>
        <td id="LC655" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L656" class="blob-num js-line-number" data-line-number="656"></td>
        <td id="LC656" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--recorders<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>recorders<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">1</span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L657" class="blob-num js-line-number" data-line-number="657"></td>
        <td id="LC657" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Number of simultaneous recorders (default: <span class="pl-c1">%d</span>efault). <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L658" class="blob-num js-line-number" data-line-number="658"></td>
        <td id="LC658" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>It should be set to the number of CPU cores in your server. <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L659" class="blob-num js-line-number" data-line-number="659"></td>
        <td id="LC659" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>You can also experiment with higher values which may increase performance until a certain point<span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L660" class="blob-num js-line-number" data-line-number="660"></td>
        <td id="LC660" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L661" class="blob-num js-line-number" data-line-number="661"></td>
        <td id="LC661" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L662" class="blob-num js-line-number" data-line-number="662"></td>
        <td id="LC662" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--recorder-max-payload-size<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>recorder_max_payload_size<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">200</span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L663" class="blob-num js-line-number" data-line-number="663"></td>
        <td id="LC663" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Maximum number of log entries to record in one tracking request (default: <span class="pl-c1">%d</span>efault). <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L664" class="blob-num js-line-number" data-line-number="664"></td>
        <td id="LC664" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L665" class="blob-num js-line-number" data-line-number="665"></td>
        <td id="LC665" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L666" class="blob-num js-line-number" data-line-number="666"></td>
        <td id="LC666" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--replay-tracking<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>replay_tracking<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L667" class="blob-num js-line-number" data-line-number="667"></td>
        <td id="LC667" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L668" class="blob-num js-line-number" data-line-number="668"></td>
        <td id="LC668" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Replay piwik.php requests found in custom logs (only piwik.php requests expected). <span class="pl-cce">\n</span>See http://piwik.org/faq/how-to/faq_17033/<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L669" class="blob-num js-line-number" data-line-number="669"></td>
        <td id="LC669" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L670" class="blob-num js-line-number" data-line-number="670"></td>
        <td id="LC670" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L671" class="blob-num js-line-number" data-line-number="671"></td>
        <td id="LC671" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--replay-tracking-expected-tracker-file<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>replay_tracking_expected_tracker_file<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>piwik.php<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L672" class="blob-num js-line-number" data-line-number="672"></td>
        <td id="LC672" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>The expected suffix for tracking request paths. Only logs whose paths end with this will be imported. Defaults <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L673" class="blob-num js-line-number" data-line-number="673"></td>
        <td id="LC673" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>to &#39;piwik.php&#39; so only requests to the piwik.php file will be imported.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L674" class="blob-num js-line-number" data-line-number="674"></td>
        <td id="LC674" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L675" class="blob-num js-line-number" data-line-number="675"></td>
        <td id="LC675" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L676" class="blob-num js-line-number" data-line-number="676"></td>
        <td id="LC676" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--output<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>output<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L677" class="blob-num js-line-number" data-line-number="677"></td>
        <td id="LC677" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Redirect output (stdout and stderr) to the specified file<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L678" class="blob-num js-line-number" data-line-number="678"></td>
        <td id="LC678" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L679" class="blob-num js-line-number" data-line-number="679"></td>
        <td id="LC679" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L680" class="blob-num js-line-number" data-line-number="680"></td>
        <td id="LC680" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--encoding<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>encoding<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L681" class="blob-num js-line-number" data-line-number="681"></td>
        <td id="LC681" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Log files encoding (default: <span class="pl-c1">%d</span>efault)<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L682" class="blob-num js-line-number" data-line-number="682"></td>
        <td id="LC682" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L683" class="blob-num js-line-number" data-line-number="683"></td>
        <td id="LC683" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L684" class="blob-num js-line-number" data-line-number="684"></td>
        <td id="LC684" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--disable-bulk-tracking<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>use_bulk_tracking<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L685" class="blob-num js-line-number" data-line-number="685"></td>
        <td id="LC685" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_false<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L686" class="blob-num js-line-number" data-line-number="686"></td>
        <td id="LC686" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Disables use of bulk tracking so recorders record one hit at a time.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L687" class="blob-num js-line-number" data-line-number="687"></td>
        <td id="LC687" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L688" class="blob-num js-line-number" data-line-number="688"></td>
        <td id="LC688" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L689" class="blob-num js-line-number" data-line-number="689"></td>
        <td id="LC689" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--debug-force-one-hit-every-Ns<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>force_one_action_interval<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>float<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L690" class="blob-num js-line-number" data-line-number="690"></td>
        <td id="LC690" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Debug option that will force each recorder to record one hit every N secs.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L691" class="blob-num js-line-number" data-line-number="691"></td>
        <td id="LC691" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L692" class="blob-num js-line-number" data-line-number="692"></td>
        <td id="LC692" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L693" class="blob-num js-line-number" data-line-number="693"></td>
        <td id="LC693" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--force-lowercase-path<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>force_lowercase_path<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L694" class="blob-num js-line-number" data-line-number="694"></td>
        <td id="LC694" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Make URL path lowercase so paths with the same letters but different cases are <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L695" class="blob-num js-line-number" data-line-number="695"></td>
        <td id="LC695" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>treated the same.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L696" class="blob-num js-line-number" data-line-number="696"></td>
        <td id="LC696" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L697" class="blob-num js-line-number" data-line-number="697"></td>
        <td id="LC697" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L698" class="blob-num js-line-number" data-line-number="698"></td>
        <td id="LC698" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--enable-testmode<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>enable_testmode<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L699" class="blob-num js-line-number" data-line-number="699"></td>
        <td id="LC699" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>If set, it will try to get the token_auth from the piwik_tests directory<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L700" class="blob-num js-line-number" data-line-number="700"></td>
        <td id="LC700" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L701" class="blob-num js-line-number" data-line-number="701"></td>
        <td id="LC701" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L702" class="blob-num js-line-number" data-line-number="702"></td>
        <td id="LC702" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--download-extensions<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>download_extensions<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L703" class="blob-num js-line-number" data-line-number="703"></td>
        <td id="LC703" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>By default Piwik tracks as Downloads the most popular file extensions. If you set this parameter (format: pdf,doc,...) then files with an extension found in the list will be imported as Downloads, other file extensions downloads will be skipped.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L704" class="blob-num js-line-number" data-line-number="704"></td>
        <td id="LC704" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L705" class="blob-num js-line-number" data-line-number="705"></td>
        <td id="LC705" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L706" class="blob-num js-line-number" data-line-number="706"></td>
        <td id="LC706" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--add-download-extensions<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>extra_download_extensions<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L707" class="blob-num js-line-number" data-line-number="707"></td>
        <td id="LC707" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Add extensions that should be treated as downloads. See --download-extensions for more info.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L708" class="blob-num js-line-number" data-line-number="708"></td>
        <td id="LC708" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L709" class="blob-num js-line-number" data-line-number="709"></td>
        <td id="LC709" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L710" class="blob-num js-line-number" data-line-number="710"></td>
        <td id="LC710" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--w3c-map-field<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>callback<span class="pl-pds">&#39;</span></span>, <span class="pl-v">callback</span><span class="pl-k">=</span>functools.partial(<span class="pl-c1">self</span>._set_option_map, <span class="pl-s"><span class="pl-pds">&#39;</span>custom_w3c_fields<span class="pl-pds">&#39;</span></span>), <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>string<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L711" class="blob-num js-line-number" data-line-number="711"></td>
        <td id="LC711" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Map a custom log entry field in your W3C log to a default one. Use this option to load custom log <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L712" class="blob-num js-line-number" data-line-number="712"></td>
        <td id="LC712" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>files that use the W3C extended log format such as those from the Advanced Logging W3C module. Used <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L713" class="blob-num js-line-number" data-line-number="713"></td>
        <td id="LC713" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>as, eg, --w3c-map-field my-date=date. Recognized default fields include: <span class="pl-c1">%s</span><span class="pl-cce">\n\n</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L714" class="blob-num js-line-number" data-line-number="714"></td>
        <td id="LC714" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>Formats that extend the W3C extended log format (like the cloudfront RTMP log format) may define more <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L715" class="blob-num js-line-number" data-line-number="715"></td>
        <td id="LC715" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>fields that can be mapped.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L716" class="blob-num js-line-number" data-line-number="716"></td>
        <td id="LC716" class="blob-code blob-code-inner js-file-line">                     <span class="pl-k">%</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(W3cExtendedFormat.fields.keys()))</td>
      </tr>
      <tr>
        <td id="L717" class="blob-num js-line-number" data-line-number="717"></td>
        <td id="LC717" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L718" class="blob-num js-line-number" data-line-number="718"></td>
        <td id="LC718" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L719" class="blob-num js-line-number" data-line-number="719"></td>
        <td id="LC719" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--w3c-time-taken-millisecs<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>w3c_time_taken_in_millisecs<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L720" class="blob-num js-line-number" data-line-number="720"></td>
        <td id="LC720" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>If set, interprets the time-taken W3C log field as a number of milliseconds. This must be set for importing<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L721" class="blob-num js-line-number" data-line-number="721"></td>
        <td id="LC721" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span> IIS logs.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L722" class="blob-num js-line-number" data-line-number="722"></td>
        <td id="LC722" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L723" class="blob-num js-line-number" data-line-number="723"></td>
        <td id="LC723" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L724" class="blob-num js-line-number" data-line-number="724"></td>
        <td id="LC724" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--w3c-fields<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>w3c_fields<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L725" class="blob-num js-line-number" data-line-number="725"></td>
        <td id="LC725" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Specify the &#39;#Fields:&#39; line for a log file in the W3C Extended log file format. Use this option if <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L726" class="blob-num js-line-number" data-line-number="726"></td>
        <td id="LC726" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>your log file doesn&#39;t contain the &#39;#Fields:&#39; line which is required for parsing. This option must be used <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L727" class="blob-num js-line-number" data-line-number="727"></td>
        <td id="LC727" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>in conjuction with --log-format-name=w3c_extended.<span class="pl-cce">\n</span><span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L728" class="blob-num js-line-number" data-line-number="728"></td>
        <td id="LC728" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>Example: --w3c-fields=&#39;#Fields: date time c-ip ...&#39;<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L729" class="blob-num js-line-number" data-line-number="729"></td>
        <td id="LC729" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L730" class="blob-num js-line-number" data-line-number="730"></td>
        <td id="LC730" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L731" class="blob-num js-line-number" data-line-number="731"></td>
        <td id="LC731" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--w3c-field-regex<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>callback<span class="pl-pds">&#39;</span></span>, <span class="pl-v">callback</span><span class="pl-k">=</span>functools.partial(<span class="pl-c1">self</span>._set_option_map, <span class="pl-s"><span class="pl-pds">&#39;</span>w3c_field_regexes<span class="pl-pds">&#39;</span></span>), <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>string<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L732" class="blob-num js-line-number" data-line-number="732"></td>
        <td id="LC732" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Specify a regex for a field in your W3C extended log file. You can use this option to parse fields the <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L733" class="blob-num js-line-number" data-line-number="733"></td>
        <td id="LC733" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>importer does not natively recognize and then use one of the --regex-group-to-XXX-cvar options to track <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L734" class="blob-num js-line-number" data-line-number="734"></td>
        <td id="LC734" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>the field in a custom variable. For example, specifying --w3c-field-regex=sc-win32-status=(?P&lt;win32_status&gt;<span class="pl-cce">\\</span>S+) <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L735" class="blob-num js-line-number" data-line-number="735"></td>
        <td id="LC735" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>--regex-group-to-page-cvar=<span class="pl-cce">\&quot;</span>win32_status=Windows Status Code<span class="pl-cce">\&quot;</span> will track the sc-win32-status IIS field <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L736" class="blob-num js-line-number" data-line-number="736"></td>
        <td id="LC736" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>in the &#39;Windows Status Code&#39; custom variable. Regexes must contain a named group.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L737" class="blob-num js-line-number" data-line-number="737"></td>
        <td id="LC737" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L738" class="blob-num js-line-number" data-line-number="738"></td>
        <td id="LC738" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L739" class="blob-num js-line-number" data-line-number="739"></td>
        <td id="LC739" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--title-category-delimiter<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>title_category_delimiter<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L740" class="blob-num js-line-number" data-line-number="740"></td>
        <td id="LC740" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>If --enable-http-errors is used, errors are shown in the page titles report. If you have <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L741" class="blob-num js-line-number" data-line-number="741"></td>
        <td id="LC741" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>changed General.action_title_category_delimiter in your Piwik configuration, you need to set this <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L742" class="blob-num js-line-number" data-line-number="742"></td>
        <td id="LC742" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&quot;</span>option to the same value in order to get a pretty page titles report.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L743" class="blob-num js-line-number" data-line-number="743"></td>
        <td id="LC743" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L744" class="blob-num js-line-number" data-line-number="744"></td>
        <td id="LC744" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L745" class="blob-num js-line-number" data-line-number="745"></td>
        <td id="LC745" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--dump-log-regex<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>dump_log_regex<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>store_true<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L746" class="blob-num js-line-number" data-line-number="746"></td>
        <td id="LC746" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Prints out the regex string used to parse log lines and exists. Can be useful for using formats <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L747" class="blob-num js-line-number" data-line-number="747"></td>
        <td id="LC747" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>in newer versions of the script in older versions of the script. The output regex can be used with <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L748" class="blob-num js-line-number" data-line-number="748"></td>
        <td id="LC748" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>the --log-format-regex option.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L749" class="blob-num js-line-number" data-line-number="749"></td>
        <td id="LC749" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L750" class="blob-num js-line-number" data-line-number="750"></td>
        <td id="LC750" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L751" class="blob-num js-line-number" data-line-number="751"></td>
        <td id="LC751" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L752" class="blob-num js-line-number" data-line-number="752"></td>
        <td id="LC752" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--ignore-groups<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>regex_groups_to_ignore<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L753" class="blob-num js-line-number" data-line-number="753"></td>
        <td id="LC753" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Comma separated list of regex groups to ignore when parsing log lines. Can be used to, for example, <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L754" class="blob-num js-line-number" data-line-number="754"></td>
        <td id="LC754" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>disable normal user id tracking. See documentation for --log-format-regex for list of available <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L755" class="blob-num js-line-number" data-line-number="755"></td>
        <td id="LC755" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>regex groups.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L756" class="blob-num js-line-number" data-line-number="756"></td>
        <td id="LC756" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L757" class="blob-num js-line-number" data-line-number="757"></td>
        <td id="LC757" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L758" class="blob-num js-line-number" data-line-number="758"></td>
        <td id="LC758" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L759" class="blob-num js-line-number" data-line-number="759"></td>
        <td id="LC759" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--regex-group-to-visit-cvar<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>callback<span class="pl-pds">&#39;</span></span>, <span class="pl-v">callback</span><span class="pl-k">=</span>functools.partial(<span class="pl-c1">self</span>._set_option_map, <span class="pl-s"><span class="pl-pds">&#39;</span>regex_group_to_visit_cvars_map<span class="pl-pds">&#39;</span></span>), <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>string<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L760" class="blob-num js-line-number" data-line-number="760"></td>
        <td id="LC760" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Track an attribute through a custom variable with visit scope instead of through Piwik&#39;s normal <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L761" class="blob-num js-line-number" data-line-number="761"></td>
        <td id="LC761" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>approach. For example, to track usernames as a custom variable instead of through the uid tracking <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L762" class="blob-num js-line-number" data-line-number="762"></td>
        <td id="LC762" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>parameter, supply --regex-group-to-visit-cvar=<span class="pl-cce">\&quot;</span>userid=User Name<span class="pl-cce">\&quot;</span>. This will track usernames in a <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L763" class="blob-num js-line-number" data-line-number="763"></td>
        <td id="LC763" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>custom variable named &#39;User Name&#39;. The list of available regex groups can be found in the documentation <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L764" class="blob-num js-line-number" data-line-number="764"></td>
        <td id="LC764" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>for --log-format-regex (additional regex groups you may have defined <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L765" class="blob-num js-line-number" data-line-number="765"></td>
        <td id="LC765" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>in --log-format-regex can also be used).<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L766" class="blob-num js-line-number" data-line-number="766"></td>
        <td id="LC766" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L767" class="blob-num js-line-number" data-line-number="767"></td>
        <td id="LC767" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L768" class="blob-num js-line-number" data-line-number="768"></td>
        <td id="LC768" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--regex-group-to-page-cvar<span class="pl-pds">&#39;</span></span>, <span class="pl-v">action</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>callback<span class="pl-pds">&#39;</span></span>, <span class="pl-v">callback</span><span class="pl-k">=</span>functools.partial(<span class="pl-c1">self</span>._set_option_map, <span class="pl-s"><span class="pl-pds">&#39;</span>regex_group_to_page_cvars_map<span class="pl-pds">&#39;</span></span>), <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>string<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L769" class="blob-num js-line-number" data-line-number="769"></td>
        <td id="LC769" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>Track an attribute through a custom variable with page scope instead of through Piwik&#39;s normal <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L770" class="blob-num js-line-number" data-line-number="770"></td>
        <td id="LC770" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>approach. For example, to track usernames as a custom variable instead of through the uid tracking <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L771" class="blob-num js-line-number" data-line-number="771"></td>
        <td id="LC771" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>parameter, supply --regex-group-to-page-cvar=<span class="pl-cce">\&quot;</span>userid=User Name<span class="pl-cce">\&quot;</span>. This will track usernames in a <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L772" class="blob-num js-line-number" data-line-number="772"></td>
        <td id="LC772" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>custom variable named &#39;User Name&#39;. The list of available regex groups can be found in the documentation <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L773" class="blob-num js-line-number" data-line-number="773"></td>
        <td id="LC773" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>for --log-format-regex (additional regex groups you may have defined <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L774" class="blob-num js-line-number" data-line-number="774"></td>
        <td id="LC774" class="blob-code blob-code-inner js-file-line">                 <span class="pl-s"><span class="pl-pds">&quot;</span>in --log-format-regex can also be used).<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L775" class="blob-num js-line-number" data-line-number="775"></td>
        <td id="LC775" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L776" class="blob-num js-line-number" data-line-number="776"></td>
        <td id="LC776" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L777" class="blob-num js-line-number" data-line-number="777"></td>
        <td id="LC777" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--retry-max-attempts<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>max_attempts<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">PIWIK_DEFAULT_MAX_ATTEMPTS</span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L778" class="blob-num js-line-number" data-line-number="778"></td>
        <td id="LC778" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>The maximum number of times to retry a failed tracking request.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L779" class="blob-num js-line-number" data-line-number="779"></td>
        <td id="LC779" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L780" class="blob-num js-line-number" data-line-number="780"></td>
        <td id="LC780" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L781" class="blob-num js-line-number" data-line-number="781"></td>
        <td id="LC781" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--retry-delay<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>delay_after_failure<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">PIWIK_DEFAULT_DELAY_AFTER_FAILURE</span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L782" class="blob-num js-line-number" data-line-number="782"></td>
        <td id="LC782" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>The number of seconds to wait before retrying a failed tracking request.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L783" class="blob-num js-line-number" data-line-number="783"></td>
        <td id="LC783" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L784" class="blob-num js-line-number" data-line-number="784"></td>
        <td id="LC784" class="blob-code blob-code-inner js-file-line">        option_parser.add_option(</td>
      </tr>
      <tr>
        <td id="L785" class="blob-num js-line-number" data-line-number="785"></td>
        <td id="LC785" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>--request-timeout<span class="pl-pds">&#39;</span></span>, <span class="pl-v">dest</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>request_timeout<span class="pl-pds">&#39;</span></span>, <span class="pl-v">default</span><span class="pl-k">=</span><span class="pl-c1">DEFAULT_SOCKET_TIMEOUT</span>, <span class="pl-v">type</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>int<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L786" class="blob-num js-line-number" data-line-number="786"></td>
        <td id="LC786" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">help</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&quot;</span>The maximum number of seconds to wait before terminating an HTTP request to Piwik.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L787" class="blob-num js-line-number" data-line-number="787"></td>
        <td id="LC787" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L788" class="blob-num js-line-number" data-line-number="788"></td>
        <td id="LC788" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> option_parser</td>
      </tr>
      <tr>
        <td id="L789" class="blob-num js-line-number" data-line-number="789"></td>
        <td id="LC789" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L790" class="blob-num js-line-number" data-line-number="790"></td>
        <td id="LC790" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_set_option_map</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">option_attr_name</span>, <span class="pl-smi">option</span>, <span class="pl-smi">opt_str</span>, <span class="pl-smi">value</span>, <span class="pl-smi">parser</span>):</td>
      </tr>
      <tr>
        <td id="L791" class="blob-num js-line-number" data-line-number="791"></td>
        <td id="LC791" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L792" class="blob-num js-line-number" data-line-number="792"></td>
        <td id="LC792" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Sets a key-value mapping in a dict that is built from command line options. Options that map</span></td>
      </tr>
      <tr>
        <td id="L793" class="blob-num js-line-number" data-line-number="793"></td>
        <td id="LC793" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        string keys to string values (like --w3c-map-field) can set the callback to a bound partial</span></td>
      </tr>
      <tr>
        <td id="L794" class="blob-num js-line-number" data-line-number="794"></td>
        <td id="LC794" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        of this method to handle the option.</span></td>
      </tr>
      <tr>
        <td id="L795" class="blob-num js-line-number" data-line-number="795"></td>
        <td id="LC795" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L796" class="blob-num js-line-number" data-line-number="796"></td>
        <td id="LC796" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L797" class="blob-num js-line-number" data-line-number="797"></td>
        <td id="LC797" class="blob-code blob-code-inner js-file-line">        parts <span class="pl-k">=</span> value.split(<span class="pl-s"><span class="pl-pds">&#39;</span>=<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L798" class="blob-num js-line-number" data-line-number="798"></td>
        <td id="LC798" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L799" class="blob-num js-line-number" data-line-number="799"></td>
        <td id="LC799" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(parts) <span class="pl-k">!=</span> <span class="pl-c1">2</span>:</td>
      </tr>
      <tr>
        <td id="L800" class="blob-num js-line-number" data-line-number="800"></td>
        <td id="LC800" class="blob-code blob-code-inner js-file-line">            fatal_error(<span class="pl-s"><span class="pl-pds">&quot;</span>Invalid <span class="pl-c1">%s</span> option: &#39;<span class="pl-c1">%s</span>&#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (opt_str, value))</td>
      </tr>
      <tr>
        <td id="L801" class="blob-num js-line-number" data-line-number="801"></td>
        <td id="LC801" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L802" class="blob-num js-line-number" data-line-number="802"></td>
        <td id="LC802" class="blob-code blob-code-inner js-file-line">        key, value <span class="pl-k">=</span> parts</td>
      </tr>
      <tr>
        <td id="L803" class="blob-num js-line-number" data-line-number="803"></td>
        <td id="LC803" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L804" class="blob-num js-line-number" data-line-number="804"></td>
        <td id="LC804" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(parser.values, option_attr_name):</td>
      </tr>
      <tr>
        <td id="L805" class="blob-num js-line-number" data-line-number="805"></td>
        <td id="LC805" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">setattr</span>(parser.values, option_attr_name, {})</td>
      </tr>
      <tr>
        <td id="L806" class="blob-num js-line-number" data-line-number="806"></td>
        <td id="LC806" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L807" class="blob-num js-line-number" data-line-number="807"></td>
        <td id="LC807" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">getattr</span>(parser.values, option_attr_name)[key] <span class="pl-k">=</span> value</td>
      </tr>
      <tr>
        <td id="L808" class="blob-num js-line-number" data-line-number="808"></td>
        <td id="LC808" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L809" class="blob-num js-line-number" data-line-number="809"></td>
        <td id="LC809" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_parse_args</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">option_parser</span>):</td>
      </tr>
      <tr>
        <td id="L810" class="blob-num js-line-number" data-line-number="810"></td>
        <td id="LC810" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L811" class="blob-num js-line-number" data-line-number="811"></td>
        <td id="LC811" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Parse the command line args and create self.options and self.filenames.</span></td>
      </tr>
      <tr>
        <td id="L812" class="blob-num js-line-number" data-line-number="812"></td>
        <td id="LC812" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L813" class="blob-num js-line-number" data-line-number="813"></td>
        <td id="LC813" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.options, <span class="pl-c1">self</span>.filenames <span class="pl-k">=</span> option_parser.parse_args(sys.argv[<span class="pl-c1">1</span>:])</td>
      </tr>
      <tr>
        <td id="L814" class="blob-num js-line-number" data-line-number="814"></td>
        <td id="LC814" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L815" class="blob-num js-line-number" data-line-number="815"></td>
        <td id="LC815" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.output:</td>
      </tr>
      <tr>
        <td id="L816" class="blob-num js-line-number" data-line-number="816"></td>
        <td id="LC816" class="blob-code blob-code-inner js-file-line">            sys.stdout <span class="pl-k">=</span> sys.stderr <span class="pl-k">=</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.options.output, <span class="pl-s"><span class="pl-pds">&#39;</span>a+<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L817" class="blob-num js-line-number" data-line-number="817"></td>
        <td id="LC817" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L818" class="blob-num js-line-number" data-line-number="818"></td>
        <td id="LC818" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>.filenames:</td>
      </tr>
      <tr>
        <td id="L819" class="blob-num js-line-number" data-line-number="819"></td>
        <td id="LC819" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span>(option_parser.format_help())</td>
      </tr>
      <tr>
        <td id="L820" class="blob-num js-line-number" data-line-number="820"></td>
        <td id="LC820" class="blob-code blob-code-inner js-file-line">            sys.exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L821" class="blob-num js-line-number" data-line-number="821"></td>
        <td id="LC821" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L822" class="blob-num js-line-number" data-line-number="822"></td>
        <td id="LC822" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Configure logging before calling logging.{debug,info}.</span></td>
      </tr>
      <tr>
        <td id="L823" class="blob-num js-line-number" data-line-number="823"></td>
        <td id="LC823" class="blob-code blob-code-inner js-file-line">        logging.basicConfig(</td>
      </tr>
      <tr>
        <td id="L824" class="blob-num js-line-number" data-line-number="824"></td>
        <td id="LC824" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">format</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%(asctime)s</span>: [<span class="pl-c1">%(levelname)s</span>] <span class="pl-c1">%(message)s</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L825" class="blob-num js-line-number" data-line-number="825"></td>
        <td id="LC825" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">level</span><span class="pl-k">=</span>logging.<span class="pl-c1">DEBUG</span> <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.debug <span class="pl-k">&gt;=</span> <span class="pl-c1">1</span> <span class="pl-k">else</span> logging.<span class="pl-c1">INFO</span>,</td>
      </tr>
      <tr>
        <td id="L826" class="blob-num js-line-number" data-line-number="826"></td>
        <td id="LC826" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L827" class="blob-num js-line-number" data-line-number="827"></td>
        <td id="LC827" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L828" class="blob-num js-line-number" data-line-number="828"></td>
        <td id="LC828" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.options.excluded_useragents <span class="pl-k">=</span> <span class="pl-c1">set</span>([s.lower() <span class="pl-k">for</span> s <span class="pl-k">in</span> <span class="pl-c1">self</span>.options.excluded_useragents])</td>
      </tr>
      <tr>
        <td id="L829" class="blob-num js-line-number" data-line-number="829"></td>
        <td id="LC829" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L830" class="blob-num js-line-number" data-line-number="830"></td>
        <td id="LC830" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.exclude_path_from:</td>
      </tr>
      <tr>
        <td id="L831" class="blob-num js-line-number" data-line-number="831"></td>
        <td id="LC831" class="blob-code blob-code-inner js-file-line">            paths <span class="pl-k">=</span> [path.strip() <span class="pl-k">for</span> path <span class="pl-k">in</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.options.exclude_path_from).readlines()]</td>
      </tr>
      <tr>
        <td id="L832" class="blob-num js-line-number" data-line-number="832"></td>
        <td id="LC832" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.excluded_paths.extend(path <span class="pl-k">for</span> path <span class="pl-k">in</span> paths <span class="pl-k">if</span> <span class="pl-c1">len</span>(path) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L833" class="blob-num js-line-number" data-line-number="833"></td>
        <td id="LC833" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.excluded_paths:</td>
      </tr>
      <tr>
        <td id="L834" class="blob-num js-line-number" data-line-number="834"></td>
        <td id="LC834" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.excluded_paths <span class="pl-k">=</span> <span class="pl-c1">set</span>(<span class="pl-c1">self</span>.options.excluded_paths)</td>
      </tr>
      <tr>
        <td id="L835" class="blob-num js-line-number" data-line-number="835"></td>
        <td id="LC835" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Excluded paths: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.options.excluded_paths))</td>
      </tr>
      <tr>
        <td id="L836" class="blob-num js-line-number" data-line-number="836"></td>
        <td id="LC836" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L837" class="blob-num js-line-number" data-line-number="837"></td>
        <td id="LC837" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.include_path_from:</td>
      </tr>
      <tr>
        <td id="L838" class="blob-num js-line-number" data-line-number="838"></td>
        <td id="LC838" class="blob-code blob-code-inner js-file-line">            paths <span class="pl-k">=</span> [path.strip() <span class="pl-k">for</span> path <span class="pl-k">in</span> <span class="pl-c1">open</span>(<span class="pl-c1">self</span>.options.include_path_from).readlines()]</td>
      </tr>
      <tr>
        <td id="L839" class="blob-num js-line-number" data-line-number="839"></td>
        <td id="LC839" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.included_paths.extend(path <span class="pl-k">for</span> path <span class="pl-k">in</span> paths <span class="pl-k">if</span> <span class="pl-c1">len</span>(path) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L840" class="blob-num js-line-number" data-line-number="840"></td>
        <td id="LC840" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.included_paths:</td>
      </tr>
      <tr>
        <td id="L841" class="blob-num js-line-number" data-line-number="841"></td>
        <td id="LC841" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.included_paths <span class="pl-k">=</span> <span class="pl-c1">set</span>(<span class="pl-c1">self</span>.options.included_paths)</td>
      </tr>
      <tr>
        <td id="L842" class="blob-num js-line-number" data-line-number="842"></td>
        <td id="LC842" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Included paths: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.options.included_paths))</td>
      </tr>
      <tr>
        <td id="L843" class="blob-num js-line-number" data-line-number="843"></td>
        <td id="LC843" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L844" class="blob-num js-line-number" data-line-number="844"></td>
        <td id="LC844" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.hostnames:</td>
      </tr>
      <tr>
        <td id="L845" class="blob-num js-line-number" data-line-number="845"></td>
        <td id="LC845" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Accepted hostnames: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>, <span class="pl-pds">&#39;</span></span>.join(<span class="pl-c1">self</span>.options.hostnames))</td>
      </tr>
      <tr>
        <td id="L846" class="blob-num js-line-number" data-line-number="846"></td>
        <td id="LC846" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L847" class="blob-num js-line-number" data-line-number="847"></td>
        <td id="LC847" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Accepted hostnames: all<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L848" class="blob-num js-line-number" data-line-number="848"></td>
        <td id="LC848" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L849" class="blob-num js-line-number" data-line-number="849"></td>
        <td id="LC849" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.log_format_regex:</td>
      </tr>
      <tr>
        <td id="L850" class="blob-num js-line-number" data-line-number="850"></td>
        <td id="LC850" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.format <span class="pl-k">=</span> RegexFormat(<span class="pl-s"><span class="pl-pds">&#39;</span>custom<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.options.log_format_regex, <span class="pl-c1">self</span>.options.log_date_format)</td>
      </tr>
      <tr>
        <td id="L851" class="blob-num js-line-number" data-line-number="851"></td>
        <td id="LC851" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-c1">self</span>.options.log_format_name:</td>
      </tr>
      <tr>
        <td id="L852" class="blob-num js-line-number" data-line-number="852"></td>
        <td id="LC852" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L853" class="blob-num js-line-number" data-line-number="853"></td>
        <td id="LC853" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.format <span class="pl-k">=</span> <span class="pl-c1">FORMATS</span>[<span class="pl-c1">self</span>.options.log_format_name]</td>
      </tr>
      <tr>
        <td id="L854" class="blob-num js-line-number" data-line-number="854"></td>
        <td id="LC854" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L855" class="blob-num js-line-number" data-line-number="855"></td>
        <td id="LC855" class="blob-code blob-code-inner js-file-line">                fatal_error(<span class="pl-s"><span class="pl-pds">&#39;</span>invalid log format: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-c1">self</span>.options.log_format_name)</td>
      </tr>
      <tr>
        <td id="L856" class="blob-num js-line-number" data-line-number="856"></td>
        <td id="LC856" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L857" class="blob-num js-line-number" data-line-number="857"></td>
        <td id="LC857" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.format <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L858" class="blob-num js-line-number" data-line-number="858"></td>
        <td id="LC858" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L859" class="blob-num js-line-number" data-line-number="859"></td>
        <td id="LC859" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(<span class="pl-c1">self</span>.options, <span class="pl-s"><span class="pl-pds">&#39;</span>custom_w3c_fields<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L860" class="blob-num js-line-number" data-line-number="860"></td>
        <td id="LC860" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.custom_w3c_fields <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L861" class="blob-num js-line-number" data-line-number="861"></td>
        <td id="LC861" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-c1">self</span>.format <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L862" class="blob-num js-line-number" data-line-number="862"></td>
        <td id="LC862" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> validate custom field mappings</span></td>
      </tr>
      <tr>
        <td id="L863" class="blob-num js-line-number" data-line-number="863"></td>
        <td id="LC863" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> custom_name, default_name <span class="pl-k">in</span> <span class="pl-c1">self</span>.options.custom_w3c_fields.iteritems():</td>
      </tr>
      <tr>
        <td id="L864" class="blob-num js-line-number" data-line-number="864"></td>
        <td id="LC864" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> default_name <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">type</span>(<span class="pl-c1">format</span>).fields:</td>
      </tr>
      <tr>
        <td id="L865" class="blob-num js-line-number" data-line-number="865"></td>
        <td id="LC865" class="blob-code blob-code-inner js-file-line">                    fatal_error(<span class="pl-s"><span class="pl-pds">&quot;</span>custom W3C field mapping error: don&#39;t know how to parse and use the &#39;%&#39; field<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> default_name)</td>
      </tr>
      <tr>
        <td id="L866" class="blob-num js-line-number" data-line-number="866"></td>
        <td id="LC866" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L867" class="blob-num js-line-number" data-line-number="867"></td>
        <td id="LC867" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L868" class="blob-num js-line-number" data-line-number="868"></td>
        <td id="LC868" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(<span class="pl-c1">self</span>.options, <span class="pl-s"><span class="pl-pds">&#39;</span>regex_group_to_visit_cvars_map<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L869" class="blob-num js-line-number" data-line-number="869"></td>
        <td id="LC869" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.regex_group_to_visit_cvars_map <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L870" class="blob-num js-line-number" data-line-number="870"></td>
        <td id="LC870" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L871" class="blob-num js-line-number" data-line-number="871"></td>
        <td id="LC871" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(<span class="pl-c1">self</span>.options, <span class="pl-s"><span class="pl-pds">&#39;</span>regex_group_to_page_cvars_map<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L872" class="blob-num js-line-number" data-line-number="872"></td>
        <td id="LC872" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.regex_group_to_page_cvars_map <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L873" class="blob-num js-line-number" data-line-number="873"></td>
        <td id="LC873" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L874" class="blob-num js-line-number" data-line-number="874"></td>
        <td id="LC874" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(<span class="pl-c1">self</span>.options, <span class="pl-s"><span class="pl-pds">&#39;</span>w3c_field_regexes<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L875" class="blob-num js-line-number" data-line-number="875"></td>
        <td id="LC875" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.w3c_field_regexes <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L876" class="blob-num js-line-number" data-line-number="876"></td>
        <td id="LC876" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L877" class="blob-num js-line-number" data-line-number="877"></td>
        <td id="LC877" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> make sure each custom w3c field regex has a named group</span></td>
      </tr>
      <tr>
        <td id="L878" class="blob-num js-line-number" data-line-number="878"></td>
        <td id="LC878" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> field_name, field_regex <span class="pl-k">in</span> <span class="pl-c1">self</span>.options.w3c_field_regexes.iteritems():</td>
      </tr>
      <tr>
        <td id="L879" class="blob-num js-line-number" data-line-number="879"></td>
        <td id="LC879" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>(?P&lt;<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> field_regex:</td>
      </tr>
      <tr>
        <td id="L880" class="blob-num js-line-number" data-line-number="880"></td>
        <td id="LC880" class="blob-code blob-code-inner js-file-line">                    fatal_error(<span class="pl-s"><span class="pl-pds">&quot;</span>cannot find named group in custom w3c field regex &#39;<span class="pl-c1">%s</span>&#39; for field &#39;<span class="pl-c1">%s</span>&#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (field_regex, field_name))</td>
      </tr>
      <tr>
        <td id="L881" class="blob-num js-line-number" data-line-number="881"></td>
        <td id="LC881" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L882" class="blob-num js-line-number" data-line-number="882"></td>
        <td id="LC882" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L883" class="blob-num js-line-number" data-line-number="883"></td>
        <td id="LC883" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>.options.piwik_url:</td>
      </tr>
      <tr>
        <td id="L884" class="blob-num js-line-number" data-line-number="884"></td>
        <td id="LC884" class="blob-code blob-code-inner js-file-line">            fatal_error(<span class="pl-s"><span class="pl-pds">&#39;</span>no URL given for Piwik<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L885" class="blob-num js-line-number" data-line-number="885"></td>
        <td id="LC885" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L886" class="blob-num js-line-number" data-line-number="886"></td>
        <td id="LC886" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> (<span class="pl-c1">self</span>.options.piwik_url.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> <span class="pl-c1">self</span>.options.piwik_url.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>https://<span class="pl-pds">&#39;</span></span>)):</td>
      </tr>
      <tr>
        <td id="L887" class="blob-num js-line-number" data-line-number="887"></td>
        <td id="LC887" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.piwik_url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">self</span>.options.piwik_url</td>
      </tr>
      <tr>
        <td id="L888" class="blob-num js-line-number" data-line-number="888"></td>
        <td id="LC888" class="blob-code blob-code-inner js-file-line">        logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Piwik Tracker API URL is: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.options.piwik_url)</td>
      </tr>
      <tr>
        <td id="L889" class="blob-num js-line-number" data-line-number="889"></td>
        <td id="LC889" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L890" class="blob-num js-line-number" data-line-number="890"></td>
        <td id="LC890" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>.options.piwik_api_url:</td>
      </tr>
      <tr>
        <td id="L891" class="blob-num js-line-number" data-line-number="891"></td>
        <td id="LC891" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.piwik_api_url <span class="pl-k">=</span> <span class="pl-c1">self</span>.options.piwik_url</td>
      </tr>
      <tr>
        <td id="L892" class="blob-num js-line-number" data-line-number="892"></td>
        <td id="LC892" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L893" class="blob-num js-line-number" data-line-number="893"></td>
        <td id="LC893" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> (<span class="pl-c1">self</span>.options.piwik_api_url.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> <span class="pl-c1">self</span>.options.piwik_api_url.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>https://<span class="pl-pds">&#39;</span></span>)):</td>
      </tr>
      <tr>
        <td id="L894" class="blob-num js-line-number" data-line-number="894"></td>
        <td id="LC894" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.piwik_api_url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> <span class="pl-c1">self</span>.options.piwik_api_url</td>
      </tr>
      <tr>
        <td id="L895" class="blob-num js-line-number" data-line-number="895"></td>
        <td id="LC895" class="blob-code blob-code-inner js-file-line">        logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Piwik Analytics API URL is: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.options.piwik_api_url)</td>
      </tr>
      <tr>
        <td id="L896" class="blob-num js-line-number" data-line-number="896"></td>
        <td id="LC896" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L897" class="blob-num js-line-number" data-line-number="897"></td>
        <td id="LC897" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>.options.piwik_token_auth:</td>
      </tr>
      <tr>
        <td id="L898" class="blob-num js-line-number" data-line-number="898"></td>
        <td id="LC898" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L899" class="blob-num js-line-number" data-line-number="899"></td>
        <td id="LC899" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.options.piwik_token_auth <span class="pl-k">=</span> <span class="pl-c1">self</span>._get_token_auth()</td>
      </tr>
      <tr>
        <td id="L900" class="blob-num js-line-number" data-line-number="900"></td>
        <td id="LC900" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> Piwik.Error, e:</td>
      </tr>
      <tr>
        <td id="L901" class="blob-num js-line-number" data-line-number="901"></td>
        <td id="LC901" class="blob-code blob-code-inner js-file-line">                fatal_error(e)</td>
      </tr>
      <tr>
        <td id="L902" class="blob-num js-line-number" data-line-number="902"></td>
        <td id="LC902" class="blob-code blob-code-inner js-file-line">        logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Authentication token token_auth is: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, <span class="pl-c1">self</span>.options.piwik_token_auth)</td>
      </tr>
      <tr>
        <td id="L903" class="blob-num js-line-number" data-line-number="903"></td>
        <td id="LC903" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L904" class="blob-num js-line-number" data-line-number="904"></td>
        <td id="LC904" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.recorders <span class="pl-k">&lt;</span> <span class="pl-c1">1</span>:</td>
      </tr>
      <tr>
        <td id="L905" class="blob-num js-line-number" data-line-number="905"></td>
        <td id="LC905" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.recorders <span class="pl-k">=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L906" class="blob-num js-line-number" data-line-number="906"></td>
        <td id="LC906" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L907" class="blob-num js-line-number" data-line-number="907"></td>
        <td id="LC907" class="blob-code blob-code-inner js-file-line">        download_extensions <span class="pl-k">=</span> <span class="pl-c1">DOWNLOAD_EXTENSIONS</span></td>
      </tr>
      <tr>
        <td id="L908" class="blob-num js-line-number" data-line-number="908"></td>
        <td id="LC908" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.download_extensions:</td>
      </tr>
      <tr>
        <td id="L909" class="blob-num js-line-number" data-line-number="909"></td>
        <td id="LC909" class="blob-code blob-code-inner js-file-line">            download_extensions <span class="pl-k">=</span> <span class="pl-c1">set</span>(<span class="pl-c1">self</span>.options.download_extensions.split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L910" class="blob-num js-line-number" data-line-number="910"></td>
        <td id="LC910" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L911" class="blob-num js-line-number" data-line-number="911"></td>
        <td id="LC911" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.extra_download_extensions:</td>
      </tr>
      <tr>
        <td id="L912" class="blob-num js-line-number" data-line-number="912"></td>
        <td id="LC912" class="blob-code blob-code-inner js-file-line">            download_extensions.update(<span class="pl-c1">self</span>.options.extra_download_extensions.split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L913" class="blob-num js-line-number" data-line-number="913"></td>
        <td id="LC913" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.options.download_extensions <span class="pl-k">=</span> download_extensions</td>
      </tr>
      <tr>
        <td id="L914" class="blob-num js-line-number" data-line-number="914"></td>
        <td id="LC914" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L915" class="blob-num js-line-number" data-line-number="915"></td>
        <td id="LC915" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.regex_groups_to_ignore:</td>
      </tr>
      <tr>
        <td id="L916" class="blob-num js-line-number" data-line-number="916"></td>
        <td id="LC916" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.options.regex_groups_to_ignore <span class="pl-k">=</span> <span class="pl-c1">set</span>(<span class="pl-c1">self</span>.options.regex_groups_to_ignore.split(<span class="pl-s"><span class="pl-pds">&#39;</span>,<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L917" class="blob-num js-line-number" data-line-number="917"></td>
        <td id="LC917" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L918" class="blob-num js-line-number" data-line-number="918"></td>
        <td id="LC918" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L919" class="blob-num js-line-number" data-line-number="919"></td>
        <td id="LC919" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._parse_args(<span class="pl-c1">self</span>._create_parser())</td>
      </tr>
      <tr>
        <td id="L920" class="blob-num js-line-number" data-line-number="920"></td>
        <td id="LC920" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L921" class="blob-num js-line-number" data-line-number="921"></td>
        <td id="LC921" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_get_token_auth</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L922" class="blob-num js-line-number" data-line-number="922"></td>
        <td id="LC922" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L923" class="blob-num js-line-number" data-line-number="923"></td>
        <td id="LC923" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        If the token auth is not specified in the options, get it from Piwik.</span></td>
      </tr>
      <tr>
        <td id="L924" class="blob-num js-line-number" data-line-number="924"></td>
        <td id="LC924" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L925" class="blob-num js-line-number" data-line-number="925"></td>
        <td id="LC925" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Get superuser login/password from the options.</span></td>
      </tr>
      <tr>
        <td id="L926" class="blob-num js-line-number" data-line-number="926"></td>
        <td id="LC926" class="blob-code blob-code-inner js-file-line">        logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>No token-auth specified<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L927" class="blob-num js-line-number" data-line-number="927"></td>
        <td id="LC927" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L928" class="blob-num js-line-number" data-line-number="928"></td>
        <td id="LC928" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.login <span class="pl-k">and</span> <span class="pl-c1">self</span>.options.password:</td>
      </tr>
      <tr>
        <td id="L929" class="blob-num js-line-number" data-line-number="929"></td>
        <td id="LC929" class="blob-code blob-code-inner js-file-line">            piwik_login <span class="pl-k">=</span> <span class="pl-c1">self</span>.options.login</td>
      </tr>
      <tr>
        <td id="L930" class="blob-num js-line-number" data-line-number="930"></td>
        <td id="LC930" class="blob-code blob-code-inner js-file-line">            piwik_password <span class="pl-k">=</span> hashlib.md5(<span class="pl-c1">self</span>.options.password).hexdigest()</td>
      </tr>
      <tr>
        <td id="L931" class="blob-num js-line-number" data-line-number="931"></td>
        <td id="LC931" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L932" class="blob-num js-line-number" data-line-number="932"></td>
        <td id="LC932" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Using credentials: (login = <span class="pl-c1">%s</span>, password = <span class="pl-c1">%s</span>)<span class="pl-pds">&#39;</span></span>, piwik_login, piwik_password)</td>
      </tr>
      <tr>
        <td id="L933" class="blob-num js-line-number" data-line-number="933"></td>
        <td id="LC933" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L934" class="blob-num js-line-number" data-line-number="934"></td>
        <td id="LC934" class="blob-code blob-code-inner js-file-line">                api_result <span class="pl-k">=</span> piwik.call_api(<span class="pl-s"><span class="pl-pds">&#39;</span>UsersManager.getTokenAuth<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L935" class="blob-num js-line-number" data-line-number="935"></td>
        <td id="LC935" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">userLogin</span><span class="pl-k">=</span>piwik_login,</td>
      </tr>
      <tr>
        <td id="L936" class="blob-num js-line-number" data-line-number="936"></td>
        <td id="LC936" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">md5Password</span><span class="pl-k">=</span>piwik_password,</td>
      </tr>
      <tr>
        <td id="L937" class="blob-num js-line-number" data-line-number="937"></td>
        <td id="LC937" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">_token_auth</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L938" class="blob-num js-line-number" data-line-number="938"></td>
        <td id="LC938" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">_url</span><span class="pl-k">=</span><span class="pl-c1">self</span>.options.piwik_api_url,</td>
      </tr>
      <tr>
        <td id="L939" class="blob-num js-line-number" data-line-number="939"></td>
        <td id="LC939" class="blob-code blob-code-inner js-file-line">                )</td>
      </tr>
      <tr>
        <td id="L940" class="blob-num js-line-number" data-line-number="940"></td>
        <td id="LC940" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> urllib2.URLError, e:</td>
      </tr>
      <tr>
        <td id="L941" class="blob-num js-line-number" data-line-number="941"></td>
        <td id="LC941" class="blob-code blob-code-inner js-file-line">                fatal_error(<span class="pl-s"><span class="pl-pds">&#39;</span>error when fetching token_auth from the API: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> e)</td>
      </tr>
      <tr>
        <td id="L942" class="blob-num js-line-number" data-line-number="942"></td>
        <td id="LC942" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L943" class="blob-num js-line-number" data-line-number="943"></td>
        <td id="LC943" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L944" class="blob-num js-line-number" data-line-number="944"></td>
        <td id="LC944" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> api_result[<span class="pl-s"><span class="pl-pds">&#39;</span>value<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L945" class="blob-num js-line-number" data-line-number="945"></td>
        <td id="LC945" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L946" class="blob-num js-line-number" data-line-number="946"></td>
        <td id="LC946" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> Happens when the credentials are invalid.</span></td>
      </tr>
      <tr>
        <td id="L947" class="blob-num js-line-number" data-line-number="947"></td>
        <td id="LC947" class="blob-code blob-code-inner js-file-line">                message <span class="pl-k">=</span> api_result.get(<span class="pl-s"><span class="pl-pds">&#39;</span>message<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L948" class="blob-num js-line-number" data-line-number="948"></td>
        <td id="LC948" class="blob-code blob-code-inner js-file-line">                fatal_error(</td>
      </tr>
      <tr>
        <td id="L949" class="blob-num js-line-number" data-line-number="949"></td>
        <td id="LC949" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>error fetching authentication token token_auth<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (</td>
      </tr>
      <tr>
        <td id="L950" class="blob-num js-line-number" data-line-number="950"></td>
        <td id="LC950" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> message <span class="pl-k">if</span> message <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L951" class="blob-num js-line-number" data-line-number="951"></td>
        <td id="LC951" class="blob-code blob-code-inner js-file-line">                )</td>
      </tr>
      <tr>
        <td id="L952" class="blob-num js-line-number" data-line-number="952"></td>
        <td id="LC952" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L953" class="blob-num js-line-number" data-line-number="953"></td>
        <td id="LC953" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> Fallback to the given (or default) configuration file, then</span></td>
      </tr>
      <tr>
        <td id="L954" class="blob-num js-line-number" data-line-number="954"></td>
        <td id="LC954" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> get the token from the API.</span></td>
      </tr>
      <tr>
        <td id="L955" class="blob-num js-line-number" data-line-number="955"></td>
        <td id="LC955" class="blob-code blob-code-inner js-file-line">            logging.debug(</td>
      </tr>
      <tr>
        <td id="L956" class="blob-num js-line-number" data-line-number="956"></td>
        <td id="LC956" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>No credentials specified, reading them from &quot;<span class="pl-c1">%s</span>&quot;<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L957" class="blob-num js-line-number" data-line-number="957"></td>
        <td id="LC957" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.options.config_file,</td>
      </tr>
      <tr>
        <td id="L958" class="blob-num js-line-number" data-line-number="958"></td>
        <td id="LC958" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L959" class="blob-num js-line-number" data-line-number="959"></td>
        <td id="LC959" class="blob-code blob-code-inner js-file-line">            config_file <span class="pl-k">=</span> ConfigParser.RawConfigParser()</td>
      </tr>
      <tr>
        <td id="L960" class="blob-num js-line-number" data-line-number="960"></td>
        <td id="LC960" class="blob-code blob-code-inner js-file-line">            success <span class="pl-k">=</span> <span class="pl-c1">len</span>(config_file.read(<span class="pl-c1">self</span>.options.config_file)) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L961" class="blob-num js-line-number" data-line-number="961"></td>
        <td id="LC961" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> success:</td>
      </tr>
      <tr>
        <td id="L962" class="blob-num js-line-number" data-line-number="962"></td>
        <td id="LC962" class="blob-code blob-code-inner js-file-line">                fatal_error(</td>
      </tr>
      <tr>
        <td id="L963" class="blob-num js-line-number" data-line-number="963"></td>
        <td id="LC963" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&quot;</span>the configuration file<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">self</span>.options.config_file <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span> could not be read. Please check permission. This file must be readable by the user running this script to get the authentication token<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L964" class="blob-num js-line-number" data-line-number="964"></td>
        <td id="LC964" class="blob-code blob-code-inner js-file-line">                )</td>
      </tr>
      <tr>
        <td id="L965" class="blob-num js-line-number" data-line-number="965"></td>
        <td id="LC965" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L966" class="blob-num js-line-number" data-line-number="966"></td>
        <td id="LC966" class="blob-code blob-code-inner js-file-line">            updatetokenfile <span class="pl-k">=</span> os.path.abspath(</td>
      </tr>
      <tr>
        <td id="L967" class="blob-num js-line-number" data-line-number="967"></td>
        <td id="LC967" class="blob-code blob-code-inner js-file-line">                os.path.join(os.path.dirname(<span class="pl-c1">__file__</span>),</td>
      </tr>
      <tr>
        <td id="L968" class="blob-num js-line-number" data-line-number="968"></td>
        <td id="LC968" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>../../misc/cron/updatetoken.php<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L969" class="blob-num js-line-number" data-line-number="969"></td>
        <td id="LC969" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L970" class="blob-num js-line-number" data-line-number="970"></td>
        <td id="LC970" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L971" class="blob-num js-line-number" data-line-number="971"></td>
        <td id="LC971" class="blob-code blob-code-inner js-file-line">            phpBinary <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>php<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L972" class="blob-num js-line-number" data-line-number="972"></td>
        <td id="LC972" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L973" class="blob-num js-line-number" data-line-number="973"></td>
        <td id="LC973" class="blob-code blob-code-inner js-file-line">            is_windows <span class="pl-k">=</span> sys.platform.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>win<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L974" class="blob-num js-line-number" data-line-number="974"></td>
        <td id="LC974" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> is_windows:</td>
      </tr>
      <tr>
        <td id="L975" class="blob-num js-line-number" data-line-number="975"></td>
        <td id="LC975" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L976" class="blob-num js-line-number" data-line-number="976"></td>
        <td id="LC976" class="blob-code blob-code-inner js-file-line">                    processWin <span class="pl-k">=</span> subprocess.Popen(<span class="pl-s"><span class="pl-pds">&#39;</span>where php.exe<span class="pl-pds">&#39;</span></span>, <span class="pl-v">stdout</span><span class="pl-k">=</span>subprocess.<span class="pl-c1">PIPE</span>, <span class="pl-v">stderr</span><span class="pl-k">=</span>subprocess.<span class="pl-c1">PIPE</span>)</td>
      </tr>
      <tr>
        <td id="L977" class="blob-num js-line-number" data-line-number="977"></td>
        <td id="LC977" class="blob-code blob-code-inner js-file-line">                    [stdout, stderr] <span class="pl-k">=</span> processWin.communicate()</td>
      </tr>
      <tr>
        <td id="L978" class="blob-num js-line-number" data-line-number="978"></td>
        <td id="LC978" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> processWin.returncode <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L979" class="blob-num js-line-number" data-line-number="979"></td>
        <td id="LC979" class="blob-code blob-code-inner js-file-line">                        phpBinary <span class="pl-k">=</span> stdout.strip()</td>
      </tr>
      <tr>
        <td id="L980" class="blob-num js-line-number" data-line-number="980"></td>
        <td id="LC980" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L981" class="blob-num js-line-number" data-line-number="981"></td>
        <td id="LC981" class="blob-code blob-code-inner js-file-line">                        fatal_error(<span class="pl-s"><span class="pl-pds">&quot;</span>We couldn&#39;t detect PHP. It might help to add your php.exe to the path or alternatively run the importer using the --login and --password option<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L982" class="blob-num js-line-number" data-line-number="982"></td>
        <td id="LC982" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L983" class="blob-num js-line-number" data-line-number="983"></td>
        <td id="LC983" class="blob-code blob-code-inner js-file-line">                    fatal_error(<span class="pl-s"><span class="pl-pds">&quot;</span>We couldn&#39;t detect PHP. You can run the importer using the --login and --password option to fix this issue<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L984" class="blob-num js-line-number" data-line-number="984"></td>
        <td id="LC984" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L985" class="blob-num js-line-number" data-line-number="985"></td>
        <td id="LC985" class="blob-code blob-code-inner js-file-line">            command <span class="pl-k">=</span> [phpBinary, updatetokenfile]</td>
      </tr>
      <tr>
        <td id="L986" class="blob-num js-line-number" data-line-number="986"></td>
        <td id="LC986" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.enable_testmode:</td>
      </tr>
      <tr>
        <td id="L987" class="blob-num js-line-number" data-line-number="987"></td>
        <td id="LC987" class="blob-code blob-code-inner js-file-line">                command.append(<span class="pl-s"><span class="pl-pds">&#39;</span>--testmode<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L988" class="blob-num js-line-number" data-line-number="988"></td>
        <td id="LC988" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L989" class="blob-num js-line-number" data-line-number="989"></td>
        <td id="LC989" class="blob-code blob-code-inner js-file-line">            hostname <span class="pl-k">=</span> urlparse.urlparse( <span class="pl-c1">self</span>.options.piwik_url ).hostname</td>
      </tr>
      <tr>
        <td id="L990" class="blob-num js-line-number" data-line-number="990"></td>
        <td id="LC990" class="blob-code blob-code-inner js-file-line">            command.append(<span class="pl-s"><span class="pl-pds">&#39;</span>--piwik-domain=<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> hostname )</td>
      </tr>
      <tr>
        <td id="L991" class="blob-num js-line-number" data-line-number="991"></td>
        <td id="LC991" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L992" class="blob-num js-line-number" data-line-number="992"></td>
        <td id="LC992" class="blob-code blob-code-inner js-file-line">            command <span class="pl-k">=</span> subprocess.list2cmdline(command)</td>
      </tr>
      <tr>
        <td id="L993" class="blob-num js-line-number" data-line-number="993"></td>
        <td id="LC993" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L994" class="blob-num js-line-number" data-line-number="994"></td>
        <td id="LC994" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>            logging.debug(command);</span></td>
      </tr>
      <tr>
        <td id="L995" class="blob-num js-line-number" data-line-number="995"></td>
        <td id="LC995" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L996" class="blob-num js-line-number" data-line-number="996"></td>
        <td id="LC996" class="blob-code blob-code-inner js-file-line">            process <span class="pl-k">=</span> subprocess.Popen(command, <span class="pl-v">stdout</span><span class="pl-k">=</span>subprocess.<span class="pl-c1">PIPE</span>, <span class="pl-v">stderr</span><span class="pl-k">=</span>subprocess.<span class="pl-c1">PIPE</span>, <span class="pl-v">shell</span><span class="pl-k">=</span><span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L997" class="blob-num js-line-number" data-line-number="997"></td>
        <td id="LC997" class="blob-code blob-code-inner js-file-line">            [stdout, stderr] <span class="pl-k">=</span> process.communicate()</td>
      </tr>
      <tr>
        <td id="L998" class="blob-num js-line-number" data-line-number="998"></td>
        <td id="LC998" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> process.returncode <span class="pl-k">!=</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L999" class="blob-num js-line-number" data-line-number="999"></td>
        <td id="LC999" class="blob-code blob-code-inner js-file-line">                fatal_error(<span class="pl-s"><span class="pl-pds">&quot;</span>`<span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> command <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>` failed with error: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> stderr <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>.<span class="pl-cce">\n</span>Reponse code was: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> <span class="pl-c1">str</span>(process.returncode) <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>. You can alternatively run the importer using the --login and --password option<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1000" class="blob-num js-line-number" data-line-number="1000"></td>
        <td id="LC1000" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1001" class="blob-num js-line-number" data-line-number="1001"></td>
        <td id="LC1001" class="blob-code blob-code-inner js-file-line">            filename <span class="pl-k">=</span> stdout</td>
      </tr>
      <tr>
        <td id="L1002" class="blob-num js-line-number" data-line-number="1002"></td>
        <td id="LC1002" class="blob-code blob-code-inner js-file-line">            credentials <span class="pl-k">=</span> <span class="pl-c1">open</span>(filename, <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>).readline()</td>
      </tr>
      <tr>
        <td id="L1003" class="blob-num js-line-number" data-line-number="1003"></td>
        <td id="LC1003" class="blob-code blob-code-inner js-file-line">            credentials <span class="pl-k">=</span> credentials.split(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\t</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1004" class="blob-num js-line-number" data-line-number="1004"></td>
        <td id="LC1004" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> credentials[<span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L1005" class="blob-num js-line-number" data-line-number="1005"></td>
        <td id="LC1005" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1006" class="blob-num js-line-number" data-line-number="1006"></td>
        <td id="LC1006" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_resolver</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1007" class="blob-num js-line-number" data-line-number="1007"></td>
        <td id="LC1007" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.options.site_id:</td>
      </tr>
      <tr>
        <td id="L1008" class="blob-num js-line-number" data-line-number="1008"></td>
        <td id="LC1008" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Resolver: static<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1009" class="blob-num js-line-number" data-line-number="1009"></td>
        <td id="LC1009" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> StaticResolver(<span class="pl-c1">self</span>.options.site_id)</td>
      </tr>
      <tr>
        <td id="L1010" class="blob-num js-line-number" data-line-number="1010"></td>
        <td id="LC1010" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1011" class="blob-num js-line-number" data-line-number="1011"></td>
        <td id="LC1011" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Resolver: dynamic<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1012" class="blob-num js-line-number" data-line-number="1012"></td>
        <td id="LC1012" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> DynamicResolver()</td>
      </tr>
      <tr>
        <td id="L1013" class="blob-num js-line-number" data-line-number="1013"></td>
        <td id="LC1013" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1014" class="blob-num js-line-number" data-line-number="1014"></td>
        <td id="LC1014" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Statistics</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L1015" class="blob-num js-line-number" data-line-number="1015"></td>
        <td id="LC1015" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1016" class="blob-num js-line-number" data-line-number="1016"></td>
        <td id="LC1016" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Store statistics about parsed logs and recorded entries.</span></td>
      </tr>
      <tr>
        <td id="L1017" class="blob-num js-line-number" data-line-number="1017"></td>
        <td id="LC1017" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Can optionally print statistics on standard output every second.</span></td>
      </tr>
      <tr>
        <td id="L1018" class="blob-num js-line-number" data-line-number="1018"></td>
        <td id="LC1018" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1019" class="blob-num js-line-number" data-line-number="1019"></td>
        <td id="LC1019" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1020" class="blob-num js-line-number" data-line-number="1020"></td>
        <td id="LC1020" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">class</span> <span class="pl-en">Counter</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L1021" class="blob-num js-line-number" data-line-number="1021"></td>
        <td id="LC1021" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1022" class="blob-num js-line-number" data-line-number="1022"></td>
        <td id="LC1022" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Simple integers cannot be used by multithreaded programs. See:</span></td>
      </tr>
      <tr>
        <td id="L1023" class="blob-num js-line-number" data-line-number="1023"></td>
        <td id="LC1023" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        http://stackoverflow.com/questions/6320107/are-python-ints-thread-safe</span></td>
      </tr>
      <tr>
        <td id="L1024" class="blob-num js-line-number" data-line-number="1024"></td>
        <td id="LC1024" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1025" class="blob-num js-line-number" data-line-number="1025"></td>
        <td id="LC1025" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1026" class="blob-num js-line-number" data-line-number="1026"></td>
        <td id="LC1026" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> itertools.count&#39;s implementation in C does not release the GIL and</span></td>
      </tr>
      <tr>
        <td id="L1027" class="blob-num js-line-number" data-line-number="1027"></td>
        <td id="LC1027" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> therefore is thread-safe.</span></td>
      </tr>
      <tr>
        <td id="L1028" class="blob-num js-line-number" data-line-number="1028"></td>
        <td id="LC1028" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.counter <span class="pl-k">=</span> itertools.count(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L1029" class="blob-num js-line-number" data-line-number="1029"></td>
        <td id="LC1029" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.value <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L1030" class="blob-num js-line-number" data-line-number="1030"></td>
        <td id="LC1030" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1031" class="blob-num js-line-number" data-line-number="1031"></td>
        <td id="LC1031" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">increment</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1032" class="blob-num js-line-number" data-line-number="1032"></td>
        <td id="LC1032" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.value <span class="pl-k">=</span> <span class="pl-c1">self</span>.counter.next()</td>
      </tr>
      <tr>
        <td id="L1033" class="blob-num js-line-number" data-line-number="1033"></td>
        <td id="LC1033" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1034" class="blob-num js-line-number" data-line-number="1034"></td>
        <td id="LC1034" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">advance</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">n</span>):</td>
      </tr>
      <tr>
        <td id="L1035" class="blob-num js-line-number" data-line-number="1035"></td>
        <td id="LC1035" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-c1">range</span>(n):</td>
      </tr>
      <tr>
        <td id="L1036" class="blob-num js-line-number" data-line-number="1036"></td>
        <td id="LC1036" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.increment()</td>
      </tr>
      <tr>
        <td id="L1037" class="blob-num js-line-number" data-line-number="1037"></td>
        <td id="LC1037" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1038" class="blob-num js-line-number" data-line-number="1038"></td>
        <td id="LC1038" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-c1">__str__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1039" class="blob-num js-line-number" data-line-number="1039"></td>
        <td id="LC1039" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">str</span>(<span class="pl-c1">int</span>(<span class="pl-c1">self</span>.value))</td>
      </tr>
      <tr>
        <td id="L1040" class="blob-num js-line-number" data-line-number="1040"></td>
        <td id="LC1040" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1041" class="blob-num js-line-number" data-line-number="1041"></td>
        <td id="LC1041" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1042" class="blob-num js-line-number" data-line-number="1042"></td>
        <td id="LC1042" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.time_start <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L1043" class="blob-num js-line-number" data-line-number="1043"></td>
        <td id="LC1043" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.time_stop <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L1044" class="blob-num js-line-number" data-line-number="1044"></td>
        <td id="LC1044" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1045" class="blob-num js-line-number" data-line-number="1045"></td>
        <td id="LC1045" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.piwik_sites <span class="pl-k">=</span> <span class="pl-c1">set</span>()                <span class="pl-c"><span class="pl-c">#</span> sites ID</span></td>
      </tr>
      <tr>
        <td id="L1046" class="blob-num js-line-number" data-line-number="1046"></td>
        <td id="LC1046" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.piwik_sites_created <span class="pl-k">=</span> []           <span class="pl-c"><span class="pl-c">#</span> (hostname, site ID)</span></td>
      </tr>
      <tr>
        <td id="L1047" class="blob-num js-line-number" data-line-number="1047"></td>
        <td id="LC1047" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.piwik_sites_ignored <span class="pl-k">=</span> <span class="pl-c1">set</span>()        <span class="pl-c"><span class="pl-c">#</span> hostname</span></td>
      </tr>
      <tr>
        <td id="L1048" class="blob-num js-line-number" data-line-number="1048"></td>
        <td id="LC1048" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1049" class="blob-num js-line-number" data-line-number="1049"></td>
        <td id="LC1049" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_parsed <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1050" class="blob-num js-line-number" data-line-number="1050"></td>
        <td id="LC1050" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_recorded <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1051" class="blob-num js-line-number" data-line-number="1051"></td>
        <td id="LC1051" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1052" class="blob-num js-line-number" data-line-number="1052"></td>
        <td id="LC1052" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> requests that the Piwik tracker considered invalid (or failed to track)</span></td>
      </tr>
      <tr>
        <td id="L1053" class="blob-num js-line-number" data-line-number="1053"></td>
        <td id="LC1053" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.invalid_lines <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1054" class="blob-num js-line-number" data-line-number="1054"></td>
        <td id="LC1054" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1055" class="blob-num js-line-number" data-line-number="1055"></td>
        <td id="LC1055" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Do not match the regexp.</span></td>
      </tr>
      <tr>
        <td id="L1056" class="blob-num js-line-number" data-line-number="1056"></td>
        <td id="LC1056" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_invalid <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1057" class="blob-num js-line-number" data-line-number="1057"></td>
        <td id="LC1057" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> No site ID found by the resolver.</span></td>
      </tr>
      <tr>
        <td id="L1058" class="blob-num js-line-number" data-line-number="1058"></td>
        <td id="LC1058" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_no_site <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1059" class="blob-num js-line-number" data-line-number="1059"></td>
        <td id="LC1059" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Hostname filtered by config.options.hostnames</span></td>
      </tr>
      <tr>
        <td id="L1060" class="blob-num js-line-number" data-line-number="1060"></td>
        <td id="LC1060" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_hostname_skipped <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1061" class="blob-num js-line-number" data-line-number="1061"></td>
        <td id="LC1061" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Static files.</span></td>
      </tr>
      <tr>
        <td id="L1062" class="blob-num js-line-number" data-line-number="1062"></td>
        <td id="LC1062" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_static <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1063" class="blob-num js-line-number" data-line-number="1063"></td>
        <td id="LC1063" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Ignored user-agents.</span></td>
      </tr>
      <tr>
        <td id="L1064" class="blob-num js-line-number" data-line-number="1064"></td>
        <td id="LC1064" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_skipped_user_agent <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1065" class="blob-num js-line-number" data-line-number="1065"></td>
        <td id="LC1065" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Ignored HTTP erors.</span></td>
      </tr>
      <tr>
        <td id="L1066" class="blob-num js-line-number" data-line-number="1066"></td>
        <td id="LC1066" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_skipped_http_errors <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1067" class="blob-num js-line-number" data-line-number="1067"></td>
        <td id="LC1067" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Ignored HTTP redirects.</span></td>
      </tr>
      <tr>
        <td id="L1068" class="blob-num js-line-number" data-line-number="1068"></td>
        <td id="LC1068" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_skipped_http_redirects <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1069" class="blob-num js-line-number" data-line-number="1069"></td>
        <td id="LC1069" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Downloads</span></td>
      </tr>
      <tr>
        <td id="L1070" class="blob-num js-line-number" data-line-number="1070"></td>
        <td id="LC1070" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_downloads <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1071" class="blob-num js-line-number" data-line-number="1071"></td>
        <td id="LC1071" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Ignored downloads when --download-extensions is used</span></td>
      </tr>
      <tr>
        <td id="L1072" class="blob-num js-line-number" data-line-number="1072"></td>
        <td id="LC1072" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.count_lines_skipped_downloads <span class="pl-k">=</span> <span class="pl-c1">self</span>.Counter()</td>
      </tr>
      <tr>
        <td id="L1073" class="blob-num js-line-number" data-line-number="1073"></td>
        <td id="LC1073" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1074" class="blob-num js-line-number" data-line-number="1074"></td>
        <td id="LC1074" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Misc</span></td>
      </tr>
      <tr>
        <td id="L1075" class="blob-num js-line-number" data-line-number="1075"></td>
        <td id="LC1075" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.dates_recorded <span class="pl-k">=</span> <span class="pl-c1">set</span>()</td>
      </tr>
      <tr>
        <td id="L1076" class="blob-num js-line-number" data-line-number="1076"></td>
        <td id="LC1076" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.monitor_stop <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1077" class="blob-num js-line-number" data-line-number="1077"></td>
        <td id="LC1077" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1078" class="blob-num js-line-number" data-line-number="1078"></td>
        <td id="LC1078" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">set_time_start</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1079" class="blob-num js-line-number" data-line-number="1079"></td>
        <td id="LC1079" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.time_start <span class="pl-k">=</span> time.time()</td>
      </tr>
      <tr>
        <td id="L1080" class="blob-num js-line-number" data-line-number="1080"></td>
        <td id="LC1080" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1081" class="blob-num js-line-number" data-line-number="1081"></td>
        <td id="LC1081" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">set_time_stop</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1082" class="blob-num js-line-number" data-line-number="1082"></td>
        <td id="LC1082" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.time_stop <span class="pl-k">=</span> time.time()</td>
      </tr>
      <tr>
        <td id="L1083" class="blob-num js-line-number" data-line-number="1083"></td>
        <td id="LC1083" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1084" class="blob-num js-line-number" data-line-number="1084"></td>
        <td id="LC1084" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_compute_speed</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">value</span>, <span class="pl-smi">start</span>, <span class="pl-smi">end</span>):</td>
      </tr>
      <tr>
        <td id="L1085" class="blob-num js-line-number" data-line-number="1085"></td>
        <td id="LC1085" class="blob-code blob-code-inner js-file-line">        delta_time <span class="pl-k">=</span> end <span class="pl-k">-</span> start</td>
      </tr>
      <tr>
        <td id="L1086" class="blob-num js-line-number" data-line-number="1086"></td>
        <td id="LC1086" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> value <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1087" class="blob-num js-line-number" data-line-number="1087"></td>
        <td id="LC1087" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L1088" class="blob-num js-line-number" data-line-number="1088"></td>
        <td id="LC1088" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> delta_time <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1089" class="blob-num js-line-number" data-line-number="1089"></td>
        <td id="LC1089" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span>very high!<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1090" class="blob-num js-line-number" data-line-number="1090"></td>
        <td id="LC1090" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1091" class="blob-num js-line-number" data-line-number="1091"></td>
        <td id="LC1091" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> value <span class="pl-k">/</span> delta_time</td>
      </tr>
      <tr>
        <td id="L1092" class="blob-num js-line-number" data-line-number="1092"></td>
        <td id="LC1092" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1093" class="blob-num js-line-number" data-line-number="1093"></td>
        <td id="LC1093" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_round_value</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">value</span>, <span class="pl-smi">base</span><span class="pl-k">=</span><span class="pl-c1">100</span>):</td>
      </tr>
      <tr>
        <td id="L1094" class="blob-num js-line-number" data-line-number="1094"></td>
        <td id="LC1094" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">round</span>(value <span class="pl-k">*</span> base) <span class="pl-k">/</span> base</td>
      </tr>
      <tr>
        <td id="L1095" class="blob-num js-line-number" data-line-number="1095"></td>
        <td id="LC1095" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1096" class="blob-num js-line-number" data-line-number="1096"></td>
        <td id="LC1096" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_indent_text</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">lines</span>, <span class="pl-smi">level</span><span class="pl-k">=</span><span class="pl-c1">1</span>):</td>
      </tr>
      <tr>
        <td id="L1097" class="blob-num js-line-number" data-line-number="1097"></td>
        <td id="LC1097" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1098" class="blob-num js-line-number" data-line-number="1098"></td>
        <td id="LC1098" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Return an indented text. &#39;lines&#39; can be a list of lines or a single</span></td>
      </tr>
      <tr>
        <td id="L1099" class="blob-num js-line-number" data-line-number="1099"></td>
        <td id="LC1099" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        line (as a string). One level of indentation is 4 spaces.</span></td>
      </tr>
      <tr>
        <td id="L1100" class="blob-num js-line-number" data-line-number="1100"></td>
        <td id="LC1100" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1101" class="blob-num js-line-number" data-line-number="1101"></td>
        <td id="LC1101" class="blob-code blob-code-inner js-file-line">        prefix <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span> <span class="pl-k">*</span> (<span class="pl-c1">4</span> <span class="pl-k">*</span> level)</td>
      </tr>
      <tr>
        <td id="L1102" class="blob-num js-line-number" data-line-number="1102"></td>
        <td id="LC1102" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(lines, <span class="pl-v">basestring</span>):</td>
      </tr>
      <tr>
        <td id="L1103" class="blob-num js-line-number" data-line-number="1103"></td>
        <td id="LC1103" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> prefix <span class="pl-k">+</span> lines</td>
      </tr>
      <tr>
        <td id="L1104" class="blob-num js-line-number" data-line-number="1104"></td>
        <td id="LC1104" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1105" class="blob-num js-line-number" data-line-number="1105"></td>
        <td id="LC1105" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>.join(</td>
      </tr>
      <tr>
        <td id="L1106" class="blob-num js-line-number" data-line-number="1106"></td>
        <td id="LC1106" class="blob-code blob-code-inner js-file-line">                prefix <span class="pl-k">+</span> line</td>
      </tr>
      <tr>
        <td id="L1107" class="blob-num js-line-number" data-line-number="1107"></td>
        <td id="LC1107" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> line <span class="pl-k">in</span> lines</td>
      </tr>
      <tr>
        <td id="L1108" class="blob-num js-line-number" data-line-number="1108"></td>
        <td id="LC1108" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L1109" class="blob-num js-line-number" data-line-number="1109"></td>
        <td id="LC1109" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1110" class="blob-num js-line-number" data-line-number="1110"></td>
        <td id="LC1110" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">print_summary</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1111" class="blob-num js-line-number" data-line-number="1111"></td>
        <td id="LC1111" class="blob-code blob-code-inner js-file-line">        invalid_lines_summary <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1112" class="blob-num js-line-number" data-line-number="1112"></td>
        <td id="LC1112" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">self</span>.invalid_lines:</td>
      </tr>
      <tr>
        <td id="L1113" class="blob-num js-line-number" data-line-number="1113"></td>
        <td id="LC1113" class="blob-code blob-code-inner js-file-line">            invalid_lines_summary <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span>Invalid log lines</span></td>
      </tr>
      <tr>
        <td id="L1114" class="blob-num js-line-number" data-line-number="1114"></td>
        <td id="LC1114" class="blob-code blob-code-inner js-file-line"><span class="pl-s">-----------------</span></td>
      </tr>
      <tr>
        <td id="L1115" class="blob-num js-line-number" data-line-number="1115"></td>
        <td id="LC1115" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1116" class="blob-num js-line-number" data-line-number="1116"></td>
        <td id="LC1116" class="blob-code blob-code-inner js-file-line"><span class="pl-s">The following lines were not tracked by Piwik, either due to a malformed tracker request or error in the tracker:</span></td>
      </tr>
      <tr>
        <td id="L1117" class="blob-num js-line-number" data-line-number="1117"></td>
        <td id="LC1117" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1118" class="blob-num js-line-number" data-line-number="1118"></td>
        <td id="LC1118" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-c1">%s</span></span></td>
      </tr>
      <tr>
        <td id="L1119" class="blob-num js-line-number" data-line-number="1119"></td>
        <td id="LC1119" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1120" class="blob-num js-line-number" data-line-number="1120"></td>
        <td id="LC1120" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span> <span class="pl-k">%</span> textwrap.fill(<span class="pl-s"><span class="pl-pds">&quot;</span>, <span class="pl-pds">&quot;</span></span>.join(<span class="pl-c1">self</span>.invalid_lines), <span class="pl-c1">80</span>)</td>
      </tr>
      <tr>
        <td id="L1121" class="blob-num js-line-number" data-line-number="1121"></td>
        <td id="LC1121" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1122" class="blob-num js-line-number" data-line-number="1122"></td>
        <td id="LC1122" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1123" class="blob-num js-line-number" data-line-number="1123"></td>
        <td id="LC1123" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-c1">%(invalid_lines)s</span>Logs import summary</span></td>
      </tr>
      <tr>
        <td id="L1124" class="blob-num js-line-number" data-line-number="1124"></td>
        <td id="LC1124" class="blob-code blob-code-inner js-file-line"><span class="pl-s">-------------------</span></td>
      </tr>
      <tr>
        <td id="L1125" class="blob-num js-line-number" data-line-number="1125"></td>
        <td id="LC1125" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1126" class="blob-num js-line-number" data-line-number="1126"></td>
        <td id="LC1126" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-c1">%(count_lines_recorded)d</span> requests imported successfully</span></td>
      </tr>
      <tr>
        <td id="L1127" class="blob-num js-line-number" data-line-number="1127"></td>
        <td id="LC1127" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-c1">%(count_lines_downloads)d</span> requests were downloads</span></td>
      </tr>
      <tr>
        <td id="L1128" class="blob-num js-line-number" data-line-number="1128"></td>
        <td id="LC1128" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-c1">%(total_lines_ignored)d</span> requests ignored:</span></td>
      </tr>
      <tr>
        <td id="L1129" class="blob-num js-line-number" data-line-number="1129"></td>
        <td id="LC1129" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(count_lines_skipped_http_errors)d</span> HTTP errors</span></td>
      </tr>
      <tr>
        <td id="L1130" class="blob-num js-line-number" data-line-number="1130"></td>
        <td id="LC1130" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(count_lines_skipped_http_redirects)d</span> HTTP redirects</span></td>
      </tr>
      <tr>
        <td id="L1131" class="blob-num js-line-number" data-line-number="1131"></td>
        <td id="LC1131" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(count_lines_invalid)d</span> invalid log lines</span></td>
      </tr>
      <tr>
        <td id="L1132" class="blob-num js-line-number" data-line-number="1132"></td>
        <td id="LC1132" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(count_lines_no_site)d</span> requests did not match any known site</span></td>
      </tr>
      <tr>
        <td id="L1133" class="blob-num js-line-number" data-line-number="1133"></td>
        <td id="LC1133" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(count_lines_hostname_skipped)d</span> requests did not match any --hostname</span></td>
      </tr>
      <tr>
        <td id="L1134" class="blob-num js-line-number" data-line-number="1134"></td>
        <td id="LC1134" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(count_lines_skipped_user_agent)d</span> requests done by bots, search engines...</span></td>
      </tr>
      <tr>
        <td id="L1135" class="blob-num js-line-number" data-line-number="1135"></td>
        <td id="LC1135" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(count_lines_static)d</span> requests to static resources (css, js, images, ico, ttf...)</span></td>
      </tr>
      <tr>
        <td id="L1136" class="blob-num js-line-number" data-line-number="1136"></td>
        <td id="LC1136" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(count_lines_skipped_downloads)d</span> requests to file downloads did not match any --download-extensions</span></td>
      </tr>
      <tr>
        <td id="L1137" class="blob-num js-line-number" data-line-number="1137"></td>
        <td id="LC1137" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1138" class="blob-num js-line-number" data-line-number="1138"></td>
        <td id="LC1138" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Website import summary</span></td>
      </tr>
      <tr>
        <td id="L1139" class="blob-num js-line-number" data-line-number="1139"></td>
        <td id="LC1139" class="blob-code blob-code-inner js-file-line"><span class="pl-s">----------------------</span></td>
      </tr>
      <tr>
        <td id="L1140" class="blob-num js-line-number" data-line-number="1140"></td>
        <td id="LC1140" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1141" class="blob-num js-line-number" data-line-number="1141"></td>
        <td id="LC1141" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-c1">%(count_lines_recorded)d</span> requests imported to <span class="pl-c1">%(total_sites)d</span> sites</span></td>
      </tr>
      <tr>
        <td id="L1142" class="blob-num js-line-number" data-line-number="1142"></td>
        <td id="LC1142" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(total_sites_existing)d</span> sites already existed</span></td>
      </tr>
      <tr>
        <td id="L1143" class="blob-num js-line-number" data-line-number="1143"></td>
        <td id="LC1143" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-c1">%(total_sites_created)d</span> sites were created:</span></td>
      </tr>
      <tr>
        <td id="L1144" class="blob-num js-line-number" data-line-number="1144"></td>
        <td id="LC1144" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-c1">%(sites_created)s</span></span></td>
      </tr>
      <tr>
        <td id="L1145" class="blob-num js-line-number" data-line-number="1145"></td>
        <td id="LC1145" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-c1">%(total_sites_ignored)d</span> distinct hostnames did not match any existing site:</span></td>
      </tr>
      <tr>
        <td id="L1146" class="blob-num js-line-number" data-line-number="1146"></td>
        <td id="LC1146" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-c1">%(sites_ignored)s</span></span></td>
      </tr>
      <tr>
        <td id="L1147" class="blob-num js-line-number" data-line-number="1147"></td>
        <td id="LC1147" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-c1">%(sites_ignored_tips)s</span></span></td>
      </tr>
      <tr>
        <td id="L1148" class="blob-num js-line-number" data-line-number="1148"></td>
        <td id="LC1148" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1149" class="blob-num js-line-number" data-line-number="1149"></td>
        <td id="LC1149" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Performance summary</span></td>
      </tr>
      <tr>
        <td id="L1150" class="blob-num js-line-number" data-line-number="1150"></td>
        <td id="LC1150" class="blob-code blob-code-inner js-file-line"><span class="pl-s">-------------------</span></td>
      </tr>
      <tr>
        <td id="L1151" class="blob-num js-line-number" data-line-number="1151"></td>
        <td id="LC1151" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1152" class="blob-num js-line-number" data-line-number="1152"></td>
        <td id="LC1152" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Total time: <span class="pl-c1">%(total_time)d</span> seconds</span></td>
      </tr>
      <tr>
        <td id="L1153" class="blob-num js-line-number" data-line-number="1153"></td>
        <td id="LC1153" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Requests imported per second: <span class="pl-c1">%(speed_recording)s</span> requests per second</span></td>
      </tr>
      <tr>
        <td id="L1154" class="blob-num js-line-number" data-line-number="1154"></td>
        <td id="LC1154" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1155" class="blob-num js-line-number" data-line-number="1155"></td>
        <td id="LC1155" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Processing your log data</span></td>
      </tr>
      <tr>
        <td id="L1156" class="blob-num js-line-number" data-line-number="1156"></td>
        <td id="LC1156" class="blob-code blob-code-inner js-file-line"><span class="pl-s">------------------------</span></td>
      </tr>
      <tr>
        <td id="L1157" class="blob-num js-line-number" data-line-number="1157"></td>
        <td id="LC1157" class="blob-code blob-code-inner js-file-line"><span class="pl-s"></span></td>
      </tr>
      <tr>
        <td id="L1158" class="blob-num js-line-number" data-line-number="1158"></td>
        <td id="LC1158" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    In order for your logs to be processed by Piwik, you may need to run the following command:</span></td>
      </tr>
      <tr>
        <td id="L1159" class="blob-num js-line-number" data-line-number="1159"></td>
        <td id="LC1159" class="blob-code blob-code-inner js-file-line"><span class="pl-s">     ./console core:archive --force-all-websites --force-all-periods=315576000 --force-date-last-n=1000 --url=&#39;<span class="pl-c1">%(url)s</span>&#39;</span></td>
      </tr>
      <tr>
        <td id="L1160" class="blob-num js-line-number" data-line-number="1160"></td>
        <td id="LC1160" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span> <span class="pl-k">%</span> {</td>
      </tr>
      <tr>
        <td id="L1161" class="blob-num js-line-number" data-line-number="1161"></td>
        <td id="LC1161" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1162" class="blob-num js-line-number" data-line-number="1162"></td>
        <td id="LC1162" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_recorded<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_recorded.value,</td>
      </tr>
      <tr>
        <td id="L1163" class="blob-num js-line-number" data-line-number="1163"></td>
        <td id="LC1163" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_downloads<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_downloads.value,</td>
      </tr>
      <tr>
        <td id="L1164" class="blob-num js-line-number" data-line-number="1164"></td>
        <td id="LC1164" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>total_lines_ignored<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">sum</span>([</td>
      </tr>
      <tr>
        <td id="L1165" class="blob-num js-line-number" data-line-number="1165"></td>
        <td id="LC1165" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_invalid.value,</td>
      </tr>
      <tr>
        <td id="L1166" class="blob-num js-line-number" data-line-number="1166"></td>
        <td id="LC1166" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_skipped_user_agent.value,</td>
      </tr>
      <tr>
        <td id="L1167" class="blob-num js-line-number" data-line-number="1167"></td>
        <td id="LC1167" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_skipped_http_errors.value,</td>
      </tr>
      <tr>
        <td id="L1168" class="blob-num js-line-number" data-line-number="1168"></td>
        <td id="LC1168" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_skipped_http_redirects.value,</td>
      </tr>
      <tr>
        <td id="L1169" class="blob-num js-line-number" data-line-number="1169"></td>
        <td id="LC1169" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_static.value,</td>
      </tr>
      <tr>
        <td id="L1170" class="blob-num js-line-number" data-line-number="1170"></td>
        <td id="LC1170" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_skipped_downloads.value,</td>
      </tr>
      <tr>
        <td id="L1171" class="blob-num js-line-number" data-line-number="1171"></td>
        <td id="LC1171" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_no_site.value,</td>
      </tr>
      <tr>
        <td id="L1172" class="blob-num js-line-number" data-line-number="1172"></td>
        <td id="LC1172" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_hostname_skipped.value,</td>
      </tr>
      <tr>
        <td id="L1173" class="blob-num js-line-number" data-line-number="1173"></td>
        <td id="LC1173" class="blob-code blob-code-inner js-file-line">        ]),</td>
      </tr>
      <tr>
        <td id="L1174" class="blob-num js-line-number" data-line-number="1174"></td>
        <td id="LC1174" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_invalid<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_invalid.value,</td>
      </tr>
      <tr>
        <td id="L1175" class="blob-num js-line-number" data-line-number="1175"></td>
        <td id="LC1175" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_skipped_user_agent<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_skipped_user_agent.value,</td>
      </tr>
      <tr>
        <td id="L1176" class="blob-num js-line-number" data-line-number="1176"></td>
        <td id="LC1176" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_skipped_http_errors<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_skipped_http_errors.value,</td>
      </tr>
      <tr>
        <td id="L1177" class="blob-num js-line-number" data-line-number="1177"></td>
        <td id="LC1177" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_skipped_http_redirects<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_skipped_http_redirects.value,</td>
      </tr>
      <tr>
        <td id="L1178" class="blob-num js-line-number" data-line-number="1178"></td>
        <td id="LC1178" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_static<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_static.value,</td>
      </tr>
      <tr>
        <td id="L1179" class="blob-num js-line-number" data-line-number="1179"></td>
        <td id="LC1179" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_skipped_downloads<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_skipped_downloads.value,</td>
      </tr>
      <tr>
        <td id="L1180" class="blob-num js-line-number" data-line-number="1180"></td>
        <td id="LC1180" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_no_site<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_no_site.value,</td>
      </tr>
      <tr>
        <td id="L1181" class="blob-num js-line-number" data-line-number="1181"></td>
        <td id="LC1181" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>count_lines_hostname_skipped<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.count_lines_hostname_skipped.value,</td>
      </tr>
      <tr>
        <td id="L1182" class="blob-num js-line-number" data-line-number="1182"></td>
        <td id="LC1182" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>total_sites<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.piwik_sites),</td>
      </tr>
      <tr>
        <td id="L1183" class="blob-num js-line-number" data-line-number="1183"></td>
        <td id="LC1183" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>total_sites_existing<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.piwik_sites <span class="pl-k">-</span> <span class="pl-c1">set</span>(site_id <span class="pl-k">for</span> hostname, site_id <span class="pl-k">in</span> <span class="pl-c1">self</span>.piwik_sites_created)),</td>
      </tr>
      <tr>
        <td id="L1184" class="blob-num js-line-number" data-line-number="1184"></td>
        <td id="LC1184" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>total_sites_created<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.piwik_sites_created),</td>
      </tr>
      <tr>
        <td id="L1185" class="blob-num js-line-number" data-line-number="1185"></td>
        <td id="LC1185" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>sites_created<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>._indent_text(</td>
      </tr>
      <tr>
        <td id="L1186" class="blob-num js-line-number" data-line-number="1186"></td>
        <td id="LC1186" class="blob-code blob-code-inner js-file-line">            [<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span> (ID: <span class="pl-c1">%d</span>)<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (hostname, site_id) <span class="pl-k">for</span> hostname, site_id <span class="pl-k">in</span> <span class="pl-c1">self</span>.piwik_sites_created],</td>
      </tr>
      <tr>
        <td id="L1187" class="blob-num js-line-number" data-line-number="1187"></td>
        <td id="LC1187" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">level</span><span class="pl-k">=</span><span class="pl-c1">3</span>,</td>
      </tr>
      <tr>
        <td id="L1188" class="blob-num js-line-number" data-line-number="1188"></td>
        <td id="LC1188" class="blob-code blob-code-inner js-file-line">        ),</td>
      </tr>
      <tr>
        <td id="L1189" class="blob-num js-line-number" data-line-number="1189"></td>
        <td id="LC1189" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>total_sites_ignored<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.piwik_sites_ignored),</td>
      </tr>
      <tr>
        <td id="L1190" class="blob-num js-line-number" data-line-number="1190"></td>
        <td id="LC1190" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>sites_ignored<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>._indent_text(</td>
      </tr>
      <tr>
        <td id="L1191" class="blob-num js-line-number" data-line-number="1191"></td>
        <td id="LC1191" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.piwik_sites_ignored, <span class="pl-v">level</span><span class="pl-k">=</span><span class="pl-c1">3</span>,</td>
      </tr>
      <tr>
        <td id="L1192" class="blob-num js-line-number" data-line-number="1192"></td>
        <td id="LC1192" class="blob-code blob-code-inner js-file-line">        ),</td>
      </tr>
      <tr>
        <td id="L1193" class="blob-num js-line-number" data-line-number="1193"></td>
        <td id="LC1193" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>sites_ignored_tips<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1194" class="blob-num js-line-number" data-line-number="1194"></td>
        <td id="LC1194" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        TIPs:</span></td>
      </tr>
      <tr>
        <td id="L1195" class="blob-num js-line-number" data-line-number="1195"></td>
        <td id="LC1195" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         - if one of these hosts is an alias host for one of the websites</span></td>
      </tr>
      <tr>
        <td id="L1196" class="blob-num js-line-number" data-line-number="1196"></td>
        <td id="LC1196" class="blob-code blob-code-inner js-file-line"><span class="pl-s">           in Piwik, you can add this host as an &quot;Alias URL&quot; in Settings &gt; Websites.</span></td>
      </tr>
      <tr>
        <td id="L1197" class="blob-num js-line-number" data-line-number="1197"></td>
        <td id="LC1197" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         - use --add-sites-new-hosts if you wish to automatically create</span></td>
      </tr>
      <tr>
        <td id="L1198" class="blob-num js-line-number" data-line-number="1198"></td>
        <td id="LC1198" class="blob-code blob-code-inner js-file-line"><span class="pl-s">           one website for each of these hosts in Piwik rather than discarding</span></td>
      </tr>
      <tr>
        <td id="L1199" class="blob-num js-line-number" data-line-number="1199"></td>
        <td id="LC1199" class="blob-code blob-code-inner js-file-line"><span class="pl-s">           these requests.</span></td>
      </tr>
      <tr>
        <td id="L1200" class="blob-num js-line-number" data-line-number="1200"></td>
        <td id="LC1200" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         - use --idsite-fallback to force all these log lines with a new hostname</span></td>
      </tr>
      <tr>
        <td id="L1201" class="blob-num js-line-number" data-line-number="1201"></td>
        <td id="LC1201" class="blob-code blob-code-inner js-file-line"><span class="pl-s">           to be recorded in a specific idsite (for example for troubleshooting/visualizing the data)</span></td>
      </tr>
      <tr>
        <td id="L1202" class="blob-num js-line-number" data-line-number="1202"></td>
        <td id="LC1202" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         - use --idsite to force all lines in the specified log files</span></td>
      </tr>
      <tr>
        <td id="L1203" class="blob-num js-line-number" data-line-number="1203"></td>
        <td id="LC1203" class="blob-code blob-code-inner js-file-line"><span class="pl-s">           to be all recorded in the specified idsite</span></td>
      </tr>
      <tr>
        <td id="L1204" class="blob-num js-line-number" data-line-number="1204"></td>
        <td id="LC1204" class="blob-code blob-code-inner js-file-line"><span class="pl-s">         - or you can also manually create a new Website in Piwik with the URL set to this hostname</span></td>
      </tr>
      <tr>
        <td id="L1205" class="blob-num js-line-number" data-line-number="1205"></td>
        <td id="LC1205" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span> <span class="pl-k">if</span> <span class="pl-c1">self</span>.piwik_sites_ignored <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1206" class="blob-num js-line-number" data-line-number="1206"></td>
        <td id="LC1206" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>total_time<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.time_stop <span class="pl-k">-</span> <span class="pl-c1">self</span>.time_start,</td>
      </tr>
      <tr>
        <td id="L1207" class="blob-num js-line-number" data-line-number="1207"></td>
        <td id="LC1207" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>speed_recording<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>._round_value(<span class="pl-c1">self</span>._compute_speed(</td>
      </tr>
      <tr>
        <td id="L1208" class="blob-num js-line-number" data-line-number="1208"></td>
        <td id="LC1208" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.count_lines_recorded.value,</td>
      </tr>
      <tr>
        <td id="L1209" class="blob-num js-line-number" data-line-number="1209"></td>
        <td id="LC1209" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.time_start, <span class="pl-c1">self</span>.time_stop,</td>
      </tr>
      <tr>
        <td id="L1210" class="blob-num js-line-number" data-line-number="1210"></td>
        <td id="LC1210" class="blob-code blob-code-inner js-file-line">        )),</td>
      </tr>
      <tr>
        <td id="L1211" class="blob-num js-line-number" data-line-number="1211"></td>
        <td id="LC1211" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>: config.options.piwik_api_url,</td>
      </tr>
      <tr>
        <td id="L1212" class="blob-num js-line-number" data-line-number="1212"></td>
        <td id="LC1212" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&#39;</span>invalid_lines<span class="pl-pds">&#39;</span></span>: invalid_lines_summary</td>
      </tr>
      <tr>
        <td id="L1213" class="blob-num js-line-number" data-line-number="1213"></td>
        <td id="LC1213" class="blob-code blob-code-inner js-file-line">}</td>
      </tr>
      <tr>
        <td id="L1214" class="blob-num js-line-number" data-line-number="1214"></td>
        <td id="LC1214" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1215" class="blob-num js-line-number" data-line-number="1215"></td>
        <td id="LC1215" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L1216" class="blob-num js-line-number" data-line-number="1216"></td>
        <td id="LC1216" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span># The monitor is a thread that prints a short summary each second.</span></td>
      </tr>
      <tr>
        <td id="L1217" class="blob-num js-line-number" data-line-number="1217"></td>
        <td id="LC1217" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L1218" class="blob-num js-line-number" data-line-number="1218"></td>
        <td id="LC1218" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1219" class="blob-num js-line-number" data-line-number="1219"></td>
        <td id="LC1219" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_monitor</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1220" class="blob-num js-line-number" data-line-number="1220"></td>
        <td id="LC1220" class="blob-code blob-code-inner js-file-line">        latest_total_recorded <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L1221" class="blob-num js-line-number" data-line-number="1221"></td>
        <td id="LC1221" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-k">not</span> <span class="pl-c1">self</span>.monitor_stop:</td>
      </tr>
      <tr>
        <td id="L1222" class="blob-num js-line-number" data-line-number="1222"></td>
        <td id="LC1222" class="blob-code blob-code-inner js-file-line">            current_total <span class="pl-k">=</span> stats.count_lines_recorded.value</td>
      </tr>
      <tr>
        <td id="L1223" class="blob-num js-line-number" data-line-number="1223"></td>
        <td id="LC1223" class="blob-code blob-code-inner js-file-line">            time_elapsed <span class="pl-k">=</span> time.time() <span class="pl-k">-</span> <span class="pl-c1">self</span>.time_start</td>
      </tr>
      <tr>
        <td id="L1224" class="blob-num js-line-number" data-line-number="1224"></td>
        <td id="LC1224" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%d</span> lines parsed, <span class="pl-c1">%d</span> lines recorded, <span class="pl-c1">%d</span> records/sec (avg), <span class="pl-c1">%d</span> records/sec (current)<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (</td>
      </tr>
      <tr>
        <td id="L1225" class="blob-num js-line-number" data-line-number="1225"></td>
        <td id="LC1225" class="blob-code blob-code-inner js-file-line">                stats.count_lines_parsed.value,</td>
      </tr>
      <tr>
        <td id="L1226" class="blob-num js-line-number" data-line-number="1226"></td>
        <td id="LC1226" class="blob-code blob-code-inner js-file-line">                current_total,</td>
      </tr>
      <tr>
        <td id="L1227" class="blob-num js-line-number" data-line-number="1227"></td>
        <td id="LC1227" class="blob-code blob-code-inner js-file-line">                current_total <span class="pl-k">/</span> time_elapsed <span class="pl-k">if</span> time_elapsed <span class="pl-k">!=</span> <span class="pl-c1">0</span> <span class="pl-k">else</span> <span class="pl-c1">0</span>,</td>
      </tr>
      <tr>
        <td id="L1228" class="blob-num js-line-number" data-line-number="1228"></td>
        <td id="LC1228" class="blob-code blob-code-inner js-file-line">                (current_total <span class="pl-k">-</span> latest_total_recorded) <span class="pl-k">/</span> config.options.show_progress_delay,</td>
      </tr>
      <tr>
        <td id="L1229" class="blob-num js-line-number" data-line-number="1229"></td>
        <td id="LC1229" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L1230" class="blob-num js-line-number" data-line-number="1230"></td>
        <td id="LC1230" class="blob-code blob-code-inner js-file-line">            latest_total_recorded <span class="pl-k">=</span> current_total</td>
      </tr>
      <tr>
        <td id="L1231" class="blob-num js-line-number" data-line-number="1231"></td>
        <td id="LC1231" class="blob-code blob-code-inner js-file-line">            time.sleep(config.options.show_progress_delay)</td>
      </tr>
      <tr>
        <td id="L1232" class="blob-num js-line-number" data-line-number="1232"></td>
        <td id="LC1232" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1233" class="blob-num js-line-number" data-line-number="1233"></td>
        <td id="LC1233" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">start_monitor</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1234" class="blob-num js-line-number" data-line-number="1234"></td>
        <td id="LC1234" class="blob-code blob-code-inner js-file-line">        t <span class="pl-k">=</span> threading.Thread(<span class="pl-v">target</span><span class="pl-k">=</span><span class="pl-c1">self</span>._monitor)</td>
      </tr>
      <tr>
        <td id="L1235" class="blob-num js-line-number" data-line-number="1235"></td>
        <td id="LC1235" class="blob-code blob-code-inner js-file-line">        t.daemon <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1236" class="blob-num js-line-number" data-line-number="1236"></td>
        <td id="LC1236" class="blob-code blob-code-inner js-file-line">        t.start()</td>
      </tr>
      <tr>
        <td id="L1237" class="blob-num js-line-number" data-line-number="1237"></td>
        <td id="LC1237" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1238" class="blob-num js-line-number" data-line-number="1238"></td>
        <td id="LC1238" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">stop_monitor</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1239" class="blob-num js-line-number" data-line-number="1239"></td>
        <td id="LC1239" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.monitor_stop <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1240" class="blob-num js-line-number" data-line-number="1240"></td>
        <td id="LC1240" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1241" class="blob-num js-line-number" data-line-number="1241"></td>
        <td id="LC1241" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Piwik</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L1242" class="blob-num js-line-number" data-line-number="1242"></td>
        <td id="LC1242" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1243" class="blob-num js-line-number" data-line-number="1243"></td>
        <td id="LC1243" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Make requests to Piwik.</span></td>
      </tr>
      <tr>
        <td id="L1244" class="blob-num js-line-number" data-line-number="1244"></td>
        <td id="LC1244" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1245" class="blob-num js-line-number" data-line-number="1245"></td>
        <td id="LC1245" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1246" class="blob-num js-line-number" data-line-number="1246"></td>
        <td id="LC1246" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">class</span> <span class="pl-en">Error</span>(<span class="pl-c1">Exception</span>):</td>
      </tr>
      <tr>
        <td id="L1247" class="blob-num js-line-number" data-line-number="1247"></td>
        <td id="LC1247" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1248" class="blob-num js-line-number" data-line-number="1248"></td>
        <td id="LC1248" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">message</span>, <span class="pl-smi">code</span> <span class="pl-k">=</span> <span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L1249" class="blob-num js-line-number" data-line-number="1249"></td>
        <td id="LC1249" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">super</span>(<span class="pl-c1">Exception</span>, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>(message)</td>
      </tr>
      <tr>
        <td id="L1250" class="blob-num js-line-number" data-line-number="1250"></td>
        <td id="LC1250" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1251" class="blob-num js-line-number" data-line-number="1251"></td>
        <td id="LC1251" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.code <span class="pl-k">=</span> code</td>
      </tr>
      <tr>
        <td id="L1252" class="blob-num js-line-number" data-line-number="1252"></td>
        <td id="LC1252" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1253" class="blob-num js-line-number" data-line-number="1253"></td>
        <td id="LC1253" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">class</span> <span class="pl-en">RedirectHandlerWithLogging</span>(<span class="pl-e">urllib2</span>.<span class="pl-e">HTTPRedirectHandler</span>):</td>
      </tr>
      <tr>
        <td id="L1254" class="blob-num js-line-number" data-line-number="1254"></td>
        <td id="LC1254" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1255" class="blob-num js-line-number" data-line-number="1255"></td>
        <td id="LC1255" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Special implementation of HTTPRedirectHandler that logs redirects in debug mode</span></td>
      </tr>
      <tr>
        <td id="L1256" class="blob-num js-line-number" data-line-number="1256"></td>
        <td id="LC1256" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        to help users debug system issues.</span></td>
      </tr>
      <tr>
        <td id="L1257" class="blob-num js-line-number" data-line-number="1257"></td>
        <td id="LC1257" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1258" class="blob-num js-line-number" data-line-number="1258"></td>
        <td id="LC1258" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1259" class="blob-num js-line-number" data-line-number="1259"></td>
        <td id="LC1259" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">redirect_request</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">req</span>, <span class="pl-smi">fp</span>, <span class="pl-smi">code</span>, <span class="pl-smi">msg</span>, <span class="pl-smi">hdrs</span>, <span class="pl-smi">newurl</span>):</td>
      </tr>
      <tr>
        <td id="L1260" class="blob-num js-line-number" data-line-number="1260"></td>
        <td id="LC1260" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&quot;</span>Request redirected (code: <span class="pl-c1">%s</span>) to &#39;<span class="pl-c1">%s</span>&#39;<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (code, newurl))</td>
      </tr>
      <tr>
        <td id="L1261" class="blob-num js-line-number" data-line-number="1261"></td>
        <td id="LC1261" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1262" class="blob-num js-line-number" data-line-number="1262"></td>
        <td id="LC1262" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> urllib2.HTTPRedirectHandler.redirect_request(<span class="pl-c1">self</span>, req, fp, code, msg, hdrs, newurl)</td>
      </tr>
      <tr>
        <td id="L1263" class="blob-num js-line-number" data-line-number="1263"></td>
        <td id="LC1263" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1264" class="blob-num js-line-number" data-line-number="1264"></td>
        <td id="LC1264" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">staticmethod</span></td>
      </tr>
      <tr>
        <td id="L1265" class="blob-num js-line-number" data-line-number="1265"></td>
        <td id="LC1265" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_call</span>(<span class="pl-smi">path</span>, <span class="pl-smi">args</span>, <span class="pl-smi">headers</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">url</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">data</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L1266" class="blob-num js-line-number" data-line-number="1266"></td>
        <td id="LC1266" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1267" class="blob-num js-line-number" data-line-number="1267"></td>
        <td id="LC1267" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Make a request to the Piwik site. It is up to the caller to format</span></td>
      </tr>
      <tr>
        <td id="L1268" class="blob-num js-line-number" data-line-number="1268"></td>
        <td id="LC1268" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        arguments, to embed authentication, etc.</span></td>
      </tr>
      <tr>
        <td id="L1269" class="blob-num js-line-number" data-line-number="1269"></td>
        <td id="LC1269" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1270" class="blob-num js-line-number" data-line-number="1270"></td>
        <td id="LC1270" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> url <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1271" class="blob-num js-line-number" data-line-number="1271"></td>
        <td id="LC1271" class="blob-code blob-code-inner js-file-line">            url <span class="pl-k">=</span> config.options.piwik_url</td>
      </tr>
      <tr>
        <td id="L1272" class="blob-num js-line-number" data-line-number="1272"></td>
        <td id="LC1272" class="blob-code blob-code-inner js-file-line">        headers <span class="pl-k">=</span> headers <span class="pl-k">or</span> {}</td>
      </tr>
      <tr>
        <td id="L1273" class="blob-num js-line-number" data-line-number="1273"></td>
        <td id="LC1273" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1274" class="blob-num js-line-number" data-line-number="1274"></td>
        <td id="LC1274" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> data <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1275" class="blob-num js-line-number" data-line-number="1275"></td>
        <td id="LC1275" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> If Content-Type isn&#39;t defined, PHP do not parse the request&#39;s body.</span></td>
      </tr>
      <tr>
        <td id="L1276" class="blob-num js-line-number" data-line-number="1276"></td>
        <td id="LC1276" class="blob-code blob-code-inner js-file-line">            headers[<span class="pl-s"><span class="pl-pds">&#39;</span>Content-type<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>application/x-www-form-urlencoded<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1277" class="blob-num js-line-number" data-line-number="1277"></td>
        <td id="LC1277" class="blob-code blob-code-inner js-file-line">            data <span class="pl-k">=</span> urllib.urlencode(args)</td>
      </tr>
      <tr>
        <td id="L1278" class="blob-num js-line-number" data-line-number="1278"></td>
        <td id="LC1278" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(data, <span class="pl-v">basestring</span>) <span class="pl-k">and</span> headers[<span class="pl-s"><span class="pl-pds">&#39;</span>Content-type<span class="pl-pds">&#39;</span></span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>application/json<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1279" class="blob-num js-line-number" data-line-number="1279"></td>
        <td id="LC1279" class="blob-code blob-code-inner js-file-line">            data <span class="pl-k">=</span> json.dumps(data)</td>
      </tr>
      <tr>
        <td id="L1280" class="blob-num js-line-number" data-line-number="1280"></td>
        <td id="LC1280" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1281" class="blob-num js-line-number" data-line-number="1281"></td>
        <td id="LC1281" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> args:</td>
      </tr>
      <tr>
        <td id="L1282" class="blob-num js-line-number" data-line-number="1282"></td>
        <td id="LC1282" class="blob-code blob-code-inner js-file-line">                path <span class="pl-k">=</span> path <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>?<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> urllib.urlencode(args)</td>
      </tr>
      <tr>
        <td id="L1283" class="blob-num js-line-number" data-line-number="1283"></td>
        <td id="LC1283" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1284" class="blob-num js-line-number" data-line-number="1284"></td>
        <td id="LC1284" class="blob-code blob-code-inner js-file-line">        headers[<span class="pl-s"><span class="pl-pds">&#39;</span>User-Agent<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Piwik/LogImport<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1285" class="blob-num js-line-number" data-line-number="1285"></td>
        <td id="LC1285" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1286" class="blob-num js-line-number" data-line-number="1286"></td>
        <td id="LC1286" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1287" class="blob-num js-line-number" data-line-number="1287"></td>
        <td id="LC1287" class="blob-code blob-code-inner js-file-line">            timeout <span class="pl-k">=</span> config.options.request_timeout</td>
      </tr>
      <tr>
        <td id="L1288" class="blob-num js-line-number" data-line-number="1288"></td>
        <td id="LC1288" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L1289" class="blob-num js-line-number" data-line-number="1289"></td>
        <td id="LC1289" class="blob-code blob-code-inner js-file-line">            timeout <span class="pl-k">=</span> <span class="pl-c1">None</span> <span class="pl-c"><span class="pl-c">#</span> the config global object may not be created at this point</span></td>
      </tr>
      <tr>
        <td id="L1290" class="blob-num js-line-number" data-line-number="1290"></td>
        <td id="LC1290" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1291" class="blob-num js-line-number" data-line-number="1291"></td>
        <td id="LC1291" class="blob-code blob-code-inner js-file-line">        request <span class="pl-k">=</span> urllib2.Request(url <span class="pl-k">+</span> path, data, headers)</td>
      </tr>
      <tr>
        <td id="L1292" class="blob-num js-line-number" data-line-number="1292"></td>
        <td id="LC1292" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1293" class="blob-num js-line-number" data-line-number="1293"></td>
        <td id="LC1293" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Handle basic auth if auth_user set</span></td>
      </tr>
      <tr>
        <td id="L1294" class="blob-num js-line-number" data-line-number="1294"></td>
        <td id="LC1294" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1295" class="blob-num js-line-number" data-line-number="1295"></td>
        <td id="LC1295" class="blob-code blob-code-inner js-file-line">            auth_user <span class="pl-k">=</span> config.options.auth_user</td>
      </tr>
      <tr>
        <td id="L1296" class="blob-num js-line-number" data-line-number="1296"></td>
        <td id="LC1296" class="blob-code blob-code-inner js-file-line">            auth_password <span class="pl-k">=</span> config.options.auth_password</td>
      </tr>
      <tr>
        <td id="L1297" class="blob-num js-line-number" data-line-number="1297"></td>
        <td id="LC1297" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L1298" class="blob-num js-line-number" data-line-number="1298"></td>
        <td id="LC1298" class="blob-code blob-code-inner js-file-line">            auth_user <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L1299" class="blob-num js-line-number" data-line-number="1299"></td>
        <td id="LC1299" class="blob-code blob-code-inner js-file-line">            auth_password <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L1300" class="blob-num js-line-number" data-line-number="1300"></td>
        <td id="LC1300" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1301" class="blob-num js-line-number" data-line-number="1301"></td>
        <td id="LC1301" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> auth_user <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1302" class="blob-num js-line-number" data-line-number="1302"></td>
        <td id="LC1302" class="blob-code blob-code-inner js-file-line">            base64string <span class="pl-k">=</span> base64.encodestring(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>:<span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (auth_user, auth_password)).replace(<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1303" class="blob-num js-line-number" data-line-number="1303"></td>
        <td id="LC1303" class="blob-code blob-code-inner js-file-line">            request.add_header(<span class="pl-s"><span class="pl-pds">&quot;</span>Authorization<span class="pl-pds">&quot;</span></span>, <span class="pl-s"><span class="pl-pds">&quot;</span>Basic <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> base64string)        </td>
      </tr>
      <tr>
        <td id="L1304" class="blob-num js-line-number" data-line-number="1304"></td>
        <td id="LC1304" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1305" class="blob-num js-line-number" data-line-number="1305"></td>
        <td id="LC1305" class="blob-code blob-code-inner js-file-line">        opener <span class="pl-k">=</span> urllib2.build_opener(Piwik.RedirectHandlerWithLogging())</td>
      </tr>
      <tr>
        <td id="L1306" class="blob-num js-line-number" data-line-number="1306"></td>
        <td id="LC1306" class="blob-code blob-code-inner js-file-line">        response <span class="pl-k">=</span> opener.open(request, <span class="pl-v">timeout</span> <span class="pl-k">=</span> timeout)</td>
      </tr>
      <tr>
        <td id="L1307" class="blob-num js-line-number" data-line-number="1307"></td>
        <td id="LC1307" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">=</span> response.read()</td>
      </tr>
      <tr>
        <td id="L1308" class="blob-num js-line-number" data-line-number="1308"></td>
        <td id="LC1308" class="blob-code blob-code-inner js-file-line">        response.close()</td>
      </tr>
      <tr>
        <td id="L1309" class="blob-num js-line-number" data-line-number="1309"></td>
        <td id="LC1309" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L1310" class="blob-num js-line-number" data-line-number="1310"></td>
        <td id="LC1310" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1311" class="blob-num js-line-number" data-line-number="1311"></td>
        <td id="LC1311" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">staticmethod</span></td>
      </tr>
      <tr>
        <td id="L1312" class="blob-num js-line-number" data-line-number="1312"></td>
        <td id="LC1312" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_call_api</span>(<span class="pl-smi">method</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L1313" class="blob-num js-line-number" data-line-number="1313"></td>
        <td id="LC1313" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1314" class="blob-num js-line-number" data-line-number="1314"></td>
        <td id="LC1314" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Make a request to the Piwik API taking care of authentication, body</span></td>
      </tr>
      <tr>
        <td id="L1315" class="blob-num js-line-number" data-line-number="1315"></td>
        <td id="LC1315" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        formatting, etc.</span></td>
      </tr>
      <tr>
        <td id="L1316" class="blob-num js-line-number" data-line-number="1316"></td>
        <td id="LC1316" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1317" class="blob-num js-line-number" data-line-number="1317"></td>
        <td id="LC1317" class="blob-code blob-code-inner js-file-line">        args <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L1318" class="blob-num js-line-number" data-line-number="1318"></td>
        <td id="LC1318" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>module<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span>API<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1319" class="blob-num js-line-number" data-line-number="1319"></td>
        <td id="LC1319" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>format<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span>json2<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1320" class="blob-num js-line-number" data-line-number="1320"></td>
        <td id="LC1320" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>method<span class="pl-pds">&#39;</span></span> : method,</td>
      </tr>
      <tr>
        <td id="L1321" class="blob-num js-line-number" data-line-number="1321"></td>
        <td id="LC1321" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>filter_limit<span class="pl-pds">&#39;</span></span> : <span class="pl-s"><span class="pl-pds">&#39;</span>-1<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1322" class="blob-num js-line-number" data-line-number="1322"></td>
        <td id="LC1322" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L1323" class="blob-num js-line-number" data-line-number="1323"></td>
        <td id="LC1323" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> token_auth, by default, is taken from config.</span></td>
      </tr>
      <tr>
        <td id="L1324" class="blob-num js-line-number" data-line-number="1324"></td>
        <td id="LC1324" class="blob-code blob-code-inner js-file-line">        token_auth <span class="pl-k">=</span> kwargs.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>_token_auth<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L1325" class="blob-num js-line-number" data-line-number="1325"></td>
        <td id="LC1325" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> token_auth <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1326" class="blob-num js-line-number" data-line-number="1326"></td>
        <td id="LC1326" class="blob-code blob-code-inner js-file-line">            token_auth <span class="pl-k">=</span> config.options.piwik_token_auth</td>
      </tr>
      <tr>
        <td id="L1327" class="blob-num js-line-number" data-line-number="1327"></td>
        <td id="LC1327" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> token_auth:</td>
      </tr>
      <tr>
        <td id="L1328" class="blob-num js-line-number" data-line-number="1328"></td>
        <td id="LC1328" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>token_auth<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> token_auth</td>
      </tr>
      <tr>
        <td id="L1329" class="blob-num js-line-number" data-line-number="1329"></td>
        <td id="LC1329" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1330" class="blob-num js-line-number" data-line-number="1330"></td>
        <td id="LC1330" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> kwargs.pop(<span class="pl-s"><span class="pl-pds">&#39;</span>_url<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L1331" class="blob-num js-line-number" data-line-number="1331"></td>
        <td id="LC1331" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> url <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1332" class="blob-num js-line-number" data-line-number="1332"></td>
        <td id="LC1332" class="blob-code blob-code-inner js-file-line">            url <span class="pl-k">=</span> config.options.piwik_api_url</td>
      </tr>
      <tr>
        <td id="L1333" class="blob-num js-line-number" data-line-number="1333"></td>
        <td id="LC1333" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1334" class="blob-num js-line-number" data-line-number="1334"></td>
        <td id="LC1334" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1335" class="blob-num js-line-number" data-line-number="1335"></td>
        <td id="LC1335" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> kwargs:</td>
      </tr>
      <tr>
        <td id="L1336" class="blob-num js-line-number" data-line-number="1336"></td>
        <td id="LC1336" class="blob-code blob-code-inner js-file-line">            args.update(kwargs)</td>
      </tr>
      <tr>
        <td id="L1337" class="blob-num js-line-number" data-line-number="1337"></td>
        <td id="LC1337" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1338" class="blob-num js-line-number" data-line-number="1338"></td>
        <td id="LC1338" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Convert lists into appropriate format.</span></td>
      </tr>
      <tr>
        <td id="L1339" class="blob-num js-line-number" data-line-number="1339"></td>
        <td id="LC1339" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> See: http://developer.piwik.org/api-reference/reporting-api#passing-an-array-of-data-as-a-parameter</span></td>
      </tr>
      <tr>
        <td id="L1340" class="blob-num js-line-number" data-line-number="1340"></td>
        <td id="LC1340" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Warning: we have to pass the parameters in order: foo[0], foo[1], foo[2]</span></td>
      </tr>
      <tr>
        <td id="L1341" class="blob-num js-line-number" data-line-number="1341"></td>
        <td id="LC1341" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> and not foo[1], foo[0], foo[2] (it will break Piwik otherwise.)</span></td>
      </tr>
      <tr>
        <td id="L1342" class="blob-num js-line-number" data-line-number="1342"></td>
        <td id="LC1342" class="blob-code blob-code-inner js-file-line">        final_args <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1343" class="blob-num js-line-number" data-line-number="1343"></td>
        <td id="LC1343" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> key, value <span class="pl-k">in</span> args.iteritems():</td>
      </tr>
      <tr>
        <td id="L1344" class="blob-num js-line-number" data-line-number="1344"></td>
        <td id="LC1344" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(value, (<span class="pl-c1">list</span>, <span class="pl-c1">tuple</span>)):</td>
      </tr>
      <tr>
        <td id="L1345" class="blob-num js-line-number" data-line-number="1345"></td>
        <td id="LC1345" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">for</span> index, obj <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(value):</td>
      </tr>
      <tr>
        <td id="L1346" class="blob-num js-line-number" data-line-number="1346"></td>
        <td id="LC1346" class="blob-code blob-code-inner js-file-line">                    final_args.append((<span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span>[<span class="pl-c1">%d</span>]<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (key, index), obj))</td>
      </tr>
      <tr>
        <td id="L1347" class="blob-num js-line-number" data-line-number="1347"></td>
        <td id="LC1347" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1348" class="blob-num js-line-number" data-line-number="1348"></td>
        <td id="LC1348" class="blob-code blob-code-inner js-file-line">                final_args.append((key, value))</td>
      </tr>
      <tr>
        <td id="L1349" class="blob-num js-line-number" data-line-number="1349"></td>
        <td id="LC1349" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1350" class="blob-num js-line-number" data-line-number="1350"></td>
        <td id="LC1350" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1351" class="blob-num js-line-number" data-line-number="1351"></td>
        <td id="LC1351" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>        logging.debug(&#39;%s&#39; % final_args)</span></td>
      </tr>
      <tr>
        <td id="L1352" class="blob-num js-line-number" data-line-number="1352"></td>
        <td id="LC1352" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>        logging.debug(&#39;%s&#39; % url)</span></td>
      </tr>
      <tr>
        <td id="L1353" class="blob-num js-line-number" data-line-number="1353"></td>
        <td id="LC1353" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1354" class="blob-num js-line-number" data-line-number="1354"></td>
        <td id="LC1354" class="blob-code blob-code-inner js-file-line">        res <span class="pl-k">=</span> Piwik._call(<span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>, final_args, <span class="pl-v">url</span><span class="pl-k">=</span>url)</td>
      </tr>
      <tr>
        <td id="L1355" class="blob-num js-line-number" data-line-number="1355"></td>
        <td id="LC1355" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1356" class="blob-num js-line-number" data-line-number="1356"></td>
        <td id="LC1356" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1357" class="blob-num js-line-number" data-line-number="1357"></td>
        <td id="LC1357" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1358" class="blob-num js-line-number" data-line-number="1358"></td>
        <td id="LC1358" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> json.loads(res)</td>
      </tr>
      <tr>
        <td id="L1359" class="blob-num js-line-number" data-line-number="1359"></td>
        <td id="LC1359" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L1360" class="blob-num js-line-number" data-line-number="1360"></td>
        <td id="LC1360" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">raise</span> urllib2.URLError(<span class="pl-s"><span class="pl-pds">&#39;</span>Piwik returned an invalid response: <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> res)</td>
      </tr>
      <tr>
        <td id="L1361" class="blob-num js-line-number" data-line-number="1361"></td>
        <td id="LC1361" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1362" class="blob-num js-line-number" data-line-number="1362"></td>
        <td id="LC1362" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">staticmethod</span></td>
      </tr>
      <tr>
        <td id="L1363" class="blob-num js-line-number" data-line-number="1363"></td>
        <td id="LC1363" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_call_wrapper</span>(<span class="pl-smi">func</span>, <span class="pl-smi">expected_response</span>, <span class="pl-smi">on_failure</span>, <span class="pl-k">*</span><span class="pl-smi">args</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L1364" class="blob-num js-line-number" data-line-number="1364"></td>
        <td id="LC1364" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1365" class="blob-num js-line-number" data-line-number="1365"></td>
        <td id="LC1365" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Try to make requests to Piwik at most PIWIK_FAILURE_MAX_RETRY times.</span></td>
      </tr>
      <tr>
        <td id="L1366" class="blob-num js-line-number" data-line-number="1366"></td>
        <td id="LC1366" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1367" class="blob-num js-line-number" data-line-number="1367"></td>
        <td id="LC1367" class="blob-code blob-code-inner js-file-line">        errors <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L1368" class="blob-num js-line-number" data-line-number="1368"></td>
        <td id="LC1368" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1369" class="blob-num js-line-number" data-line-number="1369"></td>
        <td id="LC1369" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1370" class="blob-num js-line-number" data-line-number="1370"></td>
        <td id="LC1370" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> func(<span class="pl-k">*</span>args, <span class="pl-k">**</span>kwargs)</td>
      </tr>
      <tr>
        <td id="L1371" class="blob-num js-line-number" data-line-number="1371"></td>
        <td id="LC1371" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> expected_response <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> <span class="pl-k">and</span> response <span class="pl-k">!=</span> expected_response:</td>
      </tr>
      <tr>
        <td id="L1372" class="blob-num js-line-number" data-line-number="1372"></td>
        <td id="LC1372" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> on_failure <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1373" class="blob-num js-line-number" data-line-number="1373"></td>
        <td id="LC1373" class="blob-code blob-code-inner js-file-line">                        error_message <span class="pl-k">=</span> on_failure(response, kwargs.get(<span class="pl-s"><span class="pl-pds">&#39;</span>data<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L1374" class="blob-num js-line-number" data-line-number="1374"></td>
        <td id="LC1374" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1375" class="blob-num js-line-number" data-line-number="1375"></td>
        <td id="LC1375" class="blob-code blob-code-inner js-file-line">                        error_message <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>didn&#39;t receive the expected response. Response was <span class="pl-c1">%s</span> <span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> response</td>
      </tr>
      <tr>
        <td id="L1376" class="blob-num js-line-number" data-line-number="1376"></td>
        <td id="LC1376" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1377" class="blob-num js-line-number" data-line-number="1377"></td>
        <td id="LC1377" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">raise</span> urllib2.URLError(error_message)</td>
      </tr>
      <tr>
        <td id="L1378" class="blob-num js-line-number" data-line-number="1378"></td>
        <td id="LC1378" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> response</td>
      </tr>
      <tr>
        <td id="L1379" class="blob-num js-line-number" data-line-number="1379"></td>
        <td id="LC1379" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> (urllib2.URLError, httplib.HTTPException, <span class="pl-c1">ValueError</span>, socket.timeout), e:</td>
      </tr>
      <tr>
        <td id="L1380" class="blob-num js-line-number" data-line-number="1380"></td>
        <td id="LC1380" class="blob-code blob-code-inner js-file-line">                logging.info(<span class="pl-s"><span class="pl-pds">&#39;</span>Error when connecting to Piwik: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, e)</td>
      </tr>
      <tr>
        <td id="L1381" class="blob-num js-line-number" data-line-number="1381"></td>
        <td id="LC1381" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1382" class="blob-num js-line-number" data-line-number="1382"></td>
        <td id="LC1382" class="blob-code blob-code-inner js-file-line">                code <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L1383" class="blob-num js-line-number" data-line-number="1383"></td>
        <td id="LC1383" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(e, urllib2.HTTPError):</td>
      </tr>
      <tr>
        <td id="L1384" class="blob-num js-line-number" data-line-number="1384"></td>
        <td id="LC1384" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> See Python issue 13211.</span></td>
      </tr>
      <tr>
        <td id="L1385" class="blob-num js-line-number" data-line-number="1385"></td>
        <td id="LC1385" class="blob-code blob-code-inner js-file-line">                    message <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>HTTP Error <span class="pl-c1">%s</span> <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (e.code, e.msg)</td>
      </tr>
      <tr>
        <td id="L1386" class="blob-num js-line-number" data-line-number="1386"></td>
        <td id="LC1386" class="blob-code blob-code-inner js-file-line">                    code <span class="pl-k">=</span> e.code</td>
      </tr>
      <tr>
        <td id="L1387" class="blob-num js-line-number" data-line-number="1387"></td>
        <td id="LC1387" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> <span class="pl-c1">isinstance</span>(e, urllib2.URLError):</td>
      </tr>
      <tr>
        <td id="L1388" class="blob-num js-line-number" data-line-number="1388"></td>
        <td id="LC1388" class="blob-code blob-code-inner js-file-line">                    message <span class="pl-k">=</span> e.reason</td>
      </tr>
      <tr>
        <td id="L1389" class="blob-num js-line-number" data-line-number="1389"></td>
        <td id="LC1389" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1390" class="blob-num js-line-number" data-line-number="1390"></td>
        <td id="LC1390" class="blob-code blob-code-inner js-file-line">                    message <span class="pl-k">=</span> <span class="pl-c1">str</span>(e)</td>
      </tr>
      <tr>
        <td id="L1391" class="blob-num js-line-number" data-line-number="1391"></td>
        <td id="LC1391" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1392" class="blob-num js-line-number" data-line-number="1392"></td>
        <td id="LC1392" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> decorate message w/ HTTP response, if it can be retrieved</span></td>
      </tr>
      <tr>
        <td id="L1393" class="blob-num js-line-number" data-line-number="1393"></td>
        <td id="LC1393" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">hasattr</span>(e, <span class="pl-s"><span class="pl-pds">&#39;</span>read<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L1394" class="blob-num js-line-number" data-line-number="1394"></td>
        <td id="LC1394" class="blob-code blob-code-inner js-file-line">                    message <span class="pl-k">=</span> message <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&quot;</span>, response: <span class="pl-pds">&quot;</span></span> <span class="pl-k">+</span> e.read()</td>
      </tr>
      <tr>
        <td id="L1395" class="blob-num js-line-number" data-line-number="1395"></td>
        <td id="LC1395" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1396" class="blob-num js-line-number" data-line-number="1396"></td>
        <td id="LC1396" class="blob-code blob-code-inner js-file-line">                errors <span class="pl-k">+=</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L1397" class="blob-num js-line-number" data-line-number="1397"></td>
        <td id="LC1397" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> errors <span class="pl-k">==</span> config.options.max_attempts:</td>
      </tr>
      <tr>
        <td id="L1398" class="blob-num js-line-number" data-line-number="1398"></td>
        <td id="LC1398" class="blob-code blob-code-inner js-file-line">                    logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>Max number of attempts reached, server is unreachable!<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1399" class="blob-num js-line-number" data-line-number="1399"></td>
        <td id="LC1399" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1400" class="blob-num js-line-number" data-line-number="1400"></td>
        <td id="LC1400" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">raise</span> Piwik.Error(message, code)</td>
      </tr>
      <tr>
        <td id="L1401" class="blob-num js-line-number" data-line-number="1401"></td>
        <td id="LC1401" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1402" class="blob-num js-line-number" data-line-number="1402"></td>
        <td id="LC1402" class="blob-code blob-code-inner js-file-line">                    logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>Retrying request, attempt number <span class="pl-c1">%d</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (errors <span class="pl-k">+</span> <span class="pl-c1">1</span>))</td>
      </tr>
      <tr>
        <td id="L1403" class="blob-num js-line-number" data-line-number="1403"></td>
        <td id="LC1403" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1404" class="blob-num js-line-number" data-line-number="1404"></td>
        <td id="LC1404" class="blob-code blob-code-inner js-file-line">                    time.sleep(config.options.delay_after_failure)</td>
      </tr>
      <tr>
        <td id="L1405" class="blob-num js-line-number" data-line-number="1405"></td>
        <td id="LC1405" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1406" class="blob-num js-line-number" data-line-number="1406"></td>
        <td id="LC1406" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">classmethod</span></td>
      </tr>
      <tr>
        <td id="L1407" class="blob-num js-line-number" data-line-number="1407"></td>
        <td id="LC1407" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">call</span>(<span class="pl-smi"><span class="pl-smi">cls</span></span>, <span class="pl-smi">path</span>, <span class="pl-smi">args</span>, <span class="pl-smi">expected_content</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">headers</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">data</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">on_failure</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L1408" class="blob-num js-line-number" data-line-number="1408"></td>
        <td id="LC1408" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">cls</span>._call_wrapper(<span class="pl-c1">cls</span>._call, expected_content, on_failure, path, args, headers,</td>
      </tr>
      <tr>
        <td id="L1409" class="blob-num js-line-number" data-line-number="1409"></td>
        <td id="LC1409" class="blob-code blob-code-inner js-file-line">                                    <span class="pl-v">data</span><span class="pl-k">=</span>data)</td>
      </tr>
      <tr>
        <td id="L1410" class="blob-num js-line-number" data-line-number="1410"></td>
        <td id="LC1410" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1411" class="blob-num js-line-number" data-line-number="1411"></td>
        <td id="LC1411" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">classmethod</span></td>
      </tr>
      <tr>
        <td id="L1412" class="blob-num js-line-number" data-line-number="1412"></td>
        <td id="LC1412" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">call_api</span>(<span class="pl-smi"><span class="pl-smi">cls</span></span>, <span class="pl-smi">method</span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L1413" class="blob-num js-line-number" data-line-number="1413"></td>
        <td id="LC1413" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">cls</span>._call_wrapper(<span class="pl-c1">cls</span>._call_api, <span class="pl-c1">None</span>, <span class="pl-c1">None</span>, method, <span class="pl-k">**</span>kwargs)</td>
      </tr>
      <tr>
        <td id="L1414" class="blob-num js-line-number" data-line-number="1414"></td>
        <td id="LC1414" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1415" class="blob-num js-line-number" data-line-number="1415"></td>
        <td id="LC1415" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L1416" class="blob-num js-line-number" data-line-number="1416"></td>
        <td id="LC1416" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span># Resolvers.</span></td>
      </tr>
      <tr>
        <td id="L1417" class="blob-num js-line-number" data-line-number="1417"></td>
        <td id="LC1417" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L1418" class="blob-num js-line-number" data-line-number="1418"></td>
        <td id="LC1418" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span># A resolver is a class that turns a hostname into a Piwik site ID.</span></td>
      </tr>
      <tr>
        <td id="L1419" class="blob-num js-line-number" data-line-number="1419"></td>
        <td id="LC1419" class="blob-code blob-code-inner js-file-line"><span class="pl-c"><span class="pl-c">#</span>#</span></td>
      </tr>
      <tr>
        <td id="L1420" class="blob-num js-line-number" data-line-number="1420"></td>
        <td id="LC1420" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1421" class="blob-num js-line-number" data-line-number="1421"></td>
        <td id="LC1421" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">StaticResolver</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L1422" class="blob-num js-line-number" data-line-number="1422"></td>
        <td id="LC1422" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1423" class="blob-num js-line-number" data-line-number="1423"></td>
        <td id="LC1423" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Always return the same site ID, specified in the configuration.</span></td>
      </tr>
      <tr>
        <td id="L1424" class="blob-num js-line-number" data-line-number="1424"></td>
        <td id="LC1424" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1425" class="blob-num js-line-number" data-line-number="1425"></td>
        <td id="LC1425" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1426" class="blob-num js-line-number" data-line-number="1426"></td>
        <td id="LC1426" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">site_id</span>):</td>
      </tr>
      <tr>
        <td id="L1427" class="blob-num js-line-number" data-line-number="1427"></td>
        <td id="LC1427" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.site_id <span class="pl-k">=</span> site_id</td>
      </tr>
      <tr>
        <td id="L1428" class="blob-num js-line-number" data-line-number="1428"></td>
        <td id="LC1428" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Go get the main URL</span></td>
      </tr>
      <tr>
        <td id="L1429" class="blob-num js-line-number" data-line-number="1429"></td>
        <td id="LC1429" class="blob-code blob-code-inner js-file-line">        site <span class="pl-k">=</span> piwik.call_api(</td>
      </tr>
      <tr>
        <td id="L1430" class="blob-num js-line-number" data-line-number="1430"></td>
        <td id="LC1430" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>SitesManager.getSiteFromId<span class="pl-pds">&#39;</span></span>, <span class="pl-v">idSite</span><span class="pl-k">=</span><span class="pl-c1">self</span>.site_id</td>
      </tr>
      <tr>
        <td id="L1431" class="blob-num js-line-number" data-line-number="1431"></td>
        <td id="LC1431" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L1432" class="blob-num js-line-number" data-line-number="1432"></td>
        <td id="LC1432" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> site.get(<span class="pl-s"><span class="pl-pds">&#39;</span>result<span class="pl-pds">&#39;</span></span>) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>error<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1433" class="blob-num js-line-number" data-line-number="1433"></td>
        <td id="LC1433" class="blob-code blob-code-inner js-file-line">            fatal_error(</td>
      </tr>
      <tr>
        <td id="L1434" class="blob-num js-line-number" data-line-number="1434"></td>
        <td id="LC1434" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>cannot get the main URL of this site: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> site.get(<span class="pl-s"><span class="pl-pds">&#39;</span>message<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1435" class="blob-num js-line-number" data-line-number="1435"></td>
        <td id="LC1435" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L1436" class="blob-num js-line-number" data-line-number="1436"></td>
        <td id="LC1436" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._main_url <span class="pl-k">=</span> site[<span class="pl-s"><span class="pl-pds">&#39;</span>main_url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1437" class="blob-num js-line-number" data-line-number="1437"></td>
        <td id="LC1437" class="blob-code blob-code-inner js-file-line">        stats.piwik_sites.add(<span class="pl-c1">self</span>.site_id)</td>
      </tr>
      <tr>
        <td id="L1438" class="blob-num js-line-number" data-line-number="1438"></td>
        <td id="LC1438" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1439" class="blob-num js-line-number" data-line-number="1439"></td>
        <td id="LC1439" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">resolve</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1440" class="blob-num js-line-number" data-line-number="1440"></td>
        <td id="LC1440" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> (<span class="pl-c1">self</span>.site_id, <span class="pl-c1">self</span>._main_url)</td>
      </tr>
      <tr>
        <td id="L1441" class="blob-num js-line-number" data-line-number="1441"></td>
        <td id="LC1441" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1442" class="blob-num js-line-number" data-line-number="1442"></td>
        <td id="LC1442" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_format</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">format</span>):</td>
      </tr>
      <tr>
        <td id="L1443" class="blob-num js-line-number" data-line-number="1443"></td>
        <td id="LC1443" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L1444" class="blob-num js-line-number" data-line-number="1444"></td>
        <td id="LC1444" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1445" class="blob-num js-line-number" data-line-number="1445"></td>
        <td id="LC1445" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">DynamicResolver</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L1446" class="blob-num js-line-number" data-line-number="1446"></td>
        <td id="LC1446" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1447" class="blob-num js-line-number" data-line-number="1447"></td>
        <td id="LC1447" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Use Piwik API to determine the site ID.</span></td>
      </tr>
      <tr>
        <td id="L1448" class="blob-num js-line-number" data-line-number="1448"></td>
        <td id="LC1448" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1449" class="blob-num js-line-number" data-line-number="1449"></td>
        <td id="LC1449" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1450" class="blob-num js-line-number" data-line-number="1450"></td>
        <td id="LC1450" class="blob-code blob-code-inner js-file-line">    _add_site_lock <span class="pl-k">=</span> threading.Lock()</td>
      </tr>
      <tr>
        <td id="L1451" class="blob-num js-line-number" data-line-number="1451"></td>
        <td id="LC1451" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1452" class="blob-num js-line-number" data-line-number="1452"></td>
        <td id="LC1452" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1453" class="blob-num js-line-number" data-line-number="1453"></td>
        <td id="LC1453" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._cache <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L1454" class="blob-num js-line-number" data-line-number="1454"></td>
        <td id="LC1454" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.replay_tracking:</td>
      </tr>
      <tr>
        <td id="L1455" class="blob-num js-line-number" data-line-number="1455"></td>
        <td id="LC1455" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> get existing sites</span></td>
      </tr>
      <tr>
        <td id="L1456" class="blob-num js-line-number" data-line-number="1456"></td>
        <td id="LC1456" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._cache[<span class="pl-s"><span class="pl-pds">&#39;</span>sites<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> piwik.call_api(<span class="pl-s"><span class="pl-pds">&#39;</span>SitesManager.getAllSites<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1457" class="blob-num js-line-number" data-line-number="1457"></td>
        <td id="LC1457" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1458" class="blob-num js-line-number" data-line-number="1458"></td>
        <td id="LC1458" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_get_site_id_from_hit_host</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1459" class="blob-num js-line-number" data-line-number="1459"></td>
        <td id="LC1459" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> piwik.call_api(</td>
      </tr>
      <tr>
        <td id="L1460" class="blob-num js-line-number" data-line-number="1460"></td>
        <td id="LC1460" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>SitesManager.getSitesIdFromSiteUrl<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1461" class="blob-num js-line-number" data-line-number="1461"></td>
        <td id="LC1461" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">url</span><span class="pl-k">=</span>hit.host,</td>
      </tr>
      <tr>
        <td id="L1462" class="blob-num js-line-number" data-line-number="1462"></td>
        <td id="LC1462" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L1463" class="blob-num js-line-number" data-line-number="1463"></td>
        <td id="LC1463" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1464" class="blob-num js-line-number" data-line-number="1464"></td>
        <td id="LC1464" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_add_site</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1465" class="blob-num js-line-number" data-line-number="1465"></td>
        <td id="LC1465" class="blob-code blob-code-inner js-file-line">        main_url <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> hit.host</td>
      </tr>
      <tr>
        <td id="L1466" class="blob-num js-line-number" data-line-number="1466"></td>
        <td id="LC1466" class="blob-code blob-code-inner js-file-line">        DynamicResolver._add_site_lock.acquire()</td>
      </tr>
      <tr>
        <td id="L1467" class="blob-num js-line-number" data-line-number="1467"></td>
        <td id="LC1467" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1468" class="blob-num js-line-number" data-line-number="1468"></td>
        <td id="LC1468" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1469" class="blob-num js-line-number" data-line-number="1469"></td>
        <td id="LC1469" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> After we obtain the lock, make sure the site hasn&#39;t already been created.</span></td>
      </tr>
      <tr>
        <td id="L1470" class="blob-num js-line-number" data-line-number="1470"></td>
        <td id="LC1470" class="blob-code blob-code-inner js-file-line">            res <span class="pl-k">=</span> <span class="pl-c1">self</span>._get_site_id_from_hit_host(hit)</td>
      </tr>
      <tr>
        <td id="L1471" class="blob-num js-line-number" data-line-number="1471"></td>
        <td id="LC1471" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> res:</td>
      </tr>
      <tr>
        <td id="L1472" class="blob-num js-line-number" data-line-number="1472"></td>
        <td id="LC1472" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> res[<span class="pl-c1">0</span>][<span class="pl-s"><span class="pl-pds">&#39;</span>idsite<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1473" class="blob-num js-line-number" data-line-number="1473"></td>
        <td id="LC1473" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1474" class="blob-num js-line-number" data-line-number="1474"></td>
        <td id="LC1474" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> The site doesn&#39;t exist.</span></td>
      </tr>
      <tr>
        <td id="L1475" class="blob-num js-line-number" data-line-number="1475"></td>
        <td id="LC1475" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>No Piwik site found for the hostname: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, hit.host)</td>
      </tr>
      <tr>
        <td id="L1476" class="blob-num js-line-number" data-line-number="1476"></td>
        <td id="LC1476" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.site_id_fallback <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1477" class="blob-num js-line-number" data-line-number="1477"></td>
        <td id="LC1477" class="blob-code blob-code-inner js-file-line">                logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Using default site for hostname: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, hit.host)</td>
      </tr>
      <tr>
        <td id="L1478" class="blob-num js-line-number" data-line-number="1478"></td>
        <td id="LC1478" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> config.options.site_id_fallback</td>
      </tr>
      <tr>
        <td id="L1479" class="blob-num js-line-number" data-line-number="1479"></td>
        <td id="LC1479" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> config.options.add_sites_new_hosts:</td>
      </tr>
      <tr>
        <td id="L1480" class="blob-num js-line-number" data-line-number="1480"></td>
        <td id="LC1480" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> config.options.dry_run:</td>
      </tr>
      <tr>
        <td id="L1481" class="blob-num js-line-number" data-line-number="1481"></td>
        <td id="LC1481" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> Let&#39;s just return a fake ID.</span></td>
      </tr>
      <tr>
        <td id="L1482" class="blob-num js-line-number" data-line-number="1482"></td>
        <td id="LC1482" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L1483" class="blob-num js-line-number" data-line-number="1483"></td>
        <td id="LC1483" class="blob-code blob-code-inner js-file-line">                logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Creating a Piwik site for hostname <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, hit.host)</td>
      </tr>
      <tr>
        <td id="L1484" class="blob-num js-line-number" data-line-number="1484"></td>
        <td id="LC1484" class="blob-code blob-code-inner js-file-line">                result <span class="pl-k">=</span> piwik.call_api(</td>
      </tr>
      <tr>
        <td id="L1485" class="blob-num js-line-number" data-line-number="1485"></td>
        <td id="LC1485" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>SitesManager.addSite<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1486" class="blob-num js-line-number" data-line-number="1486"></td>
        <td id="LC1486" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">siteName</span><span class="pl-k">=</span>hit.host,</td>
      </tr>
      <tr>
        <td id="L1487" class="blob-num js-line-number" data-line-number="1487"></td>
        <td id="LC1487" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">urls</span><span class="pl-k">=</span>[main_url],</td>
      </tr>
      <tr>
        <td id="L1488" class="blob-num js-line-number" data-line-number="1488"></td>
        <td id="LC1488" class="blob-code blob-code-inner js-file-line">                )</td>
      </tr>
      <tr>
        <td id="L1489" class="blob-num js-line-number" data-line-number="1489"></td>
        <td id="LC1489" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> result.get(<span class="pl-s"><span class="pl-pds">&#39;</span>result<span class="pl-pds">&#39;</span></span>) <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>error<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1490" class="blob-num js-line-number" data-line-number="1490"></td>
        <td id="LC1490" class="blob-code blob-code-inner js-file-line">                    logging.error(<span class="pl-s"><span class="pl-pds">&quot;</span>Couldn&#39;t create a Piwik site for host <span class="pl-c1">%s</span>: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1491" class="blob-num js-line-number" data-line-number="1491"></td>
        <td id="LC1491" class="blob-code blob-code-inner js-file-line">                        hit.host, result.get(<span class="pl-s"><span class="pl-pds">&#39;</span>message<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L1492" class="blob-num js-line-number" data-line-number="1492"></td>
        <td id="LC1492" class="blob-code blob-code-inner js-file-line">                    )</td>
      </tr>
      <tr>
        <td id="L1493" class="blob-num js-line-number" data-line-number="1493"></td>
        <td id="LC1493" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L1494" class="blob-num js-line-number" data-line-number="1494"></td>
        <td id="LC1494" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1495" class="blob-num js-line-number" data-line-number="1495"></td>
        <td id="LC1495" class="blob-code blob-code-inner js-file-line">                    site_id <span class="pl-k">=</span> result[<span class="pl-s"><span class="pl-pds">&#39;</span>value<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1496" class="blob-num js-line-number" data-line-number="1496"></td>
        <td id="LC1496" class="blob-code blob-code-inner js-file-line">                    stats.piwik_sites_created.append((hit.host, site_id))</td>
      </tr>
      <tr>
        <td id="L1497" class="blob-num js-line-number" data-line-number="1497"></td>
        <td id="LC1497" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span> site_id</td>
      </tr>
      <tr>
        <td id="L1498" class="blob-num js-line-number" data-line-number="1498"></td>
        <td id="LC1498" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1499" class="blob-num js-line-number" data-line-number="1499"></td>
        <td id="LC1499" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> The site doesn&#39;t exist, we don&#39;t want to create new sites and</span></td>
      </tr>
      <tr>
        <td id="L1500" class="blob-num js-line-number" data-line-number="1500"></td>
        <td id="LC1500" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> there&#39;s no default site ID. We thus have to ignore this hit.</span></td>
      </tr>
      <tr>
        <td id="L1501" class="blob-num js-line-number" data-line-number="1501"></td>
        <td id="LC1501" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L1502" class="blob-num js-line-number" data-line-number="1502"></td>
        <td id="LC1502" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">finally</span>:</td>
      </tr>
      <tr>
        <td id="L1503" class="blob-num js-line-number" data-line-number="1503"></td>
        <td id="LC1503" class="blob-code blob-code-inner js-file-line">            DynamicResolver._add_site_lock.release()</td>
      </tr>
      <tr>
        <td id="L1504" class="blob-num js-line-number" data-line-number="1504"></td>
        <td id="LC1504" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1505" class="blob-num js-line-number" data-line-number="1505"></td>
        <td id="LC1505" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_resolve</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1506" class="blob-num js-line-number" data-line-number="1506"></td>
        <td id="LC1506" class="blob-code blob-code-inner js-file-line">        res <span class="pl-k">=</span> <span class="pl-c1">self</span>._get_site_id_from_hit_host(hit)</td>
      </tr>
      <tr>
        <td id="L1507" class="blob-num js-line-number" data-line-number="1507"></td>
        <td id="LC1507" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> res:</td>
      </tr>
      <tr>
        <td id="L1508" class="blob-num js-line-number" data-line-number="1508"></td>
        <td id="LC1508" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> The site already exists.</span></td>
      </tr>
      <tr>
        <td id="L1509" class="blob-num js-line-number" data-line-number="1509"></td>
        <td id="LC1509" class="blob-code blob-code-inner js-file-line">            site_id <span class="pl-k">=</span> res[<span class="pl-c1">0</span>][<span class="pl-s"><span class="pl-pds">&#39;</span>idsite<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1510" class="blob-num js-line-number" data-line-number="1510"></td>
        <td id="LC1510" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1511" class="blob-num js-line-number" data-line-number="1511"></td>
        <td id="LC1511" class="blob-code blob-code-inner js-file-line">            site_id <span class="pl-k">=</span> <span class="pl-c1">self</span>._add_site(hit)</td>
      </tr>
      <tr>
        <td id="L1512" class="blob-num js-line-number" data-line-number="1512"></td>
        <td id="LC1512" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> site_id <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1513" class="blob-num js-line-number" data-line-number="1513"></td>
        <td id="LC1513" class="blob-code blob-code-inner js-file-line">            stats.piwik_sites.add(site_id)</td>
      </tr>
      <tr>
        <td id="L1514" class="blob-num js-line-number" data-line-number="1514"></td>
        <td id="LC1514" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> site_id</td>
      </tr>
      <tr>
        <td id="L1515" class="blob-num js-line-number" data-line-number="1515"></td>
        <td id="LC1515" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1516" class="blob-num js-line-number" data-line-number="1516"></td>
        <td id="LC1516" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_resolve_when_replay_tracking</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1517" class="blob-num js-line-number" data-line-number="1517"></td>
        <td id="LC1517" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1518" class="blob-num js-line-number" data-line-number="1518"></td>
        <td id="LC1518" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        If parsed site ID found in the _cache[&#39;sites&#39;] return site ID and main_url,</span></td>
      </tr>
      <tr>
        <td id="L1519" class="blob-num js-line-number" data-line-number="1519"></td>
        <td id="LC1519" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        otherwise return (None, None) tuple.</span></td>
      </tr>
      <tr>
        <td id="L1520" class="blob-num js-line-number" data-line-number="1520"></td>
        <td id="LC1520" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1521" class="blob-num js-line-number" data-line-number="1521"></td>
        <td id="LC1521" class="blob-code blob-code-inner js-file-line">        site_id <span class="pl-k">=</span> hit.args[<span class="pl-s"><span class="pl-pds">&#39;</span>idsite<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1522" class="blob-num js-line-number" data-line-number="1522"></td>
        <td id="LC1522" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> site_id <span class="pl-k">in</span> <span class="pl-c1">self</span>._cache[<span class="pl-s"><span class="pl-pds">&#39;</span>sites<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L1523" class="blob-num js-line-number" data-line-number="1523"></td>
        <td id="LC1523" class="blob-code blob-code-inner js-file-line">            stats.piwik_sites.add(site_id)</td>
      </tr>
      <tr>
        <td id="L1524" class="blob-num js-line-number" data-line-number="1524"></td>
        <td id="LC1524" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> (site_id, <span class="pl-c1">self</span>._cache[<span class="pl-s"><span class="pl-pds">&#39;</span>sites<span class="pl-pds">&#39;</span></span>][site_id][<span class="pl-s"><span class="pl-pds">&#39;</span>main_url<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1525" class="blob-num js-line-number" data-line-number="1525"></td>
        <td id="LC1525" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1526" class="blob-num js-line-number" data-line-number="1526"></td>
        <td id="LC1526" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> (<span class="pl-c1">None</span>, <span class="pl-c1">None</span>)</td>
      </tr>
      <tr>
        <td id="L1527" class="blob-num js-line-number" data-line-number="1527"></td>
        <td id="LC1527" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1528" class="blob-num js-line-number" data-line-number="1528"></td>
        <td id="LC1528" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_resolve_by_host</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1529" class="blob-num js-line-number" data-line-number="1529"></td>
        <td id="LC1529" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1530" class="blob-num js-line-number" data-line-number="1530"></td>
        <td id="LC1530" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Returns the site ID and site URL for a hit based on the hostname.</span></td>
      </tr>
      <tr>
        <td id="L1531" class="blob-num js-line-number" data-line-number="1531"></td>
        <td id="LC1531" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1532" class="blob-num js-line-number" data-line-number="1532"></td>
        <td id="LC1532" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1533" class="blob-num js-line-number" data-line-number="1533"></td>
        <td id="LC1533" class="blob-code blob-code-inner js-file-line">            site_id <span class="pl-k">=</span> <span class="pl-c1">self</span>._cache[hit.host]</td>
      </tr>
      <tr>
        <td id="L1534" class="blob-num js-line-number" data-line-number="1534"></td>
        <td id="LC1534" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">KeyError</span>:</td>
      </tr>
      <tr>
        <td id="L1535" class="blob-num js-line-number" data-line-number="1535"></td>
        <td id="LC1535" class="blob-code blob-code-inner js-file-line">            logging.debug(</td>
      </tr>
      <tr>
        <td id="L1536" class="blob-num js-line-number" data-line-number="1536"></td>
        <td id="LC1536" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>Site ID for hostname <span class="pl-c1">%s</span> not in cache<span class="pl-pds">&#39;</span></span>, hit.host</td>
      </tr>
      <tr>
        <td id="L1537" class="blob-num js-line-number" data-line-number="1537"></td>
        <td id="LC1537" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L1538" class="blob-num js-line-number" data-line-number="1538"></td>
        <td id="LC1538" class="blob-code blob-code-inner js-file-line">            site_id <span class="pl-k">=</span> <span class="pl-c1">self</span>._resolve(hit)</td>
      </tr>
      <tr>
        <td id="L1539" class="blob-num js-line-number" data-line-number="1539"></td>
        <td id="LC1539" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Site ID for hostname <span class="pl-c1">%s</span>: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, hit.host, site_id)</td>
      </tr>
      <tr>
        <td id="L1540" class="blob-num js-line-number" data-line-number="1540"></td>
        <td id="LC1540" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>._cache[hit.host] <span class="pl-k">=</span> site_id</td>
      </tr>
      <tr>
        <td id="L1541" class="blob-num js-line-number" data-line-number="1541"></td>
        <td id="LC1541" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> (site_id, <span class="pl-s"><span class="pl-pds">&#39;</span>http://<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> hit.host)</td>
      </tr>
      <tr>
        <td id="L1542" class="blob-num js-line-number" data-line-number="1542"></td>
        <td id="LC1542" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1543" class="blob-num js-line-number" data-line-number="1543"></td>
        <td id="LC1543" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">resolve</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1544" class="blob-num js-line-number" data-line-number="1544"></td>
        <td id="LC1544" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1545" class="blob-num js-line-number" data-line-number="1545"></td>
        <td id="LC1545" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Return the site ID from the cache if found, otherwise call _resolve.</span></td>
      </tr>
      <tr>
        <td id="L1546" class="blob-num js-line-number" data-line-number="1546"></td>
        <td id="LC1546" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        If replay_tracking option is enabled, call _resolve_when_replay_tracking.</span></td>
      </tr>
      <tr>
        <td id="L1547" class="blob-num js-line-number" data-line-number="1547"></td>
        <td id="LC1547" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1548" class="blob-num js-line-number" data-line-number="1548"></td>
        <td id="LC1548" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.replay_tracking:</td>
      </tr>
      <tr>
        <td id="L1549" class="blob-num js-line-number" data-line-number="1549"></td>
        <td id="LC1549" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> We only consider requests with piwik.php which don&#39;t need host to be imported</span></td>
      </tr>
      <tr>
        <td id="L1550" class="blob-num js-line-number" data-line-number="1550"></td>
        <td id="LC1550" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">self</span>._resolve_when_replay_tracking(hit)</td>
      </tr>
      <tr>
        <td id="L1551" class="blob-num js-line-number" data-line-number="1551"></td>
        <td id="LC1551" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1552" class="blob-num js-line-number" data-line-number="1552"></td>
        <td id="LC1552" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">self</span>._resolve_by_host(hit)</td>
      </tr>
      <tr>
        <td id="L1553" class="blob-num js-line-number" data-line-number="1553"></td>
        <td id="LC1553" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1554" class="blob-num js-line-number" data-line-number="1554"></td>
        <td id="LC1554" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_format</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">format</span>):</td>
      </tr>
      <tr>
        <td id="L1555" class="blob-num js-line-number" data-line-number="1555"></td>
        <td id="LC1555" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.replay_tracking:</td>
      </tr>
      <tr>
        <td id="L1556" class="blob-num js-line-number" data-line-number="1556"></td>
        <td id="LC1556" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L1557" class="blob-num js-line-number" data-line-number="1557"></td>
        <td id="LC1557" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> <span class="pl-c1">format</span>.regex <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span> <span class="pl-k">and</span> <span class="pl-s"><span class="pl-pds">&#39;</span>host<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">format</span>.regex.groupindex <span class="pl-k">and</span> <span class="pl-k">not</span> config.options.log_hostname:</td>
      </tr>
      <tr>
        <td id="L1558" class="blob-num js-line-number" data-line-number="1558"></td>
        <td id="LC1558" class="blob-code blob-code-inner js-file-line">            fatal_error(</td>
      </tr>
      <tr>
        <td id="L1559" class="blob-num js-line-number" data-line-number="1559"></td>
        <td id="LC1559" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>the selected log format doesn&#39;t include the hostname: you must <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1560" class="blob-num js-line-number" data-line-number="1560"></td>
        <td id="LC1560" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&quot;</span>specify the Piwik site ID with the --idsite argument<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1561" class="blob-num js-line-number" data-line-number="1561"></td>
        <td id="LC1561" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L1562" class="blob-num js-line-number" data-line-number="1562"></td>
        <td id="LC1562" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1563" class="blob-num js-line-number" data-line-number="1563"></td>
        <td id="LC1563" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Recorder</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L1564" class="blob-num js-line-number" data-line-number="1564"></td>
        <td id="LC1564" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1565" class="blob-num js-line-number" data-line-number="1565"></td>
        <td id="LC1565" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    A Recorder fetches hits from the Queue and inserts them into Piwik using</span></td>
      </tr>
      <tr>
        <td id="L1566" class="blob-num js-line-number" data-line-number="1566"></td>
        <td id="LC1566" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    the API.</span></td>
      </tr>
      <tr>
        <td id="L1567" class="blob-num js-line-number" data-line-number="1567"></td>
        <td id="LC1567" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1568" class="blob-num js-line-number" data-line-number="1568"></td>
        <td id="LC1568" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1569" class="blob-num js-line-number" data-line-number="1569"></td>
        <td id="LC1569" class="blob-code blob-code-inner js-file-line">    recorders <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1570" class="blob-num js-line-number" data-line-number="1570"></td>
        <td id="LC1570" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1571" class="blob-num js-line-number" data-line-number="1571"></td>
        <td id="LC1571" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1572" class="blob-num js-line-number" data-line-number="1572"></td>
        <td id="LC1572" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.queue <span class="pl-k">=</span> Queue.Queue(<span class="pl-v">maxsize</span><span class="pl-k">=</span><span class="pl-c1">2</span>)</td>
      </tr>
      <tr>
        <td id="L1573" class="blob-num js-line-number" data-line-number="1573"></td>
        <td id="LC1573" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1574" class="blob-num js-line-number" data-line-number="1574"></td>
        <td id="LC1574" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if bulk tracking disabled, make sure we can store hits outside of the Queue</span></td>
      </tr>
      <tr>
        <td id="L1575" class="blob-num js-line-number" data-line-number="1575"></td>
        <td id="LC1575" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> config.options.use_bulk_tracking:</td>
      </tr>
      <tr>
        <td id="L1576" class="blob-num js-line-number" data-line-number="1576"></td>
        <td id="LC1576" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.unrecorded_hits <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L1577" class="blob-num js-line-number" data-line-number="1577"></td>
        <td id="LC1577" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1578" class="blob-num js-line-number" data-line-number="1578"></td>
        <td id="LC1578" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">classmethod</span></td>
      </tr>
      <tr>
        <td id="L1579" class="blob-num js-line-number" data-line-number="1579"></td>
        <td id="LC1579" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">launch</span>(<span class="pl-smi"><span class="pl-smi">cls</span></span>, <span class="pl-smi">recorder_count</span>):</td>
      </tr>
      <tr>
        <td id="L1580" class="blob-num js-line-number" data-line-number="1580"></td>
        <td id="LC1580" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1581" class="blob-num js-line-number" data-line-number="1581"></td>
        <td id="LC1581" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Launch a bunch of Recorder objects in a separate thread.</span></td>
      </tr>
      <tr>
        <td id="L1582" class="blob-num js-line-number" data-line-number="1582"></td>
        <td id="LC1582" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1583" class="blob-num js-line-number" data-line-number="1583"></td>
        <td id="LC1583" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i <span class="pl-k">in</span> <span class="pl-v">xrange</span>(recorder_count):</td>
      </tr>
      <tr>
        <td id="L1584" class="blob-num js-line-number" data-line-number="1584"></td>
        <td id="LC1584" class="blob-code blob-code-inner js-file-line">            recorder <span class="pl-k">=</span> Recorder()</td>
      </tr>
      <tr>
        <td id="L1585" class="blob-num js-line-number" data-line-number="1585"></td>
        <td id="LC1585" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">cls</span>.recorders.append(recorder)</td>
      </tr>
      <tr>
        <td id="L1586" class="blob-num js-line-number" data-line-number="1586"></td>
        <td id="LC1586" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1587" class="blob-num js-line-number" data-line-number="1587"></td>
        <td id="LC1587" class="blob-code blob-code-inner js-file-line">            run <span class="pl-k">=</span> recorder._run_bulk <span class="pl-k">if</span> config.options.use_bulk_tracking <span class="pl-k">else</span> recorder._run_single</td>
      </tr>
      <tr>
        <td id="L1588" class="blob-num js-line-number" data-line-number="1588"></td>
        <td id="LC1588" class="blob-code blob-code-inner js-file-line">            t <span class="pl-k">=</span> threading.Thread(<span class="pl-v">target</span><span class="pl-k">=</span>run)</td>
      </tr>
      <tr>
        <td id="L1589" class="blob-num js-line-number" data-line-number="1589"></td>
        <td id="LC1589" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1590" class="blob-num js-line-number" data-line-number="1590"></td>
        <td id="LC1590" class="blob-code blob-code-inner js-file-line">            t.daemon <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1591" class="blob-num js-line-number" data-line-number="1591"></td>
        <td id="LC1591" class="blob-code blob-code-inner js-file-line">            t.start()</td>
      </tr>
      <tr>
        <td id="L1592" class="blob-num js-line-number" data-line-number="1592"></td>
        <td id="LC1592" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Launched recorder<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1593" class="blob-num js-line-number" data-line-number="1593"></td>
        <td id="LC1593" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1594" class="blob-num js-line-number" data-line-number="1594"></td>
        <td id="LC1594" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">classmethod</span></td>
      </tr>
      <tr>
        <td id="L1595" class="blob-num js-line-number" data-line-number="1595"></td>
        <td id="LC1595" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">add_hits</span>(<span class="pl-smi"><span class="pl-smi">cls</span></span>, <span class="pl-smi">all_hits</span>):</td>
      </tr>
      <tr>
        <td id="L1596" class="blob-num js-line-number" data-line-number="1596"></td>
        <td id="LC1596" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1597" class="blob-num js-line-number" data-line-number="1597"></td>
        <td id="LC1597" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Add a set of hits to the recorders queue.</span></td>
      </tr>
      <tr>
        <td id="L1598" class="blob-num js-line-number" data-line-number="1598"></td>
        <td id="LC1598" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1599" class="blob-num js-line-number" data-line-number="1599"></td>
        <td id="LC1599" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Organize hits so that one client IP will always use the same queue.</span></td>
      </tr>
      <tr>
        <td id="L1600" class="blob-num js-line-number" data-line-number="1600"></td>
        <td id="LC1600" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> We have to do this so visits from the same IP will be added in the right order.</span></td>
      </tr>
      <tr>
        <td id="L1601" class="blob-num js-line-number" data-line-number="1601"></td>
        <td id="LC1601" class="blob-code blob-code-inner js-file-line">        hits_by_client <span class="pl-k">=</span> [[] <span class="pl-k">for</span> r <span class="pl-k">in</span> <span class="pl-c1">cls</span>.recorders]</td>
      </tr>
      <tr>
        <td id="L1602" class="blob-num js-line-number" data-line-number="1602"></td>
        <td id="LC1602" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> hit <span class="pl-k">in</span> all_hits:</td>
      </tr>
      <tr>
        <td id="L1603" class="blob-num js-line-number" data-line-number="1603"></td>
        <td id="LC1603" class="blob-code blob-code-inner js-file-line">            hits_by_client[hit.get_visitor_id_hash() <span class="pl-k">%</span> <span class="pl-c1">len</span>(<span class="pl-c1">cls</span>.recorders)].append(hit)</td>
      </tr>
      <tr>
        <td id="L1604" class="blob-num js-line-number" data-line-number="1604"></td>
        <td id="LC1604" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1605" class="blob-num js-line-number" data-line-number="1605"></td>
        <td id="LC1605" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> i, recorder <span class="pl-k">in</span> <span class="pl-c1">enumerate</span>(<span class="pl-c1">cls</span>.recorders):</td>
      </tr>
      <tr>
        <td id="L1606" class="blob-num js-line-number" data-line-number="1606"></td>
        <td id="LC1606" class="blob-code blob-code-inner js-file-line">            recorder.queue.put(hits_by_client[i])</td>
      </tr>
      <tr>
        <td id="L1607" class="blob-num js-line-number" data-line-number="1607"></td>
        <td id="LC1607" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1608" class="blob-num js-line-number" data-line-number="1608"></td>
        <td id="LC1608" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">classmethod</span></td>
      </tr>
      <tr>
        <td id="L1609" class="blob-num js-line-number" data-line-number="1609"></td>
        <td id="LC1609" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">wait_empty</span>(<span class="pl-smi"><span class="pl-smi">cls</span></span>):</td>
      </tr>
      <tr>
        <td id="L1610" class="blob-num js-line-number" data-line-number="1610"></td>
        <td id="LC1610" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1611" class="blob-num js-line-number" data-line-number="1611"></td>
        <td id="LC1611" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Wait until all recorders have an empty queue.</span></td>
      </tr>
      <tr>
        <td id="L1612" class="blob-num js-line-number" data-line-number="1612"></td>
        <td id="LC1612" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1613" class="blob-num js-line-number" data-line-number="1613"></td>
        <td id="LC1613" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> recorder <span class="pl-k">in</span> <span class="pl-c1">cls</span>.recorders:</td>
      </tr>
      <tr>
        <td id="L1614" class="blob-num js-line-number" data-line-number="1614"></td>
        <td id="LC1614" class="blob-code blob-code-inner js-file-line">            recorder._wait_empty()</td>
      </tr>
      <tr>
        <td id="L1615" class="blob-num js-line-number" data-line-number="1615"></td>
        <td id="LC1615" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1616" class="blob-num js-line-number" data-line-number="1616"></td>
        <td id="LC1616" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_run_bulk</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1617" class="blob-num js-line-number" data-line-number="1617"></td>
        <td id="LC1617" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1618" class="blob-num js-line-number" data-line-number="1618"></td>
        <td id="LC1618" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1619" class="blob-num js-line-number" data-line-number="1619"></td>
        <td id="LC1619" class="blob-code blob-code-inner js-file-line">                hits <span class="pl-k">=</span> <span class="pl-c1">self</span>.queue.get()</td>
      </tr>
      <tr>
        <td id="L1620" class="blob-num js-line-number" data-line-number="1620"></td>
        <td id="LC1620" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L1621" class="blob-num js-line-number" data-line-number="1621"></td>
        <td id="LC1621" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> <span class="pl-k">TODO</span>: we should log something here, however when this happens, logging.etc will throw</span></td>
      </tr>
      <tr>
        <td id="L1622" class="blob-num js-line-number" data-line-number="1622"></td>
        <td id="LC1622" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1623" class="blob-num js-line-number" data-line-number="1623"></td>
        <td id="LC1623" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1624" class="blob-num js-line-number" data-line-number="1624"></td>
        <td id="LC1624" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(hits) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1625" class="blob-num js-line-number" data-line-number="1625"></td>
        <td id="LC1625" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1626" class="blob-num js-line-number" data-line-number="1626"></td>
        <td id="LC1626" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>._record_hits(hits)</td>
      </tr>
      <tr>
        <td id="L1627" class="blob-num js-line-number" data-line-number="1627"></td>
        <td id="LC1627" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> Piwik.Error, e:</td>
      </tr>
      <tr>
        <td id="L1628" class="blob-num js-line-number" data-line-number="1628"></td>
        <td id="LC1628" class="blob-code blob-code-inner js-file-line">                    fatal_error(e, hits[<span class="pl-c1">0</span>].filename, hits[<span class="pl-c1">0</span>].lineno) <span class="pl-c"><span class="pl-c">#</span> approximate location of error</span></td>
      </tr>
      <tr>
        <td id="L1629" class="blob-num js-line-number" data-line-number="1629"></td>
        <td id="LC1629" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.queue.task_done()</td>
      </tr>
      <tr>
        <td id="L1630" class="blob-num js-line-number" data-line-number="1630"></td>
        <td id="LC1630" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1631" class="blob-num js-line-number" data-line-number="1631"></td>
        <td id="LC1631" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_run_single</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1632" class="blob-num js-line-number" data-line-number="1632"></td>
        <td id="LC1632" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1633" class="blob-num js-line-number" data-line-number="1633"></td>
        <td id="LC1633" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.force_one_action_interval <span class="pl-k">!=</span> <span class="pl-c1">False</span>:</td>
      </tr>
      <tr>
        <td id="L1634" class="blob-num js-line-number" data-line-number="1634"></td>
        <td id="LC1634" class="blob-code blob-code-inner js-file-line">                time.sleep(config.options.force_one_action_interval)</td>
      </tr>
      <tr>
        <td id="L1635" class="blob-num js-line-number" data-line-number="1635"></td>
        <td id="LC1635" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1636" class="blob-num js-line-number" data-line-number="1636"></td>
        <td id="LC1636" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.unrecorded_hits) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1637" class="blob-num js-line-number" data-line-number="1637"></td>
        <td id="LC1637" class="blob-code blob-code-inner js-file-line">                hit <span class="pl-k">=</span> <span class="pl-c1">self</span>.unrecorded_hits.pop(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L1638" class="blob-num js-line-number" data-line-number="1638"></td>
        <td id="LC1638" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1639" class="blob-num js-line-number" data-line-number="1639"></td>
        <td id="LC1639" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1640" class="blob-num js-line-number" data-line-number="1640"></td>
        <td id="LC1640" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">self</span>._record_hits([hit])</td>
      </tr>
      <tr>
        <td id="L1641" class="blob-num js-line-number" data-line-number="1641"></td>
        <td id="LC1641" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> Piwik.Error, e:</td>
      </tr>
      <tr>
        <td id="L1642" class="blob-num js-line-number" data-line-number="1642"></td>
        <td id="LC1642" class="blob-code blob-code-inner js-file-line">                    fatal_error(e, hit.filename, hit.lineno)</td>
      </tr>
      <tr>
        <td id="L1643" class="blob-num js-line-number" data-line-number="1643"></td>
        <td id="LC1643" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1644" class="blob-num js-line-number" data-line-number="1644"></td>
        <td id="LC1644" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.unrecorded_hits <span class="pl-k">=</span> <span class="pl-c1">self</span>.queue.get()</td>
      </tr>
      <tr>
        <td id="L1645" class="blob-num js-line-number" data-line-number="1645"></td>
        <td id="LC1645" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.queue.task_done()</td>
      </tr>
      <tr>
        <td id="L1646" class="blob-num js-line-number" data-line-number="1646"></td>
        <td id="LC1646" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1647" class="blob-num js-line-number" data-line-number="1647"></td>
        <td id="LC1647" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_wait_empty</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1648" class="blob-num js-line-number" data-line-number="1648"></td>
        <td id="LC1648" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1649" class="blob-num js-line-number" data-line-number="1649"></td>
        <td id="LC1649" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Wait until the queue is empty.</span></td>
      </tr>
      <tr>
        <td id="L1650" class="blob-num js-line-number" data-line-number="1650"></td>
        <td id="LC1650" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1651" class="blob-num js-line-number" data-line-number="1651"></td>
        <td id="LC1651" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L1652" class="blob-num js-line-number" data-line-number="1652"></td>
        <td id="LC1652" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">self</span>.queue.empty():</td>
      </tr>
      <tr>
        <td id="L1653" class="blob-num js-line-number" data-line-number="1653"></td>
        <td id="LC1653" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> We still have to wait for the last queue item being processed</span></td>
      </tr>
      <tr>
        <td id="L1654" class="blob-num js-line-number" data-line-number="1654"></td>
        <td id="LC1654" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> (queue.empty() returns True before queue.task_done() is</span></td>
      </tr>
      <tr>
        <td id="L1655" class="blob-num js-line-number" data-line-number="1655"></td>
        <td id="LC1655" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> called).</span></td>
      </tr>
      <tr>
        <td id="L1656" class="blob-num js-line-number" data-line-number="1656"></td>
        <td id="LC1656" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>.queue.join()</td>
      </tr>
      <tr>
        <td id="L1657" class="blob-num js-line-number" data-line-number="1657"></td>
        <td id="LC1657" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1658" class="blob-num js-line-number" data-line-number="1658"></td>
        <td id="LC1658" class="blob-code blob-code-inner js-file-line">            time.sleep(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L1659" class="blob-num js-line-number" data-line-number="1659"></td>
        <td id="LC1659" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1660" class="blob-num js-line-number" data-line-number="1660"></td>
        <td id="LC1660" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">date_to_piwik</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">date</span>):</td>
      </tr>
      <tr>
        <td id="L1661" class="blob-num js-line-number" data-line-number="1661"></td>
        <td id="LC1661" class="blob-code blob-code-inner js-file-line">        date, time <span class="pl-k">=</span> date.isoformat(<span class="pl-v">sep</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span> <span class="pl-pds">&#39;</span></span>).split()</td>
      </tr>
      <tr>
        <td id="L1662" class="blob-num js-line-number" data-line-number="1662"></td>
        <td id="LC1662" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s</span> <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (date, time.replace(<span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>:<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L1663" class="blob-num js-line-number" data-line-number="1663"></td>
        <td id="LC1663" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1664" class="blob-num js-line-number" data-line-number="1664"></td>
        <td id="LC1664" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_get_hit_args</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1665" class="blob-num js-line-number" data-line-number="1665"></td>
        <td id="LC1665" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1666" class="blob-num js-line-number" data-line-number="1666"></td>
        <td id="LC1666" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Returns the args used in tracking a hit, without the token_auth.</span></td>
      </tr>
      <tr>
        <td id="L1667" class="blob-num js-line-number" data-line-number="1667"></td>
        <td id="LC1667" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1668" class="blob-num js-line-number" data-line-number="1668"></td>
        <td id="LC1668" class="blob-code blob-code-inner js-file-line">        site_id, main_url <span class="pl-k">=</span> resolver.resolve(hit)</td>
      </tr>
      <tr>
        <td id="L1669" class="blob-num js-line-number" data-line-number="1669"></td>
        <td id="LC1669" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> site_id <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L1670" class="blob-num js-line-number" data-line-number="1670"></td>
        <td id="LC1670" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> This hit doesn&#39;t match any known Piwik site.</span></td>
      </tr>
      <tr>
        <td id="L1671" class="blob-num js-line-number" data-line-number="1671"></td>
        <td id="LC1671" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.replay_tracking:</td>
      </tr>
      <tr>
        <td id="L1672" class="blob-num js-line-number" data-line-number="1672"></td>
        <td id="LC1672" class="blob-code blob-code-inner js-file-line">                stats.piwik_sites_ignored.add(<span class="pl-s"><span class="pl-pds">&#39;</span>unrecognized site ID <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> hit.args.get(<span class="pl-s"><span class="pl-pds">&#39;</span>idsite<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L1673" class="blob-num js-line-number" data-line-number="1673"></td>
        <td id="LC1673" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1674" class="blob-num js-line-number" data-line-number="1674"></td>
        <td id="LC1674" class="blob-code blob-code-inner js-file-line">                stats.piwik_sites_ignored.add(hit.host)</td>
      </tr>
      <tr>
        <td id="L1675" class="blob-num js-line-number" data-line-number="1675"></td>
        <td id="LC1675" class="blob-code blob-code-inner js-file-line">            stats.count_lines_no_site.increment()</td>
      </tr>
      <tr>
        <td id="L1676" class="blob-num js-line-number" data-line-number="1676"></td>
        <td id="LC1676" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1677" class="blob-num js-line-number" data-line-number="1677"></td>
        <td id="LC1677" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1678" class="blob-num js-line-number" data-line-number="1678"></td>
        <td id="LC1678" class="blob-code blob-code-inner js-file-line">        stats.dates_recorded.add(hit.date.date())</td>
      </tr>
      <tr>
        <td id="L1679" class="blob-num js-line-number" data-line-number="1679"></td>
        <td id="LC1679" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1680" class="blob-num js-line-number" data-line-number="1680"></td>
        <td id="LC1680" class="blob-code blob-code-inner js-file-line">        path <span class="pl-k">=</span> hit.path</td>
      </tr>
      <tr>
        <td id="L1681" class="blob-num js-line-number" data-line-number="1681"></td>
        <td id="LC1681" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.query_string <span class="pl-k">and</span> <span class="pl-k">not</span> config.options.strip_query_string:</td>
      </tr>
      <tr>
        <td id="L1682" class="blob-num js-line-number" data-line-number="1682"></td>
        <td id="LC1682" class="blob-code blob-code-inner js-file-line">            path <span class="pl-k">+=</span> config.options.query_string_delimiter <span class="pl-k">+</span> hit.query_string</td>
      </tr>
      <tr>
        <td id="L1683" class="blob-num js-line-number" data-line-number="1683"></td>
        <td id="LC1683" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1684" class="blob-num js-line-number" data-line-number="1684"></td>
        <td id="LC1684" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> only prepend main url / host if it&#39;s a path</span></td>
      </tr>
      <tr>
        <td id="L1685" class="blob-num js-line-number" data-line-number="1685"></td>
        <td id="LC1685" class="blob-code blob-code-inner js-file-line">        url_prefix <span class="pl-k">=</span> <span class="pl-c1">self</span>._get_host_with_protocol(hit.host, main_url) <span class="pl-k">if</span> <span class="pl-c1">hasattr</span>(hit, <span class="pl-s"><span class="pl-pds">&#39;</span>host<span class="pl-pds">&#39;</span></span>) <span class="pl-k">else</span> main_url</td>
      </tr>
      <tr>
        <td id="L1686" class="blob-num js-line-number" data-line-number="1686"></td>
        <td id="LC1686" class="blob-code blob-code-inner js-file-line">        url <span class="pl-k">=</span> (url_prefix <span class="pl-k">if</span> path.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>/<span class="pl-pds">&#39;</span></span>) <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>) <span class="pl-k">+</span> path[:<span class="pl-c1">1024</span>]</td>
      </tr>
      <tr>
        <td id="L1687" class="blob-num js-line-number" data-line-number="1687"></td>
        <td id="LC1687" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1688" class="blob-num js-line-number" data-line-number="1688"></td>
        <td id="LC1688" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> handle custom variables before generating args dict</span></td>
      </tr>
      <tr>
        <td id="L1689" class="blob-num js-line-number" data-line-number="1689"></td>
        <td id="LC1689" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.enable_bots:</td>
      </tr>
      <tr>
        <td id="L1690" class="blob-num js-line-number" data-line-number="1690"></td>
        <td id="LC1690" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> hit.is_robot:</td>
      </tr>
      <tr>
        <td id="L1691" class="blob-num js-line-number" data-line-number="1691"></td>
        <td id="LC1691" class="blob-code blob-code-inner js-file-line">                hit.add_visit_custom_var(<span class="pl-s"><span class="pl-pds">&quot;</span>Bot<span class="pl-pds">&quot;</span></span>, hit.user_agent)</td>
      </tr>
      <tr>
        <td id="L1692" class="blob-num js-line-number" data-line-number="1692"></td>
        <td id="LC1692" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1693" class="blob-num js-line-number" data-line-number="1693"></td>
        <td id="LC1693" class="blob-code blob-code-inner js-file-line">                hit.add_visit_custom_var(<span class="pl-s"><span class="pl-pds">&quot;</span>Not-Bot<span class="pl-pds">&quot;</span></span>, hit.user_agent)</td>
      </tr>
      <tr>
        <td id="L1694" class="blob-num js-line-number" data-line-number="1694"></td>
        <td id="LC1694" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1695" class="blob-num js-line-number" data-line-number="1695"></td>
        <td id="LC1695" class="blob-code blob-code-inner js-file-line">        hit.add_page_custom_var(<span class="pl-s"><span class="pl-pds">&quot;</span>HTTP-code<span class="pl-pds">&quot;</span></span>, hit.status)</td>
      </tr>
      <tr>
        <td id="L1696" class="blob-num js-line-number" data-line-number="1696"></td>
        <td id="LC1696" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1697" class="blob-num js-line-number" data-line-number="1697"></td>
        <td id="LC1697" class="blob-code blob-code-inner js-file-line">        args <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L1698" class="blob-num js-line-number" data-line-number="1698"></td>
        <td id="LC1698" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>rec<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1699" class="blob-num js-line-number" data-line-number="1699"></td>
        <td id="LC1699" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>apiv<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1700" class="blob-num js-line-number" data-line-number="1700"></td>
        <td id="LC1700" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>: url.encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L1701" class="blob-num js-line-number" data-line-number="1701"></td>
        <td id="LC1701" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>urlref<span class="pl-pds">&#39;</span></span>: hit.referrer[:<span class="pl-c1">1024</span>].encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L1702" class="blob-num js-line-number" data-line-number="1702"></td>
        <td id="LC1702" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>cip<span class="pl-pds">&#39;</span></span>: hit.ip,</td>
      </tr>
      <tr>
        <td id="L1703" class="blob-num js-line-number" data-line-number="1703"></td>
        <td id="LC1703" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>cdt<span class="pl-pds">&#39;</span></span>: <span class="pl-c1">self</span>.date_to_piwik(hit.date),</td>
      </tr>
      <tr>
        <td id="L1704" class="blob-num js-line-number" data-line-number="1704"></td>
        <td id="LC1704" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>idsite<span class="pl-pds">&#39;</span></span>: site_id,</td>
      </tr>
      <tr>
        <td id="L1705" class="blob-num js-line-number" data-line-number="1705"></td>
        <td id="LC1705" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>dp<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span> <span class="pl-k">if</span> config.options.reverse_dns <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span>,</td>
      </tr>
      <tr>
        <td id="L1706" class="blob-num js-line-number" data-line-number="1706"></td>
        <td id="LC1706" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>ua<span class="pl-pds">&#39;</span></span>: hit.user_agent.encode(<span class="pl-s"><span class="pl-pds">&#39;</span>utf8<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1707" class="blob-num js-line-number" data-line-number="1707"></td>
        <td id="LC1707" class="blob-code blob-code-inner js-file-line">        }</td>
      </tr>
      <tr>
        <td id="L1708" class="blob-num js-line-number" data-line-number="1708"></td>
        <td id="LC1708" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1709" class="blob-num js-line-number" data-line-number="1709"></td>
        <td id="LC1709" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.replay_tracking:</td>
      </tr>
      <tr>
        <td id="L1710" class="blob-num js-line-number" data-line-number="1710"></td>
        <td id="LC1710" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> prevent request to be force recorded when option replay-tracking</span></td>
      </tr>
      <tr>
        <td id="L1711" class="blob-num js-line-number" data-line-number="1711"></td>
        <td id="LC1711" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>rec<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>0<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1712" class="blob-num js-line-number" data-line-number="1712"></td>
        <td id="LC1712" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L1713" class="blob-num js-line-number" data-line-number="1713"></td>
        <td id="LC1713" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> idsite is already determined by resolver</span></td>
      </tr>
      <tr>
        <td id="L1714" class="blob-num js-line-number" data-line-number="1714"></td>
        <td id="LC1714" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>idsite<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> hit.args:</td>
      </tr>
      <tr>
        <td id="L1715" class="blob-num js-line-number" data-line-number="1715"></td>
        <td id="LC1715" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">del</span> hit.args[<span class="pl-s"><span class="pl-pds">&#39;</span>idsite<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1716" class="blob-num js-line-number" data-line-number="1716"></td>
        <td id="LC1716" class="blob-code blob-code-inner js-file-line">            </td>
      </tr>
      <tr>
        <td id="L1717" class="blob-num js-line-number" data-line-number="1717"></td>
        <td id="LC1717" class="blob-code blob-code-inner js-file-line">        args.update(hit.args)</td>
      </tr>
      <tr>
        <td id="L1718" class="blob-num js-line-number" data-line-number="1718"></td>
        <td id="LC1718" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1719" class="blob-num js-line-number" data-line-number="1719"></td>
        <td id="LC1719" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.is_download:</td>
      </tr>
      <tr>
        <td id="L1720" class="blob-num js-line-number" data-line-number="1720"></td>
        <td id="LC1720" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>download<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> args[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1721" class="blob-num js-line-number" data-line-number="1721"></td>
        <td id="LC1721" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1722" class="blob-num js-line-number" data-line-number="1722"></td>
        <td id="LC1722" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.enable_bots:</td>
      </tr>
      <tr>
        <td id="L1723" class="blob-num js-line-number" data-line-number="1723"></td>
        <td id="LC1723" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>bots<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1724" class="blob-num js-line-number" data-line-number="1724"></td>
        <td id="LC1724" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1725" class="blob-num js-line-number" data-line-number="1725"></td>
        <td id="LC1725" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.is_error <span class="pl-k">or</span> hit.is_redirect:</td>
      </tr>
      <tr>
        <td id="L1726" class="blob-num js-line-number" data-line-number="1726"></td>
        <td id="LC1726" class="blob-code blob-code-inner js-file-line">			args[<span class="pl-s"><span class="pl-pds">&#39;</span>action_name<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%s%s</span>URL = <span class="pl-c1">%s%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (</td>
      </tr>
      <tr>
        <td id="L1727" class="blob-num js-line-number" data-line-number="1727"></td>
        <td id="LC1727" class="blob-code blob-code-inner js-file-line">				hit.status,</td>
      </tr>
      <tr>
        <td id="L1728" class="blob-num js-line-number" data-line-number="1728"></td>
        <td id="LC1728" class="blob-code blob-code-inner js-file-line">				config.options.title_category_delimiter,</td>
      </tr>
      <tr>
        <td id="L1729" class="blob-num js-line-number" data-line-number="1729"></td>
        <td id="LC1729" class="blob-code blob-code-inner js-file-line">				urllib.quote(args[<span class="pl-s"><span class="pl-pds">&#39;</span>url<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L1730" class="blob-num js-line-number" data-line-number="1730"></td>
        <td id="LC1730" class="blob-code blob-code-inner js-file-line">				(<span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-c1">%s</span>From = <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> ( </td>
      </tr>
      <tr>
        <td id="L1731" class="blob-num js-line-number" data-line-number="1731"></td>
        <td id="LC1731" class="blob-code blob-code-inner js-file-line">					config.options.title_category_delimiter,</td>
      </tr>
      <tr>
        <td id="L1732" class="blob-num js-line-number" data-line-number="1732"></td>
        <td id="LC1732" class="blob-code blob-code-inner js-file-line">					urllib.quote(args[<span class="pl-s"><span class="pl-pds">&#39;</span>urlref<span class="pl-pds">&#39;</span></span>], <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1733" class="blob-num js-line-number" data-line-number="1733"></td>
        <td id="LC1733" class="blob-code blob-code-inner js-file-line">				) <span class="pl-k">if</span> args[<span class="pl-s"><span class="pl-pds">&#39;</span>urlref<span class="pl-pds">&#39;</span></span>] <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>  <span class="pl-k">else</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1734" class="blob-num js-line-number" data-line-number="1734"></td>
        <td id="LC1734" class="blob-code blob-code-inner js-file-line">			)</td>
      </tr>
      <tr>
        <td id="L1735" class="blob-num js-line-number" data-line-number="1735"></td>
        <td id="LC1735" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1736" class="blob-num js-line-number" data-line-number="1736"></td>
        <td id="LC1736" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.generation_time_milli <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1737" class="blob-num js-line-number" data-line-number="1737"></td>
        <td id="LC1737" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>gt_ms<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-c1">int</span>(hit.generation_time_milli)</td>
      </tr>
      <tr>
        <td id="L1738" class="blob-num js-line-number" data-line-number="1738"></td>
        <td id="LC1738" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1739" class="blob-num js-line-number" data-line-number="1739"></td>
        <td id="LC1739" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.event_category <span class="pl-k">and</span> hit.event_action:</td>
      </tr>
      <tr>
        <td id="L1740" class="blob-num js-line-number" data-line-number="1740"></td>
        <td id="LC1740" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>e_c<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hit.event_category</td>
      </tr>
      <tr>
        <td id="L1741" class="blob-num js-line-number" data-line-number="1741"></td>
        <td id="LC1741" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>e_a<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hit.event_action</td>
      </tr>
      <tr>
        <td id="L1742" class="blob-num js-line-number" data-line-number="1742"></td>
        <td id="LC1742" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1743" class="blob-num js-line-number" data-line-number="1743"></td>
        <td id="LC1743" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> hit.event_name:</td>
      </tr>
      <tr>
        <td id="L1744" class="blob-num js-line-number" data-line-number="1744"></td>
        <td id="LC1744" class="blob-code blob-code-inner js-file-line">                args[<span class="pl-s"><span class="pl-pds">&#39;</span>e_n<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hit.event_name</td>
      </tr>
      <tr>
        <td id="L1745" class="blob-num js-line-number" data-line-number="1745"></td>
        <td id="LC1745" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1746" class="blob-num js-line-number" data-line-number="1746"></td>
        <td id="LC1746" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.length:</td>
      </tr>
      <tr>
        <td id="L1747" class="blob-num js-line-number" data-line-number="1747"></td>
        <td id="LC1747" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>bw_bytes<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hit.length</td>
      </tr>
      <tr>
        <td id="L1748" class="blob-num js-line-number" data-line-number="1748"></td>
        <td id="LC1748" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1749" class="blob-num js-line-number" data-line-number="1749"></td>
        <td id="LC1749" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> convert custom variable args to JSON</span></td>
      </tr>
      <tr>
        <td id="L1750" class="blob-num js-line-number" data-line-number="1750"></td>
        <td id="LC1750" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>cvar<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> args <span class="pl-k">and</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(args[<span class="pl-s"><span class="pl-pds">&#39;</span>cvar<span class="pl-pds">&#39;</span></span>], <span class="pl-v">basestring</span>):</td>
      </tr>
      <tr>
        <td id="L1751" class="blob-num js-line-number" data-line-number="1751"></td>
        <td id="LC1751" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>cvar<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> json.dumps(args[<span class="pl-s"><span class="pl-pds">&#39;</span>cvar<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1752" class="blob-num js-line-number" data-line-number="1752"></td>
        <td id="LC1752" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1753" class="blob-num js-line-number" data-line-number="1753"></td>
        <td id="LC1753" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>_cvar<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> args <span class="pl-k">and</span> <span class="pl-k">not</span> <span class="pl-c1">isinstance</span>(args[<span class="pl-s"><span class="pl-pds">&#39;</span>_cvar<span class="pl-pds">&#39;</span></span>], <span class="pl-v">basestring</span>):</td>
      </tr>
      <tr>
        <td id="L1754" class="blob-num js-line-number" data-line-number="1754"></td>
        <td id="LC1754" class="blob-code blob-code-inner js-file-line">            args[<span class="pl-s"><span class="pl-pds">&#39;</span>_cvar<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> json.dumps(args[<span class="pl-s"><span class="pl-pds">&#39;</span>_cvar<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1755" class="blob-num js-line-number" data-line-number="1755"></td>
        <td id="LC1755" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1756" class="blob-num js-line-number" data-line-number="1756"></td>
        <td id="LC1756" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> args</td>
      </tr>
      <tr>
        <td id="L1757" class="blob-num js-line-number" data-line-number="1757"></td>
        <td id="LC1757" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1758" class="blob-num js-line-number" data-line-number="1758"></td>
        <td id="LC1758" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_get_host_with_protocol</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">host</span>, <span class="pl-smi">main_url</span>):</td>
      </tr>
      <tr>
        <td id="L1759" class="blob-num js-line-number" data-line-number="1759"></td>
        <td id="LC1759" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-s"><span class="pl-pds">&#39;</span>://<span class="pl-pds">&#39;</span></span> <span class="pl-k">not</span> <span class="pl-k">in</span> host:</td>
      </tr>
      <tr>
        <td id="L1760" class="blob-num js-line-number" data-line-number="1760"></td>
        <td id="LC1760" class="blob-code blob-code-inner js-file-line">            parts <span class="pl-k">=</span> urlparse.urlparse(main_url)</td>
      </tr>
      <tr>
        <td id="L1761" class="blob-num js-line-number" data-line-number="1761"></td>
        <td id="LC1761" class="blob-code blob-code-inner js-file-line">            host <span class="pl-k">=</span> parts.scheme <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span>://<span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> host</td>
      </tr>
      <tr>
        <td id="L1762" class="blob-num js-line-number" data-line-number="1762"></td>
        <td id="LC1762" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> host</td>
      </tr>
      <tr>
        <td id="L1763" class="blob-num js-line-number" data-line-number="1763"></td>
        <td id="LC1763" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1764" class="blob-num js-line-number" data-line-number="1764"></td>
        <td id="LC1764" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_record_hits</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hits</span>):</td>
      </tr>
      <tr>
        <td id="L1765" class="blob-num js-line-number" data-line-number="1765"></td>
        <td id="LC1765" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1766" class="blob-num js-line-number" data-line-number="1766"></td>
        <td id="LC1766" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Inserts several hits into Piwik.</span></td>
      </tr>
      <tr>
        <td id="L1767" class="blob-num js-line-number" data-line-number="1767"></td>
        <td id="LC1767" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1768" class="blob-num js-line-number" data-line-number="1768"></td>
        <td id="LC1768" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> config.options.dry_run:</td>
      </tr>
      <tr>
        <td id="L1769" class="blob-num js-line-number" data-line-number="1769"></td>
        <td id="LC1769" class="blob-code blob-code-inner js-file-line">            data <span class="pl-k">=</span> {</td>
      </tr>
      <tr>
        <td id="L1770" class="blob-num js-line-number" data-line-number="1770"></td>
        <td id="LC1770" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>token_auth<span class="pl-pds">&#39;</span></span>: config.options.piwik_token_auth,</td>
      </tr>
      <tr>
        <td id="L1771" class="blob-num js-line-number" data-line-number="1771"></td>
        <td id="LC1771" class="blob-code blob-code-inner js-file-line">                <span class="pl-s"><span class="pl-pds">&#39;</span>requests<span class="pl-pds">&#39;</span></span>: [<span class="pl-c1">self</span>._get_hit_args(hit) <span class="pl-k">for</span> hit <span class="pl-k">in</span> hits]</td>
      </tr>
      <tr>
        <td id="L1772" class="blob-num js-line-number" data-line-number="1772"></td>
        <td id="LC1772" class="blob-code blob-code-inner js-file-line">            }</td>
      </tr>
      <tr>
        <td id="L1773" class="blob-num js-line-number" data-line-number="1773"></td>
        <td id="LC1773" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1774" class="blob-num js-line-number" data-line-number="1774"></td>
        <td id="LC1774" class="blob-code blob-code-inner js-file-line">                args <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L1775" class="blob-num js-line-number" data-line-number="1775"></td>
        <td id="LC1775" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1776" class="blob-num js-line-number" data-line-number="1776"></td>
        <td id="LC1776" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> config.options.debug_tracker:</td>
      </tr>
      <tr>
        <td id="L1777" class="blob-num js-line-number" data-line-number="1777"></td>
        <td id="LC1777" class="blob-code blob-code-inner js-file-line">                    args[<span class="pl-s"><span class="pl-pds">&#39;</span>debug<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>1<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L1778" class="blob-num js-line-number" data-line-number="1778"></td>
        <td id="LC1778" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1779" class="blob-num js-line-number" data-line-number="1779"></td>
        <td id="LC1779" class="blob-code blob-code-inner js-file-line">                response <span class="pl-k">=</span> piwik.call(</td>
      </tr>
      <tr>
        <td id="L1780" class="blob-num js-line-number" data-line-number="1780"></td>
        <td id="LC1780" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>/piwik.php<span class="pl-pds">&#39;</span></span>, <span class="pl-v">args</span><span class="pl-k">=</span>args,</td>
      </tr>
      <tr>
        <td id="L1781" class="blob-num js-line-number" data-line-number="1781"></td>
        <td id="LC1781" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">expected_content</span><span class="pl-k">=</span><span class="pl-c1">None</span>,</td>
      </tr>
      <tr>
        <td id="L1782" class="blob-num js-line-number" data-line-number="1782"></td>
        <td id="LC1782" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">headers</span><span class="pl-k">=</span>{<span class="pl-s"><span class="pl-pds">&#39;</span>Content-type<span class="pl-pds">&#39;</span></span>: <span class="pl-s"><span class="pl-pds">&#39;</span>application/json<span class="pl-pds">&#39;</span></span>},</td>
      </tr>
      <tr>
        <td id="L1783" class="blob-num js-line-number" data-line-number="1783"></td>
        <td id="LC1783" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">data</span><span class="pl-k">=</span>data,</td>
      </tr>
      <tr>
        <td id="L1784" class="blob-num js-line-number" data-line-number="1784"></td>
        <td id="LC1784" class="blob-code blob-code-inner js-file-line">                    <span class="pl-v">on_failure</span><span class="pl-k">=</span><span class="pl-c1">self</span>._on_tracking_failure</td>
      </tr>
      <tr>
        <td id="L1785" class="blob-num js-line-number" data-line-number="1785"></td>
        <td id="LC1785" class="blob-code blob-code-inner js-file-line">                )</td>
      </tr>
      <tr>
        <td id="L1786" class="blob-num js-line-number" data-line-number="1786"></td>
        <td id="LC1786" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1787" class="blob-num js-line-number" data-line-number="1787"></td>
        <td id="LC1787" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> config.options.debug_tracker:</td>
      </tr>
      <tr>
        <td id="L1788" class="blob-num js-line-number" data-line-number="1788"></td>
        <td id="LC1788" class="blob-code blob-code-inner js-file-line">                    logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>tracker response:<span class="pl-cce">\n</span><span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> response)</td>
      </tr>
      <tr>
        <td id="L1789" class="blob-num js-line-number" data-line-number="1789"></td>
        <td id="LC1789" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1790" class="blob-num js-line-number" data-line-number="1790"></td>
        <td id="LC1790" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> check for invalid requests</span></td>
      </tr>
      <tr>
        <td id="L1791" class="blob-num js-line-number" data-line-number="1791"></td>
        <td id="LC1791" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1792" class="blob-num js-line-number" data-line-number="1792"></td>
        <td id="LC1792" class="blob-code blob-code-inner js-file-line">                    response <span class="pl-k">=</span> json.loads(response)</td>
      </tr>
      <tr>
        <td id="L1793" class="blob-num js-line-number" data-line-number="1793"></td>
        <td id="LC1793" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L1794" class="blob-num js-line-number" data-line-number="1794"></td>
        <td id="LC1794" class="blob-code blob-code-inner js-file-line">                    logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>bulk tracking returned invalid JSON<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1795" class="blob-num js-line-number" data-line-number="1795"></td>
        <td id="LC1795" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1796" class="blob-num js-line-number" data-line-number="1796"></td>
        <td id="LC1796" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> don&#39;t display the tracker response if we&#39;re debugging the tracker.</span></td>
      </tr>
      <tr>
        <td id="L1797" class="blob-num js-line-number" data-line-number="1797"></td>
        <td id="LC1797" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> debug tracker output will always break the normal JSON output.</span></td>
      </tr>
      <tr>
        <td id="L1798" class="blob-num js-line-number" data-line-number="1798"></td>
        <td id="LC1798" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> <span class="pl-k">not</span> config.options.debug_tracker:</td>
      </tr>
      <tr>
        <td id="L1799" class="blob-num js-line-number" data-line-number="1799"></td>
        <td id="LC1799" class="blob-code blob-code-inner js-file-line">                        logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>tracker response:<span class="pl-cce">\n</span><span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> response)</td>
      </tr>
      <tr>
        <td id="L1800" class="blob-num js-line-number" data-line-number="1800"></td>
        <td id="LC1800" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1801" class="blob-num js-line-number" data-line-number="1801"></td>
        <td id="LC1801" class="blob-code blob-code-inner js-file-line">                    response <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L1802" class="blob-num js-line-number" data-line-number="1802"></td>
        <td id="LC1802" class="blob-code blob-code-inner js-file-line">                </td>
      </tr>
      <tr>
        <td id="L1803" class="blob-num js-line-number" data-line-number="1803"></td>
        <td id="LC1803" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>invalid_indices<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> response <span class="pl-k">and</span> <span class="pl-c1">isinstance</span>(response[<span class="pl-s"><span class="pl-pds">&#39;</span>invalid_indices<span class="pl-pds">&#39;</span></span>], <span class="pl-c1">list</span>) <span class="pl-k">and</span></td>
      </tr>
      <tr>
        <td id="L1804" class="blob-num js-line-number" data-line-number="1804"></td>
        <td id="LC1804" class="blob-code blob-code-inner js-file-line">                    response[<span class="pl-s"><span class="pl-pds">&#39;</span>invalid_indices<span class="pl-pds">&#39;</span></span>]):</td>
      </tr>
      <tr>
        <td id="L1805" class="blob-num js-line-number" data-line-number="1805"></td>
        <td id="LC1805" class="blob-code blob-code-inner js-file-line">                    invalid_count <span class="pl-k">=</span> <span class="pl-c1">len</span>(response[<span class="pl-s"><span class="pl-pds">&#39;</span>invalid_indices<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1806" class="blob-num js-line-number" data-line-number="1806"></td>
        <td id="LC1806" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1807" class="blob-num js-line-number" data-line-number="1807"></td>
        <td id="LC1807" class="blob-code blob-code-inner js-file-line">                    invalid_lines <span class="pl-k">=</span> [<span class="pl-c1">str</span>(hits[index].lineno) <span class="pl-k">for</span> index <span class="pl-k">in</span> response[<span class="pl-s"><span class="pl-pds">&#39;</span>invalid_indices<span class="pl-pds">&#39;</span></span>]]</td>
      </tr>
      <tr>
        <td id="L1808" class="blob-num js-line-number" data-line-number="1808"></td>
        <td id="LC1808" class="blob-code blob-code-inner js-file-line">                    invalid_lines_str <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&quot;</span>, <span class="pl-pds">&quot;</span></span>.join(invalid_lines)</td>
      </tr>
      <tr>
        <td id="L1809" class="blob-num js-line-number" data-line-number="1809"></td>
        <td id="LC1809" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1810" class="blob-num js-line-number" data-line-number="1810"></td>
        <td id="LC1810" class="blob-code blob-code-inner js-file-line">                    stats.invalid_lines.extend(invalid_lines)</td>
      </tr>
      <tr>
        <td id="L1811" class="blob-num js-line-number" data-line-number="1811"></td>
        <td id="LC1811" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1812" class="blob-num js-line-number" data-line-number="1812"></td>
        <td id="LC1812" class="blob-code blob-code-inner js-file-line">                    logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>The Piwik tracker identified <span class="pl-c1">%s</span> invalid requests on lines: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (invalid_count, invalid_lines_str))</td>
      </tr>
      <tr>
        <td id="L1813" class="blob-num js-line-number" data-line-number="1813"></td>
        <td id="LC1813" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> <span class="pl-s"><span class="pl-pds">&#39;</span>invalid<span class="pl-pds">&#39;</span></span> <span class="pl-k">in</span> response <span class="pl-k">and</span> response[<span class="pl-s"><span class="pl-pds">&#39;</span>invalid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L1814" class="blob-num js-line-number" data-line-number="1814"></td>
        <td id="LC1814" class="blob-code blob-code-inner js-file-line">                    logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>The Piwik tracker identified <span class="pl-c1">%s</span> invalid requests.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> response[<span class="pl-s"><span class="pl-pds">&#39;</span>invalid<span class="pl-pds">&#39;</span></span>])</td>
      </tr>
      <tr>
        <td id="L1815" class="blob-num js-line-number" data-line-number="1815"></td>
        <td id="LC1815" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> Piwik.Error, e:</td>
      </tr>
      <tr>
        <td id="L1816" class="blob-num js-line-number" data-line-number="1816"></td>
        <td id="LC1816" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> if the server returned 400 code, BulkTracking may not be enabled</span></td>
      </tr>
      <tr>
        <td id="L1817" class="blob-num js-line-number" data-line-number="1817"></td>
        <td id="LC1817" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> e.code <span class="pl-k">==</span> <span class="pl-c1">400</span>:</td>
      </tr>
      <tr>
        <td id="L1818" class="blob-num js-line-number" data-line-number="1818"></td>
        <td id="LC1818" class="blob-code blob-code-inner js-file-line">                    fatal_error(<span class="pl-s"><span class="pl-pds">&quot;</span>Server returned status 400 (Bad Request).<span class="pl-cce">\n</span>Is the BulkTracking plugin disabled?<span class="pl-pds">&quot;</span></span>, hits[<span class="pl-c1">0</span>].filename, hits[<span class="pl-c1">0</span>].lineno)</td>
      </tr>
      <tr>
        <td id="L1819" class="blob-num js-line-number" data-line-number="1819"></td>
        <td id="LC1819" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1820" class="blob-num js-line-number" data-line-number="1820"></td>
        <td id="LC1820" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">raise</span></td>
      </tr>
      <tr>
        <td id="L1821" class="blob-num js-line-number" data-line-number="1821"></td>
        <td id="LC1821" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1822" class="blob-num js-line-number" data-line-number="1822"></td>
        <td id="LC1822" class="blob-code blob-code-inner js-file-line">        stats.count_lines_recorded.advance(<span class="pl-c1">len</span>(hits))</td>
      </tr>
      <tr>
        <td id="L1823" class="blob-num js-line-number" data-line-number="1823"></td>
        <td id="LC1823" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1824" class="blob-num js-line-number" data-line-number="1824"></td>
        <td id="LC1824" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_is_json</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">result</span>):</td>
      </tr>
      <tr>
        <td id="L1825" class="blob-num js-line-number" data-line-number="1825"></td>
        <td id="LC1825" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1826" class="blob-num js-line-number" data-line-number="1826"></td>
        <td id="LC1826" class="blob-code blob-code-inner js-file-line">            json.loads(result)</td>
      </tr>
      <tr>
        <td id="L1827" class="blob-num js-line-number" data-line-number="1827"></td>
        <td id="LC1827" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1828" class="blob-num js-line-number" data-line-number="1828"></td>
        <td id="LC1828" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>, e:</td>
      </tr>
      <tr>
        <td id="L1829" class="blob-num js-line-number" data-line-number="1829"></td>
        <td id="LC1829" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1830" class="blob-num js-line-number" data-line-number="1830"></td>
        <td id="LC1830" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1831" class="blob-num js-line-number" data-line-number="1831"></td>
        <td id="LC1831" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_on_tracking_failure</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">response</span>, <span class="pl-smi">data</span>):</td>
      </tr>
      <tr>
        <td id="L1832" class="blob-num js-line-number" data-line-number="1832"></td>
        <td id="LC1832" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1833" class="blob-num js-line-number" data-line-number="1833"></td>
        <td id="LC1833" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Removes the successfully tracked hits from the request payload so</span></td>
      </tr>
      <tr>
        <td id="L1834" class="blob-num js-line-number" data-line-number="1834"></td>
        <td id="LC1834" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        they are not logged twice.</span></td>
      </tr>
      <tr>
        <td id="L1835" class="blob-num js-line-number" data-line-number="1835"></td>
        <td id="LC1835" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1836" class="blob-num js-line-number" data-line-number="1836"></td>
        <td id="LC1836" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L1837" class="blob-num js-line-number" data-line-number="1837"></td>
        <td id="LC1837" class="blob-code blob-code-inner js-file-line">            response <span class="pl-k">=</span> json.loads(response)</td>
      </tr>
      <tr>
        <td id="L1838" class="blob-num js-line-number" data-line-number="1838"></td>
        <td id="LC1838" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L1839" class="blob-num js-line-number" data-line-number="1839"></td>
        <td id="LC1839" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> the response should be in JSON, but in case it can&#39;t be parsed just try another attempt</span></td>
      </tr>
      <tr>
        <td id="L1840" class="blob-num js-line-number" data-line-number="1840"></td>
        <td id="LC1840" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&quot;</span>cannot parse tracker response, should be valid JSON<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1841" class="blob-num js-line-number" data-line-number="1841"></td>
        <td id="LC1841" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> response</td>
      </tr>
      <tr>
        <td id="L1842" class="blob-num js-line-number" data-line-number="1842"></td>
        <td id="LC1842" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1843" class="blob-num js-line-number" data-line-number="1843"></td>
        <td id="LC1843" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> remove the successfully tracked hits from payload</span></td>
      </tr>
      <tr>
        <td id="L1844" class="blob-num js-line-number" data-line-number="1844"></td>
        <td id="LC1844" class="blob-code blob-code-inner js-file-line">        tracked <span class="pl-k">=</span> response[<span class="pl-s"><span class="pl-pds">&#39;</span>tracked<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1845" class="blob-num js-line-number" data-line-number="1845"></td>
        <td id="LC1845" class="blob-code blob-code-inner js-file-line">        data[<span class="pl-s"><span class="pl-pds">&#39;</span>requests<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> data[<span class="pl-s"><span class="pl-pds">&#39;</span>requests<span class="pl-pds">&#39;</span></span>][tracked:]</td>
      </tr>
      <tr>
        <td id="L1846" class="blob-num js-line-number" data-line-number="1846"></td>
        <td id="LC1846" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1847" class="blob-num js-line-number" data-line-number="1847"></td>
        <td id="LC1847" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> response[<span class="pl-s"><span class="pl-pds">&#39;</span>message<span class="pl-pds">&#39;</span></span>]</td>
      </tr>
      <tr>
        <td id="L1848" class="blob-num js-line-number" data-line-number="1848"></td>
        <td id="LC1848" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1849" class="blob-num js-line-number" data-line-number="1849"></td>
        <td id="LC1849" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Hit</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L1850" class="blob-num js-line-number" data-line-number="1850"></td>
        <td id="LC1850" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1851" class="blob-num js-line-number" data-line-number="1851"></td>
        <td id="LC1851" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    It&#39;s a simple container.</span></td>
      </tr>
      <tr>
        <td id="L1852" class="blob-num js-line-number" data-line-number="1852"></td>
        <td id="LC1852" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1853" class="blob-num js-line-number" data-line-number="1853"></td>
        <td id="LC1853" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-k">**</span><span class="pl-smi">kwargs</span>):</td>
      </tr>
      <tr>
        <td id="L1854" class="blob-num js-line-number" data-line-number="1854"></td>
        <td id="LC1854" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> key, value <span class="pl-k">in</span> kwargs.iteritems():</td>
      </tr>
      <tr>
        <td id="L1855" class="blob-num js-line-number" data-line-number="1855"></td>
        <td id="LC1855" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">setattr</span>(<span class="pl-c1">self</span>, key, value)</td>
      </tr>
      <tr>
        <td id="L1856" class="blob-num js-line-number" data-line-number="1856"></td>
        <td id="LC1856" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">super</span>(Hit, <span class="pl-c1">self</span>).<span class="pl-c1">__init__</span>()</td>
      </tr>
      <tr>
        <td id="L1857" class="blob-num js-line-number" data-line-number="1857"></td>
        <td id="LC1857" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1858" class="blob-num js-line-number" data-line-number="1858"></td>
        <td id="LC1858" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.force_lowercase_path:</td>
      </tr>
      <tr>
        <td id="L1859" class="blob-num js-line-number" data-line-number="1859"></td>
        <td id="LC1859" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.full_path <span class="pl-k">=</span> <span class="pl-c1">self</span>.full_path.lower()</td>
      </tr>
      <tr>
        <td id="L1860" class="blob-num js-line-number" data-line-number="1860"></td>
        <td id="LC1860" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1861" class="blob-num js-line-number" data-line-number="1861"></td>
        <td id="LC1861" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">get_visitor_id_hash</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1862" class="blob-num js-line-number" data-line-number="1862"></td>
        <td id="LC1862" class="blob-code blob-code-inner js-file-line">        visitor_id <span class="pl-k">=</span> <span class="pl-c1">self</span>.ip</td>
      </tr>
      <tr>
        <td id="L1863" class="blob-num js-line-number" data-line-number="1863"></td>
        <td id="LC1863" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1864" class="blob-num js-line-number" data-line-number="1864"></td>
        <td id="LC1864" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.replay_tracking:</td>
      </tr>
      <tr>
        <td id="L1865" class="blob-num js-line-number" data-line-number="1865"></td>
        <td id="LC1865" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> param_name_to_use <span class="pl-k">in</span> [<span class="pl-s"><span class="pl-pds">&#39;</span>uid<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>cid<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>_id<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>cip<span class="pl-pds">&#39;</span></span>]:</td>
      </tr>
      <tr>
        <td id="L1866" class="blob-num js-line-number" data-line-number="1866"></td>
        <td id="LC1866" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> param_name_to_use <span class="pl-k">in</span> <span class="pl-c1">self</span>.args:</td>
      </tr>
      <tr>
        <td id="L1867" class="blob-num js-line-number" data-line-number="1867"></td>
        <td id="LC1867" class="blob-code blob-code-inner js-file-line">                    visitor_id <span class="pl-k">=</span> <span class="pl-c1">self</span>.args[param_name_to_use]</td>
      </tr>
      <tr>
        <td id="L1868" class="blob-num js-line-number" data-line-number="1868"></td>
        <td id="LC1868" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L1869" class="blob-num js-line-number" data-line-number="1869"></td>
        <td id="LC1869" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1870" class="blob-num js-line-number" data-line-number="1870"></td>
        <td id="LC1870" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">abs</span>(<span class="pl-c1">hash</span>(visitor_id))</td>
      </tr>
      <tr>
        <td id="L1871" class="blob-num js-line-number" data-line-number="1871"></td>
        <td id="LC1871" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1872" class="blob-num js-line-number" data-line-number="1872"></td>
        <td id="LC1872" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">add_page_custom_var</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">key</span>, <span class="pl-smi">value</span>):</td>
      </tr>
      <tr>
        <td id="L1873" class="blob-num js-line-number" data-line-number="1873"></td>
        <td id="LC1873" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1874" class="blob-num js-line-number" data-line-number="1874"></td>
        <td id="LC1874" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Adds a page custom variable to this Hit.</span></td>
      </tr>
      <tr>
        <td id="L1875" class="blob-num js-line-number" data-line-number="1875"></td>
        <td id="LC1875" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1876" class="blob-num js-line-number" data-line-number="1876"></td>
        <td id="LC1876" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._add_custom_var(key, value, <span class="pl-s"><span class="pl-pds">&#39;</span>cvar<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1877" class="blob-num js-line-number" data-line-number="1877"></td>
        <td id="LC1877" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1878" class="blob-num js-line-number" data-line-number="1878"></td>
        <td id="LC1878" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">add_visit_custom_var</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">key</span>, <span class="pl-smi">value</span>):</td>
      </tr>
      <tr>
        <td id="L1879" class="blob-num js-line-number" data-line-number="1879"></td>
        <td id="LC1879" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1880" class="blob-num js-line-number" data-line-number="1880"></td>
        <td id="LC1880" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Adds a visit custom variable to this Hit.</span></td>
      </tr>
      <tr>
        <td id="L1881" class="blob-num js-line-number" data-line-number="1881"></td>
        <td id="LC1881" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1882" class="blob-num js-line-number" data-line-number="1882"></td>
        <td id="LC1882" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>._add_custom_var(key, value, <span class="pl-s"><span class="pl-pds">&#39;</span>_cvar<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L1883" class="blob-num js-line-number" data-line-number="1883"></td>
        <td id="LC1883" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1884" class="blob-num js-line-number" data-line-number="1884"></td>
        <td id="LC1884" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_add_custom_var</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">key</span>, <span class="pl-smi">value</span>, <span class="pl-smi">api_arg_name</span>):</td>
      </tr>
      <tr>
        <td id="L1885" class="blob-num js-line-number" data-line-number="1885"></td>
        <td id="LC1885" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> api_arg_name <span class="pl-k">not</span> <span class="pl-k">in</span> <span class="pl-c1">self</span>.args:</td>
      </tr>
      <tr>
        <td id="L1886" class="blob-num js-line-number" data-line-number="1886"></td>
        <td id="LC1886" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">self</span>.args[api_arg_name] <span class="pl-k">=</span> {}</td>
      </tr>
      <tr>
        <td id="L1887" class="blob-num js-line-number" data-line-number="1887"></td>
        <td id="LC1887" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1888" class="blob-num js-line-number" data-line-number="1888"></td>
        <td id="LC1888" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(<span class="pl-c1">self</span>.args[api_arg_name], <span class="pl-v">basestring</span>):</td>
      </tr>
      <tr>
        <td id="L1889" class="blob-num js-line-number" data-line-number="1889"></td>
        <td id="LC1889" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&quot;</span>Ignoring custom <span class="pl-c1">%s</span> variable addition [ <span class="pl-c1">%s</span> = <span class="pl-c1">%s</span> ], custom var already set to string.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> (api_arg_name, key, value))</td>
      </tr>
      <tr>
        <td id="L1890" class="blob-num js-line-number" data-line-number="1890"></td>
        <td id="LC1890" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L1891" class="blob-num js-line-number" data-line-number="1891"></td>
        <td id="LC1891" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1892" class="blob-num js-line-number" data-line-number="1892"></td>
        <td id="LC1892" class="blob-code blob-code-inner js-file-line">        index <span class="pl-k">=</span> <span class="pl-c1">len</span>(<span class="pl-c1">self</span>.args[api_arg_name]) <span class="pl-k">+</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L1893" class="blob-num js-line-number" data-line-number="1893"></td>
        <td id="LC1893" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.args[api_arg_name][index] <span class="pl-k">=</span> [key, value]</td>
      </tr>
      <tr>
        <td id="L1894" class="blob-num js-line-number" data-line-number="1894"></td>
        <td id="LC1894" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1895" class="blob-num js-line-number" data-line-number="1895"></td>
        <td id="LC1895" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Parser</span>(<span class="pl-c1">object</span>):</td>
      </tr>
      <tr>
        <td id="L1896" class="blob-num js-line-number" data-line-number="1896"></td>
        <td id="LC1896" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1897" class="blob-num js-line-number" data-line-number="1897"></td>
        <td id="LC1897" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    The Parser parses the lines in a specified file and inserts them into</span></td>
      </tr>
      <tr>
        <td id="L1898" class="blob-num js-line-number" data-line-number="1898"></td>
        <td id="LC1898" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    a Queue.</span></td>
      </tr>
      <tr>
        <td id="L1899" class="blob-num js-line-number" data-line-number="1899"></td>
        <td id="LC1899" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L1900" class="blob-num js-line-number" data-line-number="1900"></td>
        <td id="LC1900" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1901" class="blob-num js-line-number" data-line-number="1901"></td>
        <td id="LC1901" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-c1">__init__</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>):</td>
      </tr>
      <tr>
        <td id="L1902" class="blob-num js-line-number" data-line-number="1902"></td>
        <td id="LC1902" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">self</span>.check_methods <span class="pl-k">=</span> [method <span class="pl-k">for</span> name, method</td>
      </tr>
      <tr>
        <td id="L1903" class="blob-num js-line-number" data-line-number="1903"></td>
        <td id="LC1903" class="blob-code blob-code-inner js-file-line">                              <span class="pl-k">in</span> inspect.getmembers(<span class="pl-c1">self</span>, <span class="pl-v">predicate</span><span class="pl-k">=</span>inspect.ismethod)</td>
      </tr>
      <tr>
        <td id="L1904" class="blob-num js-line-number" data-line-number="1904"></td>
        <td id="LC1904" class="blob-code blob-code-inner js-file-line">                              <span class="pl-k">if</span> name.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>check_<span class="pl-pds">&#39;</span></span>)]</td>
      </tr>
      <tr>
        <td id="L1905" class="blob-num js-line-number" data-line-number="1905"></td>
        <td id="LC1905" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1906" class="blob-num js-line-number" data-line-number="1906"></td>
        <td id="LC1906" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span># All check_* methods are called for each hit and must return True if the</span></td>
      </tr>
      <tr>
        <td id="L1907" class="blob-num js-line-number" data-line-number="1907"></td>
        <td id="LC1907" class="blob-code blob-code-inner js-file-line">    <span class="pl-c"><span class="pl-c">#</span># hit can be imported, False otherwise.</span></td>
      </tr>
      <tr>
        <td id="L1908" class="blob-num js-line-number" data-line-number="1908"></td>
        <td id="LC1908" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1909" class="blob-num js-line-number" data-line-number="1909"></td>
        <td id="LC1909" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_hostname</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1910" class="blob-num js-line-number" data-line-number="1910"></td>
        <td id="LC1910" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Check against config.hostnames.</span></td>
      </tr>
      <tr>
        <td id="L1911" class="blob-num js-line-number" data-line-number="1911"></td>
        <td id="LC1911" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">hasattr</span>(hit, <span class="pl-s"><span class="pl-pds">&#39;</span>host<span class="pl-pds">&#39;</span></span>) <span class="pl-k">or</span> <span class="pl-k">not</span> config.options.hostnames:</td>
      </tr>
      <tr>
        <td id="L1912" class="blob-num js-line-number" data-line-number="1912"></td>
        <td id="LC1912" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1913" class="blob-num js-line-number" data-line-number="1913"></td>
        <td id="LC1913" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1914" class="blob-num js-line-number" data-line-number="1914"></td>
        <td id="LC1914" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Accept the hostname only if it matches one pattern in the list.</span></td>
      </tr>
      <tr>
        <td id="L1915" class="blob-num js-line-number" data-line-number="1915"></td>
        <td id="LC1915" class="blob-code blob-code-inner js-file-line">        result <span class="pl-k">=</span> <span class="pl-c1">any</span>(</td>
      </tr>
      <tr>
        <td id="L1916" class="blob-num js-line-number" data-line-number="1916"></td>
        <td id="LC1916" class="blob-code blob-code-inner js-file-line">            fnmatch.fnmatch(hit.host, pattern)</td>
      </tr>
      <tr>
        <td id="L1917" class="blob-num js-line-number" data-line-number="1917"></td>
        <td id="LC1917" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">for</span> pattern <span class="pl-k">in</span> config.options.hostnames</td>
      </tr>
      <tr>
        <td id="L1918" class="blob-num js-line-number" data-line-number="1918"></td>
        <td id="LC1918" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L1919" class="blob-num js-line-number" data-line-number="1919"></td>
        <td id="LC1919" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> result:</td>
      </tr>
      <tr>
        <td id="L1920" class="blob-num js-line-number" data-line-number="1920"></td>
        <td id="LC1920" class="blob-code blob-code-inner js-file-line">            stats.count_lines_hostname_skipped.increment()</td>
      </tr>
      <tr>
        <td id="L1921" class="blob-num js-line-number" data-line-number="1921"></td>
        <td id="LC1921" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> result</td>
      </tr>
      <tr>
        <td id="L1922" class="blob-num js-line-number" data-line-number="1922"></td>
        <td id="LC1922" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1923" class="blob-num js-line-number" data-line-number="1923"></td>
        <td id="LC1923" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_static</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1924" class="blob-num js-line-number" data-line-number="1924"></td>
        <td id="LC1924" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.extension <span class="pl-k">in</span> <span class="pl-c1">STATIC_EXTENSIONS</span>:</td>
      </tr>
      <tr>
        <td id="L1925" class="blob-num js-line-number" data-line-number="1925"></td>
        <td id="LC1925" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.enable_static:</td>
      </tr>
      <tr>
        <td id="L1926" class="blob-num js-line-number" data-line-number="1926"></td>
        <td id="LC1926" class="blob-code blob-code-inner js-file-line">                hit.is_download <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1927" class="blob-num js-line-number" data-line-number="1927"></td>
        <td id="LC1927" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1928" class="blob-num js-line-number" data-line-number="1928"></td>
        <td id="LC1928" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1929" class="blob-num js-line-number" data-line-number="1929"></td>
        <td id="LC1929" class="blob-code blob-code-inner js-file-line">                stats.count_lines_static.increment()</td>
      </tr>
      <tr>
        <td id="L1930" class="blob-num js-line-number" data-line-number="1930"></td>
        <td id="LC1930" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1931" class="blob-num js-line-number" data-line-number="1931"></td>
        <td id="LC1931" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1932" class="blob-num js-line-number" data-line-number="1932"></td>
        <td id="LC1932" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1933" class="blob-num js-line-number" data-line-number="1933"></td>
        <td id="LC1933" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_download</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1934" class="blob-num js-line-number" data-line-number="1934"></td>
        <td id="LC1934" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.extension <span class="pl-k">in</span> config.options.download_extensions:</td>
      </tr>
      <tr>
        <td id="L1935" class="blob-num js-line-number" data-line-number="1935"></td>
        <td id="LC1935" class="blob-code blob-code-inner js-file-line">            stats.count_lines_downloads.increment()</td>
      </tr>
      <tr>
        <td id="L1936" class="blob-num js-line-number" data-line-number="1936"></td>
        <td id="LC1936" class="blob-code blob-code-inner js-file-line">            hit.is_download <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1937" class="blob-num js-line-number" data-line-number="1937"></td>
        <td id="LC1937" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1938" class="blob-num js-line-number" data-line-number="1938"></td>
        <td id="LC1938" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> the file is not in the white-listed downloads</span></td>
      </tr>
      <tr>
        <td id="L1939" class="blob-num js-line-number" data-line-number="1939"></td>
        <td id="LC1939" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if it&#39;s a know download file, we shall skip it</span></td>
      </tr>
      <tr>
        <td id="L1940" class="blob-num js-line-number" data-line-number="1940"></td>
        <td id="LC1940" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">elif</span> hit.extension <span class="pl-k">in</span> <span class="pl-c1">DOWNLOAD_EXTENSIONS</span>:</td>
      </tr>
      <tr>
        <td id="L1941" class="blob-num js-line-number" data-line-number="1941"></td>
        <td id="LC1941" class="blob-code blob-code-inner js-file-line">            stats.count_lines_skipped_downloads.increment()</td>
      </tr>
      <tr>
        <td id="L1942" class="blob-num js-line-number" data-line-number="1942"></td>
        <td id="LC1942" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1943" class="blob-num js-line-number" data-line-number="1943"></td>
        <td id="LC1943" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1944" class="blob-num js-line-number" data-line-number="1944"></td>
        <td id="LC1944" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1945" class="blob-num js-line-number" data-line-number="1945"></td>
        <td id="LC1945" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_user_agent</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1946" class="blob-num js-line-number" data-line-number="1946"></td>
        <td id="LC1946" class="blob-code blob-code-inner js-file-line">        user_agent <span class="pl-k">=</span> hit.user_agent.lower()</td>
      </tr>
      <tr>
        <td id="L1947" class="blob-num js-line-number" data-line-number="1947"></td>
        <td id="LC1947" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> s <span class="pl-k">in</span> itertools.chain(<span class="pl-c1">EXCLUDED_USER_AGENTS</span>, config.options.excluded_useragents):</td>
      </tr>
      <tr>
        <td id="L1948" class="blob-num js-line-number" data-line-number="1948"></td>
        <td id="LC1948" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> s <span class="pl-k">in</span> user_agent:</td>
      </tr>
      <tr>
        <td id="L1949" class="blob-num js-line-number" data-line-number="1949"></td>
        <td id="LC1949" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> config.options.enable_bots:</td>
      </tr>
      <tr>
        <td id="L1950" class="blob-num js-line-number" data-line-number="1950"></td>
        <td id="LC1950" class="blob-code blob-code-inner js-file-line">                    hit.is_robot <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1951" class="blob-num js-line-number" data-line-number="1951"></td>
        <td id="LC1951" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1952" class="blob-num js-line-number" data-line-number="1952"></td>
        <td id="LC1952" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1953" class="blob-num js-line-number" data-line-number="1953"></td>
        <td id="LC1953" class="blob-code blob-code-inner js-file-line">                    stats.count_lines_skipped_user_agent.increment()</td>
      </tr>
      <tr>
        <td id="L1954" class="blob-num js-line-number" data-line-number="1954"></td>
        <td id="LC1954" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1955" class="blob-num js-line-number" data-line-number="1955"></td>
        <td id="LC1955" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1956" class="blob-num js-line-number" data-line-number="1956"></td>
        <td id="LC1956" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1957" class="blob-num js-line-number" data-line-number="1957"></td>
        <td id="LC1957" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_http_error</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1958" class="blob-num js-line-number" data-line-number="1958"></td>
        <td id="LC1958" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.status[<span class="pl-c1">0</span>] <span class="pl-k">in</span> (<span class="pl-s"><span class="pl-pds">&#39;</span>4<span class="pl-pds">&#39;</span></span>, <span class="pl-s"><span class="pl-pds">&#39;</span>5<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L1959" class="blob-num js-line-number" data-line-number="1959"></td>
        <td id="LC1959" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.replay_tracking:</td>
      </tr>
      <tr>
        <td id="L1960" class="blob-num js-line-number" data-line-number="1960"></td>
        <td id="LC1960" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> process error logs for replay tracking, since we don&#39;t care if piwik error-ed the first time</span></td>
      </tr>
      <tr>
        <td id="L1961" class="blob-num js-line-number" data-line-number="1961"></td>
        <td id="LC1961" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1962" class="blob-num js-line-number" data-line-number="1962"></td>
        <td id="LC1962" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">elif</span> config.options.enable_http_errors:</td>
      </tr>
      <tr>
        <td id="L1963" class="blob-num js-line-number" data-line-number="1963"></td>
        <td id="LC1963" class="blob-code blob-code-inner js-file-line">                hit.is_error <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1964" class="blob-num js-line-number" data-line-number="1964"></td>
        <td id="LC1964" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1965" class="blob-num js-line-number" data-line-number="1965"></td>
        <td id="LC1965" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1966" class="blob-num js-line-number" data-line-number="1966"></td>
        <td id="LC1966" class="blob-code blob-code-inner js-file-line">                stats.count_lines_skipped_http_errors.increment()</td>
      </tr>
      <tr>
        <td id="L1967" class="blob-num js-line-number" data-line-number="1967"></td>
        <td id="LC1967" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1968" class="blob-num js-line-number" data-line-number="1968"></td>
        <td id="LC1968" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1969" class="blob-num js-line-number" data-line-number="1969"></td>
        <td id="LC1969" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1970" class="blob-num js-line-number" data-line-number="1970"></td>
        <td id="LC1970" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_http_redirect</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1971" class="blob-num js-line-number" data-line-number="1971"></td>
        <td id="LC1971" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> hit.status[<span class="pl-c1">0</span>] <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>3<span class="pl-pds">&#39;</span></span> <span class="pl-k">and</span> hit.status <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>304<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L1972" class="blob-num js-line-number" data-line-number="1972"></td>
        <td id="LC1972" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.enable_http_redirects:</td>
      </tr>
      <tr>
        <td id="L1973" class="blob-num js-line-number" data-line-number="1973"></td>
        <td id="LC1973" class="blob-code blob-code-inner js-file-line">                hit.is_redirect <span class="pl-k">=</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1974" class="blob-num js-line-number" data-line-number="1974"></td>
        <td id="LC1974" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1975" class="blob-num js-line-number" data-line-number="1975"></td>
        <td id="LC1975" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L1976" class="blob-num js-line-number" data-line-number="1976"></td>
        <td id="LC1976" class="blob-code blob-code-inner js-file-line">                stats.count_lines_skipped_http_redirects.increment()</td>
      </tr>
      <tr>
        <td id="L1977" class="blob-num js-line-number" data-line-number="1977"></td>
        <td id="LC1977" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1978" class="blob-num js-line-number" data-line-number="1978"></td>
        <td id="LC1978" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1979" class="blob-num js-line-number" data-line-number="1979"></td>
        <td id="LC1979" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1980" class="blob-num js-line-number" data-line-number="1980"></td>
        <td id="LC1980" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_path</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>):</td>
      </tr>
      <tr>
        <td id="L1981" class="blob-num js-line-number" data-line-number="1981"></td>
        <td id="LC1981" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> excluded_path <span class="pl-k">in</span> config.options.excluded_paths:</td>
      </tr>
      <tr>
        <td id="L1982" class="blob-num js-line-number" data-line-number="1982"></td>
        <td id="LC1982" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> fnmatch.fnmatch(hit.path, excluded_path):</td>
      </tr>
      <tr>
        <td id="L1983" class="blob-num js-line-number" data-line-number="1983"></td>
        <td id="LC1983" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1984" class="blob-num js-line-number" data-line-number="1984"></td>
        <td id="LC1984" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> By default, all paths are included.</span></td>
      </tr>
      <tr>
        <td id="L1985" class="blob-num js-line-number" data-line-number="1985"></td>
        <td id="LC1985" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.included_paths:</td>
      </tr>
      <tr>
        <td id="L1986" class="blob-num js-line-number" data-line-number="1986"></td>
        <td id="LC1986" class="blob-code blob-code-inner js-file-line">           <span class="pl-k">for</span> included_path <span class="pl-k">in</span> config.options.included_paths:</td>
      </tr>
      <tr>
        <td id="L1987" class="blob-num js-line-number" data-line-number="1987"></td>
        <td id="LC1987" class="blob-code blob-code-inner js-file-line">               <span class="pl-k">if</span> fnmatch.fnmatch(hit.path, included_path):</td>
      </tr>
      <tr>
        <td id="L1988" class="blob-num js-line-number" data-line-number="1988"></td>
        <td id="LC1988" class="blob-code blob-code-inner js-file-line">                   <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1989" class="blob-num js-line-number" data-line-number="1989"></td>
        <td id="LC1989" class="blob-code blob-code-inner js-file-line">           <span class="pl-k">return</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1990" class="blob-num js-line-number" data-line-number="1990"></td>
        <td id="LC1990" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">True</span></td>
      </tr>
      <tr>
        <td id="L1991" class="blob-num js-line-number" data-line-number="1991"></td>
        <td id="LC1991" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1992" class="blob-num js-line-number" data-line-number="1992"></td>
        <td id="LC1992" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">staticmethod</span></td>
      </tr>
      <tr>
        <td id="L1993" class="blob-num js-line-number" data-line-number="1993"></td>
        <td id="LC1993" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">check_format</span>(<span class="pl-smi">lineOrFile</span>):</td>
      </tr>
      <tr>
        <td id="L1994" class="blob-num js-line-number" data-line-number="1994"></td>
        <td id="LC1994" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">format</span> <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L1995" class="blob-num js-line-number" data-line-number="1995"></td>
        <td id="LC1995" class="blob-code blob-code-inner js-file-line">        format_groups <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L1996" class="blob-num js-line-number" data-line-number="1996"></td>
        <td id="LC1996" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> name, candidate_format <span class="pl-k">in</span> <span class="pl-c1">FORMATS</span>.iteritems():</td>
      </tr>
      <tr>
        <td id="L1997" class="blob-num js-line-number" data-line-number="1997"></td>
        <td id="LC1997" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&quot;</span>Check format <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span>, name)</td>
      </tr>
      <tr>
        <td id="L1998" class="blob-num js-line-number" data-line-number="1998"></td>
        <td id="LC1998" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L1999" class="blob-num js-line-number" data-line-number="1999"></td>
        <td id="LC1999" class="blob-code blob-code-inner js-file-line">            match <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L2000" class="blob-num js-line-number" data-line-number="2000"></td>
        <td id="LC2000" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2001" class="blob-num js-line-number" data-line-number="2001"></td>
        <td id="LC2001" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(lineOrFile, <span class="pl-v">basestring</span>):</td>
      </tr>
      <tr>
        <td id="L2002" class="blob-num js-line-number" data-line-number="2002"></td>
        <td id="LC2002" class="blob-code blob-code-inner js-file-line">                    match <span class="pl-k">=</span> candidate_format.check_format_line(lineOrFile)</td>
      </tr>
      <tr>
        <td id="L2003" class="blob-num js-line-number" data-line-number="2003"></td>
        <td id="LC2003" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2004" class="blob-num js-line-number" data-line-number="2004"></td>
        <td id="LC2004" class="blob-code blob-code-inner js-file-line">                    match <span class="pl-k">=</span> candidate_format.check_format(lineOrFile)</td>
      </tr>
      <tr>
        <td id="L2005" class="blob-num js-line-number" data-line-number="2005"></td>
        <td id="LC2005" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">Exception</span>, e:</td>
      </tr>
      <tr>
        <td id="L2006" class="blob-num js-line-number" data-line-number="2006"></td>
        <td id="LC2006" class="blob-code blob-code-inner js-file-line">                logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Error in format checking: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span>, traceback.format_exc())</td>
      </tr>
      <tr>
        <td id="L2007" class="blob-num js-line-number" data-line-number="2007"></td>
        <td id="LC2007" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L2008" class="blob-num js-line-number" data-line-number="2008"></td>
        <td id="LC2008" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2009" class="blob-num js-line-number" data-line-number="2009"></td>
        <td id="LC2009" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> match:</td>
      </tr>
      <tr>
        <td id="L2010" class="blob-num js-line-number" data-line-number="2010"></td>
        <td id="LC2010" class="blob-code blob-code-inner js-file-line">                logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Format <span class="pl-c1">%s</span> matches<span class="pl-pds">&#39;</span></span>, name)</td>
      </tr>
      <tr>
        <td id="L2011" class="blob-num js-line-number" data-line-number="2011"></td>
        <td id="LC2011" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2012" class="blob-num js-line-number" data-line-number="2012"></td>
        <td id="LC2012" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> compare format groups if this *BaseFormat has groups() method</span></td>
      </tr>
      <tr>
        <td id="L2013" class="blob-num js-line-number" data-line-number="2013"></td>
        <td id="LC2013" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2014" class="blob-num js-line-number" data-line-number="2014"></td>
        <td id="LC2014" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> if there&#39;s more info in this match, use this format</span></td>
      </tr>
      <tr>
        <td id="L2015" class="blob-num js-line-number" data-line-number="2015"></td>
        <td id="LC2015" class="blob-code blob-code-inner js-file-line">                    match_groups <span class="pl-k">=</span> <span class="pl-c1">len</span>(match.groups())</td>
      </tr>
      <tr>
        <td id="L2016" class="blob-num js-line-number" data-line-number="2016"></td>
        <td id="LC2016" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2017" class="blob-num js-line-number" data-line-number="2017"></td>
        <td id="LC2017" class="blob-code blob-code-inner js-file-line">                    logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Format match contains <span class="pl-c1">%d</span> groups<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> match_groups)</td>
      </tr>
      <tr>
        <td id="L2018" class="blob-num js-line-number" data-line-number="2018"></td>
        <td id="LC2018" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2019" class="blob-num js-line-number" data-line-number="2019"></td>
        <td id="LC2019" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> format_groups <span class="pl-k">&lt;</span> match_groups:</td>
      </tr>
      <tr>
        <td id="L2020" class="blob-num js-line-number" data-line-number="2020"></td>
        <td id="LC2020" class="blob-code blob-code-inner js-file-line">                        <span class="pl-c1">format</span> <span class="pl-k">=</span> candidate_format</td>
      </tr>
      <tr>
        <td id="L2021" class="blob-num js-line-number" data-line-number="2021"></td>
        <td id="LC2021" class="blob-code blob-code-inner js-file-line">                        format_groups <span class="pl-k">=</span> match_groups</td>
      </tr>
      <tr>
        <td id="L2022" class="blob-num js-line-number" data-line-number="2022"></td>
        <td id="LC2022" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> <span class="pl-c1">AttributeError</span>:</td>
      </tr>
      <tr>
        <td id="L2023" class="blob-num js-line-number" data-line-number="2023"></td>
        <td id="LC2023" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c1">format</span> <span class="pl-k">=</span> candidate_format</td>
      </tr>
      <tr>
        <td id="L2024" class="blob-num js-line-number" data-line-number="2024"></td>
        <td id="LC2024" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2025" class="blob-num js-line-number" data-line-number="2025"></td>
        <td id="LC2025" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2026" class="blob-num js-line-number" data-line-number="2026"></td>
        <td id="LC2026" class="blob-code blob-code-inner js-file-line">                logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Format <span class="pl-c1">%s</span> does not match<span class="pl-pds">&#39;</span></span>, name)</td>
      </tr>
      <tr>
        <td id="L2027" class="blob-num js-line-number" data-line-number="2027"></td>
        <td id="LC2027" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2028" class="blob-num js-line-number" data-line-number="2028"></td>
        <td id="LC2028" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> if the format is W3cExtendedFormat, check if the logs are from IIS and if so, issue a warning if the</span></td>
      </tr>
      <tr>
        <td id="L2029" class="blob-num js-line-number" data-line-number="2029"></td>
        <td id="LC2029" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> --w3c-time-taken-milli option isn&#39;t set</span></td>
      </tr>
      <tr>
        <td id="L2030" class="blob-num js-line-number" data-line-number="2030"></td>
        <td id="LC2030" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(<span class="pl-c1">format</span>, W3cExtendedFormat):</td>
      </tr>
      <tr>
        <td id="L2031" class="blob-num js-line-number" data-line-number="2031"></td>
        <td id="LC2031" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">format</span>.check_for_iis_option()</td>
      </tr>
      <tr>
        <td id="L2032" class="blob-num js-line-number" data-line-number="2032"></td>
        <td id="LC2032" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2033" class="blob-num js-line-number" data-line-number="2033"></td>
        <td id="LC2033" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">format</span></td>
      </tr>
      <tr>
        <td id="L2034" class="blob-num js-line-number" data-line-number="2034"></td>
        <td id="LC2034" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2035" class="blob-num js-line-number" data-line-number="2035"></td>
        <td id="LC2035" class="blob-code blob-code-inner js-file-line">    <span class="pl-en">@</span><span class="pl-c1">staticmethod</span></td>
      </tr>
      <tr>
        <td id="L2036" class="blob-num js-line-number" data-line-number="2036"></td>
        <td id="LC2036" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">detect_format</span>(<span class="pl-smi">file</span>):</td>
      </tr>
      <tr>
        <td id="L2037" class="blob-num js-line-number" data-line-number="2037"></td>
        <td id="LC2037" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2038" class="blob-num js-line-number" data-line-number="2038"></td>
        <td id="LC2038" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Return the best matching format for this file, or None if none was found.</span></td>
      </tr>
      <tr>
        <td id="L2039" class="blob-num js-line-number" data-line-number="2039"></td>
        <td id="LC2039" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2040" class="blob-num js-line-number" data-line-number="2040"></td>
        <td id="LC2040" class="blob-code blob-code-inner js-file-line">        logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Detecting the log format<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2041" class="blob-num js-line-number" data-line-number="2041"></td>
        <td id="LC2041" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2042" class="blob-num js-line-number" data-line-number="2042"></td>
        <td id="LC2042" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">format</span> <span class="pl-k">=</span> <span class="pl-c1">False</span></td>
      </tr>
      <tr>
        <td id="L2043" class="blob-num js-line-number" data-line-number="2043"></td>
        <td id="LC2043" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2044" class="blob-num js-line-number" data-line-number="2044"></td>
        <td id="LC2044" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> check the format using the file (for formats like the W3cExtendedFormat one)</span></td>
      </tr>
      <tr>
        <td id="L2045" class="blob-num js-line-number" data-line-number="2045"></td>
        <td id="LC2045" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">format</span> <span class="pl-k">=</span> Parser.check_format(<span class="pl-v">file</span>)</td>
      </tr>
      <tr>
        <td id="L2046" class="blob-num js-line-number" data-line-number="2046"></td>
        <td id="LC2046" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2047" class="blob-num js-line-number" data-line-number="2047"></td>
        <td id="LC2047" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> check the format using the first N lines (to avoid irregular ones)</span></td>
      </tr>
      <tr>
        <td id="L2048" class="blob-num js-line-number" data-line-number="2048"></td>
        <td id="LC2048" class="blob-code blob-code-inner js-file-line">        lineno <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L2049" class="blob-num js-line-number" data-line-number="2049"></td>
        <td id="LC2049" class="blob-code blob-code-inner js-file-line">        limit <span class="pl-k">=</span> <span class="pl-c1">100000</span></td>
      </tr>
      <tr>
        <td id="L2050" class="blob-num js-line-number" data-line-number="2050"></td>
        <td id="LC2050" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-k">not</span> <span class="pl-c1">format</span> <span class="pl-k">and</span> lineno <span class="pl-k">&lt;</span> limit:</td>
      </tr>
      <tr>
        <td id="L2051" class="blob-num js-line-number" data-line-number="2051"></td>
        <td id="LC2051" class="blob-code blob-code-inner js-file-line">            line <span class="pl-k">=</span> <span class="pl-v">file</span>.readline()</td>
      </tr>
      <tr>
        <td id="L2052" class="blob-num js-line-number" data-line-number="2052"></td>
        <td id="LC2052" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> line: <span class="pl-c"><span class="pl-c">#</span> if at eof, don&#39;t keep looping</span></td>
      </tr>
      <tr>
        <td id="L2053" class="blob-num js-line-number" data-line-number="2053"></td>
        <td id="LC2053" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L2054" class="blob-num js-line-number" data-line-number="2054"></td>
        <td id="LC2054" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2055" class="blob-num js-line-number" data-line-number="2055"></td>
        <td id="LC2055" class="blob-code blob-code-inner js-file-line">            lineno <span class="pl-k">=</span> lineno <span class="pl-k">+</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L2056" class="blob-num js-line-number" data-line-number="2056"></td>
        <td id="LC2056" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2057" class="blob-num js-line-number" data-line-number="2057"></td>
        <td id="LC2057" class="blob-code blob-code-inner js-file-line">            logging.debug(<span class="pl-s"><span class="pl-pds">&quot;</span>Detecting format against line <span class="pl-c1">%i</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> lineno)</td>
      </tr>
      <tr>
        <td id="L2058" class="blob-num js-line-number" data-line-number="2058"></td>
        <td id="LC2058" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">format</span> <span class="pl-k">=</span> Parser.check_format(line)</td>
      </tr>
      <tr>
        <td id="L2059" class="blob-num js-line-number" data-line-number="2059"></td>
        <td id="LC2059" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2060" class="blob-num js-line-number" data-line-number="2060"></td>
        <td id="LC2060" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2061" class="blob-num js-line-number" data-line-number="2061"></td>
        <td id="LC2061" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">file</span>.seek(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L2062" class="blob-num js-line-number" data-line-number="2062"></td>
        <td id="LC2062" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">except</span> <span class="pl-c1">IOError</span>:</td>
      </tr>
      <tr>
        <td id="L2063" class="blob-num js-line-number" data-line-number="2063"></td>
        <td id="LC2063" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L2064" class="blob-num js-line-number" data-line-number="2064"></td>
        <td id="LC2064" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2065" class="blob-num js-line-number" data-line-number="2065"></td>
        <td id="LC2065" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">format</span>:</td>
      </tr>
      <tr>
        <td id="L2066" class="blob-num js-line-number" data-line-number="2066"></td>
        <td id="LC2066" class="blob-code blob-code-inner js-file-line">            fatal_error(<span class="pl-s"><span class="pl-pds">&quot;</span>cannot automatically determine the log format using the first <span class="pl-c1">%d</span> lines of the log file. <span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> limit <span class="pl-k">+</span></td>
      </tr>
      <tr>
        <td id="L2067" class="blob-num js-line-number" data-line-number="2067"></td>
        <td id="LC2067" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>Maybe try specifying the format with the --log-format-name command line argument.<span class="pl-pds">&quot;</span></span> )</td>
      </tr>
      <tr>
        <td id="L2068" class="blob-num js-line-number" data-line-number="2068"></td>
        <td id="LC2068" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L2069" class="blob-num js-line-number" data-line-number="2069"></td>
        <td id="LC2069" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2070" class="blob-num js-line-number" data-line-number="2070"></td>
        <td id="LC2070" class="blob-code blob-code-inner js-file-line">        logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Format <span class="pl-c1">%s</span> is the best match<span class="pl-pds">&#39;</span></span>, <span class="pl-c1">format</span>.name)</td>
      </tr>
      <tr>
        <td id="L2071" class="blob-num js-line-number" data-line-number="2071"></td>
        <td id="LC2071" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">return</span> <span class="pl-c1">format</span></td>
      </tr>
      <tr>
        <td id="L2072" class="blob-num js-line-number" data-line-number="2072"></td>
        <td id="LC2072" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2073" class="blob-num js-line-number" data-line-number="2073"></td>
        <td id="LC2073" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">parse</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">filename</span>):</td>
      </tr>
      <tr>
        <td id="L2074" class="blob-num js-line-number" data-line-number="2074"></td>
        <td id="LC2074" class="blob-code blob-code-inner js-file-line">        <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2075" class="blob-num js-line-number" data-line-number="2075"></td>
        <td id="LC2075" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        Parse the specified filename and insert hits in the queue.</span></td>
      </tr>
      <tr>
        <td id="L2076" class="blob-num js-line-number" data-line-number="2076"></td>
        <td id="LC2076" class="blob-code blob-code-inner js-file-line"><span class="pl-s">        <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2077" class="blob-num js-line-number" data-line-number="2077"></td>
        <td id="LC2077" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">def</span> <span class="pl-en">invalid_line</span>(<span class="pl-smi">line</span>, <span class="pl-smi">reason</span>):</td>
      </tr>
      <tr>
        <td id="L2078" class="blob-num js-line-number" data-line-number="2078"></td>
        <td id="LC2078" class="blob-code blob-code-inner js-file-line">            stats.count_lines_invalid.increment()</td>
      </tr>
      <tr>
        <td id="L2079" class="blob-num js-line-number" data-line-number="2079"></td>
        <td id="LC2079" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.debug <span class="pl-k">&gt;=</span> <span class="pl-c1">2</span>:</td>
      </tr>
      <tr>
        <td id="L2080" class="blob-num js-line-number" data-line-number="2080"></td>
        <td id="LC2080" class="blob-code blob-code-inner js-file-line">                logging.debug(<span class="pl-s"><span class="pl-pds">&#39;</span>Invalid line detected (<span class="pl-c1">%s</span>): <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (reason, line))</td>
      </tr>
      <tr>
        <td id="L2081" class="blob-num js-line-number" data-line-number="2081"></td>
        <td id="LC2081" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2082" class="blob-num js-line-number" data-line-number="2082"></td>
        <td id="LC2082" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> filename <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L2083" class="blob-num js-line-number" data-line-number="2083"></td>
        <td id="LC2083" class="blob-code blob-code-inner js-file-line">            filename <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>(stdin)<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2084" class="blob-num js-line-number" data-line-number="2084"></td>
        <td id="LC2084" class="blob-code blob-code-inner js-file-line">            <span class="pl-v">file</span> <span class="pl-k">=</span> sys.stdin</td>
      </tr>
      <tr>
        <td id="L2085" class="blob-num js-line-number" data-line-number="2085"></td>
        <td id="LC2085" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2086" class="blob-num js-line-number" data-line-number="2086"></td>
        <td id="LC2086" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> os.path.exists(filename):</td>
      </tr>
      <tr>
        <td id="L2087" class="blob-num js-line-number" data-line-number="2087"></td>
        <td id="LC2087" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">print</span> <span class="pl-k">&gt;&gt;</span> sys.stderr, <span class="pl-s"><span class="pl-pds">&quot;</span><span class="pl-cce">\n</span>=====&gt; Warning: File <span class="pl-c1">%s</span> does not exist &lt;=====<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> filename</td>
      </tr>
      <tr>
        <td id="L2088" class="blob-num js-line-number" data-line-number="2088"></td>
        <td id="LC2088" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L2089" class="blob-num js-line-number" data-line-number="2089"></td>
        <td id="LC2089" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2090" class="blob-num js-line-number" data-line-number="2090"></td>
        <td id="LC2090" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> filename.endswith(<span class="pl-s"><span class="pl-pds">&#39;</span>.bz2<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L2091" class="blob-num js-line-number" data-line-number="2091"></td>
        <td id="LC2091" class="blob-code blob-code-inner js-file-line">                    open_func <span class="pl-k">=</span> bz2.BZ2File</td>
      </tr>
      <tr>
        <td id="L2092" class="blob-num js-line-number" data-line-number="2092"></td>
        <td id="LC2092" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">elif</span> filename.endswith(<span class="pl-s"><span class="pl-pds">&#39;</span>.gz<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L2093" class="blob-num js-line-number" data-line-number="2093"></td>
        <td id="LC2093" class="blob-code blob-code-inner js-file-line">                    open_func <span class="pl-k">=</span> gzip.open</td>
      </tr>
      <tr>
        <td id="L2094" class="blob-num js-line-number" data-line-number="2094"></td>
        <td id="LC2094" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2095" class="blob-num js-line-number" data-line-number="2095"></td>
        <td id="LC2095" class="blob-code blob-code-inner js-file-line">                    open_func <span class="pl-k">=</span> <span class="pl-c1">open</span></td>
      </tr>
      <tr>
        <td id="L2096" class="blob-num js-line-number" data-line-number="2096"></td>
        <td id="LC2096" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">file</span> <span class="pl-k">=</span> open_func(filename, <span class="pl-s"><span class="pl-pds">&#39;</span>r<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2097" class="blob-num js-line-number" data-line-number="2097"></td>
        <td id="LC2097" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2098" class="blob-num js-line-number" data-line-number="2098"></td>
        <td id="LC2098" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.show_progress:</td>
      </tr>
      <tr>
        <td id="L2099" class="blob-num js-line-number" data-line-number="2099"></td>
        <td id="LC2099" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">print</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Parsing log <span class="pl-c1">%s</span>...<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> filename</td>
      </tr>
      <tr>
        <td id="L2100" class="blob-num js-line-number" data-line-number="2100"></td>
        <td id="LC2100" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2101" class="blob-num js-line-number" data-line-number="2101"></td>
        <td id="LC2101" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.format:</td>
      </tr>
      <tr>
        <td id="L2102" class="blob-num js-line-number" data-line-number="2102"></td>
        <td id="LC2102" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> The format was explicitely specified.</span></td>
      </tr>
      <tr>
        <td id="L2103" class="blob-num js-line-number" data-line-number="2103"></td>
        <td id="LC2103" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">format</span> <span class="pl-k">=</span> config.format</td>
      </tr>
      <tr>
        <td id="L2104" class="blob-num js-line-number" data-line-number="2104"></td>
        <td id="LC2104" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2105" class="blob-num js-line-number" data-line-number="2105"></td>
        <td id="LC2105" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">isinstance</span>(<span class="pl-c1">format</span>, W3cExtendedFormat):</td>
      </tr>
      <tr>
        <td id="L2106" class="blob-num js-line-number" data-line-number="2106"></td>
        <td id="LC2106" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">format</span>.create_regex(<span class="pl-v">file</span>)</td>
      </tr>
      <tr>
        <td id="L2107" class="blob-num js-line-number" data-line-number="2107"></td>
        <td id="LC2107" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2108" class="blob-num js-line-number" data-line-number="2108"></td>
        <td id="LC2108" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">format</span>.regex <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L2109" class="blob-num js-line-number" data-line-number="2109"></td>
        <td id="LC2109" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">return</span> fatal_error(</td>
      </tr>
      <tr>
        <td id="L2110" class="blob-num js-line-number" data-line-number="2110"></td>
        <td id="LC2110" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>File is not in the correct format, is there a &#39;#Fields:&#39; line? <span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2111" class="blob-num js-line-number" data-line-number="2111"></td>
        <td id="LC2111" class="blob-code blob-code-inner js-file-line">                        <span class="pl-s"><span class="pl-pds">&quot;</span>If not, use the --w3c-fields option.<span class="pl-pds">&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2112" class="blob-num js-line-number" data-line-number="2112"></td>
        <td id="LC2112" class="blob-code blob-code-inner js-file-line">                    )</td>
      </tr>
      <tr>
        <td id="L2113" class="blob-num js-line-number" data-line-number="2113"></td>
        <td id="LC2113" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2114" class="blob-num js-line-number" data-line-number="2114"></td>
        <td id="LC2114" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> If the file is empty, don&#39;t bother.</span></td>
      </tr>
      <tr>
        <td id="L2115" class="blob-num js-line-number" data-line-number="2115"></td>
        <td id="LC2115" class="blob-code blob-code-inner js-file-line">            data <span class="pl-k">=</span> <span class="pl-v">file</span>.read(<span class="pl-c1">100</span>)</td>
      </tr>
      <tr>
        <td id="L2116" class="blob-num js-line-number" data-line-number="2116"></td>
        <td id="LC2116" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(data.strip()) <span class="pl-k">==</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L2117" class="blob-num js-line-number" data-line-number="2117"></td>
        <td id="LC2117" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L2118" class="blob-num js-line-number" data-line-number="2118"></td>
        <td id="LC2118" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2119" class="blob-num js-line-number" data-line-number="2119"></td>
        <td id="LC2119" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">file</span>.seek(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L2120" class="blob-num js-line-number" data-line-number="2120"></td>
        <td id="LC2120" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">IOError</span>:</td>
      </tr>
      <tr>
        <td id="L2121" class="blob-num js-line-number" data-line-number="2121"></td>
        <td id="LC2121" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L2122" class="blob-num js-line-number" data-line-number="2122"></td>
        <td id="LC2122" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2123" class="blob-num js-line-number" data-line-number="2123"></td>
        <td id="LC2123" class="blob-code blob-code-inner js-file-line">            <span class="pl-c1">format</span> <span class="pl-k">=</span> <span class="pl-c1">self</span>.detect_format(<span class="pl-v">file</span>)</td>
      </tr>
      <tr>
        <td id="L2124" class="blob-num js-line-number" data-line-number="2124"></td>
        <td id="LC2124" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">format</span> <span class="pl-k">is</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L2125" class="blob-num js-line-number" data-line-number="2125"></td>
        <td id="LC2125" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span> fatal_error(</td>
      </tr>
      <tr>
        <td id="L2126" class="blob-num js-line-number" data-line-number="2126"></td>
        <td id="LC2126" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>Cannot guess the logs format. Please give one using <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2127" class="blob-num js-line-number" data-line-number="2127"></td>
        <td id="LC2127" class="blob-code blob-code-inner js-file-line">                    <span class="pl-s"><span class="pl-pds">&#39;</span>either the --log-format-name or --log-format-regex option<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2128" class="blob-num js-line-number" data-line-number="2128"></td>
        <td id="LC2128" class="blob-code blob-code-inner js-file-line">                )</td>
      </tr>
      <tr>
        <td id="L2129" class="blob-num js-line-number" data-line-number="2129"></td>
        <td id="LC2129" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> Make sure the format is compatible with the resolver.</span></td>
      </tr>
      <tr>
        <td id="L2130" class="blob-num js-line-number" data-line-number="2130"></td>
        <td id="LC2130" class="blob-code blob-code-inner js-file-line">        resolver.check_format(<span class="pl-c1">format</span>)</td>
      </tr>
      <tr>
        <td id="L2131" class="blob-num js-line-number" data-line-number="2131"></td>
        <td id="LC2131" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2132" class="blob-num js-line-number" data-line-number="2132"></td>
        <td id="LC2132" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> config.options.dump_log_regex:</td>
      </tr>
      <tr>
        <td id="L2133" class="blob-num js-line-number" data-line-number="2133"></td>
        <td id="LC2133" class="blob-code blob-code-inner js-file-line">            logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>Using format &#39;<span class="pl-c1">%s</span>&#39;.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">format</span>.name)</td>
      </tr>
      <tr>
        <td id="L2134" class="blob-num js-line-number" data-line-number="2134"></td>
        <td id="LC2134" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">format</span>.regex:</td>
      </tr>
      <tr>
        <td id="L2135" class="blob-num js-line-number" data-line-number="2135"></td>
        <td id="LC2135" class="blob-code blob-code-inner js-file-line">                logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>Regex being used: <span class="pl-c1">%s</span><span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">format</span>.regex.pattern)</td>
      </tr>
      <tr>
        <td id="L2136" class="blob-num js-line-number" data-line-number="2136"></td>
        <td id="LC2136" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2137" class="blob-num js-line-number" data-line-number="2137"></td>
        <td id="LC2137" class="blob-code blob-code-inner js-file-line">                logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>Format <span class="pl-c1">%s</span> does not use a regex to parse log lines.<span class="pl-pds">&quot;</span></span> <span class="pl-k">%</span> <span class="pl-c1">format</span>.name)</td>
      </tr>
      <tr>
        <td id="L2138" class="blob-num js-line-number" data-line-number="2138"></td>
        <td id="LC2138" class="blob-code blob-code-inner js-file-line">            logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>--dump-log-regex option used, aborting log import.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2139" class="blob-num js-line-number" data-line-number="2139"></td>
        <td id="LC2139" class="blob-code blob-code-inner js-file-line">            os._exit(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L2140" class="blob-num js-line-number" data-line-number="2140"></td>
        <td id="LC2140" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2141" class="blob-num js-line-number" data-line-number="2141"></td>
        <td id="LC2141" class="blob-code blob-code-inner js-file-line">        valid_lines_count <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L2142" class="blob-num js-line-number" data-line-number="2142"></td>
        <td id="LC2142" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2143" class="blob-num js-line-number" data-line-number="2143"></td>
        <td id="LC2143" class="blob-code blob-code-inner js-file-line">        hits <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L2144" class="blob-num js-line-number" data-line-number="2144"></td>
        <td id="LC2144" class="blob-code blob-code-inner js-file-line">        lineno <span class="pl-k">=</span> <span class="pl-k">-</span><span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L2145" class="blob-num js-line-number" data-line-number="2145"></td>
        <td id="LC2145" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">while</span> <span class="pl-c1">True</span>:</td>
      </tr>
      <tr>
        <td id="L2146" class="blob-num js-line-number" data-line-number="2146"></td>
        <td id="LC2146" class="blob-code blob-code-inner js-file-line">            line <span class="pl-k">=</span> <span class="pl-v">file</span>.readline()</td>
      </tr>
      <tr>
        <td id="L2147" class="blob-num js-line-number" data-line-number="2147"></td>
        <td id="LC2147" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> line: <span class="pl-k">break</span></td>
      </tr>
      <tr>
        <td id="L2148" class="blob-num js-line-number" data-line-number="2148"></td>
        <td id="LC2148" class="blob-code blob-code-inner js-file-line">            lineno <span class="pl-k">=</span> lineno <span class="pl-k">+</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L2149" class="blob-num js-line-number" data-line-number="2149"></td>
        <td id="LC2149" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2150" class="blob-num js-line-number" data-line-number="2150"></td>
        <td id="LC2150" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2151" class="blob-num js-line-number" data-line-number="2151"></td>
        <td id="LC2151" class="blob-code blob-code-inner js-file-line">                line <span class="pl-k">=</span> line.decode(config.options.encoding)</td>
      </tr>
      <tr>
        <td id="L2152" class="blob-num js-line-number" data-line-number="2152"></td>
        <td id="LC2152" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">UnicodeDecodeError</span>:</td>
      </tr>
      <tr>
        <td id="L2153" class="blob-num js-line-number" data-line-number="2153"></td>
        <td id="LC2153" class="blob-code blob-code-inner js-file-line">                invalid_line(line, <span class="pl-s"><span class="pl-pds">&#39;</span>invalid encoding<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2154" class="blob-num js-line-number" data-line-number="2154"></td>
        <td id="LC2154" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2155" class="blob-num js-line-number" data-line-number="2155"></td>
        <td id="LC2155" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2156" class="blob-num js-line-number" data-line-number="2156"></td>
        <td id="LC2156" class="blob-code blob-code-inner js-file-line">            stats.count_lines_parsed.increment()</td>
      </tr>
      <tr>
        <td id="L2157" class="blob-num js-line-number" data-line-number="2157"></td>
        <td id="LC2157" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> stats.count_lines_parsed.value <span class="pl-k">&lt;=</span> config.options.skip:</td>
      </tr>
      <tr>
        <td id="L2158" class="blob-num js-line-number" data-line-number="2158"></td>
        <td id="LC2158" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2159" class="blob-num js-line-number" data-line-number="2159"></td>
        <td id="LC2159" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2160" class="blob-num js-line-number" data-line-number="2160"></td>
        <td id="LC2160" class="blob-code blob-code-inner js-file-line">            match <span class="pl-k">=</span> <span class="pl-c1">format</span>.match(line)</td>
      </tr>
      <tr>
        <td id="L2161" class="blob-num js-line-number" data-line-number="2161"></td>
        <td id="LC2161" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> match:</td>
      </tr>
      <tr>
        <td id="L2162" class="blob-num js-line-number" data-line-number="2162"></td>
        <td id="LC2162" class="blob-code blob-code-inner js-file-line">                invalid_line(line, <span class="pl-s"><span class="pl-pds">&#39;</span>line did not match<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2163" class="blob-num js-line-number" data-line-number="2163"></td>
        <td id="LC2163" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2164" class="blob-num js-line-number" data-line-number="2164"></td>
        <td id="LC2164" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2165" class="blob-num js-line-number" data-line-number="2165"></td>
        <td id="LC2165" class="blob-code blob-code-inner js-file-line">            valid_lines_count <span class="pl-k">=</span> valid_lines_count <span class="pl-k">+</span> <span class="pl-c1">1</span></td>
      </tr>
      <tr>
        <td id="L2166" class="blob-num js-line-number" data-line-number="2166"></td>
        <td id="LC2166" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.debug_request_limit <span class="pl-k">and</span> valid_lines_count <span class="pl-k">&gt;=</span> config.options.debug_request_limit:</td>
      </tr>
      <tr>
        <td id="L2167" class="blob-num js-line-number" data-line-number="2167"></td>
        <td id="LC2167" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-c1">len</span>(hits) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L2168" class="blob-num js-line-number" data-line-number="2168"></td>
        <td id="LC2168" class="blob-code blob-code-inner js-file-line">                    Recorder.add_hits(hits)</td>
      </tr>
      <tr>
        <td id="L2169" class="blob-num js-line-number" data-line-number="2169"></td>
        <td id="LC2169" class="blob-code blob-code-inner js-file-line">                logging.info(<span class="pl-s"><span class="pl-pds">&quot;</span>Exceeded limit specified in --debug-request-limit, exiting.<span class="pl-pds">&quot;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2170" class="blob-num js-line-number" data-line-number="2170"></td>
        <td id="LC2170" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">return</span></td>
      </tr>
      <tr>
        <td id="L2171" class="blob-num js-line-number" data-line-number="2171"></td>
        <td id="LC2171" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2172" class="blob-num js-line-number" data-line-number="2172"></td>
        <td id="LC2172" class="blob-code blob-code-inner js-file-line">            hit <span class="pl-k">=</span> Hit(</td>
      </tr>
      <tr>
        <td id="L2173" class="blob-num js-line-number" data-line-number="2173"></td>
        <td id="LC2173" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">filename</span><span class="pl-k">=</span>filename,</td>
      </tr>
      <tr>
        <td id="L2174" class="blob-num js-line-number" data-line-number="2174"></td>
        <td id="LC2174" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">lineno</span><span class="pl-k">=</span>lineno,</td>
      </tr>
      <tr>
        <td id="L2175" class="blob-num js-line-number" data-line-number="2175"></td>
        <td id="LC2175" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">status</span><span class="pl-k">=</span><span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>status<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L2176" class="blob-num js-line-number" data-line-number="2176"></td>
        <td id="LC2176" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">full_path</span><span class="pl-k">=</span><span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>path<span class="pl-pds">&#39;</span></span>),</td>
      </tr>
      <tr>
        <td id="L2177" class="blob-num js-line-number" data-line-number="2177"></td>
        <td id="LC2177" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">is_download</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L2178" class="blob-num js-line-number" data-line-number="2178"></td>
        <td id="LC2178" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">is_robot</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L2179" class="blob-num js-line-number" data-line-number="2179"></td>
        <td id="LC2179" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">is_error</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L2180" class="blob-num js-line-number" data-line-number="2180"></td>
        <td id="LC2180" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">is_redirect</span><span class="pl-k">=</span><span class="pl-c1">False</span>,</td>
      </tr>
      <tr>
        <td id="L2181" class="blob-num js-line-number" data-line-number="2181"></td>
        <td id="LC2181" class="blob-code blob-code-inner js-file-line">                <span class="pl-v">args</span><span class="pl-k">=</span>{},</td>
      </tr>
      <tr>
        <td id="L2182" class="blob-num js-line-number" data-line-number="2182"></td>
        <td id="LC2182" class="blob-code blob-code-inner js-file-line">            )</td>
      </tr>
      <tr>
        <td id="L2183" class="blob-num js-line-number" data-line-number="2183"></td>
        <td id="LC2183" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2184" class="blob-num js-line-number" data-line-number="2184"></td>
        <td id="LC2184" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.regex_group_to_page_cvars_map:</td>
      </tr>
      <tr>
        <td id="L2185" class="blob-num js-line-number" data-line-number="2185"></td>
        <td id="LC2185" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>._add_custom_vars_from_regex_groups(hit, <span class="pl-c1">format</span>, config.options.regex_group_to_page_cvars_map, <span class="pl-c1">True</span>)</td>
      </tr>
      <tr>
        <td id="L2186" class="blob-num js-line-number" data-line-number="2186"></td>
        <td id="LC2186" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2187" class="blob-num js-line-number" data-line-number="2187"></td>
        <td id="LC2187" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.regex_group_to_visit_cvars_map:</td>
      </tr>
      <tr>
        <td id="L2188" class="blob-num js-line-number" data-line-number="2188"></td>
        <td id="LC2188" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">self</span>._add_custom_vars_from_regex_groups(hit, <span class="pl-c1">format</span>, config.options.regex_group_to_visit_cvars_map, <span class="pl-c1">False</span>)</td>
      </tr>
      <tr>
        <td id="L2189" class="blob-num js-line-number" data-line-number="2189"></td>
        <td id="LC2189" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2190" class="blob-num js-line-number" data-line-number="2190"></td>
        <td id="LC2190" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.regex_groups_to_ignore:</td>
      </tr>
      <tr>
        <td id="L2191" class="blob-num js-line-number" data-line-number="2191"></td>
        <td id="LC2191" class="blob-code blob-code-inner js-file-line">                <span class="pl-c1">format</span>.remove_ignored_groups(config.options.regex_groups_to_ignore)</td>
      </tr>
      <tr>
        <td id="L2192" class="blob-num js-line-number" data-line-number="2192"></td>
        <td id="LC2192" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2193" class="blob-num js-line-number" data-line-number="2193"></td>
        <td id="LC2193" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2194" class="blob-num js-line-number" data-line-number="2194"></td>
        <td id="LC2194" class="blob-code blob-code-inner js-file-line">                hit.query_string <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>query_string<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2195" class="blob-num js-line-number" data-line-number="2195"></td>
        <td id="LC2195" class="blob-code blob-code-inner js-file-line">                hit.path <span class="pl-k">=</span> hit.full_path</td>
      </tr>
      <tr>
        <td id="L2196" class="blob-num js-line-number" data-line-number="2196"></td>
        <td id="LC2196" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> BaseFormatException:</td>
      </tr>
      <tr>
        <td id="L2197" class="blob-num js-line-number" data-line-number="2197"></td>
        <td id="LC2197" class="blob-code blob-code-inner js-file-line">                hit.path, _, hit.query_string <span class="pl-k">=</span> hit.full_path.partition(config.options.query_string_delimiter)</td>
      </tr>
      <tr>
        <td id="L2198" class="blob-num js-line-number" data-line-number="2198"></td>
        <td id="LC2198" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2199" class="blob-num js-line-number" data-line-number="2199"></td>
        <td id="LC2199" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> W3cExtendedFormat detaults to - when there is no query string, but we want empty string</span></td>
      </tr>
      <tr>
        <td id="L2200" class="blob-num js-line-number" data-line-number="2200"></td>
        <td id="LC2200" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> hit.query_string <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L2201" class="blob-num js-line-number" data-line-number="2201"></td>
        <td id="LC2201" class="blob-code blob-code-inner js-file-line">                hit.query_string <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2202" class="blob-num js-line-number" data-line-number="2202"></td>
        <td id="LC2202" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2203" class="blob-num js-line-number" data-line-number="2203"></td>
        <td id="LC2203" class="blob-code blob-code-inner js-file-line">            hit.extension <span class="pl-k">=</span> hit.path.rsplit(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)[<span class="pl-k">-</span><span class="pl-c1">1</span>].lower()</td>
      </tr>
      <tr>
        <td id="L2204" class="blob-num js-line-number" data-line-number="2204"></td>
        <td id="LC2204" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2205" class="blob-num js-line-number" data-line-number="2205"></td>
        <td id="LC2205" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2206" class="blob-num js-line-number" data-line-number="2206"></td>
        <td id="LC2206" class="blob-code blob-code-inner js-file-line">                hit.referrer <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>referrer<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2207" class="blob-num js-line-number" data-line-number="2207"></td>
        <td id="LC2207" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2208" class="blob-num js-line-number" data-line-number="2208"></td>
        <td id="LC2208" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> hit.referrer.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>&quot;<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L2209" class="blob-num js-line-number" data-line-number="2209"></td>
        <td id="LC2209" class="blob-code blob-code-inner js-file-line">                    hit.referrer <span class="pl-k">=</span> hit.referrer[<span class="pl-c1">1</span>:<span class="pl-k">-</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L2210" class="blob-num js-line-number" data-line-number="2210"></td>
        <td id="LC2210" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> BaseFormatException:</td>
      </tr>
      <tr>
        <td id="L2211" class="blob-num js-line-number" data-line-number="2211"></td>
        <td id="LC2211" class="blob-code blob-code-inner js-file-line">                hit.referrer <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2212" class="blob-num js-line-number" data-line-number="2212"></td>
        <td id="LC2212" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> hit.referrer <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L2213" class="blob-num js-line-number" data-line-number="2213"></td>
        <td id="LC2213" class="blob-code blob-code-inner js-file-line">                hit.referrer <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2214" class="blob-num js-line-number" data-line-number="2214"></td>
        <td id="LC2214" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2215" class="blob-num js-line-number" data-line-number="2215"></td>
        <td id="LC2215" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2216" class="blob-num js-line-number" data-line-number="2216"></td>
        <td id="LC2216" class="blob-code blob-code-inner js-file-line">                hit.user_agent <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>user_agent<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2217" class="blob-num js-line-number" data-line-number="2217"></td>
        <td id="LC2217" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2218" class="blob-num js-line-number" data-line-number="2218"></td>
        <td id="LC2218" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> in case a format parser included enclosing quotes, remove them so they are not</span></td>
      </tr>
      <tr>
        <td id="L2219" class="blob-num js-line-number" data-line-number="2219"></td>
        <td id="LC2219" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> sent to Piwik</span></td>
      </tr>
      <tr>
        <td id="L2220" class="blob-num js-line-number" data-line-number="2220"></td>
        <td id="LC2220" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> hit.user_agent.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>&quot;<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L2221" class="blob-num js-line-number" data-line-number="2221"></td>
        <td id="LC2221" class="blob-code blob-code-inner js-file-line">                    hit.user_agent <span class="pl-k">=</span> hit.user_agent[<span class="pl-c1">1</span>:<span class="pl-k">-</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L2222" class="blob-num js-line-number" data-line-number="2222"></td>
        <td id="LC2222" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> BaseFormatException:</td>
      </tr>
      <tr>
        <td id="L2223" class="blob-num js-line-number" data-line-number="2223"></td>
        <td id="LC2223" class="blob-code blob-code-inner js-file-line">                hit.user_agent <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2224" class="blob-num js-line-number" data-line-number="2224"></td>
        <td id="LC2224" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2225" class="blob-num js-line-number" data-line-number="2225"></td>
        <td id="LC2225" class="blob-code blob-code-inner js-file-line">            hit.ip <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>ip<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2226" class="blob-num js-line-number" data-line-number="2226"></td>
        <td id="LC2226" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2227" class="blob-num js-line-number" data-line-number="2227"></td>
        <td id="LC2227" class="blob-code blob-code-inner js-file-line">                hit.length <span class="pl-k">=</span> <span class="pl-c1">int</span>(<span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>length<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L2228" class="blob-num js-line-number" data-line-number="2228"></td>
        <td id="LC2228" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> (<span class="pl-c1">ValueError</span>, BaseFormatException):</td>
      </tr>
      <tr>
        <td id="L2229" class="blob-num js-line-number" data-line-number="2229"></td>
        <td id="LC2229" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> Some lines or formats don&#39;t have a length (e.g. 304 redirects, W3C logs)</span></td>
      </tr>
      <tr>
        <td id="L2230" class="blob-num js-line-number" data-line-number="2230"></td>
        <td id="LC2230" class="blob-code blob-code-inner js-file-line">                hit.length <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L2231" class="blob-num js-line-number" data-line-number="2231"></td>
        <td id="LC2231" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2232" class="blob-num js-line-number" data-line-number="2232"></td>
        <td id="LC2232" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2233" class="blob-num js-line-number" data-line-number="2233"></td>
        <td id="LC2233" class="blob-code blob-code-inner js-file-line">                hit.generation_time_milli <span class="pl-k">=</span> <span class="pl-c1">float</span>(<span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>generation_time_milli<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L2234" class="blob-num js-line-number" data-line-number="2234"></td>
        <td id="LC2234" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> BaseFormatException:</td>
      </tr>
      <tr>
        <td id="L2235" class="blob-num js-line-number" data-line-number="2235"></td>
        <td id="LC2235" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2236" class="blob-num js-line-number" data-line-number="2236"></td>
        <td id="LC2236" class="blob-code blob-code-inner js-file-line">                    hit.generation_time_milli <span class="pl-k">=</span> <span class="pl-c1">float</span>(<span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>generation_time_micro<span class="pl-pds">&#39;</span></span>)) <span class="pl-k">/</span> <span class="pl-c1">1000</span></td>
      </tr>
      <tr>
        <td id="L2237" class="blob-num js-line-number" data-line-number="2237"></td>
        <td id="LC2237" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> BaseFormatException:</td>
      </tr>
      <tr>
        <td id="L2238" class="blob-num js-line-number" data-line-number="2238"></td>
        <td id="LC2238" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2239" class="blob-num js-line-number" data-line-number="2239"></td>
        <td id="LC2239" class="blob-code blob-code-inner js-file-line">                        hit.generation_time_milli <span class="pl-k">=</span> <span class="pl-c1">float</span>(<span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>generation_time_secs<span class="pl-pds">&#39;</span></span>)) <span class="pl-k">*</span> <span class="pl-c1">1000</span></td>
      </tr>
      <tr>
        <td id="L2240" class="blob-num js-line-number" data-line-number="2240"></td>
        <td id="LC2240" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">except</span> BaseFormatException:</td>
      </tr>
      <tr>
        <td id="L2241" class="blob-num js-line-number" data-line-number="2241"></td>
        <td id="LC2241" class="blob-code blob-code-inner js-file-line">                        hit.generation_time_milli <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L2242" class="blob-num js-line-number" data-line-number="2242"></td>
        <td id="LC2242" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2243" class="blob-num js-line-number" data-line-number="2243"></td>
        <td id="LC2243" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.log_hostname:</td>
      </tr>
      <tr>
        <td id="L2244" class="blob-num js-line-number" data-line-number="2244"></td>
        <td id="LC2244" class="blob-code blob-code-inner js-file-line">                hit.host <span class="pl-k">=</span> config.options.log_hostname</td>
      </tr>
      <tr>
        <td id="L2245" class="blob-num js-line-number" data-line-number="2245"></td>
        <td id="LC2245" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2246" class="blob-num js-line-number" data-line-number="2246"></td>
        <td id="LC2246" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2247" class="blob-num js-line-number" data-line-number="2247"></td>
        <td id="LC2247" class="blob-code blob-code-inner js-file-line">                    hit.host <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>host<span class="pl-pds">&#39;</span></span>).lower().strip(<span class="pl-s"><span class="pl-pds">&#39;</span>.<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2248" class="blob-num js-line-number" data-line-number="2248"></td>
        <td id="LC2248" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2249" class="blob-num js-line-number" data-line-number="2249"></td>
        <td id="LC2249" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">if</span> hit.host.startswith(<span class="pl-s"><span class="pl-pds">&#39;</span>&quot;<span class="pl-pds">&#39;</span></span>):</td>
      </tr>
      <tr>
        <td id="L2250" class="blob-num js-line-number" data-line-number="2250"></td>
        <td id="LC2250" class="blob-code blob-code-inner js-file-line">                        hit.host <span class="pl-k">=</span> hit.host[<span class="pl-c1">1</span>:<span class="pl-k">-</span><span class="pl-c1">1</span>]</td>
      </tr>
      <tr>
        <td id="L2251" class="blob-num js-line-number" data-line-number="2251"></td>
        <td id="LC2251" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> BaseFormatException:</td>
      </tr>
      <tr>
        <td id="L2252" class="blob-num js-line-number" data-line-number="2252"></td>
        <td id="LC2252" class="blob-code blob-code-inner js-file-line">                    <span class="pl-c"><span class="pl-c">#</span> Some formats have no host.</span></td>
      </tr>
      <tr>
        <td id="L2253" class="blob-num js-line-number" data-line-number="2253"></td>
        <td id="LC2253" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L2254" class="blob-num js-line-number" data-line-number="2254"></td>
        <td id="LC2254" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2255" class="blob-num js-line-number" data-line-number="2255"></td>
        <td id="LC2255" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> Add userid</span></td>
      </tr>
      <tr>
        <td id="L2256" class="blob-num js-line-number" data-line-number="2256"></td>
        <td id="LC2256" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2257" class="blob-num js-line-number" data-line-number="2257"></td>
        <td id="LC2257" class="blob-code blob-code-inner js-file-line">                hit.userid <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L2258" class="blob-num js-line-number" data-line-number="2258"></td>
        <td id="LC2258" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2259" class="blob-num js-line-number" data-line-number="2259"></td>
        <td id="LC2259" class="blob-code blob-code-inner js-file-line">                userid <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>userid<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2260" class="blob-num js-line-number" data-line-number="2260"></td>
        <td id="LC2260" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> userid <span class="pl-k">!=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L2261" class="blob-num js-line-number" data-line-number="2261"></td>
        <td id="LC2261" class="blob-code blob-code-inner js-file-line">                    hit.args[<span class="pl-s"><span class="pl-pds">&#39;</span>uid<span class="pl-pds">&#39;</span></span>] <span class="pl-k">=</span> hit.userid <span class="pl-k">=</span> userid</td>
      </tr>
      <tr>
        <td id="L2262" class="blob-num js-line-number" data-line-number="2262"></td>
        <td id="LC2262" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L2263" class="blob-num js-line-number" data-line-number="2263"></td>
        <td id="LC2263" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L2264" class="blob-num js-line-number" data-line-number="2264"></td>
        <td id="LC2264" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2265" class="blob-num js-line-number" data-line-number="2265"></td>
        <td id="LC2265" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> add event info</span></td>
      </tr>
      <tr>
        <td id="L2266" class="blob-num js-line-number" data-line-number="2266"></td>
        <td id="LC2266" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2267" class="blob-num js-line-number" data-line-number="2267"></td>
        <td id="LC2267" class="blob-code blob-code-inner js-file-line">                hit.event_category <span class="pl-k">=</span> hit.event_action <span class="pl-k">=</span> hit.event_name <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L2268" class="blob-num js-line-number" data-line-number="2268"></td>
        <td id="LC2268" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2269" class="blob-num js-line-number" data-line-number="2269"></td>
        <td id="LC2269" class="blob-code blob-code-inner js-file-line">                hit.event_category <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>event_category<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2270" class="blob-num js-line-number" data-line-number="2270"></td>
        <td id="LC2270" class="blob-code blob-code-inner js-file-line">                hit.event_action <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>event_action<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2271" class="blob-num js-line-number" data-line-number="2271"></td>
        <td id="LC2271" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2272" class="blob-num js-line-number" data-line-number="2272"></td>
        <td id="LC2272" class="blob-code blob-code-inner js-file-line">                hit.event_name <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>event_name<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2273" class="blob-num js-line-number" data-line-number="2273"></td>
        <td id="LC2273" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> hit.event_name <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L2274" class="blob-num js-line-number" data-line-number="2274"></td>
        <td id="LC2274" class="blob-code blob-code-inner js-file-line">                    hit.event_name <span class="pl-k">=</span> <span class="pl-c1">None</span></td>
      </tr>
      <tr>
        <td id="L2275" class="blob-num js-line-number" data-line-number="2275"></td>
        <td id="LC2275" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span>:</td>
      </tr>
      <tr>
        <td id="L2276" class="blob-num js-line-number" data-line-number="2276"></td>
        <td id="LC2276" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L2277" class="blob-num js-line-number" data-line-number="2277"></td>
        <td id="LC2277" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2278" class="blob-num js-line-number" data-line-number="2278"></td>
        <td id="LC2278" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> Check if the hit must be excluded.</span></td>
      </tr>
      <tr>
        <td id="L2279" class="blob-num js-line-number" data-line-number="2279"></td>
        <td id="LC2279" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-c1">all</span>((method(hit) <span class="pl-k">for</span> method <span class="pl-k">in</span> <span class="pl-c1">self</span>.check_methods)):</td>
      </tr>
      <tr>
        <td id="L2280" class="blob-num js-line-number" data-line-number="2280"></td>
        <td id="LC2280" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2281" class="blob-num js-line-number" data-line-number="2281"></td>
        <td id="LC2281" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2282" class="blob-num js-line-number" data-line-number="2282"></td>
        <td id="LC2282" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> Parse date.</span></td>
      </tr>
      <tr>
        <td id="L2283" class="blob-num js-line-number" data-line-number="2283"></td>
        <td id="LC2283" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> We parse it after calling check_methods as it&#39;s quite CPU hungry, and</span></td>
      </tr>
      <tr>
        <td id="L2284" class="blob-num js-line-number" data-line-number="2284"></td>
        <td id="LC2284" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> we want to avoid that cost for excluded hits.</span></td>
      </tr>
      <tr>
        <td id="L2285" class="blob-num js-line-number" data-line-number="2285"></td>
        <td id="LC2285" class="blob-code blob-code-inner js-file-line">            date_string <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>date<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2286" class="blob-num js-line-number" data-line-number="2286"></td>
        <td id="LC2286" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2287" class="blob-num js-line-number" data-line-number="2287"></td>
        <td id="LC2287" class="blob-code blob-code-inner js-file-line">                hit.date <span class="pl-k">=</span> datetime.datetime.strptime(date_string, <span class="pl-c1">format</span>.date_format)</td>
      </tr>
      <tr>
        <td id="L2288" class="blob-num js-line-number" data-line-number="2288"></td>
        <td id="LC2288" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>, e:</td>
      </tr>
      <tr>
        <td id="L2289" class="blob-num js-line-number" data-line-number="2289"></td>
        <td id="LC2289" class="blob-code blob-code-inner js-file-line">                invalid_line(line, <span class="pl-s"><span class="pl-pds">&#39;</span>invalid date or invalid format: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> <span class="pl-c1">str</span>(e))</td>
      </tr>
      <tr>
        <td id="L2290" class="blob-num js-line-number" data-line-number="2290"></td>
        <td id="LC2290" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2291" class="blob-num js-line-number" data-line-number="2291"></td>
        <td id="LC2291" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2292" class="blob-num js-line-number" data-line-number="2292"></td>
        <td id="LC2292" class="blob-code blob-code-inner js-file-line">            <span class="pl-c"><span class="pl-c">#</span> Parse timezone and substract its value from the date</span></td>
      </tr>
      <tr>
        <td id="L2293" class="blob-num js-line-number" data-line-number="2293"></td>
        <td id="LC2293" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2294" class="blob-num js-line-number" data-line-number="2294"></td>
        <td id="LC2294" class="blob-code blob-code-inner js-file-line">                timezone <span class="pl-k">=</span> <span class="pl-c1">float</span>(<span class="pl-c1">format</span>.get(<span class="pl-s"><span class="pl-pds">&#39;</span>timezone<span class="pl-pds">&#39;</span></span>))</td>
      </tr>
      <tr>
        <td id="L2295" class="blob-num js-line-number" data-line-number="2295"></td>
        <td id="LC2295" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> BaseFormatException:</td>
      </tr>
      <tr>
        <td id="L2296" class="blob-num js-line-number" data-line-number="2296"></td>
        <td id="LC2296" class="blob-code blob-code-inner js-file-line">                timezone <span class="pl-k">=</span> <span class="pl-c1">0</span></td>
      </tr>
      <tr>
        <td id="L2297" class="blob-num js-line-number" data-line-number="2297"></td>
        <td id="LC2297" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">except</span> <span class="pl-c1">ValueError</span>:</td>
      </tr>
      <tr>
        <td id="L2298" class="blob-num js-line-number" data-line-number="2298"></td>
        <td id="LC2298" class="blob-code blob-code-inner js-file-line">                invalid_line(line, <span class="pl-s"><span class="pl-pds">&#39;</span>invalid timezone<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2299" class="blob-num js-line-number" data-line-number="2299"></td>
        <td id="LC2299" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2300" class="blob-num js-line-number" data-line-number="2300"></td>
        <td id="LC2300" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2301" class="blob-num js-line-number" data-line-number="2301"></td>
        <td id="LC2301" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> timezone:</td>
      </tr>
      <tr>
        <td id="L2302" class="blob-num js-line-number" data-line-number="2302"></td>
        <td id="LC2302" class="blob-code blob-code-inner js-file-line">                hit.date <span class="pl-k">-=</span> datetime.timedelta(<span class="pl-v">hours</span><span class="pl-k">=</span>timezone<span class="pl-k">/</span><span class="pl-c1">100</span>)</td>
      </tr>
      <tr>
        <td id="L2303" class="blob-num js-line-number" data-line-number="2303"></td>
        <td id="LC2303" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2304" class="blob-num js-line-number" data-line-number="2304"></td>
        <td id="LC2304" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> config.options.replay_tracking:</td>
      </tr>
      <tr>
        <td id="L2305" class="blob-num js-line-number" data-line-number="2305"></td>
        <td id="LC2305" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> we need a query string and we only consider requests with piwik.php</span></td>
      </tr>
      <tr>
        <td id="L2306" class="blob-num js-line-number" data-line-number="2306"></td>
        <td id="LC2306" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-k">not</span> hit.query_string <span class="pl-k">or</span> <span class="pl-k">not</span> hit.path.lower().endswith(config.options.replay_tracking_expected_tracker_file):</td>
      </tr>
      <tr>
        <td id="L2307" class="blob-num js-line-number" data-line-number="2307"></td>
        <td id="LC2307" class="blob-code blob-code-inner js-file-line">                    invalid_line(line, <span class="pl-s"><span class="pl-pds">&#39;</span>no query string, or <span class="pl-pds">&#39;</span></span> <span class="pl-k">+</span> hit.path.lower() <span class="pl-k">+</span> <span class="pl-s"><span class="pl-pds">&#39;</span> does not end with piwik.php<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2308" class="blob-num js-line-number" data-line-number="2308"></td>
        <td id="LC2308" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2309" class="blob-num js-line-number" data-line-number="2309"></td>
        <td id="LC2309" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2310" class="blob-num js-line-number" data-line-number="2310"></td>
        <td id="LC2310" class="blob-code blob-code-inner js-file-line">                query_arguments <span class="pl-k">=</span> urlparse.parse_qs(hit.query_string)</td>
      </tr>
      <tr>
        <td id="L2311" class="blob-num js-line-number" data-line-number="2311"></td>
        <td id="LC2311" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> <span class="pl-k">not</span> <span class="pl-s"><span class="pl-pds">&quot;</span>idsite<span class="pl-pds">&quot;</span></span> <span class="pl-k">in</span> query_arguments:</td>
      </tr>
      <tr>
        <td id="L2312" class="blob-num js-line-number" data-line-number="2312"></td>
        <td id="LC2312" class="blob-code blob-code-inner js-file-line">                    invalid_line(line, <span class="pl-s"><span class="pl-pds">&#39;</span>missing idsite<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2313" class="blob-num js-line-number" data-line-number="2313"></td>
        <td id="LC2313" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2314" class="blob-num js-line-number" data-line-number="2314"></td>
        <td id="LC2314" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2315" class="blob-num js-line-number" data-line-number="2315"></td>
        <td id="LC2315" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2316" class="blob-num js-line-number" data-line-number="2316"></td>
        <td id="LC2316" class="blob-code blob-code-inner js-file-line">                    hit.args.update((k, v.pop().encode(<span class="pl-s"><span class="pl-pds">&#39;</span>raw_unicode_escape<span class="pl-pds">&#39;</span></span>).decode(config.options.encoding)) <span class="pl-k">for</span> k, v <span class="pl-k">in</span> query_arguments.iteritems())</td>
      </tr>
      <tr>
        <td id="L2317" class="blob-num js-line-number" data-line-number="2317"></td>
        <td id="LC2317" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">except</span> <span class="pl-c1">UnicodeDecodeError</span>:</td>
      </tr>
      <tr>
        <td id="L2318" class="blob-num js-line-number" data-line-number="2318"></td>
        <td id="LC2318" class="blob-code blob-code-inner js-file-line">                    invalid_line(line, <span class="pl-s"><span class="pl-pds">&#39;</span>invalid encoding<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L2319" class="blob-num js-line-number" data-line-number="2319"></td>
        <td id="LC2319" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2320" class="blob-num js-line-number" data-line-number="2320"></td>
        <td id="LC2320" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2321" class="blob-num js-line-number" data-line-number="2321"></td>
        <td id="LC2321" class="blob-code blob-code-inner js-file-line">            hits.append(hit)</td>
      </tr>
      <tr>
        <td id="L2322" class="blob-num js-line-number" data-line-number="2322"></td>
        <td id="LC2322" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2323" class="blob-num js-line-number" data-line-number="2323"></td>
        <td id="LC2323" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> <span class="pl-c1">len</span>(hits) <span class="pl-k">&gt;=</span> config.options.recorder_max_payload_size <span class="pl-k">*</span> <span class="pl-c1">len</span>(Recorder.recorders):</td>
      </tr>
      <tr>
        <td id="L2324" class="blob-num js-line-number" data-line-number="2324"></td>
        <td id="LC2324" class="blob-code blob-code-inner js-file-line">                Recorder.add_hits(hits)</td>
      </tr>
      <tr>
        <td id="L2325" class="blob-num js-line-number" data-line-number="2325"></td>
        <td id="LC2325" class="blob-code blob-code-inner js-file-line">                hits <span class="pl-k">=</span> []</td>
      </tr>
      <tr>
        <td id="L2326" class="blob-num js-line-number" data-line-number="2326"></td>
        <td id="LC2326" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2327" class="blob-num js-line-number" data-line-number="2327"></td>
        <td id="LC2327" class="blob-code blob-code-inner js-file-line">        <span class="pl-c"><span class="pl-c">#</span> add last chunk of hits</span></td>
      </tr>
      <tr>
        <td id="L2328" class="blob-num js-line-number" data-line-number="2328"></td>
        <td id="LC2328" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">if</span> <span class="pl-c1">len</span>(hits) <span class="pl-k">&gt;</span> <span class="pl-c1">0</span>:</td>
      </tr>
      <tr>
        <td id="L2329" class="blob-num js-line-number" data-line-number="2329"></td>
        <td id="LC2329" class="blob-code blob-code-inner js-file-line">            Recorder.add_hits(hits)</td>
      </tr>
      <tr>
        <td id="L2330" class="blob-num js-line-number" data-line-number="2330"></td>
        <td id="LC2330" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2331" class="blob-num js-line-number" data-line-number="2331"></td>
        <td id="LC2331" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">def</span> <span class="pl-en">_add_custom_vars_from_regex_groups</span>(<span class="pl-smi"><span class="pl-smi">self</span></span>, <span class="pl-smi">hit</span>, <span class="pl-smi">format</span>, <span class="pl-smi">groups</span>, <span class="pl-smi">is_page_var</span>):</td>
      </tr>
      <tr>
        <td id="L2332" class="blob-num js-line-number" data-line-number="2332"></td>
        <td id="LC2332" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> group_name, custom_var_name <span class="pl-k">in</span> groups.iteritems():</td>
      </tr>
      <tr>
        <td id="L2333" class="blob-num js-line-number" data-line-number="2333"></td>
        <td id="LC2333" class="blob-code blob-code-inner js-file-line">            <span class="pl-k">if</span> group_name <span class="pl-k">in</span> <span class="pl-c1">format</span>.get_all():</td>
      </tr>
      <tr>
        <td id="L2334" class="blob-num js-line-number" data-line-number="2334"></td>
        <td id="LC2334" class="blob-code blob-code-inner js-file-line">                value <span class="pl-k">=</span> <span class="pl-c1">format</span>.get(group_name)</td>
      </tr>
      <tr>
        <td id="L2335" class="blob-num js-line-number" data-line-number="2335"></td>
        <td id="LC2335" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2336" class="blob-num js-line-number" data-line-number="2336"></td>
        <td id="LC2336" class="blob-code blob-code-inner js-file-line">                <span class="pl-c"><span class="pl-c">#</span> don&#39;t track the &#39;-&#39; empty placeholder value</span></td>
      </tr>
      <tr>
        <td id="L2337" class="blob-num js-line-number" data-line-number="2337"></td>
        <td id="LC2337" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> value <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>-<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L2338" class="blob-num js-line-number" data-line-number="2338"></td>
        <td id="LC2338" class="blob-code blob-code-inner js-file-line">                    <span class="pl-k">continue</span></td>
      </tr>
      <tr>
        <td id="L2339" class="blob-num js-line-number" data-line-number="2339"></td>
        <td id="LC2339" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2340" class="blob-num js-line-number" data-line-number="2340"></td>
        <td id="LC2340" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">if</span> is_page_var:</td>
      </tr>
      <tr>
        <td id="L2341" class="blob-num js-line-number" data-line-number="2341"></td>
        <td id="LC2341" class="blob-code blob-code-inner js-file-line">                    hit.add_page_custom_var(custom_var_name, value)</td>
      </tr>
      <tr>
        <td id="L2342" class="blob-num js-line-number" data-line-number="2342"></td>
        <td id="LC2342" class="blob-code blob-code-inner js-file-line">                <span class="pl-k">else</span>:</td>
      </tr>
      <tr>
        <td id="L2343" class="blob-num js-line-number" data-line-number="2343"></td>
        <td id="LC2343" class="blob-code blob-code-inner js-file-line">                    hit.add_visit_custom_var(custom_var_name, value)</td>
      </tr>
      <tr>
        <td id="L2344" class="blob-num js-line-number" data-line-number="2344"></td>
        <td id="LC2344" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2345" class="blob-num js-line-number" data-line-number="2345"></td>
        <td id="LC2345" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">main</span>():</td>
      </tr>
      <tr>
        <td id="L2346" class="blob-num js-line-number" data-line-number="2346"></td>
        <td id="LC2346" class="blob-code blob-code-inner js-file-line">    <span class="pl-s"><span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2347" class="blob-num js-line-number" data-line-number="2347"></td>
        <td id="LC2347" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    Start the importing process.</span></td>
      </tr>
      <tr>
        <td id="L2348" class="blob-num js-line-number" data-line-number="2348"></td>
        <td id="LC2348" class="blob-code blob-code-inner js-file-line"><span class="pl-s">    <span class="pl-pds">&quot;&quot;&quot;</span></span></td>
      </tr>
      <tr>
        <td id="L2349" class="blob-num js-line-number" data-line-number="2349"></td>
        <td id="LC2349" class="blob-code blob-code-inner js-file-line">    stats.set_time_start()</td>
      </tr>
      <tr>
        <td id="L2350" class="blob-num js-line-number" data-line-number="2350"></td>
        <td id="LC2350" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2351" class="blob-num js-line-number" data-line-number="2351"></td>
        <td id="LC2351" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> config.options.show_progress:</td>
      </tr>
      <tr>
        <td id="L2352" class="blob-num js-line-number" data-line-number="2352"></td>
        <td id="LC2352" class="blob-code blob-code-inner js-file-line">        stats.start_monitor()</td>
      </tr>
      <tr>
        <td id="L2353" class="blob-num js-line-number" data-line-number="2353"></td>
        <td id="LC2353" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2354" class="blob-num js-line-number" data-line-number="2354"></td>
        <td id="LC2354" class="blob-code blob-code-inner js-file-line">    recorders <span class="pl-k">=</span> Recorder.launch(config.options.recorders)</td>
      </tr>
      <tr>
        <td id="L2355" class="blob-num js-line-number" data-line-number="2355"></td>
        <td id="LC2355" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2356" class="blob-num js-line-number" data-line-number="2356"></td>
        <td id="LC2356" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2357" class="blob-num js-line-number" data-line-number="2357"></td>
        <td id="LC2357" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">for</span> filename <span class="pl-k">in</span> config.filenames:</td>
      </tr>
      <tr>
        <td id="L2358" class="blob-num js-line-number" data-line-number="2358"></td>
        <td id="LC2358" class="blob-code blob-code-inner js-file-line">            parser.parse(filename)</td>
      </tr>
      <tr>
        <td id="L2359" class="blob-num js-line-number" data-line-number="2359"></td>
        <td id="LC2359" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2360" class="blob-num js-line-number" data-line-number="2360"></td>
        <td id="LC2360" class="blob-code blob-code-inner js-file-line">        Recorder.wait_empty()</td>
      </tr>
      <tr>
        <td id="L2361" class="blob-num js-line-number" data-line-number="2361"></td>
        <td id="LC2361" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">KeyboardInterrupt</span>:</td>
      </tr>
      <tr>
        <td id="L2362" class="blob-num js-line-number" data-line-number="2362"></td>
        <td id="LC2362" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">pass</span></td>
      </tr>
      <tr>
        <td id="L2363" class="blob-num js-line-number" data-line-number="2363"></td>
        <td id="LC2363" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2364" class="blob-num js-line-number" data-line-number="2364"></td>
        <td id="LC2364" class="blob-code blob-code-inner js-file-line">    stats.set_time_stop()</td>
      </tr>
      <tr>
        <td id="L2365" class="blob-num js-line-number" data-line-number="2365"></td>
        <td id="LC2365" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2366" class="blob-num js-line-number" data-line-number="2366"></td>
        <td id="LC2366" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> config.options.show_progress:</td>
      </tr>
      <tr>
        <td id="L2367" class="blob-num js-line-number" data-line-number="2367"></td>
        <td id="LC2367" class="blob-code blob-code-inner js-file-line">        stats.stop_monitor()</td>
      </tr>
      <tr>
        <td id="L2368" class="blob-num js-line-number" data-line-number="2368"></td>
        <td id="LC2368" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2369" class="blob-num js-line-number" data-line-number="2369"></td>
        <td id="LC2369" class="blob-code blob-code-inner js-file-line">    stats.print_summary()</td>
      </tr>
      <tr>
        <td id="L2370" class="blob-num js-line-number" data-line-number="2370"></td>
        <td id="LC2370" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2371" class="blob-num js-line-number" data-line-number="2371"></td>
        <td id="LC2371" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">fatal_error</span>(<span class="pl-smi">error</span>, <span class="pl-smi">filename</span><span class="pl-k">=</span><span class="pl-c1">None</span>, <span class="pl-smi">lineno</span><span class="pl-k">=</span><span class="pl-c1">None</span>):</td>
      </tr>
      <tr>
        <td id="L2372" class="blob-num js-line-number" data-line-number="2372"></td>
        <td id="LC2372" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">print</span> <span class="pl-k">&gt;&gt;</span> sys.stderr, <span class="pl-s"><span class="pl-pds">&#39;</span>Fatal error: <span class="pl-c1">%s</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> error</td>
      </tr>
      <tr>
        <td id="L2373" class="blob-num js-line-number" data-line-number="2373"></td>
        <td id="LC2373" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">if</span> filename <span class="pl-k">and</span> lineno <span class="pl-k">is</span> <span class="pl-k">not</span> <span class="pl-c1">None</span>:</td>
      </tr>
      <tr>
        <td id="L2374" class="blob-num js-line-number" data-line-number="2374"></td>
        <td id="LC2374" class="blob-code blob-code-inner js-file-line">        <span class="pl-c1">print</span> <span class="pl-k">&gt;&gt;</span> sys.stderr, (</td>
      </tr>
      <tr>
        <td id="L2375" class="blob-num js-line-number" data-line-number="2375"></td>
        <td id="LC2375" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>You can restart the import of &quot;<span class="pl-c1">%s</span>&quot; from the point it failed by <span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L2376" class="blob-num js-line-number" data-line-number="2376"></td>
        <td id="LC2376" class="blob-code blob-code-inner js-file-line">            <span class="pl-s"><span class="pl-pds">&#39;</span>specifying --skip=<span class="pl-c1">%d</span> on the command line.<span class="pl-cce">\n</span><span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (filename, lineno)</td>
      </tr>
      <tr>
        <td id="L2377" class="blob-num js-line-number" data-line-number="2377"></td>
        <td id="LC2377" class="blob-code blob-code-inner js-file-line">        )</td>
      </tr>
      <tr>
        <td id="L2378" class="blob-num js-line-number" data-line-number="2378"></td>
        <td id="LC2378" class="blob-code blob-code-inner js-file-line">    os._exit(<span class="pl-c1">1</span>)</td>
      </tr>
      <tr>
        <td id="L2379" class="blob-num js-line-number" data-line-number="2379"></td>
        <td id="LC2379" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L2380" class="blob-num js-line-number" data-line-number="2380"></td>
        <td id="LC2380" class="blob-code blob-code-inner js-file-line"><span class="pl-k">if</span> <span class="pl-c1">__name__</span> <span class="pl-k">==</span> <span class="pl-s"><span class="pl-pds">&#39;</span>__main__<span class="pl-pds">&#39;</span></span>:</td>
      </tr>
      <tr>
        <td id="L2381" class="blob-num js-line-number" data-line-number="2381"></td>
        <td id="LC2381" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">try</span>:</td>
      </tr>
      <tr>
        <td id="L2382" class="blob-num js-line-number" data-line-number="2382"></td>
        <td id="LC2382" class="blob-code blob-code-inner js-file-line">        piwik <span class="pl-k">=</span> Piwik()</td>
      </tr>
      <tr>
        <td id="L2383" class="blob-num js-line-number" data-line-number="2383"></td>
        <td id="LC2383" class="blob-code blob-code-inner js-file-line">        config <span class="pl-k">=</span> Configuration()</td>
      </tr>
      <tr>
        <td id="L2384" class="blob-num js-line-number" data-line-number="2384"></td>
        <td id="LC2384" class="blob-code blob-code-inner js-file-line">        stats <span class="pl-k">=</span> Statistics()</td>
      </tr>
      <tr>
        <td id="L2385" class="blob-num js-line-number" data-line-number="2385"></td>
        <td id="LC2385" class="blob-code blob-code-inner js-file-line">        resolver <span class="pl-k">=</span> config.get_resolver()</td>
      </tr>
      <tr>
        <td id="L2386" class="blob-num js-line-number" data-line-number="2386"></td>
        <td id="LC2386" class="blob-code blob-code-inner js-file-line">        parser <span class="pl-k">=</span> Parser()</td>
      </tr>
      <tr>
        <td id="L2387" class="blob-num js-line-number" data-line-number="2387"></td>
        <td id="LC2387" class="blob-code blob-code-inner js-file-line">        main()</td>
      </tr>
      <tr>
        <td id="L2388" class="blob-num js-line-number" data-line-number="2388"></td>
        <td id="LC2388" class="blob-code blob-code-inner js-file-line">        sys.exit(<span class="pl-c1">0</span>)</td>
      </tr>
      <tr>
        <td id="L2389" class="blob-num js-line-number" data-line-number="2389"></td>
        <td id="LC2389" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">except</span> <span class="pl-c1">KeyboardInterrupt</span>:</td>
      </tr>
      <tr>
        <td id="L2390" class="blob-num js-line-number" data-line-number="2390"></td>
        <td id="LC2390" class="blob-code blob-code-inner js-file-line">        <span class="pl-k">pass</span></td>
      </tr>
</table>

  </div>

</div>

<button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
<div id="jump-to-line" style="display:none">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      <div class="container site-footer-container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links float-right">
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage" class="site-footer-mark" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2017 <span title="0.13403s from github-fe138-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>
  </div>
</div>



  

  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/compat-8a4318ffea09a0cdb8214b76cf2926b9f6a0ced318a317bed419db19214c690d.js"></script>
    <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-6d109e75ad8471ba415082726c00c35fb929ceab975082492835f11eca8c07d9.js"></script>
    <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github-a6e170e1a1432572f27d4c18936acbd70b123dc8cb36302095396fb6b2096b32.js"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

