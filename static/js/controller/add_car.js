/**
 * Created by sun on 8/2/2017.
 */
//main controller
alliedApp.controller("carCtl",function ($scope) {





});

// get upload file name
alliedApp.directive('customFileInput', [function () {
    return {
        link: function (scope, element, attrs) {
            element.on('change', function  (evt) {
                var files = evt.target.files;
                scope.filename=files[0].name
            });
        }
    }
}]);

