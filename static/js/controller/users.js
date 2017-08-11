/**
 * Created by sun on 8/2/2017.
 */
//main controller
alliedApp.controller("usersCtl",function ($scope,$http,) {

            // get func
            $http.get("/api/users")
                .then(function (response) {
                    $scope.users = response.data;
                });


             $scope.sortBy = function(propertyName) {
                $scope.reverse = ($scope.propertyName === propertyName) ? !$scope.reverse : false;
                $scope.propertyName = propertyName;
              };

});
