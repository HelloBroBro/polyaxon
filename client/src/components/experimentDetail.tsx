import * as React from 'react';
import * as _ from 'lodash';

import { ExperimentModel } from '../models/experiment';
import ExperimentJobs from '../containers/experimentJobs';
import Logs from '../containers/logs';
import {
  getExperimentUrl,
  getGroupUrl,
  getProjectUrl,
  getUserUrl,
  splitUniqueName,
} from '../constants/utils';
import Breadcrumb from './breadcrumb';
import LinkedTab from './linkedTab';
import ExperimentOverview from './experimentOverview';
import EntityBuild from '../containers/EntityBuild';
import { EmptyList } from './emptyList';

export interface Props {
  experiment: ExperimentModel;
  onDelete: () => any;
  fetchData: () => any;
}

export default class ExperimentDetail extends React.Component<Props, Object> {
  componentDidMount() {
    this.props.fetchData();
  }

  public render() {
    const experiment = this.props.experiment;

    if (_.isNil(experiment)) {
      return EmptyList(false, 'experiment', 'experiment');
    }
    let values = splitUniqueName(experiment.project);
    let experimentUrl = getExperimentUrl(values[0], values[1], this.props.experiment.id);
    let group = null;
    if (!_.isNil(experiment.experiment_group)) {
      group = parseInt(splitUniqueName(experiment.experiment_group)[2], 10);
    }
    let breadcrumbLinks = [
      {name: values[0], value: getUserUrl(values[0])},
      {name: values[1], value: getProjectUrl(values[0], values[1])},
      {name: `Experiment ${experiment.id}`}];
    if (group) {
      breadcrumbLinks.splice(
        2,
        0,
        {name: `Group ${group}`, value: getGroupUrl(values[0], values[1], group)});
    }
    return (
      <div className="row">
        <div className="col-md-12">
          <div className="entity-details">
            <Breadcrumb icon="fa-cube" links={breadcrumbLinks}/>
            <LinkedTab
              baseUrl={experimentUrl}
              tabs={[
                {
                  title: 'Overview',
                  component: <ExperimentOverview experiment={experiment}/>,
                  relUrl: ''
                }, {
                  title: 'Logs',
                  component: <Logs
                    fetchData={() => null}
                    logs={''}
                    user={experiment.user}
                    project={experiment.project}
                    resource="experiments"
                    id={experiment.id}
                  />,
                  relUrl: 'logs'
                }, {
                  title: 'Jobs',
                  component: <ExperimentJobs
                    fetchData={() => null}
                    user={experiment.user}
                    experiment={experiment}
                  />,
                  relUrl: 'jobs'
                }, {
                  title: 'Build',
                  component: <EntityBuild buildName={experiment.build_job}/>,
                  relUrl: 'build'
                }
              ]}
            />
          </div>
        </div>
      </div>
    );
  }
}
