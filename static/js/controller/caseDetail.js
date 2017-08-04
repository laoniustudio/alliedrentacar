/**
 * Created by sun on 8/2/2017.
 */

alliedApp.controller("caseDetailCtl",function ($scope,$http,$filter,$window) {

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


                    }else if ($scope.selection === "Front"){
                        $scope.damageCheck2 = $scope.allDamage.frontImg
                        $scope.damageInUpdate = "frontImg"


                    }
                    else if ($scope.selection === "PassFront"){
                        $scope.damageCheck2 = $scope.allDamage.passFrontImg
                        $scope.damageInUpdate = "passFrontImg"

                    }
                    else if ($scope.selection === "PassRear"){
                        $scope.damageCheck2 = $scope.allDamage.passRearImg
                        $scope.damageInUpdate = "passRearImg"
                    }
                    else if ($scope.selection === "Rear"){
                        $scope.damageCheck2 = $scope.allDamage.rearImg
                        $scope.damageInUpdate = "rearImg"
                    }
                    else if ($scope.selection === "DriverRear"){
                        $scope.damageCheck2 = $scope.allDamage.driveRearImg
                        $scope.damageInUpdate = "driveRearImg"
                    }
                    else if ($scope.selection === "DriverFront"){
                        $scope.damageCheck2 = $scope.allDamage.driveFrontImg
                        $scope.damageInUpdate = "driveFrontImg"
                    }else {
                        for ( var i = 0; i < $scope.moreDamage.length; i++ ) {

                            if ($scope.selection == i) {
                                $scope.damageCheck2 = $scope.moreDamage[i]['damage']
                                $scope.damageInUpdate = "damage"
                                $scope.damageInUpdateID = $scope.moreDamage[i]['id']
                                $scope.moreImgName = "O"+(i+1)

                                break

                            }
                        }
                    }
                };
                //save comment
                $scope.finishUpdate = true; //hide loading circle
                $scope.updateComment = function () {
                    $scope.finishUpdate = false;
                    var params = {
                        "comment": $scope.comment
                    };

                    var config = {
                        params: params
                    };
                    var updateURL = "/api/post/"+$scope.casePK+"/update"

                    $http.put(updateURL, params, config)
                        .then(function (sucess) {
                            $scope.finishUpdate = true;
                            console.info(sucess)
                        })
                }

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
