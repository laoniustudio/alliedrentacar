/**
 * Created by sun on 8/2/2017.
 */
//main controller
alliedApp.controller("navCtl",function ($scope,$http,$window,$mdToast) {

                // get user is_staff permission
                $http.get("/api/users/permission/"+ $scope.sessid)
                .then(function (response) {
                    $scope.users_perm = response.data;

                });

            $scope.checkPermission=function () {

                // if true go to users page or show need permission toast
                if ($scope.users_perm.is_staff === true){
                    var url = "http://" + $window.location.host + "/dashboard/users";
                    $window.location.href = url;
                }else {
                    $mdToast.show({
                      hideDelay   : 5000,
                      position    : 'top right',
                      controller  : 'ToastCtl',
                      templateUrl : 'toast_permission'
                    });
                  };
                }
});


// toast template controller
alliedApp.controller('ToastCtl', function($scope,$http,$mdToast) {

    // close Toast
    $scope.closeToast = function() {
                    $mdToast.hide()
                  };


});