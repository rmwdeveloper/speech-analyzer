import React from 'react';
import s from './UploadBox.css';
import cx from 'classnames';


function UploadBox({className}) {
  return (<div className={cx(s.root, className)}>
    <i className="fa fa-upload" />
  </div>);
}

export default UploadBox;
