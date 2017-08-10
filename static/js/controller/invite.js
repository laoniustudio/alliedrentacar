/**
 * Created by sun on 8/2/2017.
 */
//main controller
alliedApp.controller("inviteCtl",function ($http,$scope) {
            // get func
            $http.get("/api/users/invitation/")
                .then(function (response) {
                    $scope.invitations = response.data;
                    console.info($scope.invitation)
                });


             $scope.sortBy = function(propertyName) {
                $scope.reverse = ($scope.propertyName === propertyName) ? !$scope.reverse : false;
                $scope.propertyName = propertyName;
              };

});
