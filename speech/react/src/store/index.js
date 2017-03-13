// import { createStore } from 'redux';
//
// // Centralized application state
// // For more information visit http://redux.js.org/
// const initialState = { count: 0 };
//
// const store = createStore((state = initialState, action) => {
//   // TODO: Add action handlers (aka "reducers")
//   switch (action.type) {
//     case 'COUNT':
//       return { ...state, count: (state.count) + 1 };
//     default:
//       return state;
//   }
// });
//
// export default store;

import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from '../reducers';


export default function configureStore(initialState, helpersConfig) {
  const helpers = createHelpers(helpersConfig);
  const middleware = [thunk.withExtraArgument(helpers)];

  let enhancer;

  if (__DEV__) {
      const createLogger = require('redux-logger'); // eslint-disable-line global-require
      middleware.push(createLogger({
        collapsed: true,
      }));


    // https://github.com/zalmoxisus/redux-devtools-extension#redux-devtools-extension
    let devToolsExtension = f => f;
    if (process.env.BROWSER && window.devToolsExtension) {
      devToolsExtension = window.devToolsExtension();
    }

    enhancer = compose(
      applyMiddleware(...middleware),
      devToolsExtension,
    );
  } else {
    enhancer = applyMiddleware(...middleware);
  }

  // See https://github.com/rackt/redux/releases/tag/v3.1.0
  const store = createStore(rootReducer, initialState, enhancer);

  // Hot reload reducers (requires Webpack or Browserify HMR to be enabled)
  if (__DEV__ && module.hot) {
    module.hot.accept('../reducers', () =>
      store.replaceReducer(require('../reducers').default) // eslint-disable-line global-require
    );
  }

  return store;
}
