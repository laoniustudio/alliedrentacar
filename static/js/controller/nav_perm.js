/**
 * Created by sun on 8/2/2017.
 */
//main controller
alliedApp.controller("navCtl",function ($scope,$http,) {
            // get func
            $http.get("/api/users/permission/"+ $scope.sessid)
                .then(function (response) {
                    $scope.users_perm = response.data;

                });

            $scope.checkPermission=function () {
                if $scope.users_perm.is_staff === true{
                    
                }

                  console.info($scope.users_perm.is_staff)
            }

});
