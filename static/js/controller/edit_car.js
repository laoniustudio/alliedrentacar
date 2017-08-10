
//main controller
alliedApp.controller("carsEditCtl",function ($http,$scope) {
            // get func
            $http.get("/api/cars/")
                .then(function (response) {
                    $scope.cars = response.data;
                });


             $scope.sortBy = function(propertyName) {
                $scope.reverse = ($scope.propertyName === propertyName) ? !$scope.reverse : false;
                $scope.propertyName = propertyName;
              };

});
