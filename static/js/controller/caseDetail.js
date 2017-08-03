/**
 * Created by sun on 8/2/2017.
 */

alliedApp.controller("caseDetailCtl",function ($scope,$http,$filter) {

                //get all damage info
                $scope.targetURL = "/api/damage/"+$scope.casePK
                $http.get($scope.targetURL)
                .then(function (response) {
                    $scope.allDamage = response.data;
                    console.info($scope.allDamage)
                });





});

// use for wheel Zoom for mouse
alliedApp.directive('bsWheelzoom', function() {
  return {
    link: function(scope, elem, attrs) {
      wheelzoom(elem[0]);
    }
  }
});

// splite case detail before & after image by ,
alliedApp.filter('split', function() {
        return function(input, splitChar, splitIndex) {
            // do some bounds checking here to ensure it has that index
            return input.split(splitChar)[splitIndex];
        }
});
