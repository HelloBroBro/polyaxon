---
title: "Roadmap"
sub_link: "roadmap"
code_link: "https://github.com/polyaxon/polyaxon/blob/master/releases/roadmap.md"
meta_title: "Polyaxon Roadmap and upcoming release notes - Polyaxon Releases"
meta_description: "Polyaxon roadmap, release notes, migrations, and deprecation notes."
visibility: public
status: published
tags:
  - reference
sidebar: "releases"
---

## Upcoming features and enhancements

### Core

 * **New**: Add support for Alibaba Cloud (Aliyun) Object Storage System (OSS).
 * **Enhancement**: Add mid-runtime update with `apply` logic.
 * **Enhancement**: Improve `modelRef` and `artifactRef` initialization process and allow passing custom init path to not force the user to know the run uuid.

### CLI

 * **Enhancement**: Collect `hash` information for uploaded artifacts in the lineage metadata.

### Hub

 * **New**: Add DVC(data version control) integration.
 * **New**: Add support for ssh connection to allow connecting VSCode and Pycharm.
 * **New**: Allow registering init containers as plugins with a hub reference.


### Client

 * **New**: Add `@component` decorator to allow declaring components based on Python functions.
   * Polyaxon CLI will automatically generate a CLI based the decorator which will allows users to reduce the boilerplate and leverage their functions directly without having to use `click` or `argparse`.
   * The decorator automatically detects `NO_OP` and becomes a pass-through.
 * **New**: Add `@op/@operation` decorator to allow invoking components programmatically.
   * The decorator automatically detects `NO_OP` and defaults to a local python function call.
 * **New**: Add support for Python type hints in the both the class and the decorator component declarations.
 * **New**: Automatically detect if the filesystem should use the stream or the artifacts store directly.

### Specification

 * **New**: (Beta) Multi-container pipeline orchestration in a single operation.
 * **Enhancement**: Allow setting DAG outputs without the SDK/Client.
 * **Enhancement**: Improve auto-complete plugins.

### UI

 * **New**: Reports; new interface to create dashboards and shareable notes.
 * **New**: Add markdown, scalar, summary, lineage, and performance widgets.
 * **New**: Show an indicator on artifacts lineage if it's promoted to a model version or artifact version.
 * **New**: Add connection information to artifacts lineage.
 * **New**: Add new advanced filters, allow filtering the runs in the comparison table based on:
   * parallel coordinate.
   * histogram.
   * activity calendar.
   * custom visualizations.
 * **New**: Allow comparing resources with metrics and cross runs resources.
 * **New**: Add predefined hyperparameter tuning widgets/visualizations.
 * **New**: When possible, the `?` will show a direct link to the docs relevant to the UI current page. e.g. if the user is on the service accounts setting tab the `?` will have a link to the guides related to the service accounts.
 * **New**: Data table widget for rendering multi-step events in addition to the per-step slider widget for:
   * audio events.
   * video events.
   * image events.
   * histogram events.
 * **New**: UI to pass parameters and check their types automatically.
 * **Enhancement**: Allow visualizing multiple images (index range) at the same time.
 * **Enhancement**: Implement lazy loading of widgets in dashboards based on their visibility in viewport.
 * **Enhancement**: Do not render large artifacts and provide preview button.

### Tracking

 * **New**: Allow to specify the connection name when logging assets and artifacts to associate the lineage to a specific connection.
 * **New**: Add support for logging data versions, summaries, reports, and quality.
 * **New**: Add log table.
 * **New**: Add custom bar plots.
 * **Enhancement**: Improve logic around assets and artifacts logging to only trigger versioned behavior (step-wise) when a step parameter is provided.
 * **Enhancement**: Improve outputs state calculation.
 * **Enhancement**: Improve artifacts names auto-generator to respect the name size limit.
 * **Enhancement**: Allow tracking dataframes as parquet files.

### Commercial

 * **New**: Project and organization info pages redesign.
 * **New**: Add cross-projects artifact/component/model versions view similar to `All Runs`.
 * **New**: Add a new tab to explore unregistered artifact/component/model versions under each project.
 * **New**: Add notification center to allow users to control and manage notifications using the UI.
 * **New**: Add selection reports, this is similar to selection in v0 but the new implementation will support all the new features and dashboard flexibility (events, artifacts, lineages, comparison, custom columns selection, multi-field sorting, ...):
   * Allows adding single runs to a report from the run's overview page.
   * Allows adding multiple runs to a report using a multi-run action.
   * Add project sidebar button `Reports`.
   * Allow running downstream-ops for a report, e.g. multi-run Tensorboard.
 * **New**: Add project contributors on the overview page to show all members who contributed to a specific project.
 * **Beta**: Add new queuing logic:
    * fair-share queuing
    * auto-preemption based on priority
    * auto-requeueing for suspended operations
    * per-queue preset
 * **Enhancement**: Allow owner/billing users to reset the billing anchor date, several users asked to change when they get billed during month.
 * **Enhancement**: Add possibility to save searches on the global runs table.
 * **Enhancement**: Add possibility to save custom analytics searches.
 * **Enhancement**: Add more informative messages and handling when scaling down usage/agents/seats or when downgrading to a plan missing a specific feature.
 * **Enhancement**: Add support for resuming pipelines and matrix operations.
 * **Enhancement**: Improve resuming or restarting an operation that is part of a pipeline.
 * **Enhancement**: Investigate the new `suspend` feature to provide immediate concurrency change instead of the current [draining logic](/faq/How-does-changing-concurrency-work/).
 * **Fix**: Regression in metric early stopping policies.
