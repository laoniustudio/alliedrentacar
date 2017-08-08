/**
 * Created by sun on 8/2/2017.
 */
//main controller
alliedApp.controller("usersCtl",function ($scope,$http,$filter) {

            // get func
            $http.get("/api/users")
                .then(function (response) {
                    $scope.users = response.data;
                    console.info($scope.posts)
                });


             $scope.sortBy = function(propertyName) {
                $scope.reverse = ($scope.propertyName === propertyName) ? !$scope.reverse : false;
                $scope.propertyName = propertyName;
              };

});
