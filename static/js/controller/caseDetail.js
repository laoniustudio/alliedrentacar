/**
 * Created by sun on 8/2/2017.
 */

alliedApp.controller("caseDetailCtl",function ($scope,$http,$filter) {

                //get all image damage info
                $http.get("/api/alldamage/"+$scope.casePK)
                .then(function (response) {
                    $scope.allDamage = response.data;
                // set the dashboard damage default
                $scope.damageCheck2 = $scope.allDamage.dashboardImg

                });

                //get more image damge info
                $http.get("/api/post/"+$scope.casePK)
                .then(function (response) {
                    $scope.moreDamage = response.data;

                });



                $scope.updateDate = function () {
                  var params = {
                    dashboardImg : true
                  };

                  var config = {
                    params: params
                  };

                  $http.put('/api/alldamage/'+$scope.casePK+'/update/', params, config)
                    .success(function (data, status, headers, config)
                    {
                      $scope.putCallResult = logResult("PUT SUCCESS", data, status, headers, config);
                    })
                    .error(function (data, status, headers, config)
                    {
                      $scope.putCallResult = logResult("PUT ERROR", data, status, headers, config);
                    });
                };



                // click the nav bar button function
                $scope.goto=function (msg) {
                    $scope.selection = msg;
                    if($scope.selection === "Dashboard"){
                        $scope.damageCheck2 = $scope.allDamage.dashboardImg
                    }else if ($scope.selection === "Front"){
                        $scope.damageCheck2 = $scope.allDamage.frontImg
                    }
                    else if ($scope.selection === "PassFront"){
                        $scope.damageCheck2 = $scope.allDamage.passFrontImg
                    }
                    else if ($scope.selection === "PassRear"){
                        $scope.damageCheck2 = $scope.allDamage.passRearImg
                    }
                    else if ($scope.selection === "Rear"){
                        $scope.damageCheck2 = $scope.allDamage.rearImg
                    }
                    else if ($scope.selection === "DriverRear"){
                        $scope.damageCheck2 = $scope.allDamage.driveRearImg
                    }
                    else if ($scope.selection === "DriverFront"){
                        $scope.damageCheck2 = $scope.allDamage.driveFrontImg
                    }else {
                        for (index in $scope.moreDamage["moreImgIn"]) {
                            if ($scope.selection === index) {
                                $scope.damageCheck2 = $scope.moreDamage["moreImgIn"][index]
                                break

                            }
                        }
                    }
                };



});

// use for wheel Zoom for mouse
alliedApp.directive('bsWheelzoom', function() {
  return {
    link: function(scope, elem, attrs) {
      wheelzoom(elem[0]);
    }
  }
});
alliedApp.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.headers.common['X-CSRFToken'] = '{{ csrf_token|escapejs }}';
}]);
// splite case detail before & after image by ,
alliedApp.filter('split', function() {
        return function(input, splitChar, splitIndex) {
            // do some bounds checking here to ensure it has that index
            return input.split(splitChar)[splitIndex];
        }
});
