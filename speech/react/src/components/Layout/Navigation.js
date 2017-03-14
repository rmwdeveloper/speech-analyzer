/**
 * React Static Boilerplate
 * https://github.com/kriasoft/react-static-boilerplate
 *
 * Copyright © 2015-present Kriasoft, LLC. All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.txt file in the root directory of this source tree.
 */

import React from 'react';
import s from './Navigation.css';
import Link from '../Link';
import {acceptedAudioMimeTypes} from '../../config';
import UploadHOC from '../../components/Uploader';
import UploadBox from '../../components/UploadBox';
class Navigation extends React.Component {

  componentDidMount() {
    window.componentHandler.upgradeElement(this.root);
  }

  componentWillUnmount() {
    window.componentHandler.downgradeElements(this.root);
  }

  render() {
    const Uploader = UploadHOC(UploadBox, '/upload', acceptedAudioMimeTypes );
    return (
      <nav className={s.root} ref={node => (this.root = node)}>
        <Link className={s.link} to="/"><i className="fa fa-home" /></Link>
        <Uploader className={s.link} {...this.props} />
        <Link className={s.link} to="#"><i className="fa fa-phone" /></Link>
        <Link className={s.link} to="#"><i className="fa fa-rocket" /></Link>
        <Link className={s.link} to="/about"><i className="fa fa-motorcycle" /></Link>
      </nav>
    );
  }

}

export default Navigation;
