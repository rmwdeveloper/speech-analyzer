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

class Navigation extends React.Component {

  componentDidMount() {
    window.componentHandler.upgradeElement(this.root);
  }

  componentWillUnmount() {
    window.componentHandler.downgradeElements(this.root);
  }

  render() {
    return (
      <nav className={s.root} ref={node => (this.root = node)}>
        <Link className={s.link} to="/"><i className="fa fa-home" /></Link>
        <Link className={s.link} to="/about"><i className="fa fa-question" /></Link>
        <Link className={s.link} to="#"><i className="fa fa-rocket" /></Link>
        <Link className={s.link} to="#"><i className="fa fa-print" /></Link>
        <Link className={s.link} to="/about"><i className="fa fa-plus" /></Link>
      </nav>
    );
  }

}

export default Navigation;
