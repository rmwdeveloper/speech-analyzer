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
import Navigation from './Navigation';
import Link from '../Link';
import s from './Sidebar.css';

class Sidebar extends React.Component {

  componentDidMount() {
    window.componentHandler.upgradeElement(this.root);
  }

  componentWillUnmount() {
    window.componentHandler.downgradeElements(this.root);
  }

  render() {
    return (
      <div className={s.sidebar} ref={node => (this.root = node)}>
        <div className={s.row}>
          <Link className={s.title} to="/">
            S
          </Link>
          <div className="mdl-layout-spacer" />
          <Navigation />
        </div>
      </div>
    );
  }

}

export default Sidebar;
