/**
 * Created by sun on 8/2/2017.
 */

alliedApp.controller("caseDetailCtl",function ($scope,$http,$filter,$window,$interval,$mdToast,shareInfo,$timeout) {


                $scope.showCustomToast = function(msg) {
                    shareInfo.addInfo(msg);// pass data to share info
                    $mdToast.show({
                      hideDelay   : 5000,
                      position    : 'top right',
                      controller  : 'ToastCtl',
                      templateUrl : 'toast-template'
                    });
                  };


                // $scope.number = 15
                // var stop;
                // $scope.finishUpdate = false;
                // $scope.loadingBar = function() {
                //
                // stop = $interval(function() {
                //     if ($scope.number<1){
                //         $interval.cancel(stop)
                //         $scope.finishUpdate = true;
                //     }else {
                //         $scope.number =$scope.number -1
                //     }
                //     console.info($scope.number)
                //   }, 100);
                //
                // }
                //get all image damage info
                $scope.getDamageInfo = function (number) {
                    $http.get("/api/alldamage/"+$scope.casePK)
                        .then(function (response) {
                            $scope.allDamage = response.data;

                            // set the dashboard damage default
                            if (number===0){
                                // if number ===0 means first time call the function
                                $scope.damageCheck2 = $scope.allDamage.dashboardImg
                            }

                 //set the damaged nav item style
                $scope.dashboard = $scope.allDamage.dashboardImg
                $scope.front = $scope.allDamage.frontImg
                $scope.pFront = $scope.allDamage.passFrontImg
                $scope.pRear = $scope.allDamage.passRearImg
                $scope.rear = $scope.allDamage.rearImg
                $scope.dRear = $scope.allDamage.driveRearImg
                $scope.dFront = $scope.allDamage.driveFrontImg

                        })
                };

                //get more image damge info
                $scope.getMoreDamageInfo = function () {
                    $http.get("/api/moredamage/"+$scope.casePK)
                        .then(function (response) {
                            $scope.moreDamage = response.data;

                //set the more damaged nav item style
                for ( var i = 0; i < $scope.moreDamage.length; i++ ) {
                    varName = "O"+(i+1)
                    $scope[varName] = $scope.moreDamage[i]["damage"]
                }

                        })
                };
                $scope.getDamageInfo(0)
                $scope.getMoreDamageInfo()




                //set the dashboardImg as the first to update by default
                $scope.damageInUpdate = "dashboardImg"
                // update damage
                $scope.updateDate = function () {

                    // realtime update damage checkbox value to show or hide nav bar ! warning style
                    if ($scope.damageInUpdate === "dashboardImg") {
                        $scope.dashboard = !$scope.damageCheck2
                    } else if ($scope.damageInUpdate === "frontImg") {
                        $scope.front = !$scope.damageCheck2
                    } else if ($scope.damageInUpdate === "passFrontImg") {
                        $scope.pFront = !$scope.damageCheck2
                    } else if ($scope.damageInUpdate === "passRearImg") {
                        $scope.pRear = !$scope.damageCheck2
                    } else if ($scope.damageInUpdate === "rearImg") {
                        $scope.rear = !$scope.damageCheck2
                    } else if ($scope.damageInUpdate === "driveRearImg") {
                        $scope.dRear = !$scope.damageCheck2
                    } else if ($scope.damageInUpdate === "driveFrontImg") {
                        $scope.dFront = !$scope.damageCheck2
                    } else {
                        for (var i = 0; i < $scope.moreDamage.length; i++) {
                            index = "O" + (i + 1)
                            if ($scope.moreImgName == index) {
                                $scope[index] = !$scope.damageCheck2
                            }
                        }
                    }


                    // update damage info to server
                    var updateName = $scope.damageInUpdate;
                    var params = {
                        [updateName]: !$scope.damageCheck2
                    };

                    var config = {
                        params: params
                    };
                    var updateURL = ""
                    if ($scope.damageInUpdate === "damage") {
                        // for more image damage
                        updateURL = '/api/moredamage/' + $scope.casePK + '/' + $scope.damageInUpdateID + '/'

                    } else {
                        //for all image damage
                        updateURL = '/api/alldamage/' + $scope.casePK + '/'
                    }
                    $http.put(updateURL, params, config)
                        .then(function (sucess) {
                            if ($scope.damageInUpdate === "damage") {
                                $scope.getMoreDamageInfo()
                            }else {
                                $scope.getDamageInfo(1)
                            }
                        })

                };


                // click the nav bar button function
                $scope.goto=function (msg) {

                    $scope.selection = msg;
                    if($scope.selection === "Dashboard"){
                        $scope.damageCheck2 = $scope.allDamage.dashboardImg
                        $scope.damageInUpdate = "dashboardImg"
                        $scope.navCounter = 0


                    }else if ($scope.selection === "Front"){
                        $scope.damageCheck2 = $scope.allDamage.frontImg
                        $scope.damageInUpdate = "frontImg"
                        $scope.navCounter = 1

                    }
                    else if ($scope.selection === "PassFront"){
                        $scope.damageCheck2 = $scope.allDamage.passFrontImg
                        $scope.damageInUpdate = "passFrontImg"
                        $scope.navCounter = 2
                    }
                    else if ($scope.selection === "PassRear"){
                        $scope.damageCheck2 = $scope.allDamage.passRearImg
                        $scope.damageInUpdate = "passRearImg"
                        $scope.navCounter = 3
                    }
                    else if ($scope.selection === "Rear"){
                        $scope.damageCheck2 = $scope.allDamage.rearImg
                        $scope.damageInUpdate = "rearImg"
                        $scope.navCounter = 4

                    }
                    else if ($scope.selection === "DriverRear"){
                        $scope.damageCheck2 = $scope.allDamage.driveRearImg
                        $scope.damageInUpdate = "driveRearImg"
                        $scope.navCounter = 5
                    }
                    else if ($scope.selection === "DriverFront"){
                        $scope.damageCheck2 = $scope.allDamage.driveFrontImg
                        $scope.damageInUpdate = "driveFrontImg"
                        $scope.navCounter = 6
                    }else {
                        for ( var i = 0; i < $scope.moreDamage.length; i++ ) {

                            if ($scope.selection == i) {
                                $scope.damageCheck2 = $scope.moreDamage[i]['damage']
                                $scope.damageInUpdate = "damage"
                                $scope.damageInUpdateID = $scope.moreDamage[i]['id']
                                $scope.moreImgName = "O"+(i+1)
                                $scope.navCounter = i+7

                                break

                            }
                        }
                    }
                };
                //save comment
                $scope.saveComment = "Save Comment"
                $scope.updateInfo = function () {

                    $scope.saveComment = "Saving..."
                    $scope.commentDisable =true
                    var params = {
                        "comment": $scope.comment
                    };
                    var config = {
                        params: params
                    };
                    var updateURL = "/api/post/"+$scope.casePK+"/update"

                    $http.put(updateURL, params, config)
                        .then(function (sucess) {

                            $scope.saveComment = "Saved"
                            $scope.commentDisable = false

                        })
                }

                $scope.navCounter = 0

                $scope.nextButton = function (msg) {
                    $timeout(function () {

                        console.info($scope.navCounter)
                        if(msg == "after"){
                            if($scope.navCounter<$scope.moreDamage.length+6){
                                $scope.navCounter += 1
                            var id = "n"+ $scope.navCounter
                            }


                        }else {
                            if ($scope.navCounter >=1){
                                $scope.navCounter = $scope.navCounter-1
                                var id = "n"+ $scope.navCounter

                            }
                        }

                        var el = document.getElementById(id).children;
                        angular.element(el).triggerHandler('click');

                    }, 0);
                }



});

