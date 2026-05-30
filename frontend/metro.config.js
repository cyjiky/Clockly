const { getDefaultConfig } = require("expo/metro-config");
const { withNativeWind } = require('nativewind/metro');
 
const config = getDefaultConfig(__dirname, { isCSSEnabled: true });
 
config.watcher = {
    ...config.watcher,
    additionalWatchers: [],
    watchman: false,
    usePolling: true,
    interval: 1000,
};

module.exports = withNativeWind(config, { input: './global.css' });