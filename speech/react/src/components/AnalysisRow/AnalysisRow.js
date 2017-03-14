import React, { PropTypes, Component } from 'react';
import s from './AnalysisRow.css';




class AnalysisRow extends Component {
    // constructor(){
    //   super();
    // }

  render() {
    console.log('props!', this.props);
    return <div className={s.root}>Analysis row</div>;
  }
}

export default AnalysisRow;