// toast template controller
alliedApp.controller('ToastCtl', function($scope, shareInfo,$http,$mdToast) {
    // get shared data
    $scope.toastStatus = shareInfo.getInfo();

    //update satatus
    $scope.updateStatus = function() {
            $scope.closeToast()
        if ($scope.toastStatus=="DELETE") {

            var params = {
                "status": $scope.statusName
            };

            var config = {
                params: params
            };
            $http.delete("/api/post/" + $scope.casePK + "/delete", params, config)
                .then(function (sucess) {
                    console.info(sucess)
                })
        }else {
                 if($scope.toastStatus=="PASS"){
            $scope.statusName = "Pass"
          }else if($scope.toastStatus=="FAIL"){
              $scope.statusName = "Fail"
          }
          var params = {
                "status": $scope.statusName
            };

            var config = {
                params: params
            };
            $http.put("/api/post/"+$scope.casePK+"/update", params, config)
                .then(function (sucess) {

                })
        }

      };

    // close Toast
    $scope.closeToast = function() {
                    $mdToast.hide()
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

// splite case detail before & after image by ,
alliedApp.filter('split', function() {
        return function(input, splitChar, splitIndex) {
            // do some bounds checking here to ensure it has that index
            return input.split(splitChar)[splitIndex];
        }
});

// service to share data between caseDetailCtl and toast controllers
alliedApp.service('shareInfo', function() {
     var info = "";

      var addInfo = function(msg) {
          info = msg;
      };

      var getInfo = function(){
          return info;
      };

      return {
        addInfo: addInfo,
        getInfo: getInfo
      };
})

