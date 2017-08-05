/**
 * Created by sun on 7/18/2017.
 */

var alliedApp = angular.module('allied',['ngMaterial','ngMessages']);

// for django csf protections
alliedApp.config(function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});

